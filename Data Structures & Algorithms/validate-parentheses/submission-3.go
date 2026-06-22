func isValid(s string) bool {
    q := []rune{}

    if len(s) < 2  || len(s) % 2 != 0 {
        return false
    }

    for _, char := range s {
        if char == '}' {
            if len(q) == 0 || q[len(q) - 1] != '{' {
                return false
            } else {
                q = q[:len(q) - 1]
            }
        } else if char == ']' {
            if len(q) == 0 || q[len(q) - 1] != '[' {
                return false
            } else {
                q = q[:len(q) - 1]
            }
        } else if char == ')' {
            if len(q) == 0 || q[len(q) - 1] != '(' {
                return false
            } else {
                q = q[:len(q) - 1]
            }
        } else {
            q = append(q, char)
        }
    }

    return len(q) == 0 
}
