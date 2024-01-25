#!/bin/bash
# Script that takes in a URL as an argument, sends a GET request
curl "$1" -sX GET -H "X-HolbertonSchool-User-Id:98"
