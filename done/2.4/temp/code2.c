#include <stdio.h>

extern int x;

void func()
{
    int y = 7;
    int r;
    r = x + y;
    printf("%d\n", r);
}   

int main()
{
	func();
	return 0;
}