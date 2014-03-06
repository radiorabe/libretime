<?php

class Rest_MediaController extends Zend_Rest_Controller
{
    public function init()
    {
        $this->view->layout()->disableLayout();
    }

    public function indexAction()
    {
        if (!$this->verifyApiKey()) {
            return;
        }
        
        $files_array = [];
        foreach (CcFilesQuery::create()->find() as $file)
        {
            array_push($files_array, $file->toArray(BasePeer::TYPE_FIELDNAME));
        }
        
        $this->getResponse()
        ->setHttpResponseCode(200)
        ->appendBody(json_encode($files_array));       
        
        /** TODO: Use this simpler code instead after we upgrade to Propel 1.7 (Airtime 2.6.x branch):
        $this->getResponse()
            ->setHttpResponseCode(200)
            ->appendBody(json_encode(CcFilesQuery::create()->find()->toArray(BasePeer::TYPE_FIELDNAME)));
        */
    }
    
    public function getAction()
    {
        if (!$this->verifyApiKey()) {
            return;
        }
        $id = $this->getId();
        if (!$id) {
            return;
        }

        $file = CcFilesQuery::create()->findPk($id);
        if ($file) {
            $this->getResponse()
                ->setHttpResponseCode(200)
                ->appendBody(json_encode($file->toArray(BasePeer::TYPE_FIELDNAME)));
        } else {
            $this->fileNotFoundResponse();
        }
    }
    
    public function postAction()
    {
        if (!$this->verifyApiKey()) {
            return;
        }
        //If we do get an ID on a POST, then that doesn't make any sense
        //since POST is only for creating.
        if ($id = $this->_getParam('id', false)) {
            $resp = $this->getResponse();
            $resp->setHttpResponseCode(400);
            $resp->appendBody("ERROR: ID should not be specified when using POST. POST is only used for show creation, and an ID will be chosen by Airtime"); 
            return;
        }

        $file = new CcFiles();
        $file->fromArray($this->getRequest()->getPost());
        $file->save();

        $this->getResponse()
            ->setHttpResponseCode(201)
            ->appendBody(json_encode($file->toArray(BasePeer::TYPE_FIELDNAME)));
    }

    public function putAction()
    {
        if (!$this->verifyApiKey()) {
            return;
        }
        $id = $this->getId();
        if (!$id) {
            return;
        }
        
        $file = CcFilesQuery::create()->findPk($id);
        if ($file)
        {
            $file->fromArray(json_decode($this->getRequest()->getRawBody(), true), BasePeer::TYPE_FIELDNAME);
            $file->save();
            $this->getResponse()
                ->setHttpResponseCode(200)
                ->appendBody(json_encode($file->toArray(BasePeer::TYPE_FIELDNAME)));
        } else {
            $this->fileNotFoundResponse();
        }
    }

    public function deleteAction()
    {
        if (!$this->verifyApiKey()) {
            return;
        }
        $id = $this->getId();
        if (!$id) {
            return;
        }
        $file = CcFilesQuery::create()->findPk($id);
        if ($file) {
            $file->delete();
            $this->getResponse()
                ->setHttpResponseCode(204);
        } else {
            $this->fileNotFoundResponse();
        }
    }

    private function getId()
    {
        if (!$id = $this->_getParam('id', false)) {
            $resp = $this->getResponse();
            $resp->setHttpResponseCode(400);
            $resp->appendBody("ERROR: No file ID specified."); 
            return false;
        } 
        return $id;
    }

    private function verifyAPIKey()
    {
        //The API key is passed in via HTTP "basic authentication":
        // http://en.wikipedia.org/wiki/Basic_access_authentication

        $CC_CONFIG = Config::getConfig();

        //Decode the API key that was passed to us in the HTTP request.
        $authHeader = $this->getRequest()->getHeader("Authorization");
        $encodedRequestApiKey = substr($authHeader, strlen("Basic "));
        $encodedStoredApiKey = base64_encode($CC_CONFIG["apiKey"][0] . ":");
        
        if ($encodedRequestApiKey === $encodedStoredApiKey) 
        {
            return true;
        } else {
            $resp = $this->getResponse();
            $resp->setHttpResponseCode(401);
            $resp->appendBody("ERROR: Incorrect API key."); 
            return false;
        }
    }

    private function fileNotFoundResponse()
    {
        $resp = $this->getResponse();
        $resp->setHttpResponseCode(404);
        $resp->appendBody("ERROR: Media not found."); 
    }
}