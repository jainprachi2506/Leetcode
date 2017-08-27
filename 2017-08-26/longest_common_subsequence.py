# X: ABCBDAB
# Y: BDCABA

# The length of LCS is 4

def lcs(x, y):

	def lcs_rec(i, j):
		# what is the lcs of x[0:i] and y[0:j]
		if i == 0 or j == 0:
			return 0
		
		if x[i-1] == y[j-1]:
			return lcs_rec(i-1, j-1) + 1
		else:
			return max(lcs_rec(i, j-1), lcs_rec(i-1, j))

	return lcs_rec(len(x), len(y))


def create_matrix(a, b):
	dp = []
	for i in xrange(a):
		dp.append([])
		for j in xrange(b):
			dp[-1].append(0)
	return dp

def lcs_dp(x, y):
	dp = create_matrix(1+len(x), 1+len(y))
	for i in xrange(1, len(x)+1):
		for j in xrange(1, len(y)+1):
			if x[i-1] == y[j-1]:
				dp[i][j] = dp[i-1][j-1] + 1
			else:
				dp[i][j] = max(dp[i][j-1], dp[i-1][j])
	return dp[len(x)][len(y)]


print lcs_dp('ABCBDAB', 'BDCABA')
