from src.Modelo.Champion import Champion

class Fiddlesticks(Champion):
    def __init__(self):
        super().__init__(
            name = "FiddleSticks",
            title = "The Ancient Fear",
            level = 1,
            base_hp = 650,
            base_hp_g = 106,
            base_hp_regen = 5.5,
            base_hp_regen_g = 0.6,
            base_mana = 500,
            base_mana_g = 28,
            base_mana_regen = 8,
            base_mana_regen_g = 0.8,
            base_energy = 0,
            base_energy_regen = 0,
            base_ad = 55,
            base_ad_g = 2.65,
            base_armor = 34,
            base_armor_g = 4.7,
            base_mr = 30,
            base_mr_g = 1.3,
            base_range = 480,
            base_move_speed = 335,
            base_attack_speed = 0.625,
            attack_speed_ratio = 0.625,
            bonus_attack_speed = 0.0211,
        )