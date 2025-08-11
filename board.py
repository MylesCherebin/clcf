class Board:
    def __init__(self):
        self.board =[ [' ', ' ', ' ', '', '', '', '']
         ['', '', '', '', '', '', ''],
         ['', '', '', '', '', '', ''],
         ['', '', '', '', '', '', ''],
        ['', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '']]

    def print(self):
        for i in range(5,-1,-1):
            row = '|'
            for j in range(7):
                row += self.board[i][j] + '|'
            print(row)