class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.inventory = {
            "gold": 100,
            "weapons": []
        }
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.coordinates = { #use coord plane for map
            'xCoord': 0,
            'yCoord': 0,
        }
    
    def get_inventory(self):
        return self.inventory
    
    def get_hp(self):
        return self.hp
    def set_hp(self,hp):
        self.hp = hp
    def get_mp(self):
        return self.mp
    def set_mp(self,mp):
        self.mp = mp
    #implement heal hp and heal mp - cannot overflow maxHP

    def get_coordinates(self):
        return self.coordinates

    def get_name(self):
        return self.name

    def set_coordinates(self,x,y):
        self.coordinates['xCoord'] = x
        self.coordinates['yCoord'] = y
    

#Notes: Perhaps make a general class that is "Mob" with HP stat... coudl be useful.





