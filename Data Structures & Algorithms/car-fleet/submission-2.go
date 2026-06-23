func carFleet(target int, position []int, speed []int) int {
	stack := []float64{}
	times := []float64{}
	positionSpeed := [][]float64{}

	for i := range position {
		positionSpeed = append(positionSpeed, []float64{
			float64(position[i]),
			float64(speed[i]),
		})
	}

	sortPositionSpeedDescending(positionSpeed)

	for i := range positionSpeed {
		time := (float64(target) - positionSpeed[i][0]) / positionSpeed[i][1]
		times = append(times, time)
	}

	for i := range times {
		if len(stack) == 0 || times[i] > stack[len(stack)-1] {
			stack = append(stack, times[i])
		}
	}

	return len(stack)
}

func sortPositionSpeedDescending(positionSpeed [][]float64) {
	sort.Slice(positionSpeed, func(i, j int) bool {
		return positionSpeed[i][0] > positionSpeed[j][0]
	})
}