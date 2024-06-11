
class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """

    def __init__(self):
        board=[['_' for j in range(7)] for i in range(7)]
        board[3].append('_')
        self.__board=board
        self.__cars=[]

        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # implement your code and erase the "pass"
        #pass

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        board_print=""
        for i in self.__board:
            for j in i:
                board_print+=j
            if len(i)==8:
                board_print += '\n'
            else:
                board_print+='|\n'
        return board_print
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        # implement your code and erase the "pass"
        #pass

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        x=[[(i,j) for j in range(7)] for i in range(7)]
        list_return=[]
        for i in x:
            for j in i:
                list_return.append(j)
        list_return.append((3,7))
        return list_return
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        # implement your code and erase the "pass"
        #pass

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,move_key,description)
                 representing legal moves

        """
        return_list=[]
        for i in self.__cars:
            car_name=i.get_name()
            move_key=i.possible_moves()
            #print(move_key)
            moves=move_key.keys()
            #print(moves)
            for move in moves:
                cheker=True
                location_chek=i.movement_requirements(move)
                for j in location_chek:
                    x=j[1]
                    y=j[0]
                    if y<0 or y>=len(self.__board):
                        cheker =False
                        continue
                    if x<0 or x>=len(self.__board[y]):
                        cheker=False
                        continue
                #print(self.cell_content(location_chek[0]))
                #print(self.__board)
                if cheker==False:
                    continue
                if self.cell_content(location_chek[0]) is None:
                    return_list.append((car_name,move, move_key[move]))
        return return_list
        # From the provided example car_config.json file, the return value
        # could be
        # [('O','d',"some description"),('R','r',"some description"),('O',
        # 'u',"some description")]
        # implement your code and erase the "pass"
        #pass

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be
        filled for victory.
        :return: (row,col) of goal location
        """
        return (3,7)

        # In this board, returns (3,7)
        # implement your code and erase the "pass"
        #pass

    def cell_content(self, coordinate):
        #print(coordinate)

        if self.__board[coordinate[0]][coordinate[1]]=="_":
            return None
        else:
            return self.__board[coordinate[0]][coordinate[1]]
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        # implement your code and erase the "pass"
        #pass

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        loc2=car.car_coordinates()
        name=car.get_name()
        list_of_cars=self.__cars
        for i in list_of_cars:
            if i.get_name()==name:
                return False
        cor=car.car_coordinates()
        for i in cor:
            if i[0]<0 or i[0]>=len(self.__board):
                return False
            if i[1]<0 or i[1]>=len(self.__board[i[0]]):
                return False
            if self.__board[i[0]][i[1]] != "_":
                return False
        for i in cor:
            x=i[1]
            y=i[0]
            self.__board[y][x]=name
        self.__cars.append(car)
        return True
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        #pass

    def move_car(self, name, move_key):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param move_key: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        car_to_move=None
        for car in self.__cars:
            if car.get_name()==name:
                car_to_move=car
                break
        if car_to_move==None:
            return False

        #print(car.possible_moves())
        if move_key not in car.possible_moves():
            return False
        possible_moves_list=self.possible_moves()
        #print(possible_moves_list)
        can_move=False
        for i in possible_moves_list:
            if i[0]==name and i[1]==move_key:
                can_move=True
                break
        if can_move==False:
            return False

        move_req=car.movement_requirements(move_key)
        for i in move_req:
            x=i[1]
            y=i[0]
            if y < 0 or y >= len(self.__board):
                return False
            if x < 0 or x >= len(self.__board[y]):
                return False
            if self.__board[y][x] != "_":
                return False

        loc_befor = car.car_coordinates()


        a = car.move(move_key)
        if a==False:
            return False

        for i in loc_befor:
            x = i[1]
            y = i[0]
            self.__board[y][x] = "_"

        loc_after=car.car_coordinates()
        for i in loc_after:
            x = i[1]
            y = i[0]
            self.__board[y][x] = name

        return True


        # implement your code and erase the "pass"
        #pass
