#!/usr/bin/env python

"""
A filter that lower cases all incoming text.
"""

import fileinput


def process(line):
    """For each line of input, lower case it and print the result."""
    print(line[:-1].lower())


for line in fileinput.input():
    process(line)
