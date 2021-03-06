class Character:
    name = ""
    age = 0
    
    def __init__(self, name=""):
        self.name = name

    def __repr__(self):
        return f"{self.name}\n{self.age} years old"