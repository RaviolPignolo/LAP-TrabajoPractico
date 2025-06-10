import importlib

ITEM_FOLDER = "src.Modelo.ItemsList" # Carpeta que contiene los items

def load_item(item_name):
    """
    Busca el item que se le dio en la carpeta con los item para hacer una instancia.
    
    Parámetros:
        - item_name : Nombre de item como str, debe ser el que figura como nombre del archivo correspondiente.
        
    Return:
        Retorna el item para hacer la instancia.
    """
    module_name = f"{ITEM_FOLDER}.{item_name}"
    try:
        module = importlib.import_module(module_name)
        item_class = getattr(module, item_name)
        return item_class()
    except (ModuleNotFoundError, AttributeError):
        raise ImportError(f"No se encontró el item {item_name} en {module_name}")

class Item:
    name: str
    cost: int
    sell: int
    
    hp: int
    hp_regen: float #%
    mana: int
    mana_regen: float #%
    ad: int
    attack_speed: float #%
    ap: int
    armor: int
    mr: int
    healshield_power: float #%
    tenacity: float
    crit_chance: float #%
    crit_damage: float #%
    armorpen_flat: int
    armorpen_percent: float #%
    magicpen_flat: int
    magicpen_percent: float #%
    lifesteal: float #%
    ah: int
    movespeed_flat: int
    movespeed_percent: float #%
    
    def __init__(self, name, cost, sell, hp, hp_regen, mana, mana_regen, ad, attack_speed, ap, armor, mr, healshield_power, tenacity, crit_chance, crit_damage, armorpen_flat, armorpen_percent, magicpen_flat, magicpen_percent, lifesteal, ah, movespeed_flat, movespeed_percent):
        """Constructor"""
        self.name = name
        self.cost = cost
        self.sell = sell
        self.hp = hp
        self.hp_regen = hp_regen
        self.mana = mana
        self.mana_regen = mana_regen
        self.ad = ad
        self.attack_speed = attack_speed
        self.ap = ap
        self.armor = armor
        self.mr = mr
        self.healshield_power = healshield_power
        self.tenacity = tenacity
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.armorpen_flat = armorpen_flat
        self.armorpen_percent = armorpen_percent
        self.magicpen_flat = magicpen_flat
        self.magicpen_percent = magicpen_percent
        self.lifesteal = lifesteal
        self.ah = ah
        self.movespeed_flat = movespeed_flat
        self.movespeed_percent = movespeed_percent

