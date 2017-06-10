<?php

class PluploadController extends Zend_Controller_Action
{
    public function init()
    {
        $ajaxContext = $this->_helper->getHelper('AjaxContext');
        $ajaxContext->addActionContext('upload',            'json')
                    ->addActionContext('recent-uploads',     'json')
                    ->initContext();
    }

    public function indexAction()
    {
        $CC_CONFIG = Config::getConfig();

        $baseUrl = Application_Common_OsPath::getBaseDir();
        $locale = Application_Model_Preference::GetLocale();

        $this->view->headScript()->appendFile($baseUrl.'lib/datatables/media/js/jquery.dataTables.min.js?'.$CC_CONFIG['airtime_version'], 'text/javascript');
        $this->view->headScript()->appendFile($baseUrl.'lib/plupload/js/plupload.full.js?'.$CC_CONFIG['airtime_version'],'text/javascript');
        $this->view->headScript()->appendFile($baseUrl.'lib/plupload/js/jquery.plupload.queue/jquery.plupload.queue.js?'.$CC_CONFIG['airtime_version'],'text/javascript');
        $this->view->headScript()->appendFile($baseUrl.'js/airtime/library/plupload.js?'.$CC_CONFIG['airtime_version'],'text/javascript');
        // todo: merge with upstream i18n after updating plupload
        $this->view->headScript()->appendFile($baseUrl.'js/plupload/i18n/'.$locale.'.js?'.$CC_CONFIG['airtime_version'],'text/javascript');
        $this->view->headScript()->appendFile($baseUrl.'lib/dropzone/dist/min/dropzone.min.js?'.$CC_CONFIG['airtime_version'],'text/javascript');

        $this->view->headLink()->appendStylesheet($baseUrl.'css/plupload.queue.css?'.$CC_CONFIG['airtime_version']);
        $this->view->headLink()->appendStylesheet($baseUrl.'css/addmedia.css?'.$CC_CONFIG['airtime_version']);
        $this->view->headLink()->appendStylesheet($baseUrl.'css/dashboard.css?'.$CC_CONFIG['airtime_version']);

        $this->view->quotaLimitReached = false;
        if (Application_Model_Systemstatus::isDiskOverQuota()) {
            $this->view->quotaLimitReached = true;
        }

        //Because uploads are done via AJAX (and we're not using Zend form for those), we manually add the CSRF
        //token in here.
        $csrf_namespace = new Zend_Session_Namespace('csrf_namespace');
        //The CSRF token is generated in Bootstrap.php

        $csrf_element = new Zend_Form_Element_Hidden('csrf');
        $csrf_element->setValue($csrf_namespace->authtoken)->setRequired('true')->removeDecorator('HtmlTag')->removeDecorator('Label');
        $csrf_form = new Zend_Form();
        $csrf_form->addElement($csrf_element);
        $this->view->form = $csrf_form;
    }

    public function uploadAction()
    {
        $current_namespace = new Zend_Session_Namespace('csrf_namespace');
        $observed_csrf_token = $this->_getParam('csrf_token');
        $expected_csrf_token = $current_namespace->authtoken;

        if($observed_csrf_token == $expected_csrf_token){
            $upload_dir = ini_get("upload_tmp_dir") . DIRECTORY_SEPARATOR . "plupload";
            $tempFilePath = Application_Model_StoredFile::uploadFile($upload_dir);
            $tempFileName = basename($tempFilePath);
         
            $this->_helper->json->sendJson(array("jsonrpc" => "2.0", "tempfilepath" => $tempFileName));
        }else{
            $this->_helper->json->sendJson(array("jsonrpc" => "2.0", "valid" => false, "error" => "CSRF token did not match."));
        }
    }

    public function recentUploadsAction()
    {
    	$request = $this->getRequest();
    	
        $filter = $request->getParam('uploadFilter', "all");
        $limit = intval($request->getParam('iDisplayLength', 10));
        $rowStart = intval($request->getParam('iDisplayStart', 0));
        
        $recentUploadsQuery = CcFilesQuery::create();
        //old propel 1.5 to reuse this query item (for counts/finds)
        $recentUploadsQuery->keepQuery(true);
        
        //Hide deleted files
        $recentUploadsQuery->filterByDbFileExists(true);
        
        $numTotalRecentUploads = $recentUploadsQuery->count();
        $numTotalDisplayUploads = $numTotalRecentUploads;
        
        if ($filter == "pending") {
            $recentUploadsQuery->filterByDbImportStatus(1);
            $numTotalDisplayUploads = $recentUploadsQuery->count();
        } else if ($filter == "failed") {
            $recentUploadsQuery->filterByDbImportStatus(2);
            $numTotalDisplayUploads = $recentUploadsQuery->count();
            //TODO: Consider using array('min' => 200)) or something if we have multiple errors codes for failure.
        }
        
        $recentUploads = $recentUploadsQuery
        	->orderByDbUtime(Criteria::DESC)
        	->offset($rowStart)
        	->limit($limit)
        	->find();
        
        $uploadsArray = array();
        $utcTimezone = new DateTimeZone("UTC");
        $displayTimezone = new DateTimeZone(Application_Model_Preference::GetUserTimezone());
        
        foreach ($recentUploads as $upload)
        {
            $upload = $upload->toArray(BasePeer::TYPE_FIELDNAME);
            //TODO: $this->sanitizeResponse($upload));
            $upload['utime'] = new DateTime($upload['utime'], $utcTimezone);
            $upload['utime']->setTimeZone($displayTimezone);
            $upload['utime'] = $upload['utime']->format(DEFAULT_TIMESTAMP_FORMAT);

            //TODO: Invoke sanitization here (MediaController's removeBlacklist stuff)
            array_push($uploadsArray, $upload);
        }
        
        $this->view->sEcho = intval($request->getParam('sEcho'));
        $this->view->iTotalDisplayRecords = $numTotalDisplayUploads;
        $this->view->iTotalRecords = $numTotalRecentUploads;
        $this->view->files = SecurityHelper::htmlescape_recursive($uploadsArray);
    }
}
