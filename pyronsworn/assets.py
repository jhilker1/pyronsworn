from pyronsworn.enums.rank import Rank

class Asset:
    def __init__(self, name="", category=""):
        self.name = name 
        self.category = category
        self.trigger = ""
        self.moves = [{"move_1": "", "taken": False}, {"move_2": "", "taken": False }, {"move_3": "","taken": False}]

class CompanionAsset(Asset):
    def __init__(self, name=""):
        super().__init__(name, "Companion")
        self.hp = 5
        
        