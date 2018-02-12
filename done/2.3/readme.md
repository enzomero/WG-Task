'''
Explain the differences between buffer1, buffer2 and buffer3 in the
example code below. Consider:
i. Scope &amp; Lifetime [4 marks]
ii. Performance &amp; use of system resources [6 marks]

      char buffer1[512];

      void func1()
      {
      char buffer2[1024];
      #...
      }

      void func2()
      {
      char* buffer3 = static_cast<char*>; ( malloc(2048) );
      #...
      }
      '''
      #Answers

      char buffer[512]

      ''' Global scope for a process, it exist while exist the process
      In general it will has low ipact for perfomance. '''

      void func1()
      {
      char buffer2[1024];
      //...
      }

''' Local scope for a function, lifetime depend from the functon,
it means that lifetime of the buffer equal of lifetime for the function.
The same as for previos case, low ipact for perfomance. '''

void func2()
{
char* buffer3 = static_cast<char*>; ( malloc(2048) );
//...
}

''' Local scope with possibility to use system scope.
The lifetime for this buffer is undepend from the function and may
exist after the function was done, it will leak memory.
In this case it will has large impact fot perfomance, especially if
was used system scope. It may be the source of many problems with security and
limitations in general. '''

