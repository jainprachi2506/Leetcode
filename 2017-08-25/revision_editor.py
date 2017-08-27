def create_matrix(m, n):
	"""
	Creates a 2D array with default values 0
	Input (int, int)
	return [[]]
	"""
	dp = []
	for i in xrange(m):
		dp.append([])
		for j in xrange(n):
			dp[-1].append(0)

	return dp

def lcs(a, b):

	# create 2D array with padding
	dp = create_matrix(len(a)+1, len(b)+1)
	for i in xrange(1, len(a)+1):
		for j in xrange(1, len(b)+1):
			if a[i-1] == b[j-1]:
				dp[i][j] = dp[i-1][j-1]+1
			else:
				dp[i][j] = max(dp[i][j-1], dp[i-1][j])
	return dp[-1][-1]

if __name__ == '__main__':
	print lcs('ABCBDAB', 'BDCABA')
