#!/usr/local/bin/python
# -*- coding:utf-8 -*-
def readTxT():
    file_object = open('/Users/miraclewong/Projects/Python-for-Linux-SAAO/chapter8/ips.txt')
    try:
        str = file_object.read()
        print(str)
    finally:
        file_object.close()
def main():
    readTxT()

if __name__ == '__main__':
    main()