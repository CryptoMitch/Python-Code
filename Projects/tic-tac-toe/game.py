# Code inspired by Kylie Ying Tutorial, but then made my own way

class TicTacToe:
    def __init__(self):
        # 3x3 board
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9] #single list to show 3x3 board
        self.current_winner = None #current winner - None is a built-in constant for nothingness
    
    def print_board(self):
        # split the board up into rows
        # use slice notation sequence[start:stop:step]
        # self is the instance of the class, board is the 3x3 grid
        # this divides the board into 3 slices called rows
        # the loop iterates 3 times with row_index taking values 0, 1, 2.
        for row in [self.board[row_index*3: (row_index+1)*3] for row_index in range(3)]:
            # row one is 1, 2, 3
            # row two is 4, 5, 6
            # row three is 7, 8, 9
            print('| ' + ' |' .join() + ' |')
            
    @staticmethod # Deco
    #to define static method in the class.     
    def print_board_numbers():
        # give the number in each row for each row
        number_board = [[str(column_index) for column_index in range(row_index*3, (row_index+1)*3)] for row_index in range(3)]
        for row in number_board:
            print('| ' + ' |' .join() + ' |')
    
    # Represent the available moves with a space
    def available_moves(self):
        # if spot is available append the index of that spot to move
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    