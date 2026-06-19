class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash_table = {}
        for i in range(0, len(nums)):
            hash_table[nums[i]] = True
        
        for i in range(0, len(nums) + 1, 1):
            if i not in hash_table:
                return i