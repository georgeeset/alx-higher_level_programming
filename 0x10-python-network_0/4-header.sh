#!/bin/bash
# Script that takes in URL as arg, sends GET req to it, + displays body
curl -s GET -H "X-School-User-Id: 98" "$1"
