.PHONY : html preview

html : README.md
	multimarkdown -t html -o README.html README.md

preview : preView.py README.md
	python3 preView.py
