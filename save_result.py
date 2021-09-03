#!/usr/bin/env python3

import requests
import bs4
import json


def main():
    ses = requests.Session()
    url = "http://ketqua1.net"
    resp = ses.get(url, timeout=5)
    tree = bs4.BeautifulSoup(markup=resp.text, features="lxml")
    nodes = tree.find_all("div", attrs={"data-sofar": True})

    result = ""
    for node in nodes[1:]:
        result = result + " " + node.text

    with open("data.txt", "w") as f:
        f.write(result)


if __name__ == "__main__":
    main()
