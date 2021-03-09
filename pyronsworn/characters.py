class Character:
    """
     A Character represents the sheet a player would use when keeping track of the game.

    """    
    name = ""
    age = 0
    vows = []
    stats = {}
    momentum = []
    def __init__(self, name=""):
        self.name = name
        self.stats = {"Edge": 0, "Iron": 0, "Heart": 0, "Shadow": 0, "Wits": 0}
    def __repr__(self):
        return f"{self.name}\n{self.age} years old"

    def __str__(self):
        print(f"{self.name}\n{self.age} years old")

    def set_stat(self, stat_name, val):
        """
        set_stat sets a certain stat to a specific value

        Args:
            stat_name (str): The name of the stat you want to update.
            val (int): The value of the stat you want to set.
        """
        self.stats[stat_name.title()] = val