from src.Modelo.Champion import Champion
from src.Modelo import globals as globals_var

class Karthus(Champion):
    
    def __init__(self):
        super().__init__(
            name = "Karthus",
            title = "The Deathsinger",
            level = 1,
            base_hp = 620,
            base_hp_g = 110,
            base_hp_regen= 6.5, 
            base_hp_regen_g = 0.55,
            base_mana = 467,
            base_mana_g = 31,
            base_mana_regen = 8,
            base_mana_regen_g = 0.8,
            base_energy = 0,
            base_energy_regen = 0, 
            base_ad = 46,
            base_ad_g = 3.25,
            base_armor = 21,
            base_armor_g = 4.7,
            base_mr = 30,
            base_mr_g = 1.3,
            base_range = 450,
            base_move_speed = 335,
            base_attack_speed = 0.625,
            attack_speed_ratio = 0.625,
            bonus_attack_speed = 0.0211,
        )
    
    q_level = 0
    w_level = 0
    e_level = 0
    r_level = 0
    
    q_mana_cost = 0
    w_mana_cost = 0
    e_mana_cost = 0
    r_mana_cost = 0
    
    e_toggle = False
    en_pasiva = False
    turno_inicio_pasiva = None
    
    def level_up_ability(self, ability):
        """
    Sube de nivel la habilidad especificada para Karthus.
    Llama al método de la clase base para manejar la lógica de subida de nivel.
    """
        super().level_up_ability(ability)
    
    
    def se_muere(self):
        """
        Maneja la lógica cuando Karthus muere.
        Si no está en estado de pasiva, activa la pasiva.
        """
        if not self.en_pasiva:
            self.pasiva(globals_var.turno_actual)
    
    def actualizar_estado(self):
        """
        Actualiza el estado de Karthus durante la pasiva.
        Si han pasado 7 turnos desde que se activó la pasiva, la desactiva y restaura los costos de maná originales.
        """
        if self.en_pasiva and self.turno_inicio_pasiva is not None:
            if globals_var.turno_actual - self.turno_inicio_pasiva >= (7 * 2):
                self.en_pasiva = False
                self.q_mana_cost = self.PREV_Q_MANA_COST
                self.w_mana_cost = self.PREV_W_MANA_COST
                self.e_mana_cost = self.PREV_E_MANA_COST
                self.r_mana_cost = self.PREV_R_MANA_COST
                super().se_muere()
    
    
    def pasiva(self, turno_actual):
        """
        [P] Death Defied
        Upon taking faltal damage, Karthus enters a zombie state for 7 seconds, during which he can cast abilities at no cost.
        If Defile(E) has been learned, it will remain toggled on for Death Defiles's duration.
        Requiem(R) becomes disabled after Death Defied has lasted 4 seconds.
    
        While under this state, Karthus becomes untergetable and immune to crowd control as well as prevents all incomings damage,
        but is also rendered unable to move, declare basic attacks, use summoner spells, and activate items.
        """
        super().p()
        
        self.PREV_Q_MANA_COST = self.q_mana_cost
        self.PREV_W_MANA_COST = self.w_mana_cost
        self.PREV_E_MANA_COST = self.e_mana_cost
        self.PREV_R_MANA_COST = self.r_mana_cost
        
        self.en_pasiva = True
        self.turno_inicio_pasiva = turno_actual
        
        self.q_mana_cost = 0
        self.w_mana_cost = 0
        self.e_mana_cost = 0
        self.r_mana_cost = 0
    
    def q(self, Champion):
        """
        [Q] Lay Waste    1s    20 Mana
        Karthus creates a blast of magic granting sight and dealing x=(40 +35%AP) magic damage.
        If the blast hits only one enemy, it instead deal x=(80 +70%AP) magic damage.
        During Death Defied, Lay Waste will cast at maximum range if cast beyond that.

        Damage          [40/59/78/97/116]
        Enhanced Damage [80/118/156/194/232]
        Mana Cost       [20/25/30/35/40]
        """
        tipo = "AP"
        nivel = self.q_level
        mana_costs = [20, 25, 30, 35, 40]
        base_damages = [80, 118, 156, 194, 232]
        ap_ratios = [0.7] * 5
        
        mana_cost = mana_costs[nivel - 1]
        damage = base_damages[nivel - 1] + (ap_ratios[nivel - 1] * self.actual_ap)
        
        if self.en_pasiva:
            mana_cost = 0
        
        if self.actual_mana < mana_cost:
            return
        
        if Champion is not None:
            super().q()
            self.actual_mana = max(self.actual_mana - mana_cost, 0)
            super().damage(damage, tipo, Champion)
        else:
            super().q()
            self.actual_mana = max(self.actual_mana - mana_cost, 0)

    def w(self, Champion):
        """
        [W] Wall of Pain    Cost: 70 Mana    Cooldown: 15s
        Active: Karthus raise a wall of pain at the target location perpendicular to his facing that lasts 5s, granting sight around its pillars and center.
        Enemies that touch the wall are inflicted with 25% magic resistance reduction and become slowed for 5 seconds, decaying over the duration.
        This can affect enemies only once per cast
    
        Wall Lenght          [800/900/1000/1100/1200]
        Move Speed Slow     [40%/50%/60%/70%/80%]
        """
        nivel = self.w_level
        mana_costs = [70] * 5
        mr_reduction = [0.25] * 5

        mana_cost = mana_costs[nivel - 1]

        if self.en_pasiva:
            mana_cost = 0

        if self.actual_mana < mana_cost:
            return

        if Champion is not None:
            super().w()
            self.actual_mana = max(self.actual_mana - mana_cost, 0)
            if Champion.actual_total_mr <= 0:
                return
            else:
                Champion.actual_total_mr = (Champion.actual_total_mr * (1 - mr_reduction[nivel - 1]))
        else:
            super().w()
            self.actual_mana = max(self.actual_mana - mana_cost, 0)


    def e(self, Champion):
        """
        [E] Defile    0.5s    30 Mana per Second
        Passive: When Karthus kills a unit, he restores 10 Mana.
        Toggle: Karthus surrounds himself with a necrotic aura that deals x=(7.5 +5%AP) every 0.25s(tick) (equal to x=(30 +20%AP) every 1s) to all nearby enemies.
        Toggling Defile off triggers a final tick of damage.
        Defile cannot be toggled off during Death Defied
    
        Damage per Tick     [7.5/12.5/17.5/22.5/27.5]
        Damage per Second   [30/50/70/90/110]
        Mana Restore        [10/20/30/40/50]   Ver cómo aplicarlo
        Mana Cost           [30/42/54/66/78]
        """
        tipo = "AP"
        nivel = self.e_level
        mana_costs = [30, 42, 54, 66, 78]
        base_damages = [30, 50, 70, 90, 110]
        ap_ratios = [0.05] * 5

        mana_cost = mana_costs[nivel - 1]
        damage = base_damages[nivel - 1] + (ap_ratios[nivel - 1] * self.actual_ap)

        if self.en_pasiva:
            mana_cost = 0
        
        if self.actual_mana < mana_cost:
            return

        if Champion is not None:
            super().e()
            self.actual_mana = max(self.actual_mana - mana_cost, 0)
            super().damage(damage, tipo, Champion)
        else:
            super().e()
            self.actual_mana = max(self.actual_mana - mana_cost, 0)


    def r(self, Champion):
        """
        [R] Requiem    200s    100 Mana
        Karthus channels for 3 seconds, then deals x=(200 +70%AP) magic damage to enemy champions, regardless of distance.
    
        Damage      [200/350/500]
        Cooldown    [200/180/160] (Starts on-cast)
        """
        tipo = "AP"
        nivel = self.r_level
        mana_costs = [100] * 3
        base_damages = [200, 350, 500]
        ap_ratios = [0.7] * 3

        mana_cost = mana_costs[nivel - 1]
        damage = base_damages[nivel - 1] + (ap_ratios[nivel - 1] * self.actual_ap)

        if self.en_pasiva:
            mana_cost = 0
        
        if self.actual_mana < mana_cost:
            return
        
        super().r()
        self.actual_mana = max(self.actual_mana - mana_cost, 0)
        super().damage(damage, tipo, Champion)