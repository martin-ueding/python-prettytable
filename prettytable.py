#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

"""
Pretty prints tables.
"""


__docformat__ = "javadoc en"

import sys
import datetime

def print_table(headers, data, margin=2, outfile=None):
    """
    Prints a table with header and data.

    @param headers List of column headers.
    @param data List of rows which are lists of columns.
    @param margin Spacing between columns-
    """
    if outfile is None:
        outfile = sys.stdout

    margin -= 1
    headers_str = map(str, headers)
    data_str = [map(str, line) for line in data]

    col_widths = [max(len(headers_str[i]), max([len(row[i]) for row in data_str])) for i in range(len(headers))]

    for i in range(len(col_widths)):
        outfile.write(headers_str[i].ljust(col_widths[i])+' '*margin+" ")

    outfile.write("\n")

    for i in range(len(col_widths)):
        outfile.write(('-'*len(headers_str[i])).ljust(col_widths[i])+' '*margin+" ")

    outfile.write("\n")

    for row, row_str in zip(data, data_str):
        for i in range(len(col_widths)):
            outfile.write(_justify(row[i], row_str[i], col_widths[i])+' '*margin+" ")

        outfile.write("\n")


def _justify(data, data_str, width):
    if any([isinstance(data, candidate) for candidate in [int]]):
        return data_str.rjust(width)
    else:
        return data_str.ljust(width)
