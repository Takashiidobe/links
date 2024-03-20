#!/usr/bin/env python3
import os
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

with open('index.md', 'a') as wf:
    title = input("Enter the title of the article:\n").strip()
    url = input("Enter the URL of the article:\n").strip()
    os.system(f"./recursive-wget.sh {url}")
    fixed_url = url
    if url.startswith('http'):
        fixed_url = fixed_url.replace("https://", "")
        fixed_url = fixed_url.replace("http://", "")
    if fixed_url.endswith("/"):
        fixed_url = fixed_url[:-1]
    string_to_write = f"- [{title}]({url}) [Backup (Last retrieved {today})](./site/backups/{fixed_url}"
    if url.endswith(('.html', '.pdf', '.epub', '.txt', '.md')):
        string_to_write += ")\n"
    else:
        string_to_write += "/index.html)\n"
    wf.write(string_to_write)

os.system("make clean && make")
