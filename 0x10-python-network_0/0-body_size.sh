#!/bin/bash
# Display size of body of response; Usage: ./0-body_size.sh 0.0.0.0:5000
curl -s "$1" | wc -c
