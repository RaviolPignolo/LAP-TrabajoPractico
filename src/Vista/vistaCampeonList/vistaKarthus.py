import pygame
from src.Modelo.ChampionsList.Karthus import Karthus
from src.Vista.vistaCampeon import vistaCampeon
from src.Vista.vistaCampeon import champions_list

karthus_abilities = [
    {'name': 'Death Defied',    'ability': 'P', 'image': 'src/Vista/Assets/Images/AbilitiesIcon/KarthusAbilityIcon/Karthus_Death_Defied.png'},
    {'name': 'Lay Waste',       'ability': 'Q', 'image': 'src/Vista/Assets/Images/AbilitiesIcon/KarthusAbilityIcon/Karthus_Lay_Waste.png'},
    {'name': 'Wall of Pain',    'ability': 'W', 'image': 'src/Vista/Assets/Images/AbilitiesIcon/KarthusAbilityIcon/Karthus_Wall_of_Pain.png'},
    {'name': 'Defile',          'ability': 'E', 'image': 'src/Vista/Assets/Images/AbilitiesIcon/KarthusAbilityIcon/Karthus_Defile.png'},
    {'name': 'Requiem',         'ability': 'R', 'image': 'src/Vista/Assets/Images/AbilitiesIcon/KarthusAbilityIcon/Karthus_Requiem.png'}
]

ability: pygame.Surface
icono_normal: pygame.Surface
icono_pasiva = karthus_abilities[0]['image']


class vistaKarthus(vistaCampeon):
    
    def __init__(self, x, y, campeon: Karthus, ability):
        """Constructor"""
        imagen_normal = next((c['image'] for c in champions_list if c['name'] == campeon.name), None)
        super().__init__(x, y, {'image': imagen_normal})
        self.ability = ability
        self.icono_normal = imagen_normal
        self.campeon_modelo = campeon
    
    def dibujar(self, pantalla):
        """
        Dibuja el icono del campeón en la pantalla. Si el campeón está en estado pasivo,
        muestra el icono de la pasiva; de lo contrario, muestra el icono normal.

        Args:
            - pantalla (pygame.Surface): Superficie donde se dibuja el icono.
        """
        if getattr(self.campeon_modelo, 'en_pasiva', False):
            icon_path = icono_pasiva
        else:
            icon_path = self.icono_normal
        icono = pygame.image.load(icon_path)
        icono = pygame.transform.scale(icono, (80, 80))
        pantalla.blit(icono, (self.x, self.y))