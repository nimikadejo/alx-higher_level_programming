#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    addition = 0
    if count > 0:
        for i in range(1, (count + 1)):
            addition += int((sys.argv[i]))
    print("{}".format(addition))
