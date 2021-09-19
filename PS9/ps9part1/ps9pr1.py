#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, height, width):
        self. height = height
        self. width = width
        self. slots= [[' ']* self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###

        s+=(self.width*2+1)*'-'+'\n'
        for i in range(self.width):
            if i>9:
                i=str(i)[-1]
            s+=" "+str(i)
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        i=0
        while i < self.height:
            if self.slots[self.height-1-i][col]==' ':
                self.slots[self.height-1-i][col]=checker
                i = self.height
            else:
                i+=1

    ### add your reset method here ###
    def reset(self):
        """ reset the Board object by setting all slots to contain
            a spsce character
        """
        self. slots= [[' ']* self.width for row in range(self.height)]


    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    def can_add_to(self, col):
        """this function returns True if it is valid to place a checker in the
            column col on the calling Board object. If the column number is too 
            high, too low, or full of checkers, it should return False. Otherwise,
            it should return True. 
        """
        if col<0 or col>=self.width:
            return False
        else:
            for i in range(self.height):
                if self.slots[i][col]==" ":
                    return True
        return False
    
    def is_full(self):
        """this functions return True is every slot is full with 'X' or 'O'
        """
        for i in range(self.width):
            if self.can_add_to(i):
                return False
        return True
    
    def remove_checker(self, col):
        """removes the ttop of checker from col if this column is not empty. 
        """
        i=0
        while i < self.height:
            if self.slots[i][col] !=' ':
                self.slots[i][col]=' '
                i = self.height
            else:
                i+=1

#Question 9
    def is_horizontal_win(self, checker):
        """ the funtion returns true if there are at least four consecutive 
            slots containing checker on the horizontal line
        """
        for i in range(self.height):
            for j in range(self.width-3):
                if self.slots[i][j]==checker:
                    if self.slots[i][j:j+4]==[checker]*4:
                        return True
        return False
    
    def is_vertical_win(self, checker):
        """the funtion returns true if there are at least four consecutive 
            slots containing checker on the vertical line
        """
        for i in range(self.width):
            for j in range(self.height-3):
                if self.slots[j][i] ==checker and \
                    self.slots[j+1][i] ==checker and \
                    self.slots[j+2][i] ==checker and \
                    self.slots[j+3][i] ==checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """the funtion returns true if there are at least four consecutive 
            slots containing checker on the diagonal line from up of left 
            to down of right
        """
        for i in range(self.width-3):
            for j in range(self.height-3):
                if self.slots[j][i]==checker and \
                   self.slots[j+1][i+1]==checker and \
                   self.slots[j+2][i+2]==checker and \
                   self.slots[j+3][i+3]==checker:
                       return True
        return False

    def is_up_diagonal_win(self, checker):
        """the funtion returns true if there are at least four consecutive 
            slots containing checker on the diagonal line from down of left 
            to up of right
        """
        for i in range(self.height-3):
            for j in range(3,self.width):
                if self.slots[i][j]==checker and \
                   self.slots[i+1][j-1]==checker and \
                   self.slots[i+2][j-2]==checker and \
                   self.slots[i+3][j-3]==checker:
                    return True
        return False

    def is_win_for(self, checker):
        """this function returns true if one of the four function about for one
        specific checker is ture. Otherwise, return false
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) or \
            self.is_vertical_win(checker) or \
            self.is_down_diagonal_win(checker) or \
            self.is_up_diagonal_win(checker):
                return True
        return False
