#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL."""
import urllib.request
from sys import argv


if __name__ == "__main__":
    request = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
