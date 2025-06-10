from src.Modelo.Item import Item

class ChempunkChainsword (Item):
    def __init__(self):
        super().__init__(
            name = "Chempunk Chainsword",
            cost = 3100,
            sell = 0,
            hp = 450,
            hp_regen = 0,
            mana = 0,
            mana_regen = 0,
            ad = 45,
            attack_speed = 0,
            ap = 0,
            armor = 0,
            mr = 0,
            healshield_power = 0,
            tenacity = 0,
            crit_chance = 0,
            crit_damage = 0,
            armorpen_flat = 0,
            armorpen_percent = 0,
            magicpen_flat = 0,
            magicpen_percent = 0,
            lifesteal = 0,
            ah = 15,
            movespeed_flat = 0,
            movespeed_percent = 0
        )