#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.

class Player:
    def __init__(self, checker):
        """ constructs a new Player object by initializing checker and num_moves.
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self. num_moves = 0

    def __repr__(self):
        """ returns a string representing a Player object.
        """
        s='Player '
        s+=self.checker
        return s

    def opponent_checker(self):
        """ this function returns a one-character string different than the 
            checker from object
        """
        if self.checker == "X":
            return "O"
        else:
            return "X"

    def next_move(self,b):
        """this functions returns the column where the player want to make next
           move. If not, it should print Try again!
        """
        self.num_moves+=1
        while True:
            col = int(input("Enter a column: "))
            if col>=0 and col <b.width:
                return col
            else:
                 print("Try again!")