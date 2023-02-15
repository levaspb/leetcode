'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''

board0 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board1 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def isValidSudoku(board) -> bool:
        for line in range(len(board)):
            nodots_line = list(filter(lambda a: a != '.', board[line]))
            print(nodots_line)
            if len(nodots_line) != len(set(nodots_line)):
                return False
            string = list()
            for row in range(len(board[0])):
                if board[row][line] != '.':
                    string.append(board[row][line])
                print(string)
                if len(string) != len(set(string)):
                    return False
            # NOT FINISHED
        return True

def isValidSudokuNew(board) -> bool:
    for j in range(len(board)): # Horizontal
      line = list(filter(lambda a: a != '.', [i for i in board[j]]))
      if len(line) != len(set(line)):
        return False
    for j in range(len(board[0])): # Vertical
        line = list(filter(lambda a: a != '.', [board[i][j] for i in range(len(board[j]))]))
        if len(line) != len(set(line)):
          return False
    centers = [ [j,i] for j in [1,4,7] for i in [1,4,7] ]
    for point in centers:
        line = [ board[point[0]-1][point[1]-1], board[point[0]-1][point[1]], board[point[0]-1][point[1]+1],
                 board[point[0]][point[1]-1], board[point[0]][point[1]], board[point[0]][point[1]+1],
                 board[point[0]+1][point[1]-1],  board[point[0]+1][point[1]],  board[point[0]+1][point[1]+1]
               ]
        no_dots = list(filter(lambda a: a != '.', [i for i in line]))
        if len(no_dots) != len(set(no_dots)):
            return False 
    return True


#print(isValidSudoku(board0))
#print(isValidSudoku(board1))

print(isValidSudokuNew(board0))
print(isValidSudokuNew(board1))
