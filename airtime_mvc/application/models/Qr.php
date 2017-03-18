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
        $class = 'qr-code';
        if ($rightAlign) {
            $class .= ' qr-code-right';
        }
        $renderer->setClass($class);
        $writer = new \BaconQrCode\Writer($renderer);

        return $writer->writeString($url);
    }
}
