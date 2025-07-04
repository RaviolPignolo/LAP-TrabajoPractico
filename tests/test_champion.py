import unittest
from src.Modelo.Champion import Champion
from src.Modelo.Item import Item
from src.Modelo.Champion import load_champion
from src.Modelo.Item import load_item

class TestChampion(unittest.TestCase):
    def setUp(self): 
        self.Karthus = load_champion("Karthus")
        self.Twitch = load_champion("Twitch")
        self.Maokai = load_champion("Maokai")
        self.Aatrox = load_champion("Aatrox")

        self.Guinsoo = load_item("GuinsoosRageblade")      # ad, ap y as
        self.Opportunity = load_item("Opportunity")        # ad y penetracion plana de armadura
        self.BlackfireTorch = load_item("BlackFireTorch")  # ap, mana y ah
        self.Thornmail = load_item("Thornmail")            # armadura
        self.SpiritVisage = load_item("SpiritVisage")      # resistencia magica
    
    def test_carga_instancia(self):
        """Verifica que los campeones e items se creen correctamente"""
        champ = load_champion("Karthus")
        item = load_item("BlackFireTorch")
        self.assertIsInstance(champ, Champion)
        self.assertIsInstance(item, Item)
    
    def test_level_up(self):
        """Verifica que al subir de nivel aumenten correctamente las estadisticas"""
        Karthus_hp_inicial = self.Karthus.actual_hp
        Karthus_hp_regen_inicial = self.Karthus.actual_hp_regen
        Karthus_mana_inicial = self.Karthus.actual_mana
        Karthus_mana_regen_inicial = self.Karthus.actual_mana_regen
        Karthus_ad_inicial = self.Karthus.actual_ad
        Karthus_attack_speed_inicial = self.Karthus.actual_attack_speed
        Karthus_armor_inicial = self.Karthus.actual_armor
        Karthus_mr_inicial = self.Karthus.actual_mr

        self.Karthus.level_up()

        self.assertGreater(self.Karthus.actual_hp, Karthus_hp_inicial)
        self.assertGreater(self.Karthus.actual_hp_regen, Karthus_hp_regen_inicial)
        self.assertGreater(self.Karthus.actual_mana, Karthus_mana_inicial)
        self.assertGreater(self.Karthus.actual_mana_regen, Karthus_mana_regen_inicial)
        self.assertGreater(self.Karthus.actual_ad, Karthus_ad_inicial)
        self.assertGreater(self.Karthus.actual_attack_speed, Karthus_attack_speed_inicial)
        self.assertGreater(self.Karthus.actual_armor, Karthus_armor_inicial)
        self.assertGreater(self.Karthus.actual_mr, Karthus_mr_inicial)
    
    def test_level_up_ability(self):
        """Verifica que se suban correctamente los niveles de las habilidades si pasar el máximo establecido"""
        Karthus_nivel_q_inicial = self.Karthus.q_level
        Karthus_nivel_r_inicial = self.Karthus.r_level
        
        self.Karthus.level_up_ability("Q")
        self.Karthus.level_up_ability("R")
        
        self.assertGreater(self.Karthus.q_level, Karthus_nivel_q_inicial)
        self.assertGreater(self.Karthus.r_level, Karthus_nivel_r_inicial)
        
        self.Karthus.level_up_ability("Q")
        self.Karthus.level_up_ability("Q")
        self.Karthus.level_up_ability("Q")
        self.Karthus.level_up_ability("Q")
        self.Karthus.level_up_ability("Q")
        
        self.Karthus.level_up_ability("R")
        self.Karthus.level_up_ability("R")
        self.Karthus.level_up_ability("R")
        self.Karthus.level_up_ability("R")
        
        self.assertEqual(self.Karthus.q_level, 5)
        self.assertEqual(self.Karthus.r_level, 3)
    
    def test_add_item(self):
        """Verifica que al agregar items aumenten las estadisticas correctamente de forma acumulativa"""
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        #Stats de Guinsoo (ad, ap, as)
        Karthus_ad_inicial = self.Karthus.actual_ad
        Karthus_ap_inicial = self.Karthus.actual_ap
        Karthus_attack_speed_inicial = self.Karthus.actual_attack_speed

        self.Karthus.add_item(self.Guinsoo)

        self.assertGreater(self.Karthus.actual_ad, Karthus_ad_inicial)
        self.assertGreater(self.Karthus.actual_ap, Karthus_ap_inicial)
        self.assertGreater(self.Karthus.actual_attack_speed, Karthus_attack_speed_inicial)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        #Stats de Opportunity (ad, armorpen_flat)
        Karthus_ad_inicial_2 = self.Karthus.actual_ad
        Karthus_armorpen_flat_inicial = self.Karthus.actual_armorpen_flat
        
        self.Karthus.add_item(self.Opportunity)

        self.assertGreater(self.Karthus.actual_ad, Karthus_ad_inicial_2)
        self.assertGreater(self.Karthus.actual_armorpen_flat, Karthus_armorpen_flat_inicial)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        #Stats de BlackfireTorch (ap, mana, ah)
        Karthus_ap_inicial_2 = self.Karthus.actual_ap
        Karthus_mana_inicial = self.Karthus.actual_mana
        Karthus_ah_inicial = self.Karthus.actual_ah

        self.Karthus.add_item(self.BlackfireTorch)

        self.assertGreater(self.Karthus.actual_ap, Karthus_ap_inicial_2)
        self.assertGreater(self.Karthus.actual_mana, Karthus_mana_inicial)
        self.assertGreater(self.Karthus.actual_ah, Karthus_ah_inicial)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        #Stats de Thornmail (hp, armor)
        Karthus_hp_inicial = self.Karthus.actual_hp
        Karthus_armor_inicial = self.Karthus.actual_total_armor

        self.Karthus.add_item(self.Thornmail)

        self.assertGreater(self.Karthus.actual_hp, Karthus_hp_inicial)
        self.assertGreater(self.Karthus.actual_total_armor, Karthus_armor_inicial)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        #Stats de SpiritVisage (ah, hp, hp_regen, mr)
        Karthus_ah_inicial_2 = self.Karthus.actual_ah
        Karthus_hp_inicial_2 = self.Karthus.actual_hp
        Karthus_hp_regen_inicial = self.Karthus.actual_hp_regen
        Karthus_mr_inicial = self.Karthus.actual_total_mr

        self.Karthus.add_item(self.SpiritVisage)

        self.assertGreater(self.Karthus.actual_ah, Karthus_ah_inicial_2)
        self.assertGreater(self.Karthus.actual_hp, Karthus_hp_inicial_2)
        self.assertGreater(self.Karthus.actual_hp_regen, Karthus_hp_regen_inicial)
        self.assertGreater(self.Karthus.actual_total_mr, Karthus_mr_inicial)
    
    def test_remove_item(self):
        """Verifica que al remover items se disminuyan las estadisticas correspondientes de forma sustractiva"""
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.Karthus.add_item(self.Thornmail)
        self.Karthus.add_item(self.SpiritVisage)

        Karthus_hp_inicial = self.Karthus.actual_hp
        Karthus_hp_regen_inicial = self.Karthus.actual_hp_regen
        Karthus_armor_inicial = self.Karthus.actual_total_armor
        Karthus_mr_inicial = self.Karthus.actual_total_mr
        Karthus_ah_inicial = self.Karthus.actual_ah

        self.Karthus.remove_item(self.Thornmail)

        self.assertLess(self.Karthus.actual_hp, Karthus_hp_inicial)
        self.assertLess(self.Karthus.actual_total_armor, Karthus_armor_inicial)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.Karthus.remove_item(self.SpiritVisage)

        self.assertLess(self.Karthus.actual_hp, Karthus_hp_inicial)
        self.assertLess(self.Karthus.actual_hp_regen, Karthus_hp_regen_inicial)
        self.assertLess(self.Karthus.actual_ah, Karthus_ah_inicial)
        self.assertLess(self.Karthus.actual_total_mr, Karthus_mr_inicial)
    
    def test_list_items(self):
        """Verifiacar que se listen los items correctamente cuando se le dan más item del máximo de inventario (6)"""
        self.Karthus.add_item(self.Guinsoo)
        self.Karthus.add_item(self.Opportunity)
        self.Karthus.add_item(self.BlackfireTorch)
        self.Karthus.add_item(self.Thornmail)
        self.Karthus.add_item(self.SpiritVisage)
        self.Karthus.add_item(self.BlackfireTorch) # último slot de inventario
        self.Karthus.add_item(self.BlackfireTorch) # no se debería agregar
        self.Karthus.add_item(self.BlackfireTorch) # no se debería agregar

        self.assertEqual(self.Karthus.list_items(),
        #Los nombres no son los mismos con los que los inicialicé, esas son abreviaciones, list_items() muestra el nombre completo
        ["Guinsoo's Rageblade", "Opportunity", "Blackfire Torch", "Thornmail", "Spirit Visage", "Blackfire Torch"])
    
    def test_armor(self):
        """Verifica que la armadura base, bonus y total se calculen correctamente"""
        Karthus_base_armor_inicial = self.Karthus.base_armor
        Karthus_actual_armor_inicial = self.Karthus.actual_armor
        Karthus_actual_bonus_armor_inicial = self.Karthus.actual_bonus_armor
        Karthus_actual_total_armor_inicial = self.Karthus.actual_total_armor
        
        self.Karthus.add_item(self.Thornmail)
        
        self.assertEqual(self.Karthus.base_armor, Karthus_base_armor_inicial)
        self.assertEqual(self.Karthus.actual_armor, Karthus_actual_armor_inicial)
        self.assertGreater(self.Karthus.actual_bonus_armor, Karthus_actual_bonus_armor_inicial)
        self.assertGreater(self.Karthus.actual_total_armor, Karthus_actual_total_armor_inicial)
    
    def test_mr(self):
        """Verifica que la resistencia mágica base, bonus y total se calcules correctamente"""
        
        Karthus_base_mr_inicial = self.Karthus.base_mr
        Karthus_actual_mr_inicial = self.Karthus.actual_mr
        Karthus_actual_bonus_mr_inicial = self.Karthus.actual_bonus_mr
        Karthus_actual_total_mr_inicial = self.Karthus.actual_total_mr
        
        self.Karthus.add_item(self.SpiritVisage)
        
        self.assertEqual(self.Karthus.base_mr, Karthus_base_mr_inicial)
        self.assertEqual(self.Karthus.actual_mr, Karthus_actual_mr_inicial)
        self.assertGreater(self.Karthus.actual_bonus_mr, Karthus_actual_bonus_mr_inicial)
        self.assertGreater(self.Karthus.actual_total_mr, Karthus_actual_total_mr_inicial)
    
# TESTEOS MÉTODOS KARTHUS
    """def test_karthus_passive(self):"""

    def test_karthus_q(self):
        Twitch_hp_inicial = self.Twitch.actual_hp
        Karthus_mana_inicial = self.Karthus.actual_mana
        
        # Karthus usa la Q con suficiente maná
        self.Karthus.q(self.Twitch)
        
        self.assertLess(self.Twitch.actual_hp, Twitch_hp_inicial)
        self.assertLess(self.Karthus.actual_mana, Karthus_mana_inicial)
    
        # Karthus usa la Q sin suficiente maná
        self.Karthus.actual_mana = 18 # Q requiere 20 de maná
        Twitch_hp_inicial_2 = self.Twitch.actual_hp
        
        self.Karthus.q(self.Twitch)
        
        self.assertEqual(self.Twitch.actual_hp, Twitch_hp_inicial_2)
        self.assertEqual(self.Karthus.actual_mana, 18)
        
        
    def test_karthus_w(self):
        Maokai_mr_inicial = self.Maokai.actual_total_mr
        Karthus_mana_inicial = self.Karthus.actual_mana
        
        self.Karthus.w(self.Maokai)
        
        """
        El efecto de la W no se debe stackear
        """
        self.assertLess(self.Maokai.actual_total_mr, Maokai_mr_inicial)
        self.assertLess(self.Karthus.actual_mana, Karthus_mana_inicial)
            
            
    def test_karthus_e(self):
        
        Twitch_hp_inicial = self.Twitch.actual_hp
        Karthus_mana_inicial = self.Karthus.actual_mana
        
        self.Karthus.e(self.Twitch) # Toggle = True
        self.Karthus.e(self.Twitch) # Toggle = False
        self.assertLess(self.Twitch.actual_hp, Twitch_hp_inicial)
        self.assertLess(self.Karthus.actual_mana, Karthus_mana_inicial)
        
        self.Karthus.actual_mana = 10
        Twitch_hp_inicial_2 = self.Twitch.actual_hp
        
        self.Karthus.e(self.Twitch) # Toggle deberia mantenerse en False despues del último Toggle = False por falta de maná para activarlo
        
        self.assertEqual(self.Twitch.actual_hp, Twitch_hp_inicial_2)
        self.assertEqual(self.Karthus.actual_mana, 10)
        
        self.Karthus.actual_mana = 300
        self.Karthus.e(self.Twitch) # Toggle = True
        self.assertEqual(self.Karthus.e_toggle, True)
        Twitch_hp_inicial_3 = self.Twitch.actual_hp
        self.Karthus.e(self.Twitch) # Toggle = False
        self.assertEqual(self.Karthus.e_toggle, False)
        self.assertLess(self.Twitch.actual_hp, Twitch_hp_inicial_3)
        
    
    def test_karthus_r(self):        
        Aartox_hp_inicial = self.Aatrox.actual_hp
        Karthus_mana_inicial = self.Karthus.actual_mana
        
        self.Karthus.r(self.Aatrox)
        
        self.assertLess(self.Aatrox.actual_hp, Aartox_hp_inicial)
        self.assertLess(self.Karthus.actual_mana, Karthus_mana_inicial)
        
        self.Karthus.actual_mana = 57
        Aartox_hp_inicial_2 = self.Aatrox.actual_hp
        
        self.Karthus.r(self.Aatrox)
        
        self.assertEqual(self.Aatrox.actual_hp, Aartox_hp_inicial_2)
        self.assertEqual(self.Karthus.actual_mana, 57)