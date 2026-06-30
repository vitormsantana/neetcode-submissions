class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(curr, opened, closed):
            if closed == opened and len(curr) == 2*n:
                res.append(curr)
                return
            if closed > opened:
                return
            
            if len(curr) > 2*n:
                return

            dfs(curr + '(', opened + 1, closed)
            dfs(curr + ')', opened, closed + 1)
        
        dfs('', 0, 0)
        return res