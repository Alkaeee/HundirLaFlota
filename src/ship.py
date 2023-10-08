import numpy as np
import random

class Ship():
    """
    Represents a ship in a game.

    A ship has a size and a set of coordinates that determine its position.

    Attributes:
    - size (int): The size or length of the ship.
    - coord (np.array): An array of coordinates that define the ship's position.

    Methods:
    - create_random_ship(size): Generate a random ship with the given size and assign it to the `coord` attribute.
    """
    def __init__(self,size:int, coord: np.array = None ):
        """
        Initialize a new ship.

        Args:
        - size (int): The size or length of the ship.
        - coord (np.array): An array of coordinates that define the ship's position.
        """
        self._size = size
        self._coord = coord

    @property
    def size(self):
        """
        Get the size of the ship.
        """
        return self._size

    @size.setter
    def size(self, new_size):
        """
        Set the size of the ship.
        """
        self._size = new_size

    @property
    def coord(self):
        """
        Get the coordinates that define the ship's position.
        """
        return self._coord

    @coord.setter
    def coord(self, new_coord):
        """
        Set the coordinates that define the ship's position.
        """
        self._coord = new_coord

    def create_random_ship(self,size):
        """
        Generate a random ship position based on the given size.

        Args:
        - size (int): The size of the ship to be generated.
        """
        ship_r = []
        line_a = np.random.randint(0,9)
        column_a = np.random.randint(0,9)
        ship_r.append((line_a,column_a))
        # Random direction of a ship
        d = random.choice(["N","S","E","W"])
        
        # West
        if d == "W":
            while len(ship_r) < size:
                column_a = column_a-1
                if column_a > 0 and column_a <=9:
                    ship_r.append((line_a,column_a))
                else:
                    return self.create_random_ship(size)
        # East
        elif d == "E":
            while len(ship_r) < size:
                column_a = column_a+1
                if column_a > 0 and column_a <=9:
                    ship_r.append((line_a,column_a))
                else:
                    return self.create_random_ship(size)
        # North
        elif d == "N":
            while len(ship_r) < size:
                line_a = line_a-1
                if line_a > 0 and line_a <=9:
                    ship_r.append((line_a,column_a))
                else:
                    return self.create_random_ship(size)    
        # South
        elif d == "S":
            while len(ship_r) < size:
                line_a = line_a+1
                if line_a > 0 and line_a <=9:
                    ship_r.append((line_a,column_a))
                else:
                    return self.create_random_ship(size)    
        self.coord = ship_r