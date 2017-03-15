import numpy

f = open("clustering.txt", "r")
num = 500
numClusters = 4

arr = []
for line in f:
    data = line.split()
    node1 = int(data[0]) - 1
    node2 = int(data[1]) - 1
    cost = int(data[2])
    arr.append([node1, node2, cost])

arr = sorted(arr, key = lambda edge: edge[2])

counter = 0
while counter < len(arr):
    # Check the lead for the current edge
    lead1 = arr[counter][0]
    lead2 = arr[counter][1]

    if lead1 == lead2:
        counter = counter + 1
        continue

    clusters = set()
        
    # Merge nodes - update all the nodes with with node2 id with node1
    for edge in arr:
        if edge[0] == lead2:
            edge[0] = lead1
        if edge[1] == lead2:
            edge[1] = lead1

        clusters.add(edge[0])
        clusters.add(edge[1])

    if len(clusters) == numClusters:
        break

    print "Counter = ", counter
    counter = counter + 1


print "Counter = ", len(clusters), clusters

maxSpacing = -1
counter = 0
while counter < len(arr):
    if arr[counter][0] != arr[counter][1]:
        if arr[counter][2] > maxSpacing:
            maxSpacing = arr[counter][2]
    
    counter = counter + 1
         
print "Spacing=", maxSpacing

