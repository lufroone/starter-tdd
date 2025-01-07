import pytest
from ..obstacle import Obstacle

class TestObstacle:
    @pytest.fixture
    def obstacle(self):
        return Obstacle(1, 5.0, 5.0, 1.0)
    
    def test_creation_obstacle(self):
        obstacle = Obstacle(1, 5.0, 5.0, 1.0)
        assert obstacle.id_obstacle == 1
        assert obstacle.position_x == 5.0
        assert obstacle.position_y == 5.0
        assert obstacle.rayon == 1.0
    
    def test_detection_collision(self, obstacle):
        # Test collision directe
        assert obstacle.est_touche(5.0, 5.0, 2, 2) == True
        # Test pas de collision (trop loin)
        assert obstacle.est_touche(10.0, 10.0, 2, 2) == False 