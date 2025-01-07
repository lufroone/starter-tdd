import pytest
from ..terrain import Terrain
from ..obstacle import Obstacle
from ..rover import Rover

class TestTerrain:
    @pytest.fixture
    def terrain(self):
        return Terrain(1, 100.0, 100.0)
    
    @pytest.fixture
    def obstacle(self):
        return Obstacle(1, 5.0, 5.0, 1.0)
    
    @pytest.fixture
    def rover(self):
        return Rover(1, 2, 2, 0.0, 0.0, "N")
    
    def test_creation_terrain(self):
        terrain = Terrain(1, 100.0, 100.0)
        assert terrain.id_terrain == 1
        assert terrain.longueur == 100.0
        assert terrain.largeur == 100.0
        assert len(terrain.obstacles) == 0
        
    def test_ajout_obstacle(self, terrain, obstacle):
        terrain.ajouter_obstacle(obstacle)
        assert len(terrain.obstacles) == 1
        assert terrain.nombre_obstacles == 1
        
    def test_detection_obstacle(self, terrain, obstacle, rover):
        terrain.ajouter_obstacle(obstacle)
        rover.position_x = 5.0
        rover.position_y = 5.0
        assert terrain.detecte_obstacle(rover) == True 