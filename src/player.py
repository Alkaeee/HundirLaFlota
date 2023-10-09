class Player():
    """
    Represents a player in a game.

    Attributes:
    - name (str): The name of the player.
    - ships (list): A list of ships owned by the player.
    - lives (int): The number of lives or health points of the player.
    - shot_record (list): A list of coordinates representing the player's shot history.
    - is_machine (bool): Indicates whether the player is a machine (AI) or not.
    - streak (int): The player's winning streak.

    Methods:
    - calculate_streak(win): Updates the player's streak based on a win (True) or loss (False).
    - check_shot(coord, record): Checks if a shot at the given coordinates is valid and not a repeat.
    """
    streak : int = 0
    def __init__(self, name: str, ships: list = None, lives: int = 0, shot_record: list = None, is_machine: bool = False):
        self._name = name
        self._ships = ships or []
        self._lives = lives
        self._shot_record = shot_record or []
        self._is_machine = is_machine

    @property
    def name(self) -> str:
        """
        Get the player's name.
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Set the player's name.
        """
        self._name = name

    @property
    def ships(self) -> list:
        """
        Get the list of ships owned by the player.
        """
        return self._ships

    @ships.setter
    def ships(self, ships: list):
        """
        Set the list of ships owned by the player.
        """
        self._ships = ships

    @property
    def lives(self) -> int:
        """
        Get the player's remaining lives or health points.
        """
        return self._lives

    @lives.setter
    def lives(self, lives: int):
        """
        Set the player's remaining lives or health points.
        """
        self._lives = lives

    @property
    def shot_record(self) -> list:
        """
        Get the player's shot history.
        """
        return self._shot_record

    @shot_record.setter
    def shot_record(self, shot_record: list):
        """
        Set the player's shot history.
        """
        self._shot_record = shot_record

    @property
    def is_machine(self) -> bool:
        """
        Get whether the player is a machine (AI).
        """
        return self._is_machine

    @is_machine.setter
    def is_machine(self, is_machine: bool):
        """
        Set whether the player is a machine (AI).
        """
        self._is_machine = is_machine

    def check_shot(self,coord:tuple, record:list):
        """
        Check if a shot at the given coordinates is valid and not a repeat.

        Args:
        - coord (tuple): The coordinates (x, y) of the shot.
        - record (list): The list of previous shot coordinates.

        Returns:
        - bool: True if the shot is valid, False otherwise.
        """
        x = coord[0]
        y = coord[1]

        if 0 <= x < 10 and 0 <= y < 10:
            if coord in record:
                print("Shot repeat")
                return False
            return True
        else:
            return False