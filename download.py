#!/usr/bin/env python3

from sys import argv
from newspaper import Article
from os import system
from urllib.parse import urlparse
from re import sub

script, url = argv

article = Article(url)

article.download()

print(article.html)

if url.startswith('http'):
    url = url.replace("https://", "")
    url = url.replace("http://.", "")


stripped_url = url

write_path = f'./site/backups/{stripped_url}'

system(f"mkdir -p {write_path}")

if write_path.endswith('/'):
    print("ends with trailing slash")
    with open(f'{write_path}index.html', 'w+') as f:
        print("writing file")
        print(f"Writing to {write_path}index.html")
        f.write(article.html)
else:
    print("does not end with trailing slash")
    with open(f'{write_path}/index.html', 'w+') as f:
        print("writing file")
        print(f"Writing to {write_path}/index.html")
        f.write(article.html)
