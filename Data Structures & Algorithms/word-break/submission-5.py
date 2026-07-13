class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = set()
        def dfs(currString):
            if currString == "":
                return True
            
            if currString in visited:
                return False
            
            visited.add(currString)
            for word in wordDict:
                if currString.startswith(word):
                    if dfs(currString[len(word):]) == True:
                        return True
            return False

        return dfs(s)
            