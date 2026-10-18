class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        maxProfit = 0

        while j < len(prices):
            if prices[i] > prices[j]:
                i = j
            else:
                maxProfit = max(maxProfit, prices[j]-prices[i])
            j += 1
        
        return maxProfit


        # while i < j:
        #     while i<j and i<=len(prices) and j <= len(prices) and prices[i] > prices[j]:
        #         i += 1
        #         j += 1
            
        #     maxProfit = max(maxProfit, prices[j] - prices[i])
        
        # return maxProfit
