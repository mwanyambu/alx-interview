#!/usr/bin/python3

""" log parsing """
import sys
import re


if __name__ == "__main__":

    sizef = 0
    count = 0
    http_codes = ["200", "301", "400", "403", "404", "405", "500"]
    log_stats = {k: 0 for k in http_codes}

    def display_stats(log_stats: dict, sizef: int) -> None:
        print("File size: {:d}".format(sizef))
        for key, value in sorted(log_stats.items()):
            if value:
                print("{}: {}".format(key, value))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in log_stats:
                    log_stats[status_code] += 1
            except BaseException:
                pass
            try:
                sizef += int(data[-1])
            except BaseException:
                pass

            if count % 10 == 0:
                display_stats(log_stats, sizef)
        display_stats(log_stats, sizef)
    except KeyboardInterrupt:
        display_stats(log_stats, sizef)
        raise
