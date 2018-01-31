# -*- coding: utf-8 -*-
'''// 1.
//
// The nth 'Factorial'; F(n) for positive integers n is defined by:
//
// F(0) = 1
// F(n) = 1*2*3*...*(n-1)*n
//
// So:
// F(2) = 1*2 = 2
// F(3) = 1*2*3 = 6
// etc.

int factorial(int n);

// (1a) Write an iterative (non-recursive) function to compute F(n) [3 marks]
// (1b) Write a recursive function to compute F(n) [3 marks]
// (1c) Which implementation do you expect to be faster and why?
// Give at least 3 reasons. [4 marks]'''

# a) The function for factorial by inerator way.
def factorial_itr(p_value):
    lv_res = 1
    for i in range(1, p_value + 1):
        lv_res *= i
    return lv_res

# b) The function for factorial by recurcive way.
def factorial_rec(p_value):
    if p_value <= 1 : return 1
    else: return p_value * factorial_rec(p_value - 1)

'''1. We need more instructions keep in memory for recursive way.
Each new execution for function get a part of memory as for a function.
It meat that iteration way will be faster.
2. Most all modern computers have optimosation for iterative calculations,
cause modern processors can manage expectable values of memory for each
step of iteraction, but in case with recursion it isn't work.
3. "Maximum recursion depth exceeded" - we depend from the number
of executions for the function, if we use recursion way.'''
