# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        
        for w in xrange(len(words)):
            word = list(words[w])
            i = 0
            j = len(word)-1
            while i <= j:
                temp = word[j]
                word[j] = word[i]
                word[i] = temp
                i += 1
                j -= 1
            word = ''.join(word)
            words[w] = word
        
        return ' '.join(words)
            
                
            