#!/usr/bin/env bash
if [[ `uname` == 'Linux' ]]; then
    if ! [[ -x "$(command -v pip)" ]]; then
        sudo apt-get install -y python-pip
    fi
else
    echo "This script is only supported on Ubuntu"
    exit 1
fi

pip install virtualenv

virtualenv --no-site-packages devvenv
source devvenv/bin/activate
python -m pip install -r requirements.txt
pyb -v -X
deactivatess
