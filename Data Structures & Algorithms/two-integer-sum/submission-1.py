class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_table:
                if i < hash_table[target - nums[i]]:
                    return [i, hash_table[target - nums[i]]] 
                return [hash_table[target - nums[i]], i] 
            else:
                hash_table[nums[i]] = i