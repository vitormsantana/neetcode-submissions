func dailyTemperatures(temperatures []int) []int {
    stack := [][]int{}
    output := make([]int, len(temperatures))

    for i := range(temperatures) {
        if len(stack) > 0 && i > 0 {
            if stack[len(stack)-1][0] < temperatures[i] {
                for len(stack) > 0 && stack[len(stack)-1][0] < temperatures[i] {
                    output[stack[len(stack)-1][1]] = i - stack[len(stack)-1][1]
                    stack = stack[:len(stack) - 1] 
                }
            }
        }
        stack = append(stack, []int{temperatures[i], i})
    }

    return output
}
