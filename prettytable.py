#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

"""
Pretty prints tables.
"""

import sys

def print_table(headers, data, margin=2, outfile=None):
    """
    Prints a table with header and data.

    @param headers: List of column headers.
    @type headers: list
    @param data: List of rows which are lists of columns.
    @type data: list
    @param margin: Spacing between columns-
    @type margin: int
    """
    if outfile is None:
        outfile = sys.stdout

    margin -= 1

    # Converts the headers to strings.
    headers_str = map(str, headers)

    # Converts the data to strings.
    data_str = [map(str, line) for line in data]

    # Calculate the widths of the columns.
    col_widths = [max(len(headers_str[i]), max([len(row[i]) for row in data_str])) for i in range(len(headers))]

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

    @param data: Data to check the instance of.
    @type data: object
    @param data_str: String to justify.
    @type data_str: str
    @param width: Justification width.
    @type width: int
    """
    if any([isinstance(data, candidate) for candidate in [int]]):
        return data_str.rjust(width)
    else:
        return data_str.ljust(width)
