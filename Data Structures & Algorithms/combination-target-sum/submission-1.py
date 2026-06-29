class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(i, curr_sum, hash_table_subsets):
            if i >= len(nums) and curr_sum == target:
                if str(subset) not in hash_table_subsets:
                    res.append(subset.copy())
                    hash_table_subsets[str(subset.copy())] = True
                return

            if i >= len(nums):
                return
            
            if curr_sum > target:
                return

            subset.append(nums[i])
            dfs(i, curr_sum + nums[i], hash_table_subsets)
            dfs(i + 1, curr_sum + nums[i], hash_table_subsets)

            subset.pop()

            dfs(i + 1, curr_sum, hash_table_subsets)

        res = []
        subset = []

        dfs(0, 0, {})

        return res