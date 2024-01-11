#!/bin/bash
# This script displays the size of the body of a http response
content_length=$(curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r\n'); echo "${content_length}"
