func productExceptSelf(nums []int) []int {
    prefixes_arr := make([]int, len(nums))
    sufixes_arr := make([]int, len(nums))
    results_arr := make([]int, len(nums))

    for i := range(len(nums)) {
        if i == 0 {
            prefixes_arr[i] = 1
        } else {
            prefixes_arr[i] = prefixes_arr[i-1] * nums[i-1]
        }
    }
    // fmt.Println(prefixes_arr)

// ------------------------------------------------------------

    for i := len(nums) -1; i >= 0; i-- {
        if i == len(nums) - 1 {
            sufixes_arr[i] = 1
        } else {
            sufixes_arr[i] = sufixes_arr[i+1] * nums[i+1]
        }
    }
    // fmt.Println(sufixes_arr)

// ------------------------------------------------------------

    for i := range(len(nums)) {
        results_arr[i] = prefixes_arr[i] * sufixes_arr[i]
    }

    return results_arr
}