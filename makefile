# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

html/index.html: prettytable.py
	epydoc -v $^

install:
	python setup.py install

.PHONY: clean
clean:
	$(RM) *.pyc
