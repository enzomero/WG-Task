def reverseTri(couple):
    temp = couple[0]
    couple[0] = couple[1]
    couple[1] = temp
    return couple

def prepareStr():
    arr = []
    str = raw_input("go:").rstrip("\r")
    arr = str.split(',')
    if (len(arr)%3) == 0:
        return arr
    else:
        return 'fuck'

def prepareTri(arr):
    arrTri = []
    itr = iter(arr)
    for t in range(1, (len(arr)/3+1)):
        temp = []
        for i in range(0, 3):
            temp.append(next(itr))
        arrTri.append(temp)
    return arrTri

def findOposite(value):
    iter = 0
    arr = [int]
    for t in value:
        a = [ t[0], t[1] ]
        b = [ t[1], t[2] ]
        c = [ t[2], t[0] ]
        for i in value:
            temp = -1
            if (i != t):
                if (reverseTri([i[0], i[1]]) == a or
                    reverseTri([i[0], i[1]]) == b or
                    reverseTri([i[0], i[1]]) == c):
                    temp = i[2];

                if (reverseTri([i[1], i[2]]) == a or
                    reverseTri([i[1], i[2]]) == b or
                    reverseTri([i[1], i[2]]) == c):
                    temp = i[0];

                if (reverseTri([i[2], i[0]]) == a or
                    reverseTri([i[2], i[0]]) == b or
                    reverseTri([i[2], i[0]]) == c):
                    temp = i[1];
            arr.append(temp)
    arr.reverse()
    print arr
    return 'pass'
    
print findOposite(prepareTri(prepareStr()))

