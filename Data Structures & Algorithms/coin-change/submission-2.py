class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.minQty = 10000000
        visited = {}
        def dfs(i, currSum, qty):
            if currSum > amount:
                return
            if currSum in visited and visited[currSum] <= qty:
                return
            
            visited[currSum] = qty
            
            if currSum == amount:
                self.minQty = min(self.minQty, qty)
                return

            for i in range(len(coins)):
                dfs(i, currSum + coins[i], qty + 1)
        
        for i in range(len(coins)):
            dfs(i, 0, 0)
            if self.minQty != 10000000:
                return self.minQty
            return -1