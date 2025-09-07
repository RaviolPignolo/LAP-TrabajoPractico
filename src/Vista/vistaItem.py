import pygame
from src.Vista.stat_icon import stat_icon_list
from src.Modelo.globals import resource_path

items_list = [ #Ubicación de los iconos correspondintes de los items
    {"name": "AbyssalMask",             "image": "src/Vista/Assets/Images/ItemsIcon/AbyssalMask_item.png"},
    {"name": "ArchangelsStaff",         "image": "src/Vista/Assets/Images/ItemsIcon/ArchangelsStaff_item.png"},
    {"name": "ArdentCenser",            "image": "src/Vista/Assets/Images/ItemsIcon/ArdentCenser_item.png"},
    {"name": "AxiomArc",                "image": "src/Vista/Assets/Images/ItemsIcon/AxiomArc_item.png"},
    {"name": "BansheesVeil",            "image": "src/Vista/Assets/Images/ItemsIcon/BansheesVeil_item.png"},
    {"name": "BlackCleaver",            "image": "src/Vista/Assets/Images/ItemsIcon/BlackCleaver_item.png"},
    {"name": "BlackfireTorch",          "image": "src/Vista/Assets/Images/ItemsIcon/BlackfireTorch_item.png"},
    {"name": "BladeOfTheRuinedKing",    "image": "src/Vista/Assets/Images/ItemsIcon/BladeOfTheRuinedKing_item.png"},
    {"name": "BloodlettersCurse",       "image": "src/Vista/Assets/Images/ItemsIcon/BloodlettersCurse_item.png"},
    {"name": "Bloodthirster",           "image": "src/Vista/Assets/Images/ItemsIcon/Bloodthirster_item.png"},
    {"name": "ChempunkChainsword",      "image": "src/Vista/Assets/Images/ItemsIcon/ChempunkChainsword_item.png"},
    {"name": "CosmicDrive",             "image": "src/Vista/Assets/Images/ItemsIcon/CosmicDrive_item.png"},
    {"name": "Cryptbloom",              "image": "src/Vista/Assets/Images/ItemsIcon/Cryptbloom_item.png"},
    {"name": "Dawncore",                "image": "src/Vista/Assets/Images/ItemsIcon/Dawncore_item.png"},
    {"name": "DeadMansPlate",           "image": "src/Vista/Assets/Images/ItemsIcon/DeadMansPlate_item.png"},
    {"name": "DeathsDance",             "image": "src/Vista/Assets/Images/ItemsIcon/DeathsDance_item.png"},
    {"name": "EchoesOfHelia",           "image": "src/Vista/Assets/Images/ItemsIcon/EchoesOfHelia_item.png"},
    {"name": "Eclipse",                 "image": "src/Vista/Assets/Images/ItemsIcon/Eclipse_item.png"},
    {"name": "EdgeOfNight",             "image": "src/Vista/Assets/Images/ItemsIcon/EdgeOfNight_item.png"},
    {"name": "EssenceReaver",           "image": "src/Vista/Assets/Images/ItemsIcon/EssenceReaver_item.png"},
    {"name": "ExperimentalHexplate",    "image": "src/Vista/Assets/Images/ItemsIcon/ExperimentalHexplate_item.png"},
    {"name": "Fimbulwinter",            "image": "src/Vista/Assets/Images/ItemsIcon/Fimbulwinter_item.png"},
    {"name": "ForceOfNature",           "image": "src/Vista/Assets/Images/ItemsIcon/ForceOfNature_item.png"},
    {"name": "FrozenHeart",             "image": "src/Vista/Assets/Images/ItemsIcon/FrozenHeart_item.png"},
    {"name": "GuardianAngel",           "image": "src/Vista/Assets/Images/ItemsIcon/GuardianAngel_item.png"},
    {"name": "GuinsoosRageblade",       "image": "src/Vista/Assets/Images/ItemsIcon/GuinsoosRageblade_item.png"},
    {"name": "Heartsteel",              "image": "src/Vista/Assets/Images/ItemsIcon/Heartsteel_item.png"},
    {"name": "HextechRocketbelt",       "image": "src/Vista/Assets/Images/ItemsIcon/HextechRocketbelt_item.png"},
    {"name": "HollowRadiance",          "image": "src/Vista/Assets/Images/ItemsIcon/HollowRadiance_item.png"},
    {"name": "HorizonFocus",            "image": "src/Vista/Assets/Images/ItemsIcon/HorizonFocus_item.png"},
    {"name": "Hubris",                  "image": "src/Vista/Assets/Images/ItemsIcon/Hubris_item.png"},
    {"name": "JakShosTheProtean",       "image": "src/Vista/Assets/Images/ItemsIcon/JakShoTheProtean_item.png"},
    {"name": "Opportunity",             "image": "src/Vista/Assets/Images/ItemsIcon/Opportunity_item.png"},
    {"name": "SpiritVisage",            "image": "src/Vista/Assets/Images/ItemsIcon/SpiritVisage_item.png"},
    {"name": "Thornmail",               "image": "src/Vista/Assets/Images/ItemsIcon/Thornmail_item.png"}
]

x: int
y: int
image: pygame.Surface
rect: pygame.Rect

class vistaItem:
    def __init__(self, x, y, item):
        """Constructor"""
        self.x = x
        self.y = y
        self.image = pygame.image.load(resource_path(item['image']))
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
    
    def dibujar(self, pantalla):
        """Dibuja la imagen del item"""
        pantalla.blit(self.image, self.rect)

    def item_info(self, item):
        info = [
            {"icon": None , "value": f"Nombre: {item.name}"}
        ]
        
        stats = {
            "Health": item.hp,
            "Health Regen": (item.hp_regen * 100),
            "Mana": item.mana,
            "Mana Regen": (item.mana_regen * 100),
            "Attack Damage": item.ad,
            "Attack Speed(%)": (item.attack_speed * 100),
            "Ability Power": item.ap,
            "Armor": item.armor,
            "Magic Resistance": item.mr,
            "Heal & Shield Power(%)": (item.healshield_power * 100),
            "Tenacity": (item.tenacity * 100),
            "Critical Strike Chance(%)": (item.crit_chance * 100),
            "Critical Dtrike Damage(%)": (item.crit_damage * 100),
            "Lethality": item.armorpen_flat,
            "Armor Penetration(%)": (item.armorpen_percent * 100),
            "MagicResist Flat Penetration": item.magicpen_flat,
            "MagicResist Penetration(%)": (item.magicpen_percent * 100),
            "Lifesteal(%)": (item.lifesteal * 100),
            "Ability Haste": item.ah,
            "Movement Speed": item.movespeed_flat,
            "Movement Speed(%)": (item.movespeed_percent * 100)
        }
        for stat_name, stat_value in stats.items():
            if stat_value > 0:
                icon_path = stat_icon_list.get(stat_name, None)
                info.append({"icon": icon_path, "value": stat_value})
        return info