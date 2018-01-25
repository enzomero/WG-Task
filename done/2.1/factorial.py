# -*- coding: utf-8 -*-

# a) The function for factorial by inerator way.
def factorial_itr( p_value ):
    l_v = 1
    for i in range( 1, p_value + 1 ):
        l_v *= i
    return l_v

# b) The function for factorial by recurcive way.
def factorial_rec( p_value ):
    return factorial_step( p_value, 1 )

def factorial_step( p_value, p_sum ):
    if p_value == 0 : return p_sum
    else : return factorial_step( p_value - 1, p_sum * p_value )

# c)  
'''
      1. We need more instructions keep in memory for recursive way.
    Each new execution for function get a part of memory as for a function.
    It meat that iteration way will be faster.
      2. Most all modern computers have optimosation for iterative calculations,
    cause modern processors can manage expectable values of memory for each
    step of iteraction, but in case with recursion it isn't work.
      3. "Maximum recursion depth exceeded" - we depend from the number
    of executions for the function, if we use recursion way.
'''
