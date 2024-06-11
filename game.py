from car import *
from helper import *
from board import *
import sys


class Game:
    """
    Add class description here
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.__gameboard = board
        # You may assume board follows the API
        # implement your code and erase the "pass"
        # pass

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """

        #if self.__gameboard.cell_content((3, 7)) != None:
            #print("the game ended")
         #   return
        move = input(
            " what color car to move, and what direction to move it? (ex 'Y,r')\nYour input:\n")
        name_possible = ['Y', 'B', 'O', 'W', 'G', 'R']
        direction_possible = ['r', 'u', 'l', 'd']
        if move == "!":
            return "end_game"
        if len(move) < 3 or len(move) > 3 or move[1] != ',':
            print("error")
            return

        name = move[0]
        direction = move[2]
        if name not in name_possible or direction not in direction_possible:
            print("error")
            return

        a = self.__gameboard.move_car(name, direction)
        if a == False:
            print("error")
        # implement your code and erase the "pass"
        # pass

    def play(self):
        while 1!= 0:
            print(self.__gameboard)
            if self.__gameboard.cell_content(self.__gameboard.target_location()) != None:
                print("the game ended")
                return
            a = self.__single_turn()

            if a == "end_game":
                return



        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        # implement your code and erase the "pass"
        #pass


if __name__ == "__main__":
    # Your code here
    # All access to files, non API constructors, and such must be in this
    # section, or in functions called from this section.
    # implement your code and erase the "pass"
    board=Board()
    n = len(sys.argv)
    # print(n)

    if n != 2:
        print("error!!!")
        exit()
    path=sys.argv[1]
    dir=load_json(path)
    colors_cars=["Y","B","O","W","G","R"]
    for i in dir:
        if i in colors_cars and 2<=dir[i][0]<=4 and -1<dir[i][2]<2:
            #print(i,dir[i][0],dir[i][1],dir[i][2])
            a=Car(i,dir[i][0],dir[i][1],dir[i][2])
            board.add_car(a)
    print(board.possible_moves())
    game=Game(board)

    game.play()
    #pass
