class Character:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.inventory = {
            "gold": 100,
            "weapons": []
        }
        self.coordinates = { #use coord plane for map
            'xCoord': 0,
            'yCoord': 0,
        }
    
    def get_inventory(self):
        return self.inventory

    def get_coordinates(self):
        return self.coordinates

    def get_name(self):
        return self.name

    def set_coordinates(self,x,y):
        self.coordinates['xCoord'] = x
        self.coordinates['yCoord'] = y
        
    def get_sex(self):
        return self.sex
    





