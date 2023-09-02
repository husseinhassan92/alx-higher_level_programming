#!/usr/bin/python3
"""
given letter as param, POST to http://0.0.0.0:5000/search_user
usage: ./8-json_api.py [letter only]
"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': q})

    try:
        dic = r.json()
        if dic:
            print("[{}] {}".format(dic["id"], dic["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
