def knapsack(values, weights, limit):
	# with a limit of l and only using first i values/weights
	def knapsack_rec(l, i):
		ret = 0
		if i <= 0 or l <= 0:
			return ret
		ret = knapsack_rec(l, i-1)
		if weights[i-1] <= l:
			ret = max(ret, values[i-1] + knapsack_rec(l-weights[i-1], i-1))
		return ret
	return knapsack_rec(limit, len(values))

def create_matrix(a, b):
	dp = []
	for i in xrange(a):
		dp.append([])
		for j in xrange(b):
			dp[-1].append(0)
	return dp

def knapsack_dp(values, weights, limit):
	"""
	dp[l][i] = what is the maximum value we can obtain
	if we have a limit of l and we can use only i weights
	i.e weights[0:i]
	"""
	dp = create_matrix(limit+1, len(values)+1)
	for l in xrange(1, limit+1):
		for i in xrange(1, len(values)+1):
			dp[l][i] = dp[l][i-1]
			if weights[i-1] <= l:
				dp[l][i] = max(dp[l][i], dp[l-weights[i-1]][i-1] + values[i-1])
	return dp[limit][len(values)]



print knapsack_dp([ 20, 5, 10, 40, 15, 25 ], [ 1, 2, 3, 8, 7, 4 ], 10)

