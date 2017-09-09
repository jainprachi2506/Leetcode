# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        if not list1 or not list2:
            return []
        
        track = {}
        min_sum = len(list1) + len(list2)
        ret = []
        
        for i in xrange(len(list1)):
            track[list1[i]] = i
        
        for i in xrange(len(list2)):
            if list2[i] in track:
                index_sum = track[list2[i]] + i
                if index_sum < min_sum:
                    min_sum = index_sum
                    ret = [list2[i]]
                elif index_sum == min_sum:
                    ret.append(list2[i])
                    
        return ret