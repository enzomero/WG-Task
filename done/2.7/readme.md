An object foo is written to a new file on platform 1 as:
  
    write( file, &amp;myFoo, sizeof(struct foo) );

...and then read on platform 2 using:
  
    read(file, &amp;myFoo, filesize(file) );

The foo object has the following definition:
  
    struct foo
    {
    char a;
    int b;
    long c;
    char* d;
    };

What kind of issues might arise when loading foo on platform 2? [6 marks]

1 The 'float' numbers

2 Pointing to invalid memory

3 Sizes of data types

4 Padding

5 Endianness

6 I think exist more also...

