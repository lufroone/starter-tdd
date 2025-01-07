from typing import List
from .obstacle import Obstacle
from .rover import Rover

class Terrain:
    def __init__(self, id_terrain: int, longueur: float, largeur: float):
        self.id_terrain = id_terrain
        self.longueur = longueur
        self.largeur = largeur
        self.obstacles: List[Obstacle] = []
        self.nombre_obstacles = 0

    def ajouter_obstacle(self, obstacle: Obstacle) -> None:
        self.obstacles.append(obstacle)
        self.nombre_obstacles += 1

    def detecte_obstacle(self, rover: Rover) -> bool:
        for obstacle in self.obstacles:
            if obstacle.est_touche(rover.position_x, rover.position_y, 
                                 rover.longueur, rover.largeur):
                return True
        return False 