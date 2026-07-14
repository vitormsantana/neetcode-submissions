class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if (summ % 2) != 0:
            return False
        
        target = summ / 2

        def dfs(i, currSum):
            if currSum == target:
                return True
            
            if i >= len(nums):
                return False
            
            if currSum + nums[i] <= target:
                return dfs(i + 1, currSum + nums[i])
            else:
                return dfs(i + 1, currSum)
        
        for i in range(len(nums)):
            if dfs(i, 0):
                return True
        return False