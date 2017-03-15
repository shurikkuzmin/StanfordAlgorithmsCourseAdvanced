import numpy
import sys

num = 1000
arr = numpy.loadtxt("g3.txt", dtype = int)

incoming = dict()
mat = numpy.ones((num, num), dtype = int) * sys.maxsize
for line in arr:
    if not incoming.has_key(line[1]-1):
        incoming[line[1] - 1] = dict()
    incoming[line[1] - 1][line[0] - 1] = line[2]

    mat[line[0] - 1, line[1] - 1] = line[2]

print incoming

def matrix_formulation():
    a = numpy.zeros((num, num, num + 1), dtype = int)
    # Initialization
    for i in range(0, num):
        for j in range(0, num):
            if i == j:
                a[i, j, 0] = 0
            elif mat[i, j] != sys.maxsize:
                a[i, j, 0] = mat[i, j]
            else:
                a[i, j, 0] = sys.maxsize

    print "Initialization is done"

    for k in range(1, num + 1):
        print k
        for i in range(0, num):
            for j in range(0, num):
                if a[i, k - 1, k - 1] == sys.maxsize or a[k - 1, j, k-1] == sys.maxsize:
                    a[i, j, k] = a[i, j, k - 1]
                else:
                    a[i, j, k] = min(a[i, j, k - 1], a[i, k - 1, k - 1] + a[k - 1, j, k - 1])

    print a[:, :, num]
    print "Answer = ", numpy.min(a[:,:,num])

def dict_formulation():
    a = [dict() for i in range(0, num + 1)]

    # Initialization
    for i in range(0, num):
        for j in range(0, num):
            if not a[0].has_key(j):
                a[0][j] = dict()
            #if i == j:
            #    a[0][j][i] = 0
            #elif mat[i, j] != sys.maxsize:
            #    a[0][j][i] = mat[i, j]
            if mat[i, j] != sys.maxsize:
                a[0][j][i] = mat[i, j]

    for k in range(1, num + 1):
        print k
        b = a[k - 1]
        for j in b:
            if not a[k].has_key(j):
                a[k][j] = dict()

            #print "b[j] = ", b[j]
            for i in b[j]:
                #print "i = ", i
                if b.has_key(k - 1):
                    if b[k - 1].has_key(i) and b[j].has_key(k - 1):
                        a[k][j][i] = min(b[j][i], b[j][k - 1] + b[k-1][i])
                    else:
                        a[k][j][i] = b[j][i]
                else:
                    a[k][j][i] = b[j][i]

    min_value = sys.maxsize
    b = a[num]
    for j in b:
        for i in b[j]:
            if j == i:
                if b[j][i] < 0:
                    print "Negative cycle is detected " 
                    return
            min_value = min(min_value, b[j][i])

    print "Answer: ", min_value

matrix_formulation()
#dict_formulation()
