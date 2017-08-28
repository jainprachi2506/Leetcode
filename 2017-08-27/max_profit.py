# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        
        buy = prices[0]
        max_profit = 0
        for i in xrange(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit = prices[i] - buy
                if profit > max_profit:
                    max_profit = profit
                    
        return max_profit
            
            
        