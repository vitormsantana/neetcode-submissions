func maxArea(heights []int) int {
	i, j := 0, len(heights) - 1
	maxx := 0
	qty := 0

	for i < j {
		qty = (min(heights[j], heights[i]) * (j - i))
		maxx = max(maxx, qty)
		
		if heights[i] < heights[j] {
			i += 1
		} else {
			j -= 1
		}
	}

	return maxx
}
