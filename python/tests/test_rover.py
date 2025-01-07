import pytest
from ..rover import Rover

class TestRover:
    @pytest.fixture
    def rover(self):
        return Rover(1, 2, 2, 0.0, 0.0, "N")
    
    def test_creation_rover(self):
        rover = Rover(1, 2, 2, 0.0, 0.0, "N")
        assert rover.id_rover == 1
        assert rover.longueur == 2
        assert rover.largeur == 2
        assert rover.position_x == 0.0
        assert rover.position_y == 0.0
        assert rover.direction == "N"
    
    def test_avancer(self, rover):
        rover.avancer()
        assert rover.position_y == 1.0
        assert rover.position_x == 0.0
        
    def test_reculer(self, rover):
        rover.reculer()
        assert rover.position_y == -1.0
        assert rover.position_x == 0.0
        
    def test_tourner_gauche(self, rover):
        rover.tourner_gauche()
        assert rover.direction == "W"
        
    def test_tourner_droite(self, rover):
        rover.tourner_droite()
        assert rover.direction == "E" 