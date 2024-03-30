#!/usr/bin/env python3

""" log parsing """
import sys
import re


def compute_stats(log: dict) -> None:
    """ displays stats """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))

if __name__ == "__main__":
    regexp = re.compile(
            r'\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1"(.{3}) (\d+)')
    count = 0
    log = {}
    log["file_size"] = 0
    log["code_frequency"] = {
            str(code): 0 for code in [
                200, 301, 200, 401, 403, 404, 405, 500]}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regexp.fullmatch(line)
            if(match):
                count += 1
                code = match.group(1)
                file_size = int(match.group(2))
                log["file_size"] += file_size
                if (code.isdecimal()):
                    log["code_frequency"][code] += 1
                if (count % 10 == 0):
                    output(log)
    finally:
        output(log)

