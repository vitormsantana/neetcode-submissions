class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = float("inf")
        maxProfit = -float("inf")
        
        for i in range(len(prices)):
            minn = min(minn, prices[i])
            maxProfit = max(maxProfit, prices[i]-minn)

        return maxProfit
