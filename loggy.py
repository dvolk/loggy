"""loggy pretty prints logs.

It:
- unquotes url quoted lines
- extracts and pretty prints json
"""

import argparse
import urllib.parse
import sys
import json
import re


def extract_parts(string, start_delim, end_delim):
    """Extract substrings with balanced delimiters."""
    json_parts = list()
    count_br = 0
    in_br = False
    curr_exp = list()
    for c in string:
        if c == start_delim:
            count_br += 1
            in_br = True
        if c == end_delim:
            count_br -= 1
            if in_br and count_br == 0:
                in_br = False
                json_parts.append("".join(curr_exp) + end_delim)
                curr_exp = list()
        if in_br:
            curr_exp.append(c)
    return json_parts


def main():
    """Process lines."""
    for line in sys.stdin:
        line = urllib.parse.unquote(line)
        json_parts = extract_parts(line, "{", "}")
        print(line)
        for p in json_parts:
            print(json.dumps(eval(p), indent=4))


if __name__ == "__main__":
    main()
