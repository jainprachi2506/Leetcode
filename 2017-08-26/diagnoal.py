def create_matrix(a, b, val):
	dp = []
	for i in xrange(a):
		dp.append([])
		for j in xrange(b):
			dp[-1].append(val)
	return dp

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = create_matrix(n, n, True)
        ret = n
        for j in xrange(1, n):
            i1 = 0
            j1 = j
            while i1 < n and j1 < n:
                # s[i1:j1+1] is a palindrome
                if s[i1] == s[j1] and dp[i1+1][j1-1]:
                    ret += 1
                    dp[i1][j1] = True
                else:
                    dp[i1][j1] = False
                i1 += 1
                j1 += 1
        #print dp
        return ret
            
        