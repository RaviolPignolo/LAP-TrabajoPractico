from src.Modelo.Champion import Champion

class Amumu(Champion):
    def __init__(self):
        super().__init__(
            name = "Amumu",
            title = "The sad mummy",
            level = 1,
            base_hp = 685,
            base_hp_g = 94,
            base_hp_regen= 9, 
            base_hp_regen_g = 0.85,
            base_mana = 285,
            base_mana_g = 40,
            base_mana_regen = 7.4,
            base_mana_regen_g = 0.55,
            base_energy = 0,
            base_energy_regen = 0,
            base_ad = 57,
            base_ad_g = 3.8,
            base_armor = 33,
            base_armor_g = 4,
            base_mr = 32,
            base_mr_g = 2.05,
            base_range = 125,
            base_move_speed = 335,
            base_attack_speed = 0.736,
            attack_speed_ratio = 0.638,
            bonus_attack_speed = 0.0218
        )