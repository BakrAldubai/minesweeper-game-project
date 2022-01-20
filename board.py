from cell import Cell
import random
from colorama import Fore, Back


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_board()
        self.assign_values_to_board()

        self.dug = set()
        # if we dig at 10 , then self.dug = {10}

    def make_board(self):
        # construct a new board based on the dim size and num bombs


        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                index = (r * self.dim_size) + c + 1
                board[r][c] = Cell(index, self.dim_size)

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size ** 2 - 1)
            # return a random integer N such that a <= N <= b
            row = loc // self.dim_size # we want the number of times dim_size goes into loc to tell us what row to look at
            col = loc % self.dim_size  # we want the remainder to tell us what index in that row to look at

            if board[row][col].bomb:
                # this means we've actually planted a bomb there already so keep going
                continue

            board[row][col].make_it_bomb()  # plant the bomb
            bombs_planted += 1

        return board

    def get_Board(self):

        print()
        for r in range(self.dim_size):
            print(Back.BLACK, end='')
            print(Fore.WHITE, '-------' * self.dim_size + '-')
            print(Fore.WHITE, '|', end='')
            for c in range(self.dim_size):
                if str(self.board[r][c]).startswith('-'):
                    print(Fore.GREEN, str(self.board[r][c]).strip('-'), Fore.WHITE, end='|')
                elif '#' in str(self.board[r][c]):
                    print(Back.RED, str(self.board[r][c]), Back.BLACK, Fore.WHITE, end='|')
                else:
                    print(Fore.YELLOW, str(self.board[r][c]), Fore.WHITE, end='|')
            print()
        print(Fore.WHITE, '-------' * self.dim_size + '-')

    def assign_values_to_board(self):

        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c].bomb:
                    # if this is already a bomb, we don't want to calculate anything
                    continue
                self.board[r][c].put_num_of_neighboring_bombs(self.get_num_neighboring_bombs(r, c))

    def get_num_neighboring_bombs(self, row, col):


        num_neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):

            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if r == row and c == col:
                    # our original location, don't check
                    continue
                if self.board[r][c].bomb:
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def reveal_all(self):  # reveal all cells in the board
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c].bomb:
                    self.board[r][c].visable = True














                     
        



    
    
    
