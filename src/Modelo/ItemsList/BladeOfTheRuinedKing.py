from src.Modelo.Item import Item

class BladeOfTheRuinedKing (Item):
    def __init__(self):
        super().__init__(
            name = "Blade of the Ruined King",
            cost = 3200,
            sell = 0,
            hp = 0,
            hp_regen = 0,
            mana = 0,
            mana_regen = 0,
            ad = 40,
            attack_speed = 0.25, #25%
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
            lifesteal = 0.10, #10%
            ah = 0,
            movespeed_flat = 0,
            movespeed_percent = 0
        )