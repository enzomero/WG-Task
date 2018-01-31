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
    return factorial_step(p_value, 1)

def factorial_step(p_value, p_sum):
    if p_value == 0 : return p_sum
    else : return factorial_step(p_value - 1, p_sum * p_value)
