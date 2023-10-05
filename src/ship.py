
import numpy as np
import random

class Ship():
    sunken: bool = False

    def __init__(self,size:int, coord: np.array = None ):
        self.size = size

    def create_random_ship(self,size, t):
        ship_r = []
        line_a = np.random.randint(0,9)
        column_a = np.random.randint(0,9)
        ship_r.append((line_a,column_a))
        # Random direction of a ship
        d = random.choice(["N","S","E","W"])
        print(d)
        print(line_a,column_a)
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
