class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        sorted_nums = sorted(nums)

        def dfs(i, curr):
            if i >= len(sorted_nums):
                res.append(curr.copy())
                return
            
            curr.append(sorted_nums[i])
            dfs(i+1, curr)
            curr.pop()

            while i < len(sorted_nums) - 1 and sorted_nums[i] == sorted_nums[i+1]:
                i += 1
            dfs(i+1, curr)

        dfs(0, [])
        return res