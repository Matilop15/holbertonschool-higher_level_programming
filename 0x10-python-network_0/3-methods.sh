#!/bin/bash
# Display all HTPP methods accept
curl -sI "$1" | grep 'Allow' | cut -d ' ' -f2-
