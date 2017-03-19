#!/bin/bash

set -xe

NAME="libretime"

curl -X POST https://build.opensuse.org/build/${NAME}?cmd=rebuild&package=${NAME}&token=${OBS_TOKEN}
