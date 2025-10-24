class InanimatedObjects():
    def __init__(self, hsize: float, vsize: float):
        self.hsize = hsize
        self.vsize = vsize


class PlayableCharacters():
    def __init__(self, name: str, hsize: float, vsize: float, health: int, damage: int, defense: int):
        self.name = name
        self.hsize = hsize
        self.vsize = vsize
        self.health = health
        self.damage = damage
        self.defense = defense

    def walking(self, speed: int, dir = "straight"):
        if dir == "straight":
            print("Follow straight")
        elif dir == "back":
            print("Back")
        elif dir == "left":
            print("Turn left")
        elif dir == "right":
            print("Turn right")
        else:
            print("Error")
    
    def attacking(self):
        print(f"You attacked it with {self.damage} of damage.")
    
    def taking_damage(self):
        print(f"You took damage and now you're {self.health - 1} of health.")


class Creatures():
    def __init__(self, hsize: float, vsize: float, health: int, damage: int, defense: int):
        self.hsize = hsize
        self.vsize = vsize
        self.health = health
        self.damage = damage
        self.defense = defense
    
    def walking(self, speed: int, dir = "straight"):
        if dir == "straight":
            print("Follow straight")
        elif dir == "back":
            print("Back")
        elif dir == "left":
            print("Turn left")
        elif dir == "right":
            print("Turn right")
        else:
            print("Error")
    
    def attacking(self):
        print(f"Enemy attacked.")
    
    def taking_damage(self):
        print(f"Enemy took damage. Now its health is {self.health - 1}.")