############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk_melon = MelonType('musk', '1998', 'green', True, True, "Musk Melon")
    casaba_melon = MelonType('cas','2003','orange', False, False, "Casaba Melon")
    crenshaw_melon = MelonType('cren','1996', 'green', True, False, "Crenshaw Melon")
    yellow_water_melon = MelonType('yw','2013', 'yellow', False, True, "Yellow Watermelon")

    musk_melon.add_pairing(["mint"])
    casaba_melon.add_pairing(["strawberries","mint"])
    crenshaw_melon.add_pairing(["proscuitto"])
    yellow_water_melon.add_pairing(["ice cream"])

    all_melon_types.extend([musk_melon, casaba_melon, crenshaw_melon, yellow_water_melon])

    return all_melon_types

def print_pairing_info():
    """Prints information about each melon type's pairings."""

    melon_types = make_melon_types()
    
    for melon in melon_types:
        print (f"{melon.name} pairs with")

        for pair in melon.pairings:
            print (f"- {pair}")
 
def make_melon_type_lookup():
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_types = make_melon_types()
    melons_dic = {}

    for melon in melon_types:
        melons_dic[melon.code] = [melon.first_harvest, melon.color, melon.is_seedless, melon.is_bestseller, melon.name, melon.pairings]

    return melons_dic

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field_loc, harvest_human):
        """Initialize a melon."""
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_loc = field_loc
        self.harvest_human = harvest_human

        self.sellable = None

    def is_sellable(self):
        """Replace the reporting code with the new_code."""

        if self.shape_rating > 5 and self.color_rating > 5 and self.field_loc != 3:
            self.sellable = True
        else:
            self.sellable = False

def make_melons():
    """Returns a list of Melon objects."""

    all_melon_types = []

    melon_1 = Melon("yw",8,7,2,"Sheila")
    melon_2 = Melon("yw",3,4,2,"Sheila")
    melon_3 = Melon("yw",9,8,3,"Sheila")
    melon_4 = Melon("cas",10,6,35,"Sheila")
    melon_5 = Melon("cren",8,9,35,"Mike")
    melon_6 = Melon("cren",8,2,35,"Mike")
    melon_7 = Melon("cren",2,3,4,"Mike")
    melon_8 = Melon("musk",6,7,4,"Mike")
    melon_9 = Melon("yw",7,10,3,"Sheila")

    all_melon_types.extend([melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9])

    for melon in all_melon_types:
        melon.is_sellable()
    
    return all_melon_types

def get_sellability_report():
    """Given a list of melon object, prints whether each one is sellable."""

    all_melon_types = make_melons()
    
    for melon in all_melon_types:
        if melon.sellable == True:
            print (f"Harvested by {melon.harvest_human} from {melon.field_loc} (CAN BE SOLD)")
        elif melon.sellable == None:
            print ("It is none")
        else:
            print (f"Harvested by {melon.harvest_human} from {melon.field_loc} (NOT SELLABLE)")
            





