#!/usr/local/bin/python
# -*- coding=utf-8 -*-

from __future__ import print_function
import subprocess
import threading

def is_reacheable(ip):
    if subprocess.call(["ping"], "-c", "1", ip):
        print("{0} is alive".format(ip))
    else:
        print("{0} is unreacheable".format(ip))

def main():
    # file_object = open('ips.txt')
    # try:
    #     str = file_object.read()
    #     print(str)
    # finally:
    #     file_object.close()
    with open('ips.txt') as f:
        lines = f.readlines()
        print(lines)
        threads = []
        for line in lines:
            print(line)
            # thr = threading.Thread(target=is_reacheable, args=(line, ))
            # thr.start()
            # threads.append(thr)
    # for thr in threads:
    #     thr.join()

if __name__ == '__main__':
    main()