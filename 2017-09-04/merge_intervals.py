def are_intervals_overlapping(i1, i2):
	s1 = i1[0]
	e1 = i1[1]
	s2 = i2[0]
	e2 = i2[1]

	return e1 >= s2

def mergeIntervals(intervals):
	print "Intervals        ==>", intervals
	intervals = sorted(intervals, lambda i1, i2: cmp(i1[0], i2[0]))
	print "Sorted Intervals ==>", intervals

	ret = [intervals[0]]

	for i in xrange(1, len(intervals)):
		overlapping = are_intervals_overlapping(ret[-1], intervals[i])
		if overlapping:
			s = ret[-1][0]
			e1 = ret[-1][1]
			e2 = intervals[i][1]
			ret[-1] = (s, max(e1, e2))
		else:
			ret.append(intervals[i])

	return ret

print mergeIntervals([(3,5), (4,5), (1,2), (4,7), (0,1)])