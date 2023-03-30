#!/bin/bash
# send a request to an URL with curl and displays the body of the response
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
