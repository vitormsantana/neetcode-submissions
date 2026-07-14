class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, qty):
            if i >= len(coins) or qty > amount:
                return 0

            if (i, qty) in memo:
                return memo[(i, qty)]

            if qty == amount:
                memo[(i, qty)] = 1
                return 1

            memo[(i, qty)] = dfs(i, qty + coins[i]) + dfs(i + 1, qty)
            return memo[(i, qty)] 
                
        return dfs(0, 0)