class Character:
    def __init__(self):
        self.name = ''
        self.char_class = ''  # Wizard, Knight, or Archer
        self.gold = 100  # currency int type
        self.maxHP = 100
        self.maxMP = 50
        self.hp = 100
        self.mp = 50
        self.inventory = []  # player inventory (item objects)
        self.status_effects = []  # list of status effects
        self.location = '00'  # coordinate list for map

    def set_name(self, name):
        self.name = name

    def set_class(self, char_class):
        self.char_class = char_class

    def get_inventory(self):
        return self.inventory

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp

    def get_mp(self):
        return self.mp

    def set_mp(self, mp):
        self.mp = mp

    # implement heal hp and heal mp - cannot overflow maxHP

    def get_location(self):
        return self.location

    def get_name(self):
        return self.name

    def set_location(self, place):
        self.location = place

    def examine(self):
        pass


# Notes: Perhaps make a general class that is "Mob" with HP stat... could be useful.
