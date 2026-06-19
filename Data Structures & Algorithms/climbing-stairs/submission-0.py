class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [None] * (n+1)

        if n == 0 or n == 1 or n == 2:
            return n
         
        memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return memo[n]
        
