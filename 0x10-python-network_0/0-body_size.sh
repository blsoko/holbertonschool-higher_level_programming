#!/bin/bash
#sends a request and displays the size
curl -s "$1" -i | grep 'Content-Length:' | cut -d ":" -f2 | cut -d ' ' -f2
