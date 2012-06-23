#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
:author: `Martin Ueding`_
:copyright: Copyright © 2012 Martin Ueding <dev@martin-ueding.de>
:license: MIT_

##################
python-prettytable
##################

Python's ``str`` class provides the ``rjust``, ``ljust`` and ``center``
functions that can be used to print a table.

This module provides a simple interface to create a pretty table.

Call it with::

	import prettytable

	prettytable.print_table(headers, data, margin=2, outfile=None)

``headers`` is a list of objects, ``data`` is a list of rows, which are lists of
objects, one for each table cell.

If you need more margin between the columns, use the ``margin`` option.

``outfile`` is set to standard out by default, you can set it to any file like
object that has a ``write`` method.

sample output
=============

This is a sample output::

	Dir  Name   Last                        Difference
	---  ----   ----                        ----------
	->   Eta    2011-12-22 14:11:24.503932  38 days, 4:51:51.942006
	->   Gamma  2012-01-13 19:54:29.646120  15 days, 23:08:46.800442
	->   Sigma  2012-01-24 19:09:00.255799  4 days, 23:54:16.191345

.. _`Martin Ueding`: mailto:dev@martin-ueding.de
.. _MIT: http://opensource.org/licenses/MIT
"""

import sys

__docformat__ = "restructuredtext en"

def print_table(headers, data, margin=2, outfile=None):
    """
    Prints a table with header and data.

    :param headers: List of column headers.
    :type headers: list
    :param data: List of rows which are lists of columns.
    :type data: list
    :param margin: Spacing between columns-
    :type margin: int
    :param outfile: File to write to.
    :type outfile: file
    """
    if outfile is None:
        outfile = sys.stdout

    margin -= 1

    if not headers is None:
        # Converts the headers to strings.
        headers_str = map(str, headers)

    # Converts the data to strings.
    data_str = [map(str, line) for line in data]

    # Calculate the widths of the columns.
    if headers is None:
        col_widths = [max([len(row[i]) for row in data_str]) for i in range(len(data_str[0]))]
    else:
        col_widths = [max(len(headers_str[i]), max([len(row[i]) for row in data_str])) for i in range(len(headers))]

    if not headers is None:
        # Print the headers.
        for i in range(len(col_widths)):
            outfile.write(headers_str[i].ljust(col_widths[i])+' '*margin+" ")

        outfile.write("\n")

        # Print a separator.
        for i in range(len(col_widths)):
            outfile.write(('-'*len(headers_str[i])).ljust(col_widths[i])+' '*margin+" ")

        outfile.write("\n")

    # Print data.
    for row, row_str in zip(data, data_str):
        for i in range(len(col_widths)):
            outfile.write(_justify(row[i], row_str[i], col_widths[i])+' '*margin+" ")

        outfile.write("\n")


def _justify(data, data_str, width):
    """
    Justifies most strings to the left.

    If the data is of instance C{int}, the given string is justified to the
    right.

    :param data: Data to check the instance of.
    :type data: object
    :param data_str: String to justify.
    :type data_str: str
    :param width: Justification width.
    :type width: int
    """
    if any([isinstance(data, candidate) for candidate in [int]]):
        return data_str.rjust(width)
    else:
        return data_str.ljust(width)
