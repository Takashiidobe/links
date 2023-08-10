#!/usr/bin/env bash

pandoc $1 --from html --to gfm -o test.md
pandoc test.md -o index.html --template=$HOME/pandoc-github-template.html.template --from gfm
