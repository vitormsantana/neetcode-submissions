func isPalindrome(s string) bool {
	// fmt.Printf("Primeira Metade: %s\n", s[0:len(s)/2])
	// fmt.Printf("Segunda Metade: %s\n", reverseString(s)[0:len(s)/2])

	lowered := strings.ToLower(s)
	clean := cleanString(lowered)

	return clean[0:len(clean)/2] == reverseString(clean)[0:len(clean)/2]
}

func reverseString(s string) string {
	runes := []rune(s)

	for i, j := 0, len(runes) - 1; i < j; i, j = i + 1, j - 1{
		runes[i], runes[j] = runes[j], runes[i]
	}

	return string(runes)
}

func cleanString(s string) string {
	var result []rune
	for _, ch := range s {
		if unicode.IsLetter(ch) || unicode.IsDigit(ch) {
			result = append(result, ch)
		}
	}
	return string(result)
}