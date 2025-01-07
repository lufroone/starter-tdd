class Obstacle:
    def __init__(self, id_obstacle: int, position_x: float, position_y: float, rayon: float):
        self.id_obstacle = id_obstacle
        self.position_x = position_x
        self.position_y = position_y
        self.rayon = rayon

    def est_touche(self, rover_x: float, rover_y: float, rover_longueur: int, rover_largeur: int) -> bool:
        dx = abs(self.position_x - rover_x)
        dy = abs(self.position_y - rover_y)

        if dx > (rover_longueur/2 + self.rayon): return False
        if dy > (rover_largeur/2 + self.rayon): return False

        if dx <= (rover_longueur/2): return True
        if dy <= (rover_largeur/2): return True

        corner_distance_sq = (dx - rover_longueur/2)**2 + (dy - rover_largeur/2)**2

        return corner_distance_sq <= (self.rayon**2) 