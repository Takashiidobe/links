#!/usr/bin/env python3

import os

for root, dirs, files in os.walk("./site/backups/", topdown=False):
    for name in dirs:
        path_name = os.path.join(root, name)
        if "?" in path_name:
            fixed_path_name = path_name.split('?')[0]
            print(path_name)
            print(fixed_path_name)
            print(f"Moving {path_name} to {fixed_path_name}")
            os.system(f'mv "{path_name}" "{fixed_path_name}"')
    for name in files:
        path_name = os.path.join(root, name)
        if "?" in path_name:
            fixed_path_name = path_name.split('?')[0]
            print(path_name)
            print(fixed_path_name)
            print(f"Moving {path_name} to {fixed_path_name}")
            os.system(f'mv "{path_name}" "{fixed_path_name}"')
