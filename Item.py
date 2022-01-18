class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value

#name, attack, armor, weight, price


class Weapon(Item):
    def __init__(self, name, value, damage):
        super().__init__(name, value)
        self.damage = damage


class Armor(Item):
    def __init__(self, name, value, defense):
        super().__init__(name, value)
        self.defense = defense


class Quest_Item(Item):
    def __init__(self, name, value, quest_item):
        super().__init__(name, value)
        self.quest_item = quest_item

# class Weapon:
# class Armor:
