#!/usr/bin/python3
"""given URL & email as params, display response body utf-8, print error codes"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    request = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
