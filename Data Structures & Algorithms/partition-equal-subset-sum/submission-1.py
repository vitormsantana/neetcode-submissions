class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if (summ % 2) != 0:
            return False
        
        target = summ / 2

        memo = {}

        def dfs(i, currSum):
            if currSum == target:
                return True
            
            if i >= len(nums):
                return False
            
            if (i, currSum) in memo:
                return memo[(i, currSum)]

            take = dfs(i + 1, currSum + nums[i])
            skip = dfs(i + 1, currSum)

            memo[(i, currSum)] = take or skip
            return memo[(i, currSum)] 

        for i in range(len(nums)):
            if dfs(i, 0):
                return True
        return False