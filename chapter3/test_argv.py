#!/usr/local/bin/python
# -*- coding=utf-8 -*-

from __future__ import print_function
import sys
import os

# 不加任何参数时，打印的就是程序的文件名
# print(sys.argv)

def main():
    sys.argv.append("")
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemExit(filename + ' does not exits')
    elif os.access(filename, os.R_OK):
        raise SystemExit(filename + ' is not accessible')
    else:
        print(filename + ' is accessible')

if __name__ == '__main__':
    main()