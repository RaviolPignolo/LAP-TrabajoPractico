from src.Modelo.Champion import Champion

class Twitch(Champion):
    def __init__(self):
        super().__init__(
            name = "Twitch",
            title = "The Plague Rat",
            level = 1,
            base_hp = 630,
            base_hp_g = 104,
            base_hp_regen = 3.75,
            base_hp_regen_g = 0.6,
            base_mana = 300,
            base_mana_g = 40,
            base_mana_regen = 7.25,
            base_mana_regen_g = 0.7,
            base_energy = 0,
            base_energy_regen = 0,
            base_ad = 250, #59
            base_ad_g = 3.1,
            base_armor = 27,
            base_armor_g = 4.2,
            base_mr = 30,
            base_mr_g = 1.3,
            base_range = 550,
            base_move_speed = 330,
            base_attack_speed = 0.679,
            attack_speed_ratio = 0.679,
            bonus_attack_speed = 0.0338
        )
    
    q_level = 1
    w_level = 1
    e_level = 1
    r_level = 1
    
    def level_up_ability(self, ability):
        return super().level_up_ability(ability)
    
    def pasiva(self):
        """
        [P] Deadly Venom
        Innate: Twitch's basic attacks on-hit apply a stack of Deadly Venom for 6 seconds, refreshing on subsequent applications and stacking up to 6 times.
        
        Deadly Venom: For each stack, the target is dealt「  1 / 2 / 3 / 4 / 5 (based on level) (+ 3% AP) true damage per second over the duration, 
        for a maximum of「 6 / 12 / 18 / 24 / 30 (based on level) (+ 18% AP) true damage with each tick. 」This effect is considered a  poison.
        
        Being applied on-hit, Deadly Venom stacks will still be applied if the attack was parried or blocked, but not if dodged and/or missed if Twitch is blinded.
        """
        super().p()
    
    def q(self):
        """
        [Q] Ambush
        Active: After a 1-second delay, Twitch becomes  camouflaged for a duration. Attacking or casting  "Venom Cask" or  "Contaminate" ends Ambush immediately.
        During this time, Twitch gains  10% bonus movement speed, increased to 30% while facing enemy  champions within a 1000-unit radius who cannot see him.
        
        Upon breaking stealth, Twitch gains bonus attack speed for 6 seconds.
        When an enemy champion dies while afflicted with Deadly Venom, Ambush's cooldown is reset.
        
        Using a basic attack breaks the stealth at the start of the attack windup.
        """
        super().q()
    
    def w(self):
        """
        [W] Venom Cask
        Active: Twitch hurls a cask of venom that explodes at the target location, applying "Deadly Venom" to enemies hit and granting sight of the area.
        The area then becomes contaminated for 3 seconds, applying a "Deadly Venom" stack each second to enemies within and slowing them.
        
        Venom Cask can apply a maximum of 4 An icon for Twitch's ability Deadly Venom Deadly Venom stacks per enemy per cast.
        """
        super().w()
    
    def e(self):
        """
        [E] Contaminate
        Active: Twitch sends out a lethal toxin to each nearby enemy afflicted by "Deadly Venom", dealing them physical damage.
        Contaminate deals additional physical damage and 35% AP magic damage for each stack of "Deadly Venom" on the target.
        
        A nearby enemy with "Deadly Venom" is required to cast this ability. The target does not have to be visible to be targeted by this ability.
        
        Contaminate will deal the additional damage to targets based on the number of Deadly Venom stacks they had at the start of the cast time.
        If the target moves out of range after the cast time, they are still dealt the damage.
        """
        super().e()
    
    def r(self):
        """
        [R] Spray and Pray
        Active: Twitch gains bonus attack damage and 300 bonus attack range for 6 seconds,
        during which his basic attacks are replaced by bolts that travel slightly further than his attack range in a straight line, dealing damage to every enemy unit hit.
        
        The bolts deal 100% - 60% (based on enemies hit) of the triggering attack's damage, apply on-hit effects, and can critically strike for (175% + An icon for the item Infinity Edge 40%) damage.
        
        The extra distance that the bolts travel scales with bonus attack range.
        If Twitch is  blinded before winding up the attack, the hits will miss against all targets.
        Runaan's Hurricane's Wind's Fury interacts with Spray and Pray's bonus attack range but not with the modified missile effect (the secondary bolts will not have pass-through effects).
        
        """
        super().r()