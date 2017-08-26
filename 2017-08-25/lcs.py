def create_array(m, n):
	dp =[]
	for i in xrange(m):
		dp.append([])
		for j in xrange(n):
			dp[-1].append(0)
	return dp

def lcs(a, b):
	# get a 2d array of len(a)+1 and len(b) + 1
	dp = create_array(len(a)+1, len(b)+1)
	for i in xrange(1, len(a)+1):
		for j in xrange(1, len(b)+1):
			if a[i-1] == b[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i][j-1], dp[i-1][j])

	return dp[-1][-1]

if __name__ == '__main__':
	print lcs('12341', '341213')