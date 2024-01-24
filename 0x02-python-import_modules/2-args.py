#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    argc = len(argv) - 1

    if argc == 0:
        print("{} argument{}.".format(argc, "" if argc == 1 else "s"))
    else:
        print("{} argument{}:".format(argc, "" if argc == 1 else "s"))

        for i in range(1, argc + 1):
            print("{}: {}".format(i, argv[i]))


