#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.
"""


from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[2], argv[1])
    r = requests.get(url)
    commits = r.json()
    for commit in commits[0:10]:
        print("{}: {}".format(
                commit.get("sha"),
                commit.get("commit").get("author").get("name")))
