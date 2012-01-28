# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

install:
	install -d $(DESTDIR)/usr/local/lib/python2.7/site-packages/prettytable
	install prettytable/* $(DESTDIR)/usr/local/lib/python2.7/site-packages/prettytable

.PHONY: clean
clean:
	$(RM) *.pyc
