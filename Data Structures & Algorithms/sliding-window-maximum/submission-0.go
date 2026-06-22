func maxSlidingWindow(nums []int, k int) []int {
    output := []int{}
    l, r := 0, 0
    q := []int{}

    for r < len(nums) {
        for len(q) > 0 && nums[r] > nums[q[len(q)-1]] {
            q = q[:len(q)-1]
        }
        q = append(q, r)

        if l > q[0] {
            q = q[1:]
        }

        if (r+1) >= k {
            output = append(output, nums[q[0]])
            l += 1
        }
        r += 1
    }

    return output
}
