# https://leetcode.com/problems/number-of-boomerangs/description/

class Solution(object):    
    def dist(self, p1, p2):
        return ((p1[0] - p2[0])*(p1[0] - p2[0])) + ((p1[1] - p2[1])*(p1[1] - p2[1]))

    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sum_dist = 0
        for p1 in points:
            d = {}
            for p2 in points:
                if p1 != p2:
                    distance = self.dist(p1, p2)
                    if distance not in d:
                        d[distance] = [p2]
                    else:
                        d[distance].append(p2)
            for k, v in d.iteritems():
                sum_dist += len(v)*(len(v)-1)
                
        return sum_dist