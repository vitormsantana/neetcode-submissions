class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        hash_table = {}
        for n in nums:
            hash_table[n] = True

        hash_table_starts = {}
        for n in nums:
            if n-1 not in hash_table:
                hash_table_starts[n] = True
        
        maxCount = 1
        count = 1
        for n in hash_table_starts:
            j = n
            while j + 1 in hash_table:
                count += 1
                j += 1
                maxCount = max(maxCount, count)
            count = 1

        return maxCount