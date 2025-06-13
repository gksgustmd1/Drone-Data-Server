#!/bin/bash

source /usr/share/bash-completion/completions/systemctl
source /root/Flask-server/bin/activate

python3 /root/Drone-Data-Server/check_license.py
