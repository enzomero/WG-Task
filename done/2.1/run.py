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
    print vl_nb
    checkTimeR(vl_nb)
    checkTimeI(vl_nb)
    print('1. We need more instructions keep in memory for recursive way.\nEach new execution for function get a part of memory as for a function.\nIt meat that iteration way will be faster.\n2. Most all modern computers have optimosation for iterative calculations,\ncause modern processors can manage expectable values of memory for each\nstep of iteraction, but in case with recursion it isn\'t work.\n3. \"Maximum recursion depth exceeded\" - we depend from the number\nof executions for the function, if we use recursion way.')
    input('')
    return;

run()
