class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_sequence = {}
        longg = 1
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        nums = sorted(nums)
        for n in range(len(nums)):
            if nums[n] - 1 in hash_sequence:
                hash_sequence[nums[n]] = hash_sequence[nums[n]-1] + 1
                longg = max(longg, hash_sequence[nums[n]])
            else:
                hash_sequence[nums[n]] = 1
        return longg