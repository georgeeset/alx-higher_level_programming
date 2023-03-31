#!/bin/bash
# Script that takes a URL, sends a request to URL, and displays the body size
curl -s "$1" | wc -c
