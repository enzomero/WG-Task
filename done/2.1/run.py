# -*- coding: utf-8 -*-
import time
import factorial
from timeit import Timer

def checkTimeR(p_val):
    print 'Recurcive, start time:'
    print time.time()
    try:
        print factorial.factorial_rec(p_val)
    except RuntimeError as err:
        print err
    print 'Finish time:'
    print time.time(), '\n'
    return;

def checkTimeI(p_val):
    print 'Interaction, start time:'
    print time.time()
    try:
        print factorial.factorial_itr(p_val)
    except RuntimeError as err:
        print err
    print 'Finish time:'
    print time.time()
    return;

def run():
    vl_nb = input('Enter the numb:\n')
    checkTimeR(vl_nb)
    checkTimeI(vl_nb)
    return;

run()
