#!/usr/bin/env bash

if [ $# -eq 0 ]; then
  echo "Please provide a url to scrape."
fi

domain=$(echo $1 | awk -F[/:] '{print $4}')

wget --max-redirect=1 --reject 'zip' -e robots=off --recursive --page-requisites --adjust-extension --span-hosts -P "./site/backups" --convert-links --restrict-file-names=windows --domains $domain --no-parent -c $1
