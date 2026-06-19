func twoSum(numbers []int, target int) []int {
	i := 0
	j := len(numbers) - 1
	result := []int{}

	for i < j {
		if numbers[i] + numbers[j] < target {
			i += 1
		} else if numbers[i] + numbers[j] > target {
			j -= 1
		} else {
			result = append(result, i+1)
			result = append(result, j+1)
			return result
		}
	}
	return nil
}
