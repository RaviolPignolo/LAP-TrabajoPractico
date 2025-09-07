import pygame
from src.Modelo.Champion import Champion
from src.Vista.stat_icon import stat_icon_list
from src.Modelo.globals import resource_path

champions_list = [ # Ubicación correspondiente de los iconos de los campeones
    {'name': 'Aatrox',          'image': 'src/Vista/Assets/Images/ChampionIcon/Aatrox_icon.png'},
    {'name': 'Ahri',            'image': 'src/Vista/Assets/Images/ChampionIcon/Ahri_icon.png'},
    {'name': 'Akali',           'image': 'src/Vista/Assets/Images/ChampionIcon/Akali_icon.png'},
    {'name': 'Akshan',          'image': 'src/Vista/Assets/Images/ChampionIcon/Akshan_icon.png'},
    {'name': 'Alistar',         'image': 'src/Vista/Assets/Images/ChampionIcon/Alistar_icon.png'},
    {'name': 'Ambessa',         'image': 'src/Vista/Assets/Images/ChampionIcon/Ambessa_icon.png'},
    {'name': 'Amumu',           'image': 'src/Vista/Assets/Images/ChampionIcon/Amumu_icon.png'},
    {'name': 'Anivia',          'image': 'src/Vista/Assets/Images/ChampionIcon/Anivia_icon.png'},
    {'name': 'Caitlyn',         'image': 'src/Vista/Assets/Images/ChampionIcon/Caitlyn_icon.png'},
    {'name': 'Fiddlesticks',    'image': 'src/Vista/Assets/Images/ChampionIcon/Fiddlesticks_icon.png'},
    {'name': 'Jhin',            'image': 'src/Vista/Assets/Images/ChampionIcon/Jhin_icon.png'},
    {'name': 'Karthus',         'image': 'src/Vista/Assets/Images/ChampionIcon/Karthus_icon.png'},
    {'name': 'Maokai',          'image': 'src/Vista/Assets/Images/ChampionIcon/Maokai_icon.png'},
    {'name': 'Nautilus',        'image': 'src/Vista/Assets/Images/ChampionIcon/Nautilus_icon.png'},
    {'name': 'TahmKench',       'image': 'src/Vista/Assets/Images/ChampionIcon/TahmKench_icon.png'},
    {'name': 'Twitch',          'image': 'src/Vista/Assets/Images/ChampionIcon/Twitch_icon.png'},
]

x: int
y: int
image: pygame.Surface
rect: pygame.Rect

CELDA_ANCHO = 80
CELDA_ALTO =  80

class vistaCampeon:
    
    def __init__(self, x, y, campeon):
        """Constructor"""
        self.x = x
        self.y = y
        self.icon_path = campeon['image']
        self.image = pygame.image.load(resource_path(campeon['image']))
        self.image = pygame.transform.scale(self.image, (CELDA_ANCHO, CELDA_ALTO))
        self.rect = self.image.get_rect(topleft = (self.x, self.y))

    def dibujar(self, pantalla):
        "Dibuja el icono del campeon"
        pantalla.blit(self.image, self.rect)

    def base_stats(self, campeon):
        base_stats = {
            "Health" : campeon.base_hp,
            "Health Growth": campeon.base_hp_g,
            "Health Regen": campeon.base_hp_regen,
            "Health Regen Growth": campeon.base_hp_regen_g,
            "Mana": campeon.base_mana,
            "Mana Growth": campeon.base_mana_g,
            "Mana Regen": campeon.base_mana_regen,
            "Mana Regen Growth": campeon.base_mana_regen_g,
            "Energy": campeon.base_energy,
            "Energy Regen": campeon.base_energy_regen,
            "Attack Damage": campeon.base_ad,
            "Attack Damage Growth": campeon.base_ad_g,
            "Armor": campeon.base_armor,
            "Armor Growth": campeon.base_armor_g,
            "Magic Resistance": campeon.base_mr,
            "Magic Resistance Growth": campeon.base_mr_g,
            "Range": campeon.base_range,
            "Movement Speed": campeon.base_move_speed,
            "Base Attack Speed": campeon.base_attack_speed,
            "Attack Speed Ratio": campeon.attack_speed_ratio,
            "Bonus Attack Speed": campeon.bonus_attack_speed,
        }
        stats_lines = []
        for stat_name, stat_value in base_stats.items():
            if stat_value > 0:
                icon_path = stat_icon_list.get(stat_name, None)
                stats_lines.append({"name": stat_name, "icon": icon_path, "value": f"{stat_name}: {stat_value}"})
        return stats_lines
    
    def dibujar_cursor_q(self, *args, **kwargs):
        pass

    def dibujar_animacion_q(self, *args, **kwargs):
        pass