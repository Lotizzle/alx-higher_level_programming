#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept
allowed_methods=$(curl -sI "$1" | grep -i "Allow" | awk -F ': ' '{print $2}'); echo "$allowed_methods"
