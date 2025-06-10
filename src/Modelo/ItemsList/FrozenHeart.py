from src.Modelo.Item import Item

class FrozenHeart (Item):
    def __init__(self):
        super().__init__(
            name = "Frozen Heart",
            cost = 2500,
            sell = 0,
            hp = 400,
            hp_regen = 0,
            mana = 0,
            mana_regen = 0,
            ad = 0,
            attack_speed = 0,
            ap = 0,
            armor = 75,
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
            ah = 20,
            movespeed_flat = 0,
            movespeed_percent = 0
        )