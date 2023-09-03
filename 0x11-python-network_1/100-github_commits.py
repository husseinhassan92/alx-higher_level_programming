#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.
"""


from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com//repos/{}/{}/commits".format(
        argv[2], argv[1])
    r = requests.get(url)
    commit = r.json()
    for i in range(10):
        print("{}: {}".format(
            commit[i].get("sha"),
            commit[i].get("author").get("name")))
