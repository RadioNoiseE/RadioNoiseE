.PHONY : html preview

html : Hist/HIDDEN.md
	multimarkdown -t html -o Hist/HIDDEN.html Hist/HIDDEN.md

preview : preView.py Hist/HIDDEN.md
	python3 preView.py
