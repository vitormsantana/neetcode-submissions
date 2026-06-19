class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table_letters = {}

        for string_ in strs:
            hash_table_letters["".join(sorted(string_))] = hash_table_letters.get("".join(sorted(string_)), [])
            hash_table_letters["".join(sorted(string_))].append(string_)           
        
        result = []
        for word in hash_table_letters:
            result.append(hash_table_letters[word])
        return result