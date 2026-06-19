class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sufix = []
        diff = []
        maxx = -float("inf")

        for i in range(len(prices)):
            if i == len(prices) - 1:
                sufix.append(0)
            
            else:
                if len(prices[i+1:]) > 0:
                    sufix.append(max(prices[i+1:]))
            maxx = max(maxx, (sufix[i] - prices[i]))
        
        print(f'sufix: {sufix}')
        return max(0, maxx)


