# https://leetcode.com/problems/palindromic-substrings/description/
def create_matrix(a, b):
	dp = []
	for i in xrange(a):
		dp.append([])
		for j in xrange(b):
			dp[-1].append(True)
	return dp

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = create_matrix(n, n)
        
        ret = n
        for j in xrange(1, n):
            i1 = 0
            j1 = j
            while i1 < n and j1 < n:
                if s[i1] == s[j1] and dp[i1+1][j1-1]:
                    ret += 1
                else:
                    dp[i1][j1] = False
                
                i1 +=1 
                j1 +=1 
            
        return ret
        