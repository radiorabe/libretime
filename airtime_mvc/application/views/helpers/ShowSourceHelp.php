<?php

class Airtime_View_Helper_ShowSourceHelp extends Zend_View_Helper_Abstract {
    public function ShowSourceHelp() {
        return array(
            'live_dj_url' => Application_Model_Preference::GetLiveDJSourceConnectionURL(),
            'live_dj_qr' => Application_Model_Qr::getShowSourceQr(),
        );
    }
}
