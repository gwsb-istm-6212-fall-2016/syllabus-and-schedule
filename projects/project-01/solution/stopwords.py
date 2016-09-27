#!/usr/bin/env python

"""
A filter that removes a set of stop words obtained from a local file.

This filter assumes that incoming text has been prepared to arrive as
one word per line, in lower case.
"""

import fileinput


STOPWORDS = open('common-english-words.txt', 'r').read().strip().split(',')


def process(line):
    """For each line (word) of input, remove any matching stopwords."""
    # Remove trailing newline first
    line = line[:-1]
    if line not in STOPWORDS:
        print(line)

    
for line in fileinput.input():
    process(line)
