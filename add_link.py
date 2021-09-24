#!/usr/bin/env python3
import os

with open('index.md', 'a') as wf:
    title = input("Enter the title of the article:\n").strip()
    url = input("Enter the URL of the article:\n").strip()
    os.system(f"bash wget.sh {url}")
    fixed_url = url
    if url.startswith('http'):
        fixed_url = fixed_url.replace("https://", "")
        fixed_url = fixed_url.replace("http://", "")
    if fixed_url.endswith("/"):
        fixed_url = fixed_url[:-1]
    if url.endswith('.html'):
        string_to_write = f"- [{title}]({url}) [Backup](./site/backups/{fixed_url})\n"
    elif url.endswith(('.pdf', '.epub', '.txt', '.md')):
        string_to_write = f"- [{title}]({url}) [Backup](./site/backups/{fixed_url})\n"
    else:
        string_to_write = f"- [{title}]({url}) [Backup](./site/backups/{fixed_url}/index.html)\n"
    wf.write(string_to_write)

os.system("make clean && make")
