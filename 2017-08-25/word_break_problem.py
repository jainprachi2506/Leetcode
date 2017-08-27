def wbp(s, words):

	if len(words) == 0:
		return False

	if len(s) == 0:
		return True

	for word in words:
		if len(word) <= len(s) and word == s[len(s)-len(word):]:
			if wbp(s[:len(s)-len(word)], words):
				return True

	return False


def wbp_dp(s, words):
	# dp[i] = can i break s[0:i] into words
	# dp[0] = True
	# dp[1] = can i break 'W' into words = False
	# dp[2] = can i break 'Wo' into words = False
	# dp[3] = can i break 'Wor' into words = False
	# dp[4] = can i break 'Word' into words = True
	# dp[5] = can i break 'Wordb' into words = True
	dp = [True] # dp[0]
	# dp[1] .. dp[len(s)]
	for i in xrange(1, 1+len(s)):
		# s[0:i]
		dp.append(False) # dp[i]
		for word in words:
			if len(word) <= i and word == s[i-len(word):]:
				if dp[i-len(word)]:
					dp[i] = True
	return dp[-1]




words = ["this", "th", "is", "famous", "Word", "break", "b",
        "r", "e", "a", "k", "br", "bre", "brea", "ak", "problem"];

print wbp("Word", words)
