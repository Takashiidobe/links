#!/usr/bin/env python3

from sys import argv
from os import system
from urllib.parse import urlsplit

url = argv[1]

stripped_url = urlsplit(url).netloc + urlsplit(url).path

print(stripped_url)
write_path = f'./site/backups/{stripped_url}'
print(write_path)
system(f"mkdir -p {write_path}")

with open(f'{write_path}/index.html', 'w+') as f:
    system(f"""
lynx -dump -nolist -display_charset=utf-8 {url} > {write_path}/index.txt
pandoc {write_path}/index.txt --template=plain_template.html -o {write_path}/index.html
rm {write_path}/index.txt
gsed -i 's/<[^\/][^<>]*> *<\/[^<>]*>//g' {write_path}/index.html
""")
