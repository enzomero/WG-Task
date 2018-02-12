import copy

'''
// Suppose that you have an array of shorts which corresponds to the vertex ids
// of a set of T triangles. The shorts would be interpreted 3 at a time, so the
// array

// 0,2,7,1,3,5,6,2,0

// would represent 3 triangles with vertex ids : (0,2,7), (1,3,5) and (6,2,0)
// There are 9 edges implicit in the data
// Triangle 1 : (0,2), (2,7), (7,0)
// Triangle 2 : (1,3), (3,5), (5,1)
// Triangle 3 : (6,2), (2,0), (0,6)

// Write a method to find all connectivity information between all triangles.
// Two triangles are considered connected if they share an edge.
// For example, triangle 1 and triangle 3 are connected because triangle 1 has
// edge (0,2) and triangle 3 has opposite edge (2,0).

// Your method should fill an output array of size 3T with the corresponding
// indices of the opposite edge. You may assume that every edge has at most one
// match. Edges with no opposite are flagged with -1.

// The output for the example above should be
// 7, -1, -1, -1, -1, -1, -1, 0, -1

// 8(a) First write the method using a brute force implementation (may be
// very slow for large T) [10 marks]

// 8(b) Then consider how you might preprocess the data to find
// the edge matches more quickly for large T. Use code or
// pseudocode to illustrate your approach. [15 marks]

// Your method declaration should look like:
void findConnectivity(unsigned short* indexTriples, int T, int* connectivityOut);
'''

def prepareStr():
    lv_arr = []
    lv_str = raw_input("Enter numberes (example: 0,2,7,1,3,5,6,2,0):").rstrip("\r")
    lv_arr = lv_str.split(',')
    if (len(lv_arr)%3) == 0:
        return lv_arr
    else:
        return 'WTF!'

def prepareTri(p_arr):
    lv_arrTri = []
    lv_itr = iter(p_arr)
    for t in range(1, (len(p_arr)/3+1)):
        lv_t = []
        for i in range(0, 3):
            lv_t.append(next(lv_itr))
        lv_arrTri.append([lv_t[0],lv_t[1]])
        lv_arrTri.append([lv_t[1],lv_t[2]])
        lv_arrTri.append([lv_t[2],lv_t[0]])
    return lv_arrTri

def findOposite(p_value):
    for t in p_value:
        lv_result = -1
        lv_itr = 0
        for i in p_value:
            if i != t:
                if t == [i[1],i[0]]:
                    lv_result = lv_itr
            lv_itr+=1
        print lv_result

#Graveyard of ideas
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
raw_input("")
