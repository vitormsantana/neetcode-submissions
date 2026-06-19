class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def mergeSort(arr):
            def merge(left,right):
                condensed = []
                i, j = 0, 0
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        condensed.append(left[i])
                        i += 1
                    
                    else:
                        condensed.append(right[j])
                        j += 1
                
                while i < len(left):
                    condensed.append(left[i])
                    i += 1

                while j < len(right):
                    condensed.append(right[j])
                    j += 1
                
                return condensed

            if len(arr) <= 1:
                return arr

            mid_index = len(arr) // 2

            left_side = mergeSort(arr[:mid_index])
            right_side = mergeSort(arr[mid_index:])

            return merge(left_side, right_side)

        def backtracking(i, curr, total, hash_appearances, hash_res):
            if total == target:
                if str(curr.copy()) not in hash_res:
                    hash_res[str(curr.copy())] = True
                    res.append(curr.copy())
                    return

            if i >= len(candidates) or total > target:
                return
            
            if str([i, candidates[i]]) not in hash_appearances:
                curr.append(candidates[i])
                hash_appearances[str([i, candidates[i]])] = True
            
                backtracking(i, curr, total + candidates[i], hash_appearances, hash_res)
                curr.pop()
                del hash_appearances[str([i, candidates[i]])]
            backtracking(i+1, curr, total, hash_appearances, hash_res)
        
        candidates = mergeSort(candidates)
        backtracking(0, [], 0, {}, {})
        return res