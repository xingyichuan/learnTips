#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Guy Xing'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

def _private_1(name1):
    return 'Hello, %s' % name1

def _private_2(name1):
    return 'Hi, %s' % name1

def greeting(name1):
    if len(name1) > 3:
        return _private_1(name1)
    else:
        return _private_2(name1)


if __name__=='__main__':
    #test()
    #greeting(['yichuan','yichuan1','yichuan2'])
    print(greeting('yichuan'))