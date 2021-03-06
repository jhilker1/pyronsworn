class Character:
    """
     A Character represents the sheet a player would use when keeping track of the game.

    """    
    name = ""
    age = 0
    
    def __init__(self, name=""):
        self.name = name

    def __repr__(self):
        return f"{self.name}\n{self.age} years old"

    def __str__(self):
        print(f"{self.name}\n{self.age} years old")