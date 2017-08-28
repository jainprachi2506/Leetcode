# https://leetcode.com/problems/shopping-offers/description/

class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        dp = {}
        
        def calculate_price_regular(needs):
            cost = 0
            for i, need in enumerate(needs):
                cost += price[i]*need
            return cost
        
        def is_offer_useful(needs, offer):
            offer_cost = offer[-1]
            offer = offer[:-1]
            needs_new = []
            for i, need in enumerate(needs):
                if need < offer[i]:
                    return False
            return calculate_price_regular(needs) > offer_cost
        
        def needs_after_offer(needs, offer):
            needs_new = []
            for i, need in enumerate(needs):
                needs_new.append(need-offer[i])
            return needs_new
                
        def rec(needs):
            tup_needs = tuple(needs)
            if tup_needs in dp:
                return dp[tup_needs]
            min_price = calculate_price_regular(needs)
            for offer in special:
                if is_offer_useful(needs, offer):
                    needs_new = needs_after_offer(needs, offer)
                    price = rec(needs_new) + offer[-1]
                    if price < min_price:
                        min_price = price
            dp[tup_needs] = min_price
            return min_price
        
        return rec(needs)
                
            
            
        