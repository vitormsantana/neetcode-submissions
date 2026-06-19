class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sufix_arr = []
        prefix_arr = []

        for i in range(len(nums)):
            if i != 0:
                prefix_arr.append(nums[i-1]*prefix_arr[i-1])
            else:
                prefix_arr.append(1)
        print(f'prefix_arr: {prefix_arr}')

        for j in range(len(nums) - 1, -1, -1):
            if j != len(nums) - 1:
                sufix_arr = [nums[j+1]*sufix_arr[0]] + sufix_arr
            else:
                sufix_arr.append(1)
        print(f'sufix_arr: {sufix_arr}')

        res = []
        for k in range(len(nums)):
            res.append(prefix_arr[k] * sufix_arr[k])
        return res