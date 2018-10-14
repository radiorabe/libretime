#!/bin/bash

set -xe

[[ "$PYTHON" == true ]] && exit 0

if [ "$TRAVIS_PHP_VERSION" == "5.4" ] || [ "$TRAVIS_PHP_VERSION" == "5.6" ]; then
    # use old composer.lock so we can downgrade things for old php versions
    # TODO: ensure this doesn't conflict with releng
    mv travis/composer.php5.lock composer.lock
fi

composer install
