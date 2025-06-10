from src.Modelo.Champion import Champion

class Ambessa(Champion):
    def __init__(self):
        super().__init__(
            name = "Ambessa",
            title = "The Matriarch of war",
            level = 1,
            base_hp = 630,
            base_hp_g = 110,
            base_hp_regen= 8.5, 
            base_hp_regen_g = 0.75,
            base_mana = 0,
            base_mana_g = 0,
            base_mana_regen = 0,
            base_mana_regen_g = 0,
            base_energy = 200,
            base_energy_regen = 50,
            base_ad = 63,
            base_ad_g = 3,
            base_armor = 35,
            base_armor_g = 4.9,
            base_mr = 32,
            base_mr_g = 2.05,
            base_range = 125,
            base_move_speed = 335,
            base_attack_speed = 0.625,
            attack_speed_ratio = 0.625,
            bonus_attack_speed = 0.025
        )