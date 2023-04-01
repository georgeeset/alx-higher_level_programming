#!/bin/bash
# Script that sends a delete req to URL passed as 1st arg + displays the body
curl -s -X DELETE "$1"
