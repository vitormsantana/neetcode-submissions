class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.answer = False

        def dfs(row, col, i, hash_table):
            if row >= len(board) or col >= len(board[0]) or row < 0 or col < 0:
                # print('false 1\n')
                return False
                
            if (row, col) in hash_table or i >= len(word) or self.answer == True:
                return
            
            if board[row][col] != word[i]:
                # print('false 2\n')
                return False

            hash_table[(row, col)] = True

            # print(f'hash_table: {hash_table}')

            if i == len(word) - 1 and board[row][col] == word[i]:
                self.answer = True
                # print(f'true\n')
                return True

            dfs(row + 1, col, i + 1, hash_table)
            dfs(row - 1, col, i + 1, hash_table)
            dfs(row, col + 1, i + 1, hash_table)
            dfs(row, col - 1, i + 1, hash_table)

            if (row, col) in hash_table:
                del hash_table[(row, col)]
        
        for j in range(len(board)):
            for k in range(len(board[0])):
                dfs(j, k, 0, {})
                if self.answer == True:
                    return True
        
        return False