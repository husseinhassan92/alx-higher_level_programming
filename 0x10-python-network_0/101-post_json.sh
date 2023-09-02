#!/bin/bash
# Take in filename and URL, post contents of file
curl -s -X "POST" -H "Content-Type: application/json" -d @"$2" "$1"
