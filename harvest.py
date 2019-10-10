############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

# yellow_watermelon = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
# yellow_watermelon.add_pairing("ice cream")
# yellow_watermelon.update_code("YW") --> yellow_watermelon.code -> "YW"

def make_melon_types():
    """Returns a list of current melon types."""
    all_melon_types = []

    yellow_watermelon = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    casaba = MelonType("cas", 2003, "orange", False, False, "Casaba")
    crenshaw = MelonType("cren", 1996, "green", False, False, "Crenshaw")

    yellow_watermelon.add_pairing("ice cream")
    muskmelon.add_pairing("mint")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    crenshaw.add_pairing("prosciutto")

    all_melon_types = [yellow_watermelon, muskmelon, casaba, crenshaw]

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with ")
        for pairing in melon.pairings:
            print(f"- {pairing}")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

    melon_code_dict = {}

    for melon in melon_types:
        melon_code_dict[melon.code] = melon.name

    return melon_code_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, code, shape_rating, color_rating, from_field, harvested_by):
        """Initialize a melon."""
        self.code = code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.from_field = from_field
        self.harvested_by = harvested_by

    def is_sellable(self):
        """Determine if melon is saleable."""
        return self.shape_rating > 5 and self.color_rating > 5 and self.from_field != 3
    

# a_melon = Melon("yw", 3, 5, 4, "Sheila")
# a_melon.is_sellable()

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



