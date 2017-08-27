# shortest common supersequence

def scs_rec(a, b):

	def scs(i, j):
		if i == 0:
			return j

		if j == 0:
			return i

		if a[i-1] == b[j-1]:
			return scs(i-1, j-1) + 1
		else:
			return min(scs(i, j-1), scs(i-1, j)) + 1

	return scs(len(a), len(b))


def create_matrix(a, b):
	dp = []
	for i in xrange(a):
		dp.append([])
		for j in xrange(b):
			dp[-1].append(0)
	return dp

def scs_dp(a, b):
	dp = create_matrix(len(a)+1, len(b)+1)

	for i in xrange(1, len(a)+1):
		dp[i][0] = i

	for j in xrange(1, len(b)+1):
		dp[0][j] = j

	for i in xrange(1, len(a)+1):
		for j in xrange(1, len(b)+1):
			if a[i-1] == b[j-1]:
				dp[i][j] = dp[i-1][j-1] + 1
			else:
				dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1

	return dp[-1][-1]

print scs_rec('ABCBDAB', 'BDCABA')
print scs_dp('ABCBDAB', 'BDCABA')