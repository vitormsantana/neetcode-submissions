class Solution:
    def rob(self, nums: List[int]) -> int:
        hash_table = {}
        def dfs(i):
            if i < 0 or i >= len(nums):
                return 0
            if i in hash_table:
                return hash_table[i]
            
            result = max(nums[i] + dfs(i + 2), dfs(i + 1))
            hash_table[i] = result
            return result
        
        return max(dfs(0), dfs(1))