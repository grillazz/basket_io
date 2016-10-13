#!/usr/bin/env python

#B) How would you find files that begin with "0aH" and delete them given a folder (with subfolders)?
#Assume there are many files in the folder.

import os


def case_b():
    prefixed = [filename for filename in os.listdir('folder_name') if filename.startswith("OaH")]
    print(prefixed)


def main():
    case_b()


if __name__ == '__main__':
    main()
