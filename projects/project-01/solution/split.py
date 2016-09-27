#!/usr/bin/env python

"""
A filter that splits incoming lines of text into one word per line.
It eliminates all tokens that are non-alphabetic, containing numbers,
punctuation, or whitespace.
""" 

import fileinput
import re


RE_SPLIT = re.compile('(\w{1,})')


def process(line):
    """For each line of input, split it into words."""
    for token in RE_SPLIT.findall(line):
        print(token)


for line in fileinput.input():
    process(line)
