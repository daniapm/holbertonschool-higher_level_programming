#!/bin/bash
# Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -s L X PUT -H "Origin: HolbertonSchool" -d  "user_id=98" "$1"
