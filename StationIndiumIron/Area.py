from pygame import sprite, Surface
from constants import *

class Area(sprite.Sprite):
    """An area object on the map which holds information."""

    def __init__(self, group, coords, level=0, food=0, medicine=0,
                 materials=0, survivors=0, threat_level=0,
                 special_properties=None, is_hidden=0, is_base=0,
                 protection={"north":0, "south":0, "east":0, "west":0}):
        """Initiates the Area instace when called."""

        sprite.Sprite.__init__(self)
        group.add(self)
        self.image = Surface((TILESIZE, TILESIZE))
        self.image.fill(TILECOLOUR)
        self.rect = self.image.get_rect()
        self.x, self.y = (coords[0]*(TILESPACE+TILESIZE),
                          coords[1]*(TILESPACE+TILESIZE))
        self.rect.x, self.rect.y = (self.x, self.y)

        self.explored = 0
        self.level = level
        self.food = food
        self.medicine = medicine
        self.materials = materials
        self.survivors = survivors
        self.threatlevel = threat_level
        self.specialproperties = special_properties
        self.protection = protection
        self.is_hidden = is_hidden
        self.is_base = is_base
        self.selected = False

    def update(self, mouse_coords, select=False):
        if select == True and self.rect.collidepoint(mouse_coords):
            self.selected = True
        elif select == True:
            self.selected = False
            
        if self.is_hidden:
            self.image.fill(WORLDBGCOLOUR)
        elif self.selected and self.is_base:
            self.image.fill(BASESELECTCOLOUR)
        elif self.selected:
            self.image.fill(TILESELECTCOLOUR)
        elif self.rect.collidepoint(mouse_coords) and self.is_base:
            self.image.fill(MOUSEOVERBASECOLOUR)
        elif self.is_base:
            self.image.fill(BASECOLOUR)
        elif self.rect.collidepoint(mouse_coords):
            self.image.fill(MOUSEOVERTILECOLOUR)
        elif not self.selected:
            self.image.fill(TILECOLOUR)

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

