
red = '🔴'
yellow = '🟡'
player1 = ''
player2 = ''
win = {'🔴': 'Red Player Wins!', '🟡': 'Yellow Player Wins!'}
t = [red,yellow,red,yellow,red,yellow,red]

board =[ t,#['  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  '],
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ']]

def print_board():
    for i in range(5,-1,-1):
            row = '|'
            for j in range(7):
                row += board[i][j] + '|'
            print(row)
    print('______________________')

def game_over():
     #check rows
     for row in board:
          count = 0
          last = ''
          for position in row:
               if position != '  ' and position == last:
                    count += 1
                    if count == 4:
                        return win[position]
               else:
                    count = 1
                    last = position

     #check cols
     for i in range(6):
          count = 0
          last = ''
          for row in board:
               position = row[i]
               if position != '  ' and position == last:
                    count += 1
                    if count == 4:
                        return win[position]
               else:
                    count = 1
                    last = position

     #check diagonals

     #right down
     for i in range(6):
          for j in range(7):
               if i >= 3 and j <= 3:
                    position = board[i][j]
                    if position != '  ' and board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == position:
                         return win[position]
                    
     for i in range(6):
          for j in range(7):
               if i < 3 and j <=3:
                    position = board[i][j]
                    if position != '  ' and board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == position:
                         return win[position]
               

     return ''

def make_move(turn, col):
     for row in board:
          if row[col] != '  ':
               row[col] = turn
     
        

if __name__ == "__main__":
    p1 = input("Player 1, please choose your color. Type 'r' for Red, and 'y' for Yellow").strip()
    while p1 not in 'ry':
         p1 = input("Please type either 'r' for Red or 'y' for Yellow").strip()
    
    if p1 == 'r':
         player1 = red
         player2 = yellow
    else:
         player1 = yellow
         player2 = red

    turn = 1
    while not game_over():
        move = input('Pick a column 1-7')
        
    print_board()
     #print(board[0][0])
    