import random
from board import Board
from colorama import Fore , Back

def bar(I,i): #function to formate a progress bar
    I = int(I*10/i)
    for j in range(10):
        if j<I:
            print(Fore.GREEN,'|',end='')
        else:
            print(Fore.RED,'-',end='')
    print(Fore.BLACK,end=' Score = ')
    print("(",I,"/",10,")")




def play(dim_size, num_bombs): #function to start a game

                board = Board(dim_size, num_bombs) # generate a board with size and number of bombs
                safe = True # declare a safe mode
                step = 0    # declare number of steps
                while len(board.dug) < board.dim_size ** 2 - num_bombs: # while digged cells less than unbombed cells
                    board.get_Board()
                    print(Back.LIGHTBLACK_EX,Fore.BLACK,"----------------- Cells -----------------")
                    print("----Step No.",Fore.GREEN, step + 1,Fore.BLACK, "------------------")
                    print("Total number of cells : ",Fore.GREEN, board.dim_size ** 2,Fore.BLACK) # number of cells
                    print("Number of cells that have been digged : ",Fore.BLUE, len(board.dug),Fore.BLACK) # number of digged cells
                    print("Number of cells that contains (Bombs) : ",Fore.RED, num_bombs,Fore.BLACK) # number of boombs in board
                    print("Number of cells that still undigged : ",Fore.GREEN, board.dim_size ** 2 - len(board.dug),Fore.BLACK) # number of digged cells  = number of cells - number of digged cells
                    print("Number of cells that still undigged and doesn't contain Bombs : ",Fore.GREEN, board.dim_size ** 2 - len(board.dug) - num_bombs,Fore.BLACK)
                    # number of undigged and not bombs cells   = number of cells - number of digged cells - number of boombs in board
                    bar(len(board.dug),(board.dim_size ** 2 - num_bombs))

                    user_input = input("Where would you like to dig? Input the index : \'0 to exit\'")  # e.g: 5

                    if user_input.isdigit(): # if user input is number
                        user_input = int(user_input) # convert user input type into int
                        row = int((int(user_input) - 1) / dim_size) # get the row index = ( user_input - 1 ) / dim_size
                        col = (int(user_input) - 1 - (dim_size * row)) # get the col index = user_input - 1 - (dim_size * row)
                        if user_input == 0: # if the user input = 0 end the game
                            break

                        if dim_size ** 2 < user_input < 0: # if user input is out of the range
                            print("Invalid index. Try again.")
                            continue

                        if user_input in board.dug:  # if user input is previously digged
                            print("Location is digged . Try again.")
                            continue

                        safe = board.board[row][col].dig(board) # check the safe value by digging the user input

                        if not safe:   # if the mode is not safe
                            break

                        step = step + 1  # increase the step value

                    else: # if user input is not a number
                        print("Please Enter a number . Try again.")
                        continue

                if user_input != 0: # if user input is 0

                    # 2 ways to end loop, lets check which one

                    if safe: # if the mode is safe
                        bar(len(board.dug), (board.dim_size ** 2 - num_bombs))

                        board.dug = [ ((board.dim_size * r) + c + 1) for r in range(board.dim_size) for c in range(board.dim_size)]
                        # dig every cell in board

                        board.reveal_all()
                        # reveal every cell in board
                        board.get_Board()
                        # show the board
                        print(Back.BLACK, Fore.GREEN, "CONGRATULATIONS!!!! YOU ARE VICTORIOUS!", Fore.WHITE)

                    else: # if the mode is not safe
                        bar(len(board.dug), (board.dim_size ** 2 - num_bombs))


                        board.dug = [((board.dim_size * r) + c + 1) for r in range(board.dim_size) for c in
                                     range(board.dim_size)]

                        # dig every cell in board
                        board.reveal_all()
                        # reveal every cell in board
                        board.get_Board()
                        # show the board
                        print(Back.BLACK,Fore.RED,"SORRY GAME OVER :(",Fore.WHITE)

                else:
                    print(Back.BLACK,Fore.RED,"Your game is ended",Fore.WHITE)
                    board.dug = [((board.dim_size * r) + c + 1) for r in range(board.dim_size) for c in
                                 range(board.dim_size)]
                    # dig every cell in board
                    board.reveal_all()
                    # reveal every cell in board
                    board.get_Board()
                    # show the board



if __name__ == '__main__':  # good practice :)
    while True:

        print("---------------- Minesweeper Game ---------------")
        print("1- New game ")
        print("2- Exit ")
        ch = input()
        if ch.isdigit():
            ch = int(ch)
            if ch == 1:
                while True:
                    size = input("Board size : ")
                    if size.isdigit():
                        size = int(size)
                        break
                    else:
                        print("Please Enter a number , try again ")

                while True:
                    level = input("Level of the game : \n 1- Easy  \n 2- Medium  \n 3- Difficult \n :")
                    if level.isdigit():
                        level = int(level)
                        if level == 1:
                            bombs = int(size * 0.5)
                            break
                        elif level == 2:
                            bombs = int(size)
                            break
                        elif level == 3:
                            bombs = int(size * 2)
                            break
                        else:
                            print("Out of the range , try again ")
                    else:
                        print("Please Enter a number , try again ")

                play(size, bombs)


            elif ch == 2:
                print("GOODBYE")
                break

            else:
                print("Invalid choice. Try again.")

        else:
            print("Please Enter a number . Try again.")
