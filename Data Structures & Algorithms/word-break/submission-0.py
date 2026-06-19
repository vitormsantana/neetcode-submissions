class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
            def canConstruct(word, array, memo):
                if len(word) == 0:
                    return True

                if word in memo:
                    return memo[word]
                
                for part in array:
                    if len(part) <= len(word):
                        if part == word[:len(part)]:
                            if canConstruct(word[len(part):], array, memo):
                                memo[word] = True
                                return memo[word]
                        
                memo[word] = False
                return False
            return canConstruct(s, wordDict, {})