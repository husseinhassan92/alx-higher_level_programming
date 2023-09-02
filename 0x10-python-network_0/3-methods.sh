#!/bin/bash
# Display all HTTP methods the server of a given URL will accept.
curl -sI "$1" | grep "Allow" | cut -f2- -d' '
