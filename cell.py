class Cell:
    def __init__(self,index,d): # constructor
        self.index = index # index of cell
        self.bomb = False # is it a bomb
        self.visable = False # is it visable
        self.num_neighboring_bombs = 0 # numbers of neighboring bombs
        self.row = int((index - 1) / d) # row index
        self.col = int(index - 1 - (d * self.row)) # column index
    
    def __str__(self):  # printing cell object
        s = ""
        if self.visable:
            if self.bomb:
                s = "#".center(3)
            else:
                if self.num_neighboring_bombs == 0 :
                    s = " ".center(4)
                else:
                    s = str("-"+str(self.num_neighboring_bombs).center(4))
        else:
            s = str(self.index).center(4)

        return str(s)

    def make_it_bomb(self):
        self.bomb = True

    def make_it_visible(self):
        self.visable = True

    def put_num_of_neighboring_bombs(self, n ):
        self.num_neighboring_bombs = n

    def dig(self,Board): # dig method
        self.visable = True
        Board.dug.add(self.index)
        if self.bomb : # if it is bomb
            return False
        elif self.num_neighboring_bombs > 0 :
            return True
        # dig neighbors
        for r in range(max(0, self.row-1), min(Board.dim_size-1, self.row+1)+1):
            for c in range(max(0, self.col-1), min(Board.dim_size-1, self.col+1)+1):
                i = (Board.dim_size * r) + c + 1
                if i in Board.dug:
                    continue # don't dig where you've already dug
                Board.board[r][c].dig(Board)

        # if our initial dig didn't hit a bomb, we *shouldn't* hit a bomb here
        return True











                
            
    
        