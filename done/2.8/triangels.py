import copy

def prepareStr():
    arr = []
    str = raw_input("go:").rstrip("\r")
    arr = str.split(',')
    if (len(arr)%3) == 0:
        return arr
    else:
        return 'WTF!'

def prepareTri(arr):
    arrTri = []
    itr = iter(arr)
    for t in range(1, (len(arr)/3+1)):
        temp = []
        for i in range(0, 3):
            temp.append(next(itr))
        arrTri.append([temp[0],temp[1]])
        arrTri.append([temp[1],temp[2]])
        arrTri.append([temp[2],temp[0]])
    return arrTri

def findOposite(value):
    for t in value:
        result = -1
        itr = 0
        for i in value:
            if i != t:
                if t == [i[1],i[0]]:
                    result = itr
            itr+=1
        print result

'''
def findOpositeOpti(arrayList, v = [0,0], index = 0):
    mid = int(len(arrayList)/2)
    if index == 0 or index == len(arrayList):
        return
    if arrayList[0] == [v[1], v[0]] :
        print index
    else:
        print '-1'
        findOpositeOpti(arrayList, arrayList[0], index + 1)
        findOpositeOpti(arrayList, arrayList[0], index - 1)

        
findOpositeOpti(prepareTri(prepareStr()))
'''

findOposite(prepareTri(prepareStr()))
