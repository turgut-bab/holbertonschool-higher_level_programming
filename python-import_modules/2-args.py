#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = len(sys.argv) - 1
    if count > 1:
        print("{} arguments:".format(count))
    elif count == 1:
        print("1 argument:")
    else:
        print("0 arguments.")
    for i in range(1, count + 1):
        print("{}: {}".format(i, sys.argv[i]))
