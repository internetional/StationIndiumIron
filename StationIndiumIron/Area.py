from pygame import sprite, Surface
from constants import TILESIZE, TILECOLOUR, TILESPACE

class Area(sprite.Sprite):
    """An area object on the map which holds information."""

    def __init__(self, group, coords, level=0, food=0, medicine=0,
                 materials=0, survivors=0, threat_level=0,
                 special_properties=None,
                 protection={"north":0, "south":0, "east":0, "west":0}):
        """Initiates the Area instace when called."""

        sprite.Sprite.__init__(self)
        group.add(self)
        self.image = Surface((TILESIZE, TILESIZE))
        self.image.fill(TILECOLOUR)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (coords[0]*(TILESPACE+TILESIZE),
                                    coords[1]*(TILESPACE+TILESIZE))

        self.explored = 0
        self.level = level
        self.food = food
        self.medicine = medicine
        self.materials = materials
        self.survivors = survivors
        self.threatlevel = threat_level
        self.specialproperties = special_properties
        self.protection = protection

    def set_explored(self, new_ratio):
        self.explored = new_ratio

    def set_food(self, new_food):
        self.food = new_food

    def set_medicine(self, new_medicine):
        self.medicine = new_medicine

    def set_materials(self, new_materials):
        self.materials = new_materials

    def set_survivors(self, new_survivors):
        self.survivors = new_survivors

    def set_threatlevel(self, new_threatlevel):
        self.threatlevel = new_threatlevel

    def set_specialproperties(self, new_specialproperties):
        self.specialproperties = new_specialproperties

    def set_protection(self, direction, new_protection):
        self.protection[direction] = new_protection



