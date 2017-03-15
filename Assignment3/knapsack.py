import numpy

main_volume = 10000
#main_volume = 2000000
values = numpy.loadtxt("knapsack.txt", dtype = int)

volumes = values[:, 0]
weights = values[:, 1]
nums = values.shape[0]
#nums = 100


# Array approach
#arr = numpy.zeros((nums + 1, main_volume + 1), dtype = int)
#for i in range(1, nums + 1):
#    print i
#    for vol in range(1, main_volume + 1):
#        if vol >= weights[i - 1]:
#            arr[i, vol] = max(arr[i - 1, vol], arr[i - 1, vol - weights[i - 1]] + volumes[i - 1])
#        else:
#            arr[i, vol] = arr[i - 1, vol]
#print arr[nums, main_volume]

# Recurrent formulation
def find(i, volume):

    if i == -1:
        return 0

    if weights[i] < volume:
        return max(find(i - 1, volume), find(i - 1, volume - weights[i]) + volumes[i])
    else:
        return find(i - 1, volume)
#print find(nums - 1, main_volume)

# Brute force approach
arr = [dict() for i in range(0, nums)]
arr[0][weights[0]] = volumes[0]
for i in range(1, nums):
    print i
    old = arr[i - 1]
    new = arr[i]

    new[weights[i]] = volumes[i]
    for j in old:
        k = j + weights[i]
        if not (j in new):
            new[j] = old[j]
        else:
            new[j] = max(new[j], old[j])
        #new[j] = old[j]
        
        if k > main_volume:
            continue
        if k in old:
            #if k in new:
            #    new[k] = max(new[k], old[k], old[j] + volumes[i])
            #else:
            #    new[k] = max(old[k], old[j] + volumes[i])
            new[k] = max(old[k], old[j] + volumes[i])
        else:
            #if k in new:
            #    new[k] = max(new[k], old[j] + volumes[i])
            #else:
            #    new[k] = old[j] + volumes[i]
            new[k] = old[j] + volumes[i]

