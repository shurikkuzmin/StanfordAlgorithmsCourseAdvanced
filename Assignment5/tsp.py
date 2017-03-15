import numpy
import itertools

data = numpy.loadtxt("tsp.txt")

num = data.shape[0]
print "Num = ", num

indices = range(1, num)

#combinations = []
#for num_set in range(1, num ):
#    for subset in itertools.combinations(indices, num_set):
#        subset = list(subset)
#        subset.insert(0,0)
#        combinations.append(subset)
a = numpy.zeros((2**num + 1, num))
for m in range(0, num):
    if m == 0:
        a[1, 0] = 0
    else:
        a[2**m, 0] = 1e30

for m in range(1, num):
    print m
    for subset in itertools.combinations(indices, m):
        
        # Prepare a code for the combination
        ind = 0
        for sub in subset:
            ind = ind + 2**sub
        ind = ind + 1

        #print "Subset = ", list(subset), ind

        
        for node in subset:
            subset2 = list(subset)
            subset2.remove(node)

            ind2 = 0
            for sub in subset2:
                ind2 = ind2 + 2**sub
            ind2 = ind2 + 1

            #print "Subset2 = ", subset2, ind2

            min_value = 1e30
            if len(subset2) == 0:
                a[ind, node] = numpy.sqrt((data[node, 0] - data[0, 0])**2 + (data[node, 1] - data[0, 1])**2)
            else:    
                for node2 in subset2:
                    dist = numpy.sqrt((data[node2, 0] - data[node, 0])**2 + (data[node2, 1] - data[node, 1])**2) 
                    #print "Node1/2/Dist", node, node2, dist, a[ind2, node2]
                    min_value = min(min_value, a[ind2, node2]+ dist)
            
                a[ind, node] = min_value

            #print "A[ind, node]=", ind, node, a[ind, node]

distances = [numpy.sqrt((data[i, 0]-data[0, 0])**2 + (data[i, 1] - data[0, 1])**2) for i in range(1,num)]
print "Distances = ", distances
print "Min = ", numpy.min(a[2**num - 1, 1:] + distances)
