import numpy


f = open("edges.txt", "r")
num = 500
arr = numpy.zeros((num, num), dtype = int)
arr.fill(10**10)

for line in f:
    data = line.split()
    row = int(data[0]) - 1
    column = int(data[1]) - 1
    cost = data[2]

    arr[row, column] = cost
    arr[column, row] = cost


# Dijkstra algorithm
processed = [0]
distance = 0

toContinue = True
while toContinue:
    minNode = -1
    minLen = 10**10
    for indNode1, node1 in enumerate(processed):
        for node2 in range(0, num):
            edge = arr[node1, node2]
            if not (node2 in processed):
                if edge < minLen:
                    minLen = edge
                    minNode = node2

        # Grow network by minNode
    if minNode == -1:
        toContinue = False
    else:
        toContinue = True
        processed.append(minNode)
        distance = distance + minLen
    print "Processed=",len(processed)

print "Distance=",distance