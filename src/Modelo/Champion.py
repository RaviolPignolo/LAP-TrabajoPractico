import importlib

CHAMPION_FOLDER = "src.Modelo.ChampionsList" # Carpeta que contiene los campeones

def load_champion(champion_name):
    """
    Busca el campeon que se le dio en la carpeta con los campeones para hacer una instancia.
    
    Parámetros:
        - champion_name : Nombre de campeon como str.
        
    Return:
        Retorna el campeon para hacer la instancia.
    """
    module_name = f"{CHAMPION_FOLDER}.{champion_name}"
    try:
        module = importlib.import_module(module_name)
        champ_class = getattr(module, champion_name)
        return champ_class()
    except (ModuleNotFoundError, AttributeError):
        raise ImportError(f"No se encontró el campeón {champion_name} en {module_name}")

class Champion:
    name: str
    title: str
    level: int
    its_alive: bool = True
    
    q_level: int
    w_level: int
    e_level: int
    r_level: int
    
    # Estadísticas base
    base_hp: float
    base_hp_g: float
    base_hp_regen_g: float
    base_mana: float
    base_mana_g: float
    base_mana_regen_g: float
    base_energy: float
    base_energy_regen: float
    base_ad: float
    base_ad_g: float
    base_armor: float
    base_armor_g: float
    base_mr: float
    base_mr_g: float
    base_range: float
    base_move_speed: float
    base_attack_speed: float
    attack_speed_ratio: float
    bonus_attack_speed: float
    
    # Estadísticas actuales que se actualizan son subidas de nivel o adquiriendo items
    actual_ap: float
    actual_healshield_power: float
    actual_tenacity: float
    actual_crit_chance: float
    actual_crit_damage: float
    actual_bonus_armor: float
    actual_total_armor: float
    actual_armorpen_flat: float
    actual_armorpen_percent: float
    actual_bonus_mr: float
    actual_total_mr: float
    actual_magicpen_flat: float
    actual_magicpen_percent: float
    actual_lifesteal: float
    actual_ah: float
    actual_attack_speed: float
    actual_attack_speed_ratio: float
    actual_bonus_attack_speed_level: float
    actual_bonus_attack_speed_external: float
    actual_total_bonus_attack_speed: float
    actual_hp: float
    actual_hp_regen: float
    actual_mana: float
    actual_mana_regen: float
    actual_energy: float
    actual_energy_regen: float
    actual_ad: float
    actual_armor: float
    actual_mr: float
    actual_range: float
    actual_move_speed: float
    actual_max_hp: float
    actual_max_mana: float
    actual_max_energy:float
    
    def __init__(self, name, title, level, base_hp, base_hp_g, base_hp_regen, base_hp_regen_g, base_mana, base_mana_g, base_mana_regen, base_mana_regen_g, base_energy, base_energy_regen, base_ad, base_ad_g, base_armor, base_armor_g, base_mr, base_mr_g, base_range, base_move_speed, base_attack_speed, attack_speed_ratio, bonus_attack_speed):
        """Constructor"""
        self.name = name
        self.title = title
        self.level = level
        self.base_hp = base_hp
        self.base_hp_g = base_hp_g
        self.base_hp_regen = base_hp_regen
        self.base_hp_regen_g = base_hp_regen_g
        self.base_mana = base_mana
        self.base_mana_g = base_mana_g
        self.base_mana_regen = base_mana_regen
        self.base_mana_regen_g = base_mana_regen_g
        self.base_energy = base_energy
        self.base_energy_regen = base_energy_regen
        self.base_ad = base_ad
        self.base_ad_g = base_ad_g
        self.base_armor = base_armor
        self.base_armor_g = base_armor_g
        self.base_mr = base_mr
        self.base_mr_g = base_mr_g
        self.base_range = base_range
        self.base_move_speed = base_move_speed
        self.base_attack_speed = base_attack_speed
        self.attack_speed_ratio = attack_speed_ratio
        self.bonus_attack_speed = bonus_attack_speed
        self.__post_init__()
        
    def __post_init__(self):
        "Post constructor"
        self.actual_hp = self.base_hp
        self.actual_hp_regen = self.base_hp_regen
        self.actual_max_hp = self.base_hp
        self.actual_mana = self.base_mana
        self.actual_mana_regen = self.base_mana_regen
        self.actual_max_mana = self.base_mana
        self.actual_energy = self.base_energy
        self.actual_energy_regen = self.base_energy_regen
        self.actual_max_energy = self.base_energy
        self.actual_ad = self.base_ad
        self.actual_armor = self.base_armor
        self.actual_mr = self.base_mr
        self.actual_range = self.base_range
        self.actual_move_speed = self.base_move_speed
        self.actual_healshield_power = 0
        self.actual_tenacity = 0
        self.actual_ap = 0
        self.actual_crit_chance = 0
        self.actual_crit_damage = 0
        self.actual_bonus_armor = 0
        self.actual_bonus_mr = 0
        self.actual_total_armor = self.actual_armor + self.actual_bonus_armor
        self.actual_total_mr = self.actual_mr + self.actual_bonus_armor
        self.actual_armorpen_flat = 0
        self.actual_armorpen_percent = 0
        self.actual_magicpen_flat = 0
        self.actual_magicpen_percent = 0
        self.actual_lifesteal = 0
        self.actual_ah = 0
        self.actual_attack_speed = self.base_attack_speed
        self.actual_attack_speed_ratio = self.attack_speed_ratio
        self.actual_bonus_attack_speed_level = 0.00
        self.actual_bonus_attack_speed_external = 0.00
        self.actual_total_bonus_attack_speed = 0
        self.inventory = [None] * 6 # Iniciación del inventario
    
    def level_up(self):
        """
        Método para subir de nivel.
        
        Parámetros:
            - self : El campeón que lo llame será el parámetro.
        
        Return:
            Si el nivel del campeon es menor a 18 sus estadísticas aumentarán por la subida de nivel, en caso contrario no pasará nada.
        """
        if self.level < 18:
            self.level += 1
            self.actual_hp = (self.base_hp + self.base_hp_g * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actual_hp_regen = (self.base_hp_regen + self.base_hp_regen_g * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actual_mana = (self.base_mana + self.base_mana_g * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actual_mana_regen = (self.base_mana_regen + self.base_mana_regen_g * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actual_ad = (self.base_ad + self.base_ad_g * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actual_armor = (self.base_armor + self.base_armor_g * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actual_total_armor = self.actual_armor + self.actual_bonus_armor
            self.actual_mr = (self.base_mr + self.base_mr_g * (self.level - 1) * (0.7025 + 0.0175 * (self.level - 1)))
            self.actual_total_mr = self.actual_mr + self.actual_bonus_mr
            self.actual_bonus_attack_speed_level += self.actual_attack_speed_ratio * self.bonus_attack_speed * (0.7025 + 0.0175 * (self.level - 1))
            self.actual_total_bonus_attack_speed = self.actual_bonus_attack_speed_level + self.actual_bonus_attack_speed_external
            self.actual_attack_speed = self.base_attack_speed * (1 + self.actual_total_bonus_attack_speed)
        else:
            return
        
    def level_up_ability(self, ability):
        """
        Método para subir de nivel las habilidades.
        
        Parámetros:
            - ability : Debe ser un strque contenga uno de los siguientes para identificar que habildiad subir de nivel, puede verse a sobre-escritura:
            "Q", "W", "E", "R".
        
        Return:
            Si cumplen las condiciones se le sube de nivel la habildiad al campeon que llamó al método
        """
        if(ability == "Q"):
            if(self.q_level == 5):
                return
            else:
                self.q_level = self.q_level + 1
        if(ability == "W"):
            if(self.w_level == 5):
                return
            else:
                self.w_level = self.w_level + 1
        if(ability == "E"):
            if(self.e_level == 5):
                return
            else:
                self.e_level = self.e_level + 1
        if(ability == "R"):
            if(self.r_level == 3):
                return
            else:
                self.r_level = self.r_level + 1
    
    def add_item(self, item):
        """
        Método para agregar un item al inventario si encuentra un espacio disponible.
        
        Parámetro:
            - item : Es el nombre del item que figura como nombre del archivo correspondiente, debe pasarse como un str.
        
        Return:
            Si encontró un espacio en el inventario para sumar el item lo añadirá, en caso contrario sale del método.
        """
        for i in range(len(self.inventory)):
            if self.inventory[i] is None:
                self.inventory[i] = item
                self.update_stats(item, add=True)
                return
        return
    
    def remove_item(self, item):
        """
        Método para quitar un item del inventario.
        
        Parámetro:
            - item : Es el nombre del item que se quiere eliminar del inventario, debe ser el nombre que figura como nombre del archivo correspondiente y se pasa como str
        
        Return:
            Si encuentra el item en el inventario lo elimina y deja el espacio vació para disponibilidad de agregar otro item.
        """
        for i in range(len(self.inventory)):
            if self.inventory[i] == item:
                self.inventory[i] = None
                self.update_stats(item, add=False)
                return
        return
    
    def list_items(self):
        """
        Método para listar los items del inventario.
        
        Parámetro:
            - self : El campeón que llamó al método.
        
        Return:
            Devuevle un array con los nombres de los items que hay en el inventario.
        """
        inventory_content = []
        for i, item in enumerate(self.inventory):
            if item is not None:
                inventory_content.append(item.name)
        return inventory_content

    def update_stats(self, item, add):
        """
        Es llamado por los métodos 'add_item()' y 'remove_item()' para actualizar las estadísticas del campeon al momento de agregar o eliminar un item.
                
        Parámetros:
            - item : Es el mismo str que obtuvieron 'add_item()' o 'remove_item()'.
            - add : Cuendo se llama al método se especifica 'add=True' o 'add=False', True indica que se suman estadisticas y False indica que se restan estadísticas.
        """
        factor = 1 if add else -1
        self.actual_hp += item.hp * factor
        self.actual_hp_regen += item.hp_regen * factor
        self.actual_mana += item.mana * factor
        self.actual_mana_regen += item.mana_regen * factor
        self.actual_ad += item.ad * factor
        self.actual_ap += item.ap * factor
        self.actual_bonus_armor += item.armor * factor
        self.actual_bonus_mr += item.mr * factor
        self.actual_total_armor = self.actual_armor + self.actual_bonus_armor
        self.actual_total_mr = self.actual_mr + self.actual_bonus_mr
        self.actual_healshield_power += item.healshield_power * factor
        self.actual_tenacity += item.tenacity * factor
        self.actual_crit_chance += item.crit_chance * factor
        self.actual_crit_damage += item.crit_damage * factor
        self.actual_armorpen_flat += item.armorpen_flat * factor
        self.actual_armorpen_percent += item.armorpen_percent * factor
        self.actual_magicpen_flat += item.magicpen_flat * factor
        self.actual_magicpen_percent += item.magicpen_percent * factor
        self.actual_lifesteal += item.lifesteal * factor
        self.actual_ah += item.ah * factor
        self.actual_move_speed += item.movespeed_flat * factor
        self.actual_move_speed += item.movespeed_percent * factor
        self.actual_bonus_attack_speed_external += item.attack_speed * factor
        self.actual_total_bonus_attack_speed = self.actual_bonus_attack_speed_level + self.actual_bonus_attack_speed_external
        self.actual_attack_speed = self.base_attack_speed * (1 + self.actual_total_bonus_attack_speed)

    def damage(self, cantidad, tipo, Champion):
        """
        Calcula el daño que se hace a un objetivo, éste método solo será llamado por las habilidades de camepones o items que inflingan daño.
        
        Parámetros:
            - cantidad : es el valor inicial del daño inflingido por parte de la habidad pre resistencias en caso de no ser daño verdadero.
            - tipo : es el tipo de daño que se hará y se pasará como un str, puede ser de los siguientes tipo:
                "AD" para daño físico ; "AP" para daño mágico ; "TRUE" para daño verdadero(ignora resistencias)
            - Champion : objetivo del daño
        
        Return:
            Le resta vida al objetivo correspondiente luego de calcular las resistencias 
        """
        from src.Main import pantalla_ganador
        daño_total = 0
        
        if(tipo == "TRUE"):
            daño_total = cantidad
        elif(tipo == "AP"):
            if(Champion.actual_total_mr > 0):
                daño_total = (cantidad / (1 + Champion.actual_total_mr / 100)) #La resistencia reduce el daño
            else:
                daño_total = (cantidad * (2 - (100 / (100 - Champion.actual_total_mr)))) #Si la resistencia del objetivo es <=0 le hará el doble de daño
        elif(tipo == "AD"):
            if(Champion.actual_total_armor > 0):
                daño_total = (cantidad / (1 + Champion.actual_total_armor / 100))
            else:
                daño_total = (cantidad * (2 - (100 / (100 - Champion.actual_total_armor))))
        else:
            return
        
        daño_total = max(daño_total, 0) #Evita que el daño sea negativo
        Champion.actual_hp -= daño_total 
        Champion.actual_hp = max(Champion.actual_hp, 0) #Evita que la vida sea negativa
        if Champion.actual_hp == 0:
            Champion.se_muere()
            #pantalla_ganador(self)
    
    def se_muere (self):
        """
        Marca al campeón como muerto estableciendo su atributo 'its_alive' en False.
        """
        self.its_alive = False
    
    # Éstos métodos de habilidades están pensados para ser sobre-escritos
    def aa(self, objetivo):
        """Método para ataque básico"""
        self.damage(self.actual_ad, "AD", objetivo)
    
    def p(self):
        """Método para habildiad pasiva"""
    
    def q(self):
        """Método para habilidad Q"""
    
    def w(self):
        """Método para habilidad W"""
    
    def e(self):
        """Método para habilidad E"""
    
    def r(self):
        """Método para habildiad R"""
        
