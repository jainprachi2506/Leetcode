# For example, consider below subsequence
# 0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15

# Longest increasing subsequence is
# 0, 2, 6, 9, 11, 15

def lis_rec(s):
	def lis_rec_helper(i):
		if i == 0:
			return 1
		ret = 0
		j = 0
		while j < i:
			if s[i] > s[j]:
				ret = max(ret, lis_rec_helper(j)+1)
			j += 1
		return ret

	ret_max = 0
	for i in xrange(len(s)):
		temp = lis_rec_helper(i)
		if temp > ret_max:
			ret_max = temp

	return ret_max

def lis_dp(s):
	if len(s) == 0:
		return 0

	dp = [1]
	ret = 1
	for i in xrange(1, len(s)):
		res = 1
		for j in xrange(i):
			if s[i] > s[j]:
				res = max(res, dp[j]+1)
		dp.append(res)
		ret = max(ret, res)
	return ret


print lis_dp([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
print lis_rec([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
