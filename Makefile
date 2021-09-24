all:
	sed -i 's/\.\/site/\./g' index.md && pandoc index.md -o site/index.html --template=template.html --metadata title="Links"
strip-query-params:
	./strip_query_params.py
clean:
	bash clean.sh
deploy:
	make && make clean && make strip-query-params && ntl deploy --prod
