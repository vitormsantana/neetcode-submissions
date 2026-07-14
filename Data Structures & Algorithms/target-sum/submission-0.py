class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i, currSum):
            if i >= len(nums):
                return 0
            
            currAnsw = 0
            if currSum + nums[i] == target and i == len(nums) - 1:
                currAnsw += 1
            if currSum - nums[i] == target and i == len(nums) - 1:
                currAnsw += 1
                
            return currAnsw + dfs(i + 1, currSum + nums[i]) + dfs(i + 1, currSum - nums[i])
        
        return dfs(0, 0)