class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table_s = {}
        hash_table_t = {}
        
        for letter in s:
            hash_table_s[letter] = hash_table_s.get(letter, 0) + 1
        
        for letter in t:
            hash_table_t[letter] = hash_table_t.get(letter, 0) + 1

        return hash_table_s == hash_table_t