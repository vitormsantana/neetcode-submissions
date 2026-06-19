func isValidSudoku(board [][]byte) bool {
	collumnsOk := false
	rowsOk := false

	for row := 0; row < 9; row++ {
		rowsOk = validateIfRowOkay(row, board)
		if rowsOk == false {
			return false
		}
	} 

	for column := 0; column < 9; column++ {
		collumnsOk = validateIfCollumnsOk(column, board)
		if collumnsOk == false {
			return false
		}
	} 

	return validateAllSquares(board)
}

func returnSquareIndex(x, y int) int {
	return (y/3) * 3 + (x/3)
}

func validateIfCollumnsOk(columnIndex int, board [][]byte) bool {
	hash_table_numbers := make(map[byte]bool)

	for row := 0; row < 9; row++ {
		if board[row][columnIndex] != '.' {
			if _, ok := hash_table_numbers[board[row][columnIndex]]; !ok {
				hash_table_numbers[board[row][columnIndex]] = true
			} else {
				return false
			}
		}
	}
	return true
}

func validateIfRowOkay(rowIndex int, board [][]byte) bool {
	hash_table_numbers := make(map[byte]bool)

	for column := 0; column < 9; column++ {
		if board[rowIndex][column] != '.' {
			if _, ok := hash_table_numbers[board[rowIndex][column]]; !ok {
				hash_table_numbers[board[rowIndex][column]] = true
			} else {
				return false
			}
		}
	}
	return true
}

func validateAllSquares(board [][]byte) bool {
	squares := make(map[int]map[byte]bool)

	for row := 0; row < 9; row++ {
		for column := 0; column < 9; column++ {
			val := board[row][column]

			if val == '.' {
				continue
			}

			squareIndex := returnSquareIndex(column, row)

			if _, ok := squares[squareIndex]; !ok {
				squares[squareIndex] = make(map[byte]bool)
			}

			if squares[squareIndex][val] {
				return false
			}

			squares[squareIndex][val] = true
		}
	}

	return true
}