#!/bin/bash
#display all http methods
curl -sI "$1" | grep 'Allow:' | cut -d ":" -f2 | cut -d ' ' -f2-
