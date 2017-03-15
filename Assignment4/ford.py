import numpy
import sys

num1 = 1000
arr = numpy.loadtxt("g2.txt", dtype = int)
num2 = arr.shape[0]
incoming = dict()

for line in arr:
    if not incoming.has_key(line[1]-1):
        incoming[line[1] - 1] = dict()
    incoming[line[1] - 1][line[0] - 1] = line[2]

print incoming
#    mat[line[0] - 1, line[1] - 1] = line[2]
#    mat[line[1] - 1, line[0] - 1] = line[2]

a = numpy.zeros((num2, num1), dtype = int)
a[0, 0] = 0
for j in range(1, num1):
    a[0, j] = sys.maxsize

for i in range(1, num2):
    print i
    for j in range(0, num1):
        # Get all the incoming edges to node i
        edges = incoming[j]

        max_incoming = sys.maxsize
        for edge in edges:
            length = edges[edge]
            if a[i - 1, edge] == sys.maxsize:
                continue
            max_incoming = min(max_incoming, a[i - 1, edge] + length)

        a[i, j] = min(a[i - 1, j], max_incoming)

print a[num2 - 2, :]
print a[num2 - 1, :] == a[num2 - 2, :]
#print arr.shape