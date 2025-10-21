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


class Creatures():
    def __init__(self, hsize: float, vsize: float, health: int, damage: int, defense: int):
        self.hsize = hsize
        self.vsize = vsize
        self.health = health
        self.damage = damage
        self.defense = defense