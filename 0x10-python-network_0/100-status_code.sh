#!/bin/bash
#sends a POST request
curl -w "%{http_code}" -s "$1" -o /dev/null
