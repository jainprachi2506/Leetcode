# https://leetcode.com/problems/judge-route-circle/description/

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        track = {'L': 0, 'R': 0, 'U': 0, 'D': 0}
        for m in moves:
            track[m] += 1
        
        return track['L'] == track['R'] and track['U'] == track['D']