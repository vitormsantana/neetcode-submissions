class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        def backtracking(i, curr, nums):
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtracking(i + 1, curr, nums)
            curr.pop()

            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            backtracking(i + 1, curr, nums)
        backtracking(0, [], nums)
        return res
