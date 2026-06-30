class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def mergeSort(array):
            if len(array) <= 1:
                return array

            mid = len(array) // 2
            left_side = array[:mid]
            right_side = array[mid:]

            left_merged = mergeSort(left_side)
            right_merged = mergeSort(right_side)

            return merge(left_merged, right_merged)

        
        def merge(left, right):
            l, r = 0, 0
            result = []

            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
                
            while l < len(left):
                result.append(left[l])
                l += 1

            while r < len(right):
                result.append(right[r])
                r += 1
            
            return result

        sorted_candidates = mergeSort(candidates)
        comb = []
        res = []

        def dfs(i, comb, curr_sum):
            if curr_sum == target:
                res.append(comb.copy())
                return

            if i == len(sorted_candidates) or curr_sum > target:
                return
            
            comb.append(sorted_candidates[i])
            dfs(i + 1, comb, curr_sum + sorted_candidates[i])

            comb.pop()

            while i < (len(sorted_candidates) - 1) and sorted_candidates[i] == sorted_candidates[i+1]:
                i += 1
            dfs(i + 1, comb, curr_sum)
        
        dfs(0, [], 0)

        return res


