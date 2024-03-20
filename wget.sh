#/usr/bin/env bash
wget --accept="*.html,*.js,*.css" --reject="*.woff,*.woff2,*.tff,*.orig" -P "./site/backups" -E -H -k -K -p -e --user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0" robots=off $1
