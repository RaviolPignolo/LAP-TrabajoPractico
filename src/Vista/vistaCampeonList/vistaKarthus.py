
import pygame
from src.Modelo.ChampionsList.Karthus import Karthus
from src.Vista.vistaCampeon import vistaCampeon
from src.Vista.vistaCampeon import champions_list
from src.Modelo.globals import resource_path

karthus_abilities = [
    {'name': 'Death Defied',    'ability': 'P', 'image': 'src/Vista/Assets/Images/AbilitiesIcon/KarthusAbilityIcon/Karthus_Death_Defied.png'},
    {'name': 'Lay Waste',       'ability': 'Q', 'image': 'src/Vista/Assets/Images/AbilitiesIcon/KarthusAbilityIcon/Karthus_Lay_Waste.png'},
    {'name': 'Wall of Pain',    'ability': 'W', 'image': 'src/Vista/Assets/Images/AbilitiesIcon/KarthusAbilityIcon/Karthus_Wall_of_Pain.png'},
    {'name': 'Defile',          'ability': 'E', 'image': 'src/Vista/Assets/Images/AbilitiesIcon/KarthusAbilityIcon/Karthus_Defile.png'},
    {'name': 'Requiem',         'ability': 'R', 'image': 'src/Vista/Assets/Images/AbilitiesIcon/KarthusAbilityIcon/Karthus_Requiem.png'}
]

karthus_animations = {
    'Q': 'src/Vista/Assets/Images/Animations/KarthusAnimations/Karthus_Q.png'
}

karthus_sounds = {
    'P': 'src/Vista/Assets/Sounds/KarthusSounds/Karthus_P.ogg'
}

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
        self.animations = karthus_animations
        self.pasiva_frame_anterior = False
    
    def dibujar(self, pantalla):
        """
        Dibuja el icono del campeón en la pantalla. Si el campeón está en estado pasivo,
        muestra el icono de la pasiva; de lo contrario, muestra el icono normal.

        Args:
            - pantalla (pygame.Surface): Superficie donde se dibuja el icono.
        """
        if getattr(self.campeon_modelo, 'en_pasiva', False):
            icon_path = icono_pasiva
            #sonido = pygame.mixer.Sound(resource_path(karthus_sounds['P']))
            #sonido.play()
        else:
            icon_path = self.icono_normal
        icono = pygame.image.load(resource_path(icon_path))
        icono = pygame.transform.scale(icono, (80, 80))
        pantalla.blit(icono, (self.x, self.y))
    
    def dibujar_cursor_q(self, pantalla, x, y, celda_ancho, celda_alto):
        """Dibuja el icono de la Q para usar como cursos y seleccionar donde castearlo"""
        icon_path = karthus_abilities[1]['image']
        icono = pygame.image.load(resource_path(icon_path))
        icono = pygame.transform.scale(icono, (celda_ancho, celda_alto))
        pantalla.blit(icono, (x * celda_ancho, y * celda_alto))
    
    def dibujar_animacion_q(self, pantalla, x, y, frame, celda_ancho, celda_alto):
        """Dibuja la animación de la Q en la celda x, y en el frame que se obtiene"""
        anim_path = self.animations['Q']
        anim_img = pygame.image.load(resource_path(anim_path)).convert_alpha()
        cols = 3
        rows = 3
        total_frames = cols * rows
        frame = frame % total_frames
        frame_w = anim_img.get_width() // cols
        frame_h = anim_img.get_height() // rows
        frame_x = (frame % cols) * frame_w
        frame_y = (frame // cols) * frame_h
        frame_rect = pygame.Rect(frame_x, frame_y, frame_w, frame_h)
        anim_frame = anim_img.subsurface(frame_rect)
        anim_frame = pygame.transform.scale(anim_frame, (celda_ancho, celda_alto))
        pantalla.blit(anim_frame, (x * celda_ancho, y * celda_alto))