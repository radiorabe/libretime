<?php

/** Hide a Zend_Form_Element unless you're logged in as a SuperAdmin. */
class Airtime_Decorator_SuperAdmin_Only extends Zend_Form_Decorator_Abstract
{
    public function render($content)
    {
        $currentUser = Application_Model_User::getCurrentUser();
        if ($currentUser->isSuperAdmin()) {
            return $content;
        } else {
            return "";
        }
    }
}

/** Hide a Zend_Form_Element unless you're logged in as an Admin or SuperAdmin. */
class Airtime_Decorator_Admin_Only extends Zend_Form_Decorator_Abstract
{
    public function render($content)
    {
        $currentUser = Application_Model_User::getCurrentUser();
        if ($currentUser->isSuperAdmin() || $currentUser->isAdmin()) {
            return $content;
        } else {
            return "";
        }
    }
}

/** Output the raw contents of the form element as html **/
class Airtime_Decorator_RawHtml extends Zend_Form_Decorator_Abstract
{
    protected $_format = '<dt><label>%s</label></dt><dd>%s</dd>';

    public function render($content)
    {
        $element = $this->getElement();
        return sprintf($this->_format, $element->getLabel(), $element->getValue());
    }
}
