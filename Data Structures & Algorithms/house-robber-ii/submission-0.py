class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] 

        memo_1 = [-1] * len(nums[:-1])
        memo_2 = [-1] * len(nums[1:])  

        def dfs(i, numbers, memo):
            if i >= len(numbers):
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(numbers[i] + dfs(i+2, numbers, memo), dfs(i+1, numbers, memo))
            return memo[i]

        return max(dfs(0, nums[:-1], memo_1), dfs(0, nums[1:], memo_2))