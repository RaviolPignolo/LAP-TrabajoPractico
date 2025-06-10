from src.Modelo.Item import Item

class ArdentCenser (Item):
    def __init__(self):
        super().__init__(
            name = "Ardent Censer",
            cost = 2200,
            sell = 0,
            hp = 0,
            hp_regen = 0,
            mana = 0,
            mana_regen = 1.25, #125%
            ad = 0,
            attack_speed = 0,
            ap = 45,
            armor = 0,
            mr = 0,
            healshield_power = 0.10, #10%
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
            movespeed_percent = 0.04 #4%
        )