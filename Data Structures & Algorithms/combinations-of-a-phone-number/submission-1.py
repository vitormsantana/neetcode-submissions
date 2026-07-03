class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_numbers_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        
        def backtracking(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return

            for letter in (hash_numbers_letters[digits[i]]):
                backtracking(i + 1, curr + letter)
        
        if digits:
            backtracking(0, '')
        return res