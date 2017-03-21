<?php

class Rest_PlaylistController extends Zend_Rest_Controller
{
    public function init()
    {
        $this->view->setScriptPath(APPLICATION_PATH . 'views/scripts/');
        $this->view->layout()->disableLayout();
        $this->_helper->viewRenderer->setNoRender(true);
    }

    /**
     * headAction is needed as it is defined as an abstract function in the base controller
     *
     * @return void
     */
    public function headAction()
    {
        Logging::info("HEAD action received");
    }

    /**
     * postAction is needed as it is defined as an abstract function in the base controller
     *
     * @return void
     */
    public function postAction()
    {
        Logging::info("POST action received");
    }

    /**
     * putAction is needed as it is defined as an abstract function in the base controller
     *
     * @return void
     */
    public function putAction()
    {
        Logging::info("PUT action received");
    }

    /**
     * Get list of playlists
     */
    public function indexAction()
    {
    }

    /**
     * get tracklisting for a playlist
     *
     * @return json array
     */
    public function showPlaylistAction()
    {
        $id = $this->getId();
        if (!$id) {
            return;
        }

        $objInfo = Application_Model_Library::getObjInfo('playlist');
        $params = $this->getRequest()->getParams();
        try {
            $obj = new $objInfo['className']($id);
            $data = array(
                "name"     => $obj->getName(),
                "description" => $obj->getDescription(),
                "creator" => $obj->getCreator(),
                "modified" => $obj->getLastModified(),
                "size" => $obj->getSize(),
                "contents" => $obj->getContents()
            );
            $data['contents'] = array_map(function($file) {
                $fileObj = Application_Model_StoredFile::RecallById($file['id'], Propel::getConnection(CcFilesPeer::DATABASE_NAME));
                $file['url'] = $fileObj->getFileUrl();
                return $file;
            }, $data['contents']);
            $this->_helper->json($data);
        } catch (PlaylistNotFoundException $e) {
            $this->_helper->json->sendJson(
                array("error" => array("code" => 404, "message" => "playlist not found ".$id))
            );
        } catch (Exception $e) {
            throw $e;
            $this->_helper->json->sendJson(
                array("error" => array("code" => 500, "message" => "playlist not found ".$id))
            );
        }
    }

}
