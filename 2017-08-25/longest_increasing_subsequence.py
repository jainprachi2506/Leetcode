def lis_ending_at(a, i):
	if i == -1:
		return 0

	if i == 0:
		return 1

	j = 0
	res = 1
	while j < i:
		if a[i] > a[j]:
			res = max(res, 1+lis_ending_at(a, j))

		j += 1
	return res

def lis(a):
	lis_max = 0
	for i in xrange(len(a)):
		out = lis_ending_at(a, i)
		if out > lis_max:
			lis_max = out
	return lis_max

# def lis_dp(a):
# 	if len(a) == 0:
# 		return 0
# 	ret = 1
# 	dp = [1]
# 	for i in xrange(1, len(a)):
# 		result = 1
# 		for j in xrange(0, i):
# 			if a[j] < a[i]:
# 				result = max(result, 1 + dp[j])
# 		ret = max(ret, result)
# 		dp.append(result)
# 	return ret

def lis_dp(a):
	if len(a) == 0:
		return 0

	dp = [1]
	ret = 1
	for i in xrange(1, len(a)):
		res = 1
		for j in xrange(i):
			if a[j] < a[i]:
				res = max(res, dp[j]+1)
		dp.append(res)
		ret = max(ret, res)
	return ret


if __name__ == '__main__':
	print lis_dp([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])



	
