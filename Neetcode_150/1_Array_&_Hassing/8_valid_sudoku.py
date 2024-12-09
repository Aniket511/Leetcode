"""
36. Valid Sudoku

Medium

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    # A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    # Only the filled cells need to be validated according to the mentioned rules.

Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Step 1: Initialize arrays to keep track of the numbers seen in each row, column, and 3x3 square.
        row_mask = [0] * 9  # Each element is a bitmask to track seen numbers in the corresponding row.
        col_mask = [0] * 9  # Each element is a bitmask to track seen numbers in the corresponding column.
        square_mask = [0] * 9  # Each element is a bitmask to track seen numbers in the corresponding 3x3 square.

        # Step 2: Iterate through each cell in the 9x9 board.
        for r in range(9):
            for c in range(9):
                # Step 3: Skip empty cells, represented by a ".".
                if board[r][c] == ".":
                    continue
                
                # Step 4: Convert the current cell value (which is a string) to an integer.
                num = int(board[r][c]) - 1  # Convert '1' to 0, '2' to 1, ..., '9' to 8 to convert to zero-based indexing

                # Step 5: Check if the number has already been seen in the current row, column, or square.
                # We use bitwise AND to check if the bit corresponding to the number is already set.
                if (1 << num) & row_mask[r]:
                    return False  # Number already found in the row
                if (1 << num) & col_mask[c]:
                    return False  # Number already found in the column
                if (1 << num) & square_mask[(r // 3) * 3 + (c // 3)]:
                    return False  # Number already found in the 3x3 square

                # Step 6: Mark the number as seen in the current row, column, and 3x3 square by setting the corresponding bit.
                row_mask[r] |= (1 << num)
                col_mask[c] |= (1 << num)
                square_mask[(r // 3) * 3 + (c // 3)] |= (1 << num)

        # Step 7: If no conflicts are found, the Sudoku board is valid.
        return True

# Time Complexity:
# O(1), because the board always has a fixed size of 9x9, so the time complexity is constant regardless of the input.

# Space Complexity:
# O(1), because the space used for row_mask, col_mask, and square_mask is constant, regardless of the input.

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Step 1: Initialize defaultdicts to store sets for rows, columns, and 3x3 squares
        rows = defaultdict(set)  # Tracks numbers seen in each row
        cols = defaultdict(set)  # Tracks numbers seen in each column
        squares = defaultdict(set)  # Tracks numbers seen in each 3x3 square

        # Step 2: Iterate through each cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                # Step 3: Skip empty cells represented by a "."
                if board[r][c] == ".":
                    continue
                
                # Step 4: Check if the current number has already been seen in the same row, column, or square
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False  # If it has been seen, the board is invalid
                
                # Step 5: Add the current number to the respective row, column, and square sets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        # Step 6: If no conflicts are found, the Sudoku board is valid
        return True

# Time Complexity:
# O(1), because the board always has a fixed size of 9x9, so the time complexity is constant regardless of the input.

# Space Complexity:
# O(1), because the space used for the defaultdicts storing the sets is constant, regardless of the input.

# Test case 1
board1 = [
    ["4","2",".",".","3",".",".",".","."],
    ["1",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
]
solution = Solution()
print(solution.isValidSudoku(board1))  # Expected output: True

# Test case 2
board2 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
solution = Solution()
print(solution.isValidSudoku(board2))  # Expected output: True

# Test case 3
board3 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
solution = Solution()
print(solution.isValidSudoku(board3))  # Expected output: False