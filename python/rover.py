class Rover:
    def __init__(self, id_rover: int, longueur: int, largeur: int, position_x: float, position_y: float, direction: str):
        self.id_rover = id_rover
        self.longueur = longueur
        self.largeur = largeur
        self.position_x = position_x
        self.position_y = position_y
        self.direction = direction

    def avancer(self) -> None:
        if self.direction == "N":
            self.position_y += 1
        elif self.direction == "S":
            self.position_y -= 1
        elif self.direction == "E":
            self.position_x += 1
        elif self.direction == "W":
            self.position_x -= 1

    def reculer(self) -> None:
        if self.direction == "N":
            self.position_y -= 1
        elif self.direction == "S":
            self.position_y += 1
        elif self.direction == "E":
            self.position_x -= 1
        elif self.direction == "W":
            self.position_x += 1

    def tourner_gauche(self) -> None:
        directions = {"N": "W", "W": "S", "S": "E", "E": "N"}
        self.direction = directions[self.direction]

    def tourner_droite(self) -> None:
        directions = {"N": "E", "E": "S", "S": "W", "W": "N"}
        self.direction = directions[self.direction] 