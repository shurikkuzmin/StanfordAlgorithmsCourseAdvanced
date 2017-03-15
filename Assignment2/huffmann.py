import numpy

arr = numpy.loadtxt("clustering_big.txt", dtype = int)

dims = arr.shape
nums = set()
indices = dict()

print "Dims = ", dims[0], dims[1]
for i in range(0, dims[0]):
    num = 0
    coeff = 1
    for j in range(dims[1] - 1, -1, -1):
        num = num + arr[i, j] * coeff
        coeff = 2 * coeff
    if not (num in nums):
        nums.add(num)
        indices[num] = i 
    #else:
    #    print num, nums

#for num in nums:
#    print "Num = ", indices[num], num, arr[indices[num],:]

print "Lens = ", len(nums), len(indices)


perms = []
# Generate permutations
for i in range(0, dims[1]):
    perm = 2**i
    perms.append(perm)

counter = 0
for i in range(0, dims[1] - 1):
    for j in range(i + 1, dims[1]):
        perm = 2**i + 2**j
        counter = counter + 1

        perms.append(perm)

clusters = [{num} for num in nums]

for ind, num in enumerate(nums):
    print "Ind=",ind
    # Find an index of cluster where num is present
    clusterIndex = -1
    for cind, cluster in enumerate(clusters):
         if num in cluster:
             clusterIndex = cind
             break
    for perm in perms:
        newNum = num^perm
        # Check whether the new number is in dataset
        if newNum in nums:
            # Find a set where this newNum present and merge it with given
            newClusterIndex = -1
            for newCind, newCluster in enumerate(clusters):
                if newNum in newCluster:
                    newClusterIndex = newCind
                    break
            if clusterIndex == newClusterIndex:
                continue
           
            index = indices[num]
            newIndex = indices[newNum]

            #print arr[index,:], num
            #print arr[newIndex,:], newNum
            # Merge the current cluster with the found one
            tempCluster = clusters[clusterIndex].union(clusters[newClusterIndex])
            clusters[clusterIndex] = tempCluster
            # Delete current set
            clusters.pop(newClusterIndex)
            if newClusterIndex < clusterIndex:
                clusterIndex = clusterIndex - 1

print "Num Clusters = ", len(clusters)
#print "Clusters = ", clusters

# for cluster in clusters:
#     print "Cluster = ", cluster
#     for num1 in cluster:
#         for num2 in cluster:
#             if num2 != num1:
#                 print "Dist = ", numpy.binary_repr(num2^num1), numpy.binary_repr(num1^num2)

# Go through all the h

# class Tree(object):
#     def __init__(self):
#         self.left = None
#         self.right = None
#         self.data = None
#         self.init = self

#     def add_number(self, row, index):
#         node = self.init
#         dims = row.shape
#         for i in range(0, dims[0]):
#             if row[i] == 0:
#                 if node.left == None:
#                     node.left = Tree()
                
#                 node = node.left

#             elif row[i] == 1:
#                 if node.right == None:
#                     node.right = Tree()
                
#                 node = node.right
#             if i == dims[0] - 1:
#                 node.data = index

# clusters = Tree()

# for ind in range(0, length):
#     clusters.add_number(arr[ind, :], ind)

