import numpy
import random
import time

arr = numpy.loadtxt("2sat6.txt", dtype = int)
min_value = abs(numpy.min(arr))
max_value = numpy.max(arr)

num = max(max_value, min_value)
print "Num = ", num

linked = dict()
for ind, line in enumerate(arr):
    i = abs(line[0])
    j = abs(line[1])
    if not linked.has_key(i):
        linked[i] = set()
    if not linked.has_key(j):
        linked[j] = set()

    linked[i].add(ind)
    linked[j].add(ind) 
is_found = False
for outer_loop in range(int(numpy.log2(num)) + 1):
    # Choose random initial assignment
    bools = num * [False]
    initial = random.sample(range(num), num / 2)
    for i in initial:
        bools[i] = True
    
    satisfied = set()
    unsatisfied = set()
    # Verify all the clauses and form two lists: satisfied and not satisfied clauses
    for ind, line in enumerate(arr):
        i = line[0]
        j = line[1]

        clause1 = bools[abs(i) - 1]
        if i < 0:
            clause1 = not clause1
 
        clause2 = bools[abs(j) - 1]
        if j < 0:
            clause2 = not clause2

        if clause1 or clause2:
            satisfied.add(ind)
        else:
            unsatisfied.add(ind)
    print "Init(satisfied) = ", len(satisfied)
    print "Init(unsatisfied) = ", len(unsatisfied)
    
    loop = 0
    while loop < 2 * num * num: 
        print "Inner loop = ", loop

        if len(unsatisfied) == 0:
            is_found = True
            print "Satisfied!"
            break
        else:
            # Pick the first unsatisfied case
            bad = unsatisfied.pop()
            val1 = arr[bad][0]
            val2 = arr[bad][1]
  
            if random.randint(0, 1) == 0:
                val = abs(val1)
            else:
                val = abs(val2)
         
            bools[val - 1] = (not bools[val - 1])
            satisfied.add(bad)
            
            for other in linked[val]:
                i = arr[other][0]
                j = arr[other][1]

                clause1 = bools[abs(i) - 1]
                if i < 0:
                    clause1 = not clause1
                clause2 = bools[abs(j) - 1]
                if j < 0:
                    clause2 = not clause2

                if clause1 or clause2:
                    satisfied.add(other)
                    if other in unsatisfied:
                        unsatisfied.remove(other)
                else:
                    unsatisfied.add(other)
                    if other in satisfied:
                        satisfied.remove(other)

        if is_found:
            break
        loop = loop + 1
    if is_found:
        break

if not is_found:
    print "Not satisfied!"
