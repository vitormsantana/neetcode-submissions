class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        hash_memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            
            if amount in hash_memo:
                return hash_memo[amount]

            res = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            
            hash_memo[amount] = res 
            return res

        asnwer = dfs(amount)

        if asnwer == float("inf"):
            return -1
        return asnwer 