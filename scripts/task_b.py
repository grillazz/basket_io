#!/usr/bin/env python
import os


def case_b():
    prefixed = [filename for filename in os.listdir('folder_name') if filename.startswith("OaH")]
    print(prefixed)


def main():
    case_b()


if __name__ == '__main__':
    main()
