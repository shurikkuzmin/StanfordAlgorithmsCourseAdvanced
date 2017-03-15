import numpy

arr = numpy.loadtxt("clustering_big.txt", dtype = int)
length = 200000

nums = []
summas = []
dims = arr.shape
for i in range(0, dims[0]):
    num = 0
    summa = 0
    coeff = 1
    for j in range(23,-1,-1):
        summa = summa + arr[i,j]
        num = num + coeff * arr[i, j] 
        coeff = coeff * 2
    nums.append(num)
    summas.append(summa)

indices = []
classes = []
ones = []
unions = []
curUnion = 0
for i in range(0, 25):
    subset = []
    for j in range(0, len(summas)):
        if summas[j] == i:
            subset.append(j)
            indices.append(j)
            unions.append(curUnion)
    if len(subset) != 0:
        curUnion = curUnion + 1
        classes.append(subset)
        ones.append(summas[subset[0]])


leads = [-1 for i in range(0, length)]
for edge in range(1,3):

    for counter in range(0, length):
        lead = leads[counter]
        if lead == -1:
            leads[counter] = counter
            lead = counter

        index = indices[counter]
        curUnion = unions[counter]
        lenUnions = sum([len(classes[i]) for i in range(0, min(curUnion + edge + 1, len(classes)))])

        print "Counter = ", counter, lead, lenUnions
        counter2 = counter 
        while counter2 < lenUnions:
            # Find distance between two numbers
            index2 = indices[counter2]
        
            dist = 0
            for bit in range(0, 24):
                if arr[index, bit] != arr[index2, bit]:
                    dist = dist + 1 
            if dist == edge:
                if leads[counter2] != -1:
                    # Traverse and update the lead for everything
                    for j in range(0, lenUnions):
                        if leads[j] == leads[counter2]:
                            leads[j] = lead
                            print "Updating the lead", j, lead
                leads[counter2] = lead        
                print "Dist = ", counter2, dist, lead
            counter2 = counter2 + 1


# After that you need to go through and do a proper job with leads, every time substitute a new lead with something else
