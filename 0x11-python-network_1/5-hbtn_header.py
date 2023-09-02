#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL."""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get("X-Request-Id")
