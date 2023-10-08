import numpy as np
class Table():
    """
    Represents a game table with ships and shots.

    This class manages the state of a game table, including placing ships, recording shots,
    and checking if ship placement is valid.

    Attributes:
    - size (tuple): The size of the table (number of rows and columns).
    - player_id (str): The identifier of the player associated with the table.
    - is_record (bool): Indicates whether this table is for recording purposes.

    Methods:
    - create_table(): Create an empty game table filled with empty cells.
    - put_ship(ship): Place a ship on the table, marking its positions as occupied.
    - shot(box): Record a shot on the table, marking the result as a hit or miss.
    - check_put_ship(ship): Check if a ship can be placed on the table without overlapping or adjacency.
    """
    def __init__(self,size: tuple, player_id: str, is_record:bool=False):
        """
        Initialize a game table.

        Args:
        - size (tuple): The size of the table (number of rows and columns).
        - player_id (str): The identifier of the player associated with the table.
        - is_record (bool): Indicates whether this table is for recording purposes.
        """
        self._size = size or (10,10)
        self._player_id = player_id
        self._is_record = is_record

    @property
    def size(self):
        """
        Get the size of the table (number of rows and columns).
        """
        return self._size

    @size.setter
    def size(self, new_size):
        """
        Set the size of the table (number of rows and columns).
        """
        self._size = new_size

    @property
    def player_id(self):
        """
        Get the identifier of the player associated with the table.
        """
        return self._player_id

    @player_id.setter
    def player_id(self, new_player_id):
        """
        Set the identifier of the player associated with the table.
        """
        self._player_id = new_player_id

    @property
    def is_record(self):
        """
        Get is used for recording purposes.
        """
        return self._is_record

    @is_record.setter
    def is_record(self, new_is_record):
        """
        Set whether the table is used for recording purposes.
        """
        self._is_record = new_is_record

    def create_table(self):
        """
        Create an empty game table filled with empty cells.

        Returns:
        - np.array: A NumPy array representing the game table.
        """
        self.table = np.full(self.size," ")
        return self.table
    
    def put_ship(self,ship):
        """
        Place a ship on the table, marking its positions as occupied.

        Args:
        - ship (list of tuple): The coordinates of the ship to be placed.

        Returns:
        - np.array: The updated game table with the ship placed.
        """
        for i in ship:
            self.table[i] = "O"
        
        return self.table
    
    def shot(self,box):
        """
        Record a shot on the table, marking the result as a hit or miss.

        Args:
        - box (tuple): The coordinates of the shot.

        Returns:
        - bool: True if it's a hit, False if it's a miss.
        """
        if self.table[box] == " ":
            print("Water")
            self.table[box] = "-"
            return False
        else:
            print("Given")
            self.table[box] = "X"
            return True
    
    def check_put_ship(self, ship):
        """
        Check if a ship can be placed on the table without overlapping or adjacency.

        Args:
        - ship (list of tuple): The coordinates of the ship to be placed.

        Returns:
        - bool: True if the placement is valid, False otherwise.
        """
        for coord in ship:
            x, y = coord
            # Verify if free position
            if self.table[x][y] == "O":
                return False

            # Verify adjacents positions
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < 10 and 0 <= new_y < 10 and self.table[new_x][new_y] == "O":
                        return False

        return True