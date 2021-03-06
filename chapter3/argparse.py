#!/usr/local/bin/python
# -*- coding=utf-8 -*-

from __future__ import print_function
import argparse
def _argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', action='store', dest='server', default="localhost", help='connect to host')
    parser.add_argument('-t', action='store_true', dest='boolean_switch', default=False, help='Set a switch to true')
    return parser.parse_args()

def main():
    parser = _argparse()
    print(parser)
    print('host = ', parser.server)
    print('boolean_switch = ', parser.boolean_switch)


if __name__ == '__main__':
    main()
