from pyronsworn.enums.rank import Rank

class Vow:

    rank = None
    name = ""
    progress = 0
    ticks = 0

    def __init__(self, rank=""):
        rank = rank.lower()
        self.rank = Rank(rank)
        self.progress = 0 
        self.ticks = 0
    def __str__(self):
        return f"{self.name} - {self.rank.value.title()} Vow, {self.progress} Progress, {self.ticks} Ticks"

    def __repr__(self):
        return f"{self.name} - {self.rank.value.title()} Vow, {self.progress} Progress, {self.ticks} Ticks"

    def update(self):
        if self.rank.value == "troublesome":
            self.progress = self.progress + 3
        elif self.rank.value == "dangerous":
            self.progress = self.progress + 2
        elif self.rank.value == "formidable":
            self.progress = self.progress + 1
        elif self.rank.value == "extreme":
            self.ticks = self.ticks + 2
        elif self.rank.value == "epic":
            self.ticks += 1
        else:
            pass