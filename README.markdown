# python-prettytable

Python's `str` class provides the `rjust`, `ljust` and `center` functions that
can be used to print a table.

This module provides a simple interface to create a pretty table.

Call it with:

	print_table(headers, data, margin=2, outfile=None)

`headers` is a list of objects, `data` is a list of rows, which are lists of
objects, one for each table cell.

If you need more margin between the columns, use the `margin` option.

`outfile` is set to standard out by default, you can set it to any file like
object that has a `write` method.

## sample

	Dir  Name   Last                        Difference                
	---  ----   ----                        ----------                
	->   Eta    2011-12-22 14:11:24.503932  38 days, 4:51:51.942006   
	->   Gamma  2012-01-13 19:54:29.646120  15 days, 23:08:46.800442  
	->   Sigma  2012-01-24 19:09:00.255799  4 days, 23:54:16.191345   
