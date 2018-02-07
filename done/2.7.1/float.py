'''
You are writing a unit test to confirm the correctness of a function which
takes 3 float values as arguments.
You decide to stress test it by testing 1000000 'random' inputs.
You find that the function will fail, but very rarely, so you include code
to print out all failure cases, hoping to grab a simple repro case which you
can debug into.
Note: All code here is run in a single-threaded environment.


//...
// Some code sets a,b,c
//...

if ( testPasses(a,b,c) )
{
printf('Pass\n');
}
else // someFunc fails, print the values so we can reproduce
{
printf('Fail: %f %f %f\n', a, b, c);
}
'''
    # Here is the problem with the precision for printf(...)

'''
where testPasses has the following signature and executes deterministically
with no side effects:
bool testPasses(float f1, float f2, float f3);

void testRepro()
{
float a = // fill in from value printed by above code
float b = // fill in from value printed by above code
float c = // fill in from value printed by above code
bool result = testPasses(a,b,c);
};

Surprisingly, when you type in the 3 values printed out in testRepro()
the test does not fail!
Modify the original code and test bed to reproduce the problem reliably. [4 marks]
'''

    # We can the bytes representing the float number instead of printing a value.

char value[4] = { 0x12, 0x34, 0x56, 0x78 };
float *a = (float*)value;
