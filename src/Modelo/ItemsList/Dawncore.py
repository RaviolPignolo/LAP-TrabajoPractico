from src.Modelo.Item import Item

class Dawncore (Item):
    def __init__(self):
        super().__init__(
            name = "Dawncore",
            cost = 2500,
            sell = 0,
            hp = 0,
            hp_regen = 0,
            mana = 0,
            mana_regen = 1.00, #100%
            ad = 0,
            attack_speed = 0,
            ap = 45,
            armor = 0,
            mr = 0,
            healshield_power = 0.16, #16%
            tenacity = 0,
            crit_chance = 0,
            crit_damage = 0,
            armorpen_flat = 0,
            armorpen_percent = 0,
            magicpen_flat = 0,
            magicpen_percent = 0,
            lifesteal = 0,
            ah = 0,
            movespeed_flat = 0,
            movespeed_percent = 0
        )