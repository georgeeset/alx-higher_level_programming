#!/usr/bin/bash
# Script that takes in URL as arg, sends GET req to it, + displays body
curl -s --head "$1" | grep Allow | cut --complement -d -f1
