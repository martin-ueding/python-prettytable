# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

install:
	python setup.py install

.PHONY: clean
clean:
	$(RM) *.pyc
