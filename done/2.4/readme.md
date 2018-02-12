'''
Choose any platform you want and describe what happens at machine level in the
execution of the code below when func() is called. [8 marks]
What changes if foo is inlined? [2 marks]
'''

    int foo( int a, int* b)
    {
    return a + *b;
    }

    extern int x;

    void func()
    {
    int y = 7;
    int r;
    r = foo( x, &y );
    printf("%d\n", r);
    }

'''
We can ask it our compiler) If we used optimization we have not any difference.
But if our compiler don't use optimistaion. We can see that execution foo()
from the function will add load for the stack.
You can saw it into attached files:
code.c.026t.inline_param1
code2.c.026t.inline_param1
'''
