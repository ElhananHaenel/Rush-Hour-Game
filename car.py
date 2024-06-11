class Car:
    """
    Add class description here
    """

    def __init__(self, name, length, location, orientation):
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, 
        col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        # Note that this function is required in your Car implementation.
        # implement your code and erase the "pass"

    def car_coordinates(self):
        loc = self.__location
        size = self.__length
        dierction = self.__orientation
        if dierction == 1:
            x = loc[1]
            list_location = []
            for i in range(size):
                list_location.append((loc[0], x))
                x += 1
        elif dierction == 0:
            y = loc[0]
            list_location = []
            for i in range(size):
                list_location.append((y,loc[1]))
                y += 1
        return list_location
        """
        :return: A list of coordinates the car is in
        """
        # implement your code and erase the "pass"
        # pass

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
        permitted by this car.
        """
        if self.__orientation == 0:
            return {'u': "cause the car move up one step",
                    'd': "cause the car move down one step"}
        elif self.__orientation == 1:
            return {'r': "cause the car move right one step",
                    'l': "cause the car move left one step"}
        # For this car type, keys are from 'udrl'
        # The keys for vertical cars are 'u' and 'd'.
        # The keys for horizontal cars are 'l' and 'r'.
        # You may choose appropriate strings.
        # implement your code and erase the "pass"
        # The dictionary returned should look something like this:
        # result = {'f': "cause the car to fly and reach the Moon",
        #          'd': "cause the car to dig and reach the core of Earth",
        #          'a': "another unknown action"}
        # A car returning this dictionary supports the commands 'f','d','a'.
        # implement your code and erase the "pass"
        #pass

    def movement_requirements(self, move_key):

        """
        :param move_key: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for
        this move to be legal.
        """

        cor = self.__location
        if move_key == "d":
            return [(cor[0]+self.__length, cor[1])]
        elif move_key == "u":
            return [(cor[0]-1, cor[1])]
        elif move_key == "r":
            return [(cor[0], cor[1]+self.__length)]
        elif move_key == "l":
            return [(cor[0], cor[1]-1)]

        # For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        # be empty in order to move down (with a key 'd').
        # implement your code and erase the "pass"
        # pass

    def move(self, move_key):
        """ 
        :param move_key: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if self.__orientation == 0 and (move_key == 'r' or move_key == 'l' ):
            return False
        elif self.__orientation == 1 and (move_key == 'u' or move_key == 'd' ):
            return False
        loc=self.__location
        x=loc[1]
        y=loc[0]
        if move_key=='r':
            self.__location=(y,x+1)
            return True
        elif move_key=='u':
            self.__location = (y-1, x)
            return True
        elif move_key == 'd':
            self.__location = (y+1, x)
            return True
        elif move_key == 'l':
            self.__location = (y, x-1)
            return True
        return False


        # implement your code and erase the "pass"
        #pass

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name
        # implement your code and erase the "pass"
        pass
