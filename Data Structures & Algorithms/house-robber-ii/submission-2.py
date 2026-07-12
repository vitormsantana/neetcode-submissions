class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def dfs(i, numsArray, hash_table):
            if i >= len(numsArray):
                return 0
            if i in hash_table:
                return hash_table[i]
            
            result = max(numsArray[i] + dfs(i+2, numsArray, hash_table), dfs(i+1, numsArray, hash_table))
            hash_table[i] = result
            return result

        _0_from_first = dfs(0, nums[:-1], {})
        print(f'_0_from_first: {_0_from_first}')
        _1_from_first = dfs(1, nums[:-1], {})
        print(f'_1_from_first: {_1_from_first}')

        _0_from_second = dfs(0, nums[1:], {})
        print(f'_0_from_second: {_0_from_second}')
        _1_from_second = dfs(1, nums[1:], {})
        print(f'_1_from_second: {_1_from_second}')

        return max(_0_from_first, _1_from_first, _0_from_second, _1_from_second)