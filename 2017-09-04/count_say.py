# https://leetcode.com/problems/count-and-say/description/

import collections
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return 0
        
        seq = ['1']
        if n == 1:
            return seq[0]
        for i in xrange(1, n):
            prev = seq[-1]
            track = collections.OrderedDict()
            track[(0, prev[0])] = 1
            last = 0
            for j in xrange(1, len(prev)):
                if prev[j] == prev[j-1]:
                    track[(last, prev[j-1])] += 1
                else:
                    last = j
                    track[(last, prev[j])] = 1
            s = []
            for key, value in track.iteritems():
                s.append(str(value))
                s.append(str(key[1]))
            seq.append(''.join(s))
            
        return seq[-1]
        
        