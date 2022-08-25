#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    if count <= 1:
        print("0")
    else:
        addition = 0
        for i in range(1, count):
            addition += int((sys.argv[i]))
    print("{}".format(addition))
