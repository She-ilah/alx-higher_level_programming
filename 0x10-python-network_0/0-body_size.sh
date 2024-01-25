#!/bin/bash
# Script takes in, requests and displays URL response.
curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2
