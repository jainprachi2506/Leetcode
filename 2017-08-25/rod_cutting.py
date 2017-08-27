def rod_cutting(lengths, prices, N):
	if len(lengths) == 0 or len(prices) == 0 or N == 0:
		return 0
	
	ret = 0
	
	for i, l in enumerate(lengths):
		if l <= N:
			ret = max(ret, prices[i] + rod_cutting(lengths, prices, N-l))
	return ret

print rod_cutting([1, 2, 3, 4, 5, 6, 7, 8], [1, 5, 8, 9, 10, 17, 17, 20], 4)



def rod_cutting_dp(lengths, prices, N):
	dp = [0]
	for i in xrange(1, N+1):
		vals = [0]
		for j, l in enumerate(lengths):
			if l <= i:
				dp.append(prices[j]+dp[i-l])
		dp.append(max(vals))

	return dp[-1]

print rod_cutting_dp([1, 2, 3, 4, 5, 6, 7, 8], [1, 5, 8, 9, 10, 17, 17, 20], 4)
