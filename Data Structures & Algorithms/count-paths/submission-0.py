class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        def cachedUniquePaths(m: int, n: int, memo_hash) -> int:
            if m == 1 and n == 1:
                return 1

            if m == 0 or n == 0:
                return 0

            if str([m, n]) in memo_hash:
                return memo_hash[str([m, n])]
            
            memo_hash[str([m, n])] = cachedUniquePaths(m-1, n, memo_hash) + cachedUniquePaths(m, n - 1, memo_hash)
            return memo_hash[str([m, n])]
        return cachedUniquePaths(m, n, {})
         