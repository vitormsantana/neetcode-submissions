func maxArea(heights []int) int {
	maxAmount := 0
	currAmount := 0
	i := 0
	j:= len(heights) - 1

	for i < j {
		currAmount = calculateArea(i, j, heights)
		if currAmount > maxAmount {
			maxAmount = currAmount
		}
		if heights[i] < heights[j] {
			i ++
		} else {
			j --
		}
	}
	return maxAmount
}

func calculateArea(i, j int, heights []int) int {
	return (j - i) * (min(heights[i], heights[j]))
}