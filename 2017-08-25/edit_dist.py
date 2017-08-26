def edit_dist(a, b):
	if len(a) == 0:
		return len(b)

	if len(b) == 0:
		return len(a)

	if a[-1] == b[-1]:
		return edit_dist(a[:len(a)-1], b[:len(b)-1])
	else:
		return min(
			edit_dist(a[:len(a)-1], b[:len(b)-1]), 
			edit_dist(a[:len(a)], b[:len(b)-1]), 
			edit_dist(a[:len(a)-1], b[:len(b)])
			) + 1

# rows / cols
def create_matrix(a, b):
	dp = []
	for i in xrange(a):
		dp.append([])
		for j in xrange(b):
			dp[-1].append(0)

	return dp

def edit_dist_dp(a, b):
	dp = create_matrix(len(a)+1, len(b)+1)

	dp[0][0] = 0

	for j in xrange(1, len(b)+1):
		dp[0][j] = j

	for i in xrange(1, len(a)+1):
		dp[i][0] = i

	for i in xrange(1, len(a)+1):
		for j in xrange(1, len(b)+1):
			if a[i-1] == b[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

	return dp[-1][-1]

if __name__ == '__main__':
	print edit_dist_dp('kitten', 'sitting')

