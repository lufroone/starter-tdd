from enum import Enum
from typing import List

class TypeAction(Enum):
    AVANCER = "AVANCER"
    RECULER = "RECULER"
    ROTATION = "ROTATION"

class Rotation(Enum):
    GAUCHE = "GAUCHE"
    DROITE = "DROITE"

class Commandes:
    def __init__(self, id_commande: int):
        self.id_commande = id_commande
        self.historique: List[str] = []

    def executer_deplacement(self, action: TypeAction, distance: float) -> None:
        if action not in [TypeAction.AVANCER, TypeAction.RECULER]:
            raise ValueError("L'action doit être AVANCER ou RECULER pour un déplacement")
        commande = f"{action.value} {distance} mètres"
        self.historique.append(commande)

    def executer_rotation(self, rotation: Rotation) -> None:
        commande = f"ROTATION {rotation.value}"
        self.historique.append(commande)

    def affiche_historique(self) -> List[str]:
        return self.historique 