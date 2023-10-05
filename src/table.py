import numpy as np
class Table():
    size: tuple = (10,10)

    def __init__(self,size: tuple = (10,10)):
        self.size = size

    def create_table(self):
        self.table = np.full(self.size," ")
        return self.table
    
    def put_ship(self,ship):
        for i in ship:
            self.table[i] = "O"
        
        return self.table
    
    def shot(self,box):
        if self.table[box] == " ":
            print("Water")
            self.table[box] = "-"
        else:
            print("Given")
            self.table[box] = "X"
        return self.table

    def check_put_ship(self,ship):
        for i in ship:
            if self.table[i] == "O":
                return False
        return True