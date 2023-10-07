#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    ctr = len(sys.argv) - 1
    if ctr == 0:
        print("0 arguments.")
    elif ctr == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(ctr))
    for i in range(ctr):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
