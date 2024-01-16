#!/bin/bash
# This script sends a GET request to the URL, and displays the body of the response
curl -sw "%{http_code}" "$1" | 
