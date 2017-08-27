# def partition_rec(list):
# 	def partition(i, s):
# 		"""
# 		can we find a subset using the first i elements of the list
# 		such that sum is s
# 		"""
# 		if s == 0:
# 			return True
# 		if i == 0:
# 			return False
# 		# don't include the last element
# 		exclude = partition(i-1, s)
# 		# include the last element
# 		last_element = list[i-1]
# 		include = False
# 		if last_element <= s:
# 			include = partition(i-1, s-last_element)
# 		return include or exclude

# 	n = len(list)
# 	s = sum(list)
# 	if (s % 2) != 0:
# 		return  False
# 	return partition(n, s/2)


def partition_rec(list):
	def partition(i, s):
		if s == 0:
			return True
		if i == 0:
			return False

		exclude = partition(i-1, s)
		include = False
		if list[i-1] <= s:
			include = partition(i-1, s-list[i-1])

		return exclude or include

	if sum(list) % 2 != 0:
		return False
	return partition(len(list), sum(list))

def create_matrix(a, b):
	dp = []
	for i in xrange(a):
		dp.append([])
		for j in xrange(b):
			dp[-1].append(False)
	return dp

def partition_dp(list):
	s = sum(list)
	if s % 2 != 0:
		return False
	# dp[i][j] whether a subset exists whose
	# target sum is j and we can use first i elements from list
	# 0 <= i <= len(list)
	# 0 <= j <= s/2
	dp = create_matrix(len(list)+1, s/2+1)

	for i in xrange(1, len(dp)):
		dp[i][0] = True

	for i in xrange(1, len(dp)):
		for j in xrange(1, len(dp[0])):
			exclude = dp[i-1][j]
			include = False
			if list[i-1] <= j:
				include = dp[i-1][j-list[i-1]]
			dp[i][j] = exclude or include

	return dp[-1][-1]

print partition_rec([3,1,1,2,2,1]), partition_rec([3,1,1,2,2,1,1])
print partition_dp([3,1,1,2,2,1]), partition_rec([3,1,1,2,2,1,1])