from pygame import sprite, Surface
from constants import *
from Area import Area

class Map(sprite.Sprite):
    """
    A container class for areas which holds and loads information
    about maps.
    """

    def __init__(self):
        self.areas = sprite.Group()

    def add_area(self, area):
        self.areas.add(area)

def load_map(map_name):
    result = []
    map_dict = {}
    line_index = 0
    with open(map_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for linestr in lines:
            line = linestr.rstrip().split("\t")
            if linestr[0] == "#": continue
            elif not line_index:
                width = int(line[0])
                height = int(line[1])
                line_index += 1
            elif len(line) != width:
                raise Exception("Map %s corrupted: width." % map_name)
            
            else:
                if line_index%height == 0: y = height
                else: y = line_index % height

                for x in range(1, width+1):
                    try:
                        map_dict[(x,y)] += line[x-1]
                    except KeyError:
                        map_dict[(x,y)] = line[x-1]
                line_index += 1

    if line_index != height*3+1:
        print(line_index)
        raise Exception("Map %s corrupted: height." % map_name)

    # Here begins translation from characters to area.
    for key in map_dict.keys():
        area_info = []
        valuestring = map_dict[key]
        is_base = False
        is_hidden = True

        if "b" in valuestring:
            is_base = True
            valuestring = valuestring.replace("b", "")
        if "e" in valuestring:
            is_hidden = False
            valuestring = valuestring.replace("e", "")

        level      = int(valuestring[0])
        survivors  = int(valuestring[1])
        food       = int(valuestring[2])
        medicine   = int(valuestring[3])
        materials  = int(valuestring[4])
        threat     = int(valuestring[5])
        protection = int(valuestring[6])

        result.append([key, level, food, medicine, materials, survivors, threat,
                       None, # special properties, function added later!
                       is_hidden, is_base, protection])

    return result
