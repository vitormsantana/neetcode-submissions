func searchMatrix(matrix [][]int, target int) bool {
    selectedRow := findPossibleRow(matrix, target)
    if selectedRow == nil {
        return false
    }
    return binarySearch(selectedRow, target)
}

func findPossibleRow(matrix [][]int, target int) []int {
    for _, row := range(matrix) {
        if row[0] <= target && row[len(row)-1] >= target {
            return row
        }
    }

    return nil
}

func binarySearch(row []int, target int) bool {
    l := 0
    r := len(row) - 1
    mid := 0

    for l <= r {
        mid = l + (r - l) / 2

        if target == row[mid] {
            return true
        }

        if target < row[mid] {
            r = mid - 1
        } else {
            l = mid + 1
        }
    }

    return false
}