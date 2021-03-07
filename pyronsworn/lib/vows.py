from enum import Enum

class Rank(Enum):
    TROUBLESOME = "Troublesome"
    DANGEROUS = "Dangerous"
    FORMIDABLE = "Formidable"
    EXTREME = "Extreme"
    EPIC = "Epic"
    RESOLVED = "Resolved"


class Vow:
    def __init__(self, rank=""):
        pass