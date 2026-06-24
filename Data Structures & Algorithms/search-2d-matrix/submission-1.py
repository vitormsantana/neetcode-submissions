class Solution:
    def findPossibleRow(self, matrix, target):
        for row in matrix:
            if row[0] <= target and row[-1] >= target:
                return row
        return 0
    
    def binarySearch(self, row, target):
        l = 0
        r = len(row) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if row[mid] == target:
                return True
            
            if row[mid] < target:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return False
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        selectedRow = self.findPossibleRow(matrix, target)
        if selectedRow == 0:
            return False
        return self.binarySearch(selectedRow, target)