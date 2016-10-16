#!/usr/bin/env python

#B) How would you find files that begin with "0aH" and delete them given a folder (with subfolders)?
#Assume there are many files in the folder.

import os


def case_b():
    prefixed = [filename for filename in os.listdir('test') if filename.startswith("0aH")]
    print(prefixed)


def case_b1():
    for subdir, dirs, files in os.walk('test'):
        print(files)
        [os.remove(os.path.join(subdir, x)) for x in files if x.startswith("0aH")]


def main():
    case_b1()


if __name__ == '__main__':
    main()
