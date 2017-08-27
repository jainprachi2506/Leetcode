# Longest common sub sequence
def lcs_rec(a, b):

	def lcs(i, j):
		if i == 0 or j == 0:
			return 0

		if a[i-1] == b[j-1]:
			return lcs(i-1, j-1) + 1
		else:
			return max(lcs(i, j-1), lcs(i-1, j))

	return lcs(len(a), len(b))


def create_matrix(a, b):
	dp = []
	for i in xrange(a):
		dp.append([])
		for j in xrange(b):
			dp[-1].append(0)
	return dp

def lcs(a, b):
	dp = create_matrix(len(a)+1, len(b)+1)

	for i in xrange(1, len(a)+1):
		for j in xrange(1, len(b)+1):
			if a[i-1] == b[j-1]:
				dp[i][j] = dp[i-1][j-1] + 1
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])

	return dp[-1][-1]

print lcs_rec('ABCBDAB', 'BDCABA')
print lcs('ABCBDAB', 'BDCABA')

