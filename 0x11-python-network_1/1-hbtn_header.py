#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL."""
import urllib.request
from sys import argv


if __name__ == "__main__":
    request = urllib.request.Request(argv[1])
    with urllib.request.urlopen(request) as response:
        print(response.getheader('X-Request-Id'))
