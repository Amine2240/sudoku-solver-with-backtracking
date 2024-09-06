import time
puzzle=[
        [6,0,0,0,3,0,0,0,0],
        [0,0,0,0,0,0,5,0,4],
        [0,0,0,0,0,0,7,0,0],
        
        [0,0,0,9,0,5,0,0,0],
        [0,0,0,4,0,0,8,0,0],
        [8,0,0,0,0,0,0,6,0],
        
        [0,5,4,7,0,0,0,0,0],
        [0,0,0,0,6,0,0,8,0],
        [0,0,0,0,0,0,0,0,2]
        ]
# extremely hard puzzle (it is going to take some time)

def is_valid(board , row , col , num):   # existance of num in row or column or 3*3 matrix
  # existance of num in row or column 
  for i in range(9):
    if board[row][i] == num or board[i][col]==num:
      return False
  
  box_row = (row // 3 )*3
  box_col = (col // 3)*3
  for i in range(3):
    for j in range(3):
      if board[i + box_row][j+ box_col] == num:
        return False
      
      
  return True


def sudoku_solution(board):
  for row in range(9):
    for col in range(9):
      if board[row][col] == 0:
        for num in range(1,10):
          if is_valid(board , row , col, num):
            board[row][col] = num
            if sudoku_solution(board): # recursion for the next cell
              return True 
            board[row][col] = 0 # backtracking
            
        return False
  return True


def render_puzzle(board , text):
  print(f"puzzle {text} : ")
  for row in range(9):
    if row % 3 == 0 :
      print("   - - - - - - - - - - - - ")
    
    for col in range(9):
      if col % 3 == 0:
        print(' | ' ,end="") # prevent going to new line 
      
      if col == 8:
        print(board[row][col])
      else:
        print(str(board[row][col]) + " " ,end="")
      
  

render_puzzle(puzzle , "before")
start_time = time.time()
print("please wait...")
sudoku_solution(puzzle)
end_time = time.time()
render_puzzle(puzzle , "after")
exectution_time = end_time = start_time
print(f" execution time : {exectution_time:.6f} seconds")









