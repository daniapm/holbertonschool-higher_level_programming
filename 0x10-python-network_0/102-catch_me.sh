#!/bin/bash
# Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -sLX PUT -d "Origin: HolbertonSchool" -H  "user_id=98" 0.0.0.0:5000/catch_me
