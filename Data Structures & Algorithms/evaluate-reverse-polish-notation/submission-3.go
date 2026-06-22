//import "strconv"

func evalRPN(tokens []string) int {
    stack := []int{}
    p := 0
    currOpResult := 0

    for p < len(tokens) {
        if tokens[p] == "*" {
            currOpResult = stack[len(stack) - 2] * stack[len(stack) - 1] 
            stack = stack[:len(stack) - 2]
            stack = append(stack, currOpResult)

        } else if tokens[p] == "/" {
            currOpResult = stack[len(stack) - 2] / stack[len(stack) - 1] 
            stack = stack[:len(stack) - 2]
            stack = append(stack, currOpResult)

        } else if tokens[p] == "-" {
            currOpResult = stack[len(stack) - 2] - stack[len(stack) - 1] 
            stack = stack[:len(stack) - 2]
            stack = append(stack, currOpResult)

        } else if tokens[p] == "+" {
            currOpResult = stack[len(stack) - 2] + stack[len(stack) - 1] 
            stack = stack[:len(stack) - 2]
            stack = append(stack, currOpResult)

        } else {
            num, err := strconv.Atoi(tokens[p])
            if err != nil {
                return 0
            }
            stack = append(stack, num)
        }
        p += 1
    
    }
    return stack[0]
}