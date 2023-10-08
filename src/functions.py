import src.player as pl, src.ship as sp, src.table as tl, src.variable as v, src.functions as ft
import numpy as np
import random

def create_ships_player(list_ships: list = None):
    """
    Create a list of player's ships with the specified sizes.

    Args:
    - list_ships (list): A list of ship sizes to create. If not provided, default ship sizes are used.

    Returns:
    - list: A list of Ship objects with the specified sizes.
    """
    ship_sizes = list_ships or [v.SHIP_1,v.SHIP_1_2,v.SHIP_1_3,v.SHIP_1_4,v.SHIP_2,v.SHIP_2_2,v.SHIP_2_3,v.SHIP_3,v.SHIP3_2,v.SHIP_4]
    ships = []
    for s in ship_sizes:
        ship = sp.Ship(s)
        ships.append(ship)
    return list(ships)

def create_lives(list_ships: list = None):
    """
    Calculate the total number of lives based on a list of ship sizes.

    This method takes a list of ship sizes and calculates the total number of lives, which is the sum of the sizes of all the ships.

    Args:
    - list_ships (list): A list of ship sizes to calculate lives from. If not provided, default ship sizes are used.

    Returns:
    - int: The total number of lives based on the provided ship sizes.
    """
    ship_sizes = list_ships or [v.SHIP_1,v.SHIP_1_2,v.SHIP_1_3,v.SHIP_1_4,v.SHIP_2,v.SHIP_2_2,v.SHIP_2_3,v.SHIP_3,v.SHIP3_2,v.SHIP_4]
    lives = sum(ship_sizes)
    return int(lives)

def create_player(player: object = None, table : object = None, list_ships: list = None):
    """
    Create a player with associated ships and a game table.

    This method allows you to create a player with an associated set of ships and a game table for a game. If the player or table objects are not provided, default values are used.

    Args:
    - player (object, optional): An existing player object. If not provided, a new player is created.
    - table (object, optional): An existing game table object. If not provided, a new game table is created.
    - list_ships (list): A list of ship sizes to create the player's ships. If not provided, default ship sizes are used.

    Returns:
    - Tuple[object, object]: A tuple containing the created player and game table objects.

    """
    if not player:
        player = pl.Player(input("Introduza nombre del jugador"))
    if not table:
        table = tl.Table(v.SIZE_DEFAULT, player.name)
    table.create_table()
    player.ships = ft.create_ships_player(list_ships)
    player.lives = ft.create_lives(list_ships)

    for s in player.ships:
        s.create_random_ship(s.size)
        while not table.check_put_ship(s.coord):
            s.create_random_ship(s.size)
        table.put_ship(s.coord)
    return player,table

def create_machine(machine: object = None, table_m : object = None, list_ships: list = None):
    """
    Create a player with associated ships and a game table.

    This method allows you to create a player with an associated set of ships and a game table for a game. If the player or table objects are not provided, default values are used.

    Args:
    - player (object, optional): An existing player object. If not provided, a new player is created.
    - table (object, optional): An existing game table object. If not provided, a new game table is created.
    - list_ships (list): A list of ship sizes to create the player's ships. If not provided, default ship sizes are used.

    Returns:
    - Tuple[object, object]: A tuple containing the created player and game table objects.
    """
    if not machine:
        machine = pl.Player("Machine", is_machine=True)
    if not table_m:
        table_m = tl.Table(v.SIZE_DEFAULT, machine.name)
    table_m.create_table()
    machine.ships = ft.create_ships_player(list_ships)
    machine.lives = ft.create_lives(list_ships)

    for s in machine.ships:
        s.create_random_ship(s.size)
        while not table_m.check_put_ship(s.coord):
            s.create_random_ship(s.size)
        table_m.put_ship(s.coord)
    return machine,table_m

def create_random_coord():
    """
    Generate random coordinates within a 10x10 grid.

    This method generates random X and Y coordinates within a 10x10 grid, where both X and Y are integers between 0 and 8 (inclusive).

    Returns:
    - A tuple containing the random X and Y coordinates.
    """
    x = np.random.randint(0,9)
    y = np.random.randint(0,9)
    return x,y

def play_game():
    """
    Play a battleship game between a player and a machine.

    This method simulates a battleship game between a player and a machine. The game continues until one of the players runs out of lives or decides to exit. The player takes turns entering coordinates to make shots, and the machine makes random shots. The game's progress and results are displayed in the console.
    """
    p1, t1 = ft.create_player()
    p2, t2 = ft.create_machine()
    #print(t2.table) -> saw machine table
    t1_record = np.array([])
    print("____________________________________________")    
    while p1.lives > 0 and p2.lives > 0:
        # Turn player 
        exit_1 = True
        while exit_1:
            print(f"Your table: \n {t1.table}")
            print(f"Your shots: \n {t1_record}" )
            x = input("P1: Enter an X coordinate (0 to 9)  If you don't want to continue playing, enter 'EXIT")
            y = input("P1: Enter an Y coordinate (0 to 9), If you don't want to continue playing, enter 'EXIT ")
            if x.lower() == "exit" or y.lower() == "exit":
                p1.lives = 0
                break
            while not p1.check_shot((int(x),int(y)),p1.shot_record):
                x,y = input("P1: Enter an X coordinate (0 to 9)"), input("P1: Enter an Y coordinate (0 to 9)")
                if x.lower() == "exit" or y.lower() == "exit":
                    print("you have given up")
                    break
            if x.lower() == "exit" or y.lower() == "exit":
                p1.lives = 0
                break
            p1.shot_record.append((int(x),int(y)))
            print("Record PLAYER: ",p1.shot_record)
            exit_1 = t2.shot((int(x),int(y)))
            if exit_1 != False:
                p2.lives = p2.lives - 1
                if p2.lives == 0:
                    break
            t1_record = t2.table.copy()
            t1_record[t1_record == "O"] = " "
            t1_record = t1_record
        if p2.lives == 0:
            break
            
        # Turn machine
        exit_2 = True
        while exit_2:
            x,y = create_random_coord()
            while not p2.check_shot((x,y),p2.shot_record):
                x,y = create_random_coord()
            p2.shot_record.append((x,y))
            print("Shot: ", (x,y))
            print("Record MACHINE: ",p2.shot_record)
            exit_2 = t1.shot((x,y))
            if exit_2:
                p1.lives = p1.lives - 1
                if p1.lives == 0:
                    break
        if p1.lives == 0:
                break
        print("____________________________________________")    
                
    if p1.lives > p2.lives:
        print(f"The player {p1.name} has won!")
    else:
        print("You lost!!")

def create_demo():
    """
    Create and play a demo battleship game between a player and a machine with custom ship sizes.

    This method creates a demo battleship game with custom ship sizes and allows you to play as a player against a machine. The game continues until one of the players runs out of lives or decides to exit. The game's progress and results are displayed in the console.
    """
    list_ships_demo = [1,2]
    p1 = pl.Player("Player Demo")
    t1 = tl.Table(v.SIZE_DEFAULT, p1.name)
    p1_demo, t1_demo = ft.create_player(p1, t1, list_ships_demo)
    p2 = pl.Player("Player Demo")
    t2 = tl.Table(v.SIZE_DEFAULT, p2.name)
    p2_demo, t2_demo = ft.create_machine(p2, t2, list_ships_demo)
    t1_record = np.array([])
    print("____________________________________________")    
    while p1_demo.lives > 0 and p2_demo.lives > 0:
        # Turn player 
        print(f"Machine table: \n{t2_demo.table}") # saw machine demo table
        exit_1 = True
        while exit_1:
            print(f"Your table: \n {t1_demo.table}")
            print(f"Your shots: \n {t1_record}" )
            x = input("P1: Enter an X coordinate (0 to 9)\n If you don't want to continue playing, enter 'EXIT': ")
            y = input("P1: Enter an Y coordinate (0 to 9)\n If you don't want to continue playing, enter 'EXIT': ")
            if x.lower() == "exit" or y.lower() == "exit":
                p1.lives = 0
                break
            while not p1.check_shot((int(x),int(y)),p1_demo.shot_record):
                x,y = input("P1: Enter an X coordinate (0 to 9)\n If you don't want to continue playing, enter 'EXIT': "), input("P1: Enter an Y coordinate (0 to 9)\nIf you don't want to continue playing, enter 'EXIT': ")
                if x.lower() == "exit" or y.lower() == "exit":
                    print("you have given up")
                    break
            if x.lower() == "exit" or y.lower() == "exit":
                p1_demo.lives = 0
                break
            p1_demo.shot_record.append((int(x),int(y)))
            print("Record PLAYER: ",p1_demo.shot_record)
            exit_1 = t2_demo.shot((int(x),int(y)))
            if exit_1 != False:
                p2_demo.lives = p2.lives - 1
                if p2_demo.lives == 0:
                    break
            t1_record = t2_demo.table.copy()
            t1_record[t1_record == "O"] = " "
            t1_record = t1_record
        if p2_demo.lives == 0:
            break
            
        # Turn machine
        exit_2 = True
        while exit_2:
            x,y = create_random_coord()
            while not p2_demo.check_shot((x,y),p2_demo.shot_record):
                x,y = create_random_coord()
            p2_demo.shot_record.append((x,y))
            print("Shot: ", (x,y))
            print("Record MACHINE: ",p2_demo.shot_record)
            exit_2 = t1_demo.shot((x,y))
            if exit_2:
                p1_demo.lives = p1_demo.lives - 1
                if p1_demo.lives == 0:
                    break
        if p1_demo.lives == 0:
                break
        print("____________________________________________")    
                
    if p1_demo.lives > p2_demo.lives:
        print(t1_record)
        print(f"The player {p1_demo.name} has won!")
    else:
        print("Lost it!!")