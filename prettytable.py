#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

###############################################################################
#                                   License                                   #
###############################################################################
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

"""
python-prettytable
==================

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

sample
------

This is a sample output::

	Dir  Name   Last                        Difference
	---  ----   ----                        ----------
	->   Eta    2011-12-22 14:11:24.503932  38 days, 4:51:51.942006
	->   Gamma  2012-01-13 19:54:29.646120  15 days, 23:08:46.800442
	->   Sigma  2012-01-24 19:09:00.255799  4 days, 23:54:16.191345
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
