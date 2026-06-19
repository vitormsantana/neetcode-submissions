class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [None] * len(cost)
        
        def dfs(i):
            if i >= len(cost):
                return 0
            
            if memo[i] is not None:
                return memo[i]
            
            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            print(f'memo: {memo}')
            print(f'-------')
            
            return memo[i]
        return min(dfs(0), dfs(1))