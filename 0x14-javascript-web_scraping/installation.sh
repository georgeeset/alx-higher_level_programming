#!/bin/bash

# install required packages for the project
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs

# install semi-standard for checking your code format
sudo npm install semistandard --global

# install request module. Note taht Request module has been deprecated since
# Feb 2022 however, it’s a really simple and powerful module
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
