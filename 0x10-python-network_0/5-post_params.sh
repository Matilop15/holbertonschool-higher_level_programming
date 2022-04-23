#!/bin/bash
# Use a POST request
curl -sX "$1" POST -d "email=test@gmail.com&subject=I will always be here for PLD"
