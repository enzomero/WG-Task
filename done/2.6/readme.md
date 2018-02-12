Identify as many bugs and assumptions as you can in the following code.
NOTE that there is/are (at least):
1 major algorithmic assumption
2 portability issues
1 syntax error

        // Function to copy 'nBytes' of data from src to dst.
        void myMemcpy(char* dst, const char* src, int nBytes)
        {
        // Try to be fast and copy a word at a time instead of byte by byte
        int* wordDst = (int*)dst;
        int* wordSrc = (int*)src;
        int numWords = nBytes >> 2;
        for (int i=0; i < numWords; i++)
        {
        *wordDst++ = *wordSrc++;
        }

        int numRemaining = nBytes - (numWords << 2);
        dst = (char*)wordDst;
        src = (char*)wordSrc;
        for (int i=0 ; i <= numRemaining; i++); 
        {
        *dst++ = *src++;
        }
        }

#1
'''
I suppose that is possibility for numRemaining be less then 0 and I think
second cycle should be like that:
    for (int i=0 ; i < numRemaining; i++); 
'''

#2 portability issues
'''
    'int' may be  not 32 bits, its depend from hardware and OS.
    
    I suppose that if 'src' is an odd address,
    trying to read 32 bits from it can make crash.
'''

#3
'''
From the code:

        dst = (char*)wordDst;
        src = (char*)wordSrc;
        for (int i=0 ; i <= numRemaining; i++)';' <-- It is syntax error
        {
            *dst++ = *src++;

'''
