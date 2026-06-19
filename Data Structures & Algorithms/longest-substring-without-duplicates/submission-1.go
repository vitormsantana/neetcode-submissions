func lengthOfLongestSubstring(s string) int {
	maxx := 0
	i, j, k := 0, 0, 0
	hash_table := make(map[byte]int)

	for k < len(s) {
		hash_table[s[k]] = 0
		k += 1
	}

	for j < len(s) {
		hash_table[s[j]] += 1
		if hash_table[s[j]] == 1 {
			j += 1
			maxx = max(maxx, j - i)
		} else {
			for i < j {
				if s[j] == s[i] {
					hash_table[s[j]] -= 1
					i += 1
					j += 1
					break
				} else {
					hash_table[s[i]] -= 1
					i += 1
				}
			}
		}
	}

	return maxx	
}