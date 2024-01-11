#!/bin/bash
# This script sends a GET request to the URL, and displays the body of the response
response=$(curl -sI "$1"); status_code=$(echo "$response" | grep -i "HTTP" | awk '{print $2}'); body=$(echo "$response" | sed '$d'); [ "$status_code" -eq 200 ] && echo "$body"
