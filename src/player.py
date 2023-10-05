class Player():
    streak : int = 0
    def __init__(self,name : str, isMachine : bool = False):
        self.name = name
        self.isMachine = isMachine

    def calculate_streak(self,win):
        if win:
            self.streak += 1
        else:
            self.streak = 0