def coin_change_problem_rec(coins, amount):
	# minimum number of coins to get exact c change
	def coin_change_problem(amount):
		if amount == 0:
			return 0
		if amount < 0:
			return -1
		retvals = []
		for coin in coins:
			if coin <= amount:
				remaining_amount = amount - coin
				retval = coin_change_problem(remaining_amount)
				if retval >= 0:
					retvals.append(1 + retval)
		if len(retvals) > 0:
			return min(retvals)
		else:
			return -1
	return coin_change_problem(amount)

print coin_change_problem_rec([2], 15)

