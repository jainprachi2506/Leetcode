# https://leetcode.com/problems/can-place-flowers/description/

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) < n:
            return False
        
        if n <= 0:
            return True
        
        for i in xrange(len(flowerbed)):
            can_plant_left = True
            can_plant_right = True
            
            if flowerbed[i] == 0:
                if i > 0 and flowerbed[i-1] == 1:
                    can_plant_left = False
                
                if i < len(flowerbed)-1 and flowerbed[i+1] == 1:
                    can_plant_right = False
                    
                if can_plant_right and can_plant_left:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return False