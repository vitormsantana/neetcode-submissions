class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(i, curr, nums):
                if i >= len(nums):
                    res.append(curr.copy())
                    return
                
                curr.append(nums[i])
                backtracking(i + 1, curr, nums)
                curr.pop()
                backtracking(i + 1, curr, nums)

        backtracking(0, [], nums)
        return res