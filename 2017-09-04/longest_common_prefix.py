# https://leetcode.com/problems/longest-common-prefix/description/

class Solution(object):
    def longestCommonPrefixBetweenTwoStrings(self, str1, str2):
        min_range = min(len(str1), len(str2))
        
        ret = []
        i = 0
        while i < min_range and str1[i] == str2[i]:
            ret.append(str1[i])
            i += 1
                
        return ret
            
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        
        if len(strs) == 1:
            return strs[0]
        
        pre = self.longestCommonPrefixBetweenTwoStrings(strs[0], strs[1])
        for i in xrange(2, len(strs)):
            pre = self.longestCommonPrefixBetweenTwoStrings(pre, strs[i])
            
        return ''.join(pre)
        