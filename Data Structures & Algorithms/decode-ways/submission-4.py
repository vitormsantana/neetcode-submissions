class Solution:
    def numDecodings(self, s: str) -> int:
        hash_table = {} 
        def dfs(i):
            if i == len(s):
                return 1
            
            if i > len(s) or s[i] == '0':
                return 0
            
            if i+1 in hash_table:
                next_one = hash_table[i+1]   
            else:
                next_one = dfs(i + 1) 
                hash_table[i+1] = next_one

            next_two = 0
            if i < len(s) - 1 and 10 <= int(s[i:i+2]) < 27:
                next_two = dfs(i + 2)
            return next_one + next_two
        
        return dfs(0)