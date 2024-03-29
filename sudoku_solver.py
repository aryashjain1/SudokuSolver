class SudokuSolver:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def print_puzzle(self):
        # Function to print the Sudoku puzzle in a human-readable format
        for i in range(len(self.puzzle)):
            cur_line = ""
            for j in range(len(self.puzzle[i])):
                if self.puzzle[i][j] != 0:
                    cur_line += str(self.puzzle[i][j]) + " "
                else:
                    cur_line += "  "
            print(cur_line)

    def is_valid(self, row, col, value):
        # Function to check if a given value is valid in a given cell
        cur_row = self.puzzle[row][0:9]
        cur_col = [self.puzzle[i][col] for i in range(len(self.puzzle))]
        
        # Getting the row and column of the top left cell in the current box
        box_row_start, box_col_start = (row // 3) * 3, (col // 3) * 3
        box = []
        # Collecting and storing all of the cells in the current box
        for i in range(len(self.puzzle) // 3):
            box.append(self.puzzle[box_row_start+i][box_col_start:box_col_start+3])
        
        # Separate check for the box since it is it's own 2D list
        for r in box:
            if value in r:
                return False
        # Final check to see if the number can be in that position
        if value in cur_row or value in cur_col:
            return False
        return True

    def solve(self):
        # Function to solve the sudoku puzzle using recursion
        cur_row, cur_col = self.find_empty()

        # Base case: if the sudoku is filled, then return True
        if cur_row == -1 and cur_col == -1:
            return True
        
        # Testing multiple values in the current cell
        for num in range(1, len(self.puzzle) + 1):
            if self.is_valid(cur_row, cur_col, num):
                self.puzzle[cur_row][cur_col] = num

                # If the current value eventually leads to the final solution, the condition will be true, 
                # resulting in the end of the recursive loop.
                if self.solve():
                    return True
                
                # If the recursive call doesn't work (i.e., the puzzle isn't solved after the number above is placed),
                # then a different number will be tried in the next function call
                self.puzzle[cur_row][cur_col] = 0    
        return False


    def find_empty(self):
        # Function to return the row and column of the first cell in puzzle that is empty/0
        for r in range(len(self.puzzle)):
            for c in range(len(self.puzzle[r])):
                if self.puzzle[r][c] == 0:
                    return r, c
        return -1, -1


def check_puzzle(puzzle):
    # Criteria: 
    # 1) The number of rows and columns are equal
    # 2) Each row has the same number of columns
    num_rows = len(puzzle)
    num_cols = len(puzzle[0])
    cols_same = True
    for i in range(1, num_rows):
        cur_col_length = len(puzzle[i])
        if cur_col_length != num_cols:
            cols_same = False
    return num_rows == num_cols and cols_same

# Main code to test the Sudoku solver
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

puzzle = SudokuSolver(board)
puzzle.print_puzzle()
print()
if check_puzzle(board):
    if puzzle.solve():
        puzzle.print_puzzle()
    else:
        print("Unsolvable Puzzle. This sudoku doesn't have a possible solution.")
else:
    print("Invalid Puzzle. This sudoku isn't a square shape")

#print(puzzle.is_valid(2, 0, 1))