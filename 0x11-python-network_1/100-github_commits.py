#!/usrg/bin/python3
""" The Holberton School staff evaluates candidates applying for a back-end
position with multiple technical challenges, like this one: """
import requests
from sys import argv

if __name__ == "__main__":
    addr = "https://api.github.com/repos/{}/{}/commits"
    .format(argv[2], argv[1])
    response = requests.get(addr)
    count = 0
    for item in r.json():
        if count > 9:
            break
        print("{}: {}"
              .format(
                  item.get("sha"),
                  item.get("commit").get("author").get("name")
              )
              )
        count += 1
