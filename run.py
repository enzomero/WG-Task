# -*- coding: utf-8 -*-
import time
import factorial
from timeit import Timer

def checkTimeR(val):
    print 'Recurcive'
    print time.time()
    try:
        print factorial.factorial_rec(val)
    except RuntimeError as err:
        print err
    print time.time(), '\n'
    return;

def checkTimeI(val):
    print 'Interaction'
    print time.time()
    try:
        print factorial.factorial_itr(val)
    except RuntimeError as err:
        print err
    print time.time()
    return;

def run():
    nb = input('Enter the numb:\n')
    print nb
    checkTimeR(nb)
    checkTimeI(nb)
    return;

run()
