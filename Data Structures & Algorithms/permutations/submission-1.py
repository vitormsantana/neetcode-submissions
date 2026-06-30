class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm, nums, pick):
            if len(nums) == len(perm):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if pick[i] == True:
                    continue
                perm.append(nums[i])
                pick[i] = True

                backtrack(perm, nums, pick)

                perm.pop()
                pick[i] = False

        backtrack([], nums, [None] * len(nums))
        return res