#!/bin/bash
# Script that takes in URL as arg, sends GET req to it, + displays body
curl -s -I "$1" | grep Allow | cut -d' ' -f2-
