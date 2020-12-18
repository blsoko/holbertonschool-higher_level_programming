#!/bin/bash
#display all http methods
curl -s "$1" -i | grep 'Content-Length:' | cut -d ":" -f2 | cut -d ' ' -f2
