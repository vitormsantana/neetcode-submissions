func groupAnagrams(strs []string) [][]string {
	groups := make(map[string][]string)
	for _, word := range strs {
		signature := sortingg(word)
		groups[signature] = append(groups[signature], word)
	}

	fmt.Println(groups)

	grouped := [][]string{}

	for _, value := range(groups) {
		grouped = append(grouped, value)
	}
	return grouped
}

func sortingg(word string) string {
	letters := []rune(word)

	sort.Slice(letters, func(i, j int) bool {
		return letters[i] < letters[j]
	})

	return string(letters)
}