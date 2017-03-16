<?php

final class Application_Model_Qr {
    public static function getMasterSourceQr() {
        return static::renderUrl(Application_Model_Preference::GetMasterDJSourceConnectionURL(false));
    }

    public static function getShowSourceQr($rightAlign = false) {
        return static::renderUrl(Application_Model_Preference::GetLiveDJSourceConnectionURL(), $rightAlign);
    }

    private static function renderUrl($url, $rightAlign = false) {
        $renderer = new \BaconQrCode\Renderer\Text\Html;
        if ($rightAlign) {
            $renderer->setClass('qr-code-right');
        }
        $writer = new \BaconQrCode\Writer($renderer);

        return $writer->writeString($url);
    }
}
