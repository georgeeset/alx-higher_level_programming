#!/bin/bash
# Script that takes a URL, sends a GET request to it, and displays the body
curl -s --location GET "$1"
