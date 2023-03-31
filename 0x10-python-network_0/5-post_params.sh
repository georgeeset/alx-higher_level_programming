#!/bin/bash
# Script that takes URL, sends a POST req to it, and displays the body response
curl -s POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
