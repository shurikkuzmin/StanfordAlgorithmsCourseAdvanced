import numpy
from operator import itemgetter

jobs = numpy.loadtxt("jobs.txt", dtype = int)
dims = jobs.shape

#indices = numpy.lexsort((jobs[:, 1], jobs[:, 0] - jobs[:, 1]))
ratio = numpy.array(jobs[:, 0], dtype=float) / jobs[:, 1]
print "Ratio = ", ratio
indices = numpy.argsort(ratio)
print "Indices = ", indices

jobs2 = numpy.array([[jobs[ind, 0] - jobs[ind, 1], jobs[ind, 0], jobs[ind, 1]] for ind in indices])

print "Jobs2 = ", jobs2

jobs3 = numpy.flipud(jobs2)

completion = 0
summation = 0
for row in jobs3:
    completion += row[2]
    summation += row[1] * completion

print "Summation = ", summation