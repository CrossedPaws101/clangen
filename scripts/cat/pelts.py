from random import choice


class SingleColour():
    name = "SingleColour"
    sprites = {1: 'single'}
    white_patches = None

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = self.colour == "white"

    def __repr__(self):
        return self.colour + self.length

class TwoColour():
    name = "TwoColour"
    sprites = {1: 'single', 2: 'white'}

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = True

    def __repr__(self):
        return f"white and {self.colour}{self.length}"

class Tabby():
    name = "Tabby"
    sprites = {1: 'tabby', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} tabby"
        else:
            return self.colour + self.length + " tabby"

class Marbled():
    name = "Marbled"
    sprites = {1: 'marbled', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} marbled"
        else:
            return self.colour + self.length + " marbled"

class Rosette():
    name = "Rosette"
    sprites = {1: 'rosette', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} rosette"
        else:
            return self.colour + self.length + " rosette"

class Smoke():
    name = "Smoke"
    sprites = {1: 'smoke', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} smoke"
        else:
            return self.colour + self.length + " smoke"

class Ticked():
    name = "Ticked"
    sprites = {1: 'ticked', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} ticked"
        else:
            return self.colour + self.length + " ticked"

class Speckled():
    name = "Speckled"
    sprites = {1: 'speckled', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} speckled{self.length}"
        else:
            return f"{self.colour} speckled{self.length}"

class Bengal():
    name = "Bengal"
    sprites = {1: 'bengal', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} bengal{self.length}"
        else:
            return f"{self.colour} bengal{self.length}"

class Mackerel():
    name = "Mackerel"
    sprites = {1: 'mackerel', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} mackerel tabby{self.length}"
        else:
            return f"{self.colour} mackerel tabby{self.length}"

class Classic():
    name = "Classic"
    sprites = {1: 'classic', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} classic tabby{self.length}"
        else:
            return f"{self.colour} classic tabby{self.length}"

class Sokoke():
    name = "Sokoke"
    sprites = {1: 'sokoke', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} sokoke tabby{self.length}"
        else:
            return f"{self.colour} sokoke tabby{self.length}"

class Agouti():
    name = "Agouti"
    sprites = {1: 'agouti', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} agouti{self.length}"
        else:
            return f"{self.colour} agouti{self.length}"

class Singlestripe():
    name = "Singlestripe"
    sprites = {1: 'singlestripe', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} singlestripe{self.length}"
        else:
            return f"{self.colour} singlestripe{self.length}"

class Tortie():
    name = "Tortie"
    sprites = {1: 'tortie', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and tortoiseshell{self.length}"
        else:
            return f"tortoiseshell{self.length}"

class Calico():
    name = "Calico"
    sprites = {1: 'calico', 2: 'white'}

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = True

    def __repr__(self):
        return f"calico{self.length}"
    
class Pinstripe():
    name = "Pinstripe"
    sprites = {1: 'pinstripe', 2: 'white'}
    
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} pinstripe{self.length}"
        else:
            return f"{self.colour} pinstripe{self.length}"
        
class Merle():
    name = "Merle"
    sprites = {1: 'merle', 2: 'white'}
    
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} merle{self.length}"
        else:
            return f"{self.colour} merle{self.length}"

class Ghost():
    name = "Ghost"
    sprites = {1: 'ghost', 2: 'white'}
    
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} ghost{self.length}"
        else:
            return f"{self.colour} ghost{self.length}"
        
class Snowflake():
    name = "Snowflake"
    sprites = {1: 'snowflake', 2: 'white'}
    
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} snowflake{self.length}"
        else:
            return f"{self.colour} snowflake{self.length}"

class Cloudy():
    name = "Cloudy"
    sprites = {1: 'cloudy', 2: 'white'}
    
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} cloudy{self.length}"
        else:
            return f"{self.colour} cloudy{self.length}"

class RTabby():
    name = "RTabby"
    sprites = {1: 'rtabby', 2: 'white'}
    
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} rtabby{self.length}"
        else:
            return f"{self.colour} rtabby{self.length}"

class Pointed():
    name = "Pointed"
    sprites = {1: 'points', 2: 'white'}
    
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} points{self.length}"
        else:
            return f"{self.colour} points{self.length}"
        
class Ragdoll():
    name = "Ragdoll"
    sprites = {1: 'ragdolls', 2: 'white'}
    
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} ragdolls{self.length}"
        else:
            return f"{self.colour} ragdolls{self.length}"

class Shaded():
    name = "Shaded"
    sprites = {1: 'shaded', 2: 'white'}
    
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} shadedtabby{self.length}"
        else:
            return f"{self.colour} shadedtabby{self.length}"

class RSingle():
    name = "RSingle"
    sprites = {1: 'rsingle', 2: 'white'}
    
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} rsingle{self.length}"
        else:
            return f"{self.colour} rsingle{self.length}"

class Abyssinian():
    name = "Abyssinian"
    sprites = {1: 'abyssinian', 2: 'white'}
    
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} abyssinian{self.length}"
        else:
            return f"{self.colour} abyssinian{self.length}"

class Spiral():
    name = "Spiral"
    sprites = {1: 'spiral', 2: 'white'}
    
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} spiral{self.length}"
        else:
            return f"{self.colour} spiral{self.length}"


# ATTRIBUTES, including non-pelt related
pelt_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN',
    'BLACK'
    'WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK', 'PALE', 'CREAM2',
    'APRICOT', 'ORANGE', 'FAWN', 'CINNAMON', 'CHOCOLATE',
    'WHITE3', 'CLOUD', 'BLUE2',
    'HAZE', 'DARKBLUE', 'SOOT', 'IVORY', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON',
    'COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET'
]
pelt_c_no_white = [
    'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'PALEGINGER', 'GOLDEN',
    'GINGER', 'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK'
    'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK', 'PALE', 'CREAM2',
    'APRICOT', 'ORANGE', 'FAWN', 'CINNAMON', 'CHOCOLATE',
    'CLOUD', 'BLUE2',
    'HAZE', 'DARKBLUE', 'SOOT', 'IVORY', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON',
    'COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET'
]
pelt_c_no_bw = [
    'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'PALEGINGER', 'GOLDEN', 'GINGER',
    'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN'
    'BLUE', 'CARAMEL', 'LILAC', 'DARK', 'PALE', 'CREAM2',
    'APRICOT', 'ORANGE', 'FAWN', 'CINNAMON', 'CHOCOLATE',
    'CLOUD', 'BLUE2',
    'HAZE', 'DARKBLUE', 'SOOT', 'IVORY', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON',
    'COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET'
]
tortiepatterns = ['tortiesolid', 'tortietabby', 'tortiebengal', 'tortiemarbled', 'tortieticked',
    'tortiesmoke', 'tortierosette', 'tortiespeckled', 'tortiemackerel', 'tortieclassic',
    'tortiesokoke', 'tortieagouti', 'tortiersolid', 'tortiertabby', 'tortiebrindle',
    'tortieghost', 'tortiepinstripe', 'tortiesnowflake', 'tortiemerle']
patch_colours = ['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR', 'GOLDONE', 'GOLDTWO',
    'GOLDTHREE', 'GOLDFOUR', 'GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR',
    'DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR', 'CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']
tortiebases = ['single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette', 'speckled', 'mackerel',
    'classic', 'sokoke', 'agouti', 'singlestripe', 'rsingle', 'rtabby', 'ghost', 'pinstripe', 'snowflake', 'merle']
tortiecolours = ["SILVER", "GREY", "DARKGREY", "BLACK", "GHOST", "LIGHTBROWN", "BROWN", "DARKBROWN",
                 "BLUE", "CARAMEL", "LILAC", "DARK", "BLACK2", "FAWN", "CINNAMON", "CHOCOLATE",
                 "BLUE2", "HAZE", "DARKBLUE", "SOOT", "SAND", "BONE", "COFFEE", "MARSH", "OAK"]

pelt_length = ["short", "medium", "long"]
eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'GREY', 'CYAN', 'EMERALD', 'PALEBLUE', 
               'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'BLUE2', 'SUNLITICE', 'GREENYELLOW', 'PINK', 'SCARLET',
               'VIOLET', 'PALEYELLOW2', 'RED', 'AQUA', 'PALEVIOLET', 'SAGEGREEN', 'PALEBLUE2', 'BROWN', 'SPRINGGREEN', 'GOLDEN',
               'HONEY', 'COPPER2', 'MAGENTA', 'MINT', 'EMERALD2', 'PUMPKIN', 'ROSEGOLD',
               'DANDELION', 'INDIGO', 'AMARANTH', 'CORAL', 'DARKGREEN', 'DARKAMBER']
yellow_eyes = ['YELLOW', 'PALEYELLOW', 'GOLD', 'COPPER', 'GREENYELLOW', 'GOLDEN', 'HONEY', 'PALEYELLOW2', 'DANDELION']
blue_eyes = ['BLUE', 'CYAN', 'PALEBLUE', 'BLUE2', 'SUNLITICE', 'GREY', 'AQUA', 'MINT', 'PALEBLUE2']
green_eyes = ['PALEGREEN', 'GREEN', 'EMERALD', 'SAGE', 'HAZEL', 'EMERALD2', 'DARKGREEN', 'SAGEGREEN', 'SPRINGGREEN']
red_eyes = ['MAGENTA', 'AMARANTH', 'CORAL', 'DARKAMBER', 'PINK', 'SCARLET', 'BROWN', 'AMBER', 'RED', 'COPPER2', 'PUMPKIN', 'ROSEGOLD']
violet_eyes = ['VIOLET', 'INDIGO', 'PALEVIOLET', 'DARKBLUE', 'HEATHERBLUE']
# scars1 is scars from other cats, other animals - scars2 is missing parts - scars3 is "special" scars that could only happen in a special event
# bite scars by @wood pank on discord
scars1 = ["ONE", "TWO", "THREE", "TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY",
            "LEGBITE", "NECKBITE", "FACE", "MANLEG", "BRIGHTHEART", "MANTAIL", "BRIDGE", "RIGHTBLIND", "LEFTBLIND",
          "BOTHBLIND", "BEAKCHEEK", "BEAKLOWER", "CATBITE", "RATBITE", "QUILLCHUNK", "QUILLSCRATCH"]
scars2 = ["LEFTEAR", "RIGHTEAR", "NOTAIL", "HALFTAIL", "NOPAW", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]
scars3 = ["SNAKE", "TOETRAP", "BURNPAWS", "BURNTAIL", "BURNBELLY", "BURNRUMP", "FROSTFACE", "FROSTTAIL", "FROSTMITT", "FROSTSOCK",]

plant_accessories = ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL",
                    "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS", "DRY HERBS",
                    "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER",
                    
                    "BEECH LEAF", "BORAGE",
                    "POPPY2", "JUNIPER2", "COLTSFOOT", "TORMENTIL", "YARROW", "DAISY", "LAUREL2",
                    "OAK LEAF", "LAVENDER2", "BINDWEED", "BRIGHT-EYE",
                    
                    "CLOVERS", "SNAKEROOT", "SEAWEED", "PUMPKINS", "IVY WRAP", "HERB WRAP", "PINK HEARTS",
                    "RED HEARTS", "LILIES", "STICKS",
                    
                    "ORANGE LILY", "HONEY", "HONEYCOMB", "RED MUSHROOMS", "BROWN MUSHROOMS",
                    
                    "BARLEY", "SUNFLOWERS", "CORNFLOWER", "DRY THISTLE", "DRAGONFLY WINGS", "PINE WREATH",
                    "ROSE", "HANGING HERBS", "LILY", "COLORFUL LEAVES", "ACORN BRANCH", "DRY FIR",
                    "PUMPKIN LEAVES", "DRY MOSS", "PINECONE", "THORN COLLAR", "AUTUMN CHAIN", "ROWAN BRANCH"        
]
wild_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS",
                    
                    "BROWN HIDE", "GRAY HIDE", "BROWN WRAP", "GRAY WRAP", "MONARCH", "BUTTERFLY",
                    
                    "ROSES", "BLUEMOON", "BUTTERCUPS", "ORCHIDS", "AUTUMN", "VINES",
                    "GRASS", "RAINBOW FLOWERS", "PETUNIA", "CHRYSANTHEMUM",
                    "CHERRY BLOSSOM", "HELIOTROPES", "VALLEY LILIES" 
]
animal_accessories = ["BROWN SNAIL", "RED SNAIL", "WORM", "BEE", "SNAKE",
                      
                      "BROWN FROG", "SNAIL", "BUMBLEBEE", "GREEN FROG"
]
collars = [
    "CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME", "GREEN", "RAINBOW",
    "BLACK", "SPIKES", "WHITE", "PINK", "PURPLE", "MULTI", "INDIGO", "CRIMSONBELL", "BLUEBELL",
    "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL", "GREENBELL",
    "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "WHITEBELL", "PINKBELL", "PURPLEBELL",
    "MULTIBELL", "INDIGOBELL", "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
    "LIMEBOW", "GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "WHITEBOW", "PINKBOW",
    "PURPLEBOW", "MULTIBOW", "INDIGOBOW", "CRIMSONNYLON", "BLUENYLON", "YELLOWNYLON", "CYANNYLON", 
    "REDNYLON", "LIMENYLON", "GREENNYLON", "RAINBOWNYLON",
    "BLACKNYLON", "SPIKESNYLON", "WHITENYLON", "PINKNYLON", "PURPLENYLON", "MULTINYLON", "INDIGONYLON",
    "WHITEYARN", "BLUEYARN", "YELLOWYARN", "PURPLEYARN", "PINKYARN", "MINTYARN",
    "GREYYARN", "RAINBOWYARN", "GREENYARN", "REDYARN", "FADEDYARN", "ORANGEYARN", "GRADIENTYARN",
    "WHITEMANE", "PALEGRAYMANE", "SILVERMANE", "GRAYMANE", "DARKGRAYMANE",
    "BLACKMANE", "PALEGINGERMANE", "GOLDENMANE", "GINGERMANE", "DARKGINGERMANE",
    "LIGHTBROWNMANE", "BROWNMANE", "DARKBROWNMANE", "REDSCARF", "BLUESCARF",
    "YELLOWSCARF", "CYANSCARF", "CRIMSONSCARF", "LIMESCARF", "GREENSCARF",
    "RAINBOWSCARF", "GREYSCARF", "GOLDSCARF", "PINKSCARF", "PURPLESCARF",
    "ORANGESCARF", "REDSCARFS", "BLUESCARFS", "ORANGESCARFS", "MINTSCARFS",
    "CRIMSONSCARFS", "GREENSCARFS", "CYANSCARFS", "BLUE2SCARFS", "PURPLESCARFS",
    "GOLDSCARFS", "PINKSCARFS", "YELLOWSCARFS", "BLACKSCARFS", "CRIMSONSPIKE",
    "BLUESPIKE", "YELLOWSPIKE", "CYANSPIKE", "REDSPIKE", "LIMESPIKE", "GREENSPIKE",
    "RAINBOWSPIKE", "BLACKSPIKE", "SPIKESSPIKE", "PINKSPIKE", "PURPLESPIKE", "MULTISPIKE",
    "REDBANDANA", "BLUEBANDANA", "YELLOWBANDANA", "CYANBANDANA", "REDBANDANA", "LIMEBANDANA",
    "GREENBANDANA", "RAINBOWBANDANA", "BLACKBANDANA", "GOLDBANDANA", "PINKBANDANA",
    "PURPLEBANDANA", "MULTIBANDANA", "CAPE"
]

tabbies = ["Tabby", "Ticked", "Mackerel", "Classic", "Sokoke", "Agouti",
           "Pinstripe", "Ghost", "RTabby", "Shaded", "Spiral"]
spotted = ["Speckled", "Rosette"]
plain = ["SingleColour", "TwoColour", "Smoke", "Singlestripe", "RSingle", "Pointed", "Ragdoll"]
exotic = ["Bengal", "Marbled", "Snowflake", "Merle", "Abyssinian"]
torties = ["Tortie", "Calico"]
pelt_categories = [tabbies, spotted, plain, exotic, torties]

# SPRITE NAMES
single_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK'
    'WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK', 'PALE', 'CREAM2',
    'APRICOT', 'ORANGE', 'FAWN', 'CINNAMON', 'CHOCOLATE', 'WHITE3', 'CLOUD', 'BLUE2',
    'HAZE', 'DARKBLUE', 'SOOT', 'IVORY', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON',
    'COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET'
]
ginger_colours = ['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'PALE', 'CREAM2', 'APRICOT', 'ORANGE',
                  'IVORY', 'SAND', 'SUNBURST', 'BONE', 'LEMON']
black_colours = ['GREY', 'DARKGREY', 'GHOST', 'BLACK', 'BLACK2', 'DARK', 'DARKBLUE', 'SOOT']
white_colours = ['WHITE', 'PALEGREY', 'SILVER', 'WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'WHITE3', 'CLOUD', 'BLUE2', 'HAZE']
brown_colours = ['LIGHTBROWN', 'BROWN', 'DARKBROWN', 'FAWN', 'CINNAMON', 'CHOCOLATE', 'CARAMEL', 'SAND', 'COFFEE', 'MARSH', 'OAK']
red_colours = ['RUSSET', 'RUBY', 'PEACH', 'SCARLET']
colour_categories = [ginger_colours, black_colours, white_colours, brown_colours, red_colours]
eye_sprites = [
    'YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'BLUEYELLOW', 'BLUEGREEN',
    'GREY', 'CYAN', 'EMERALD', 'PALEBLUE', 'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'BLUE2', 
    'SUNLITICE', 'GREENYELLOW',
    'PINK', 'SCARLET',
    'VIOLET', 'PALEYELLOW2', 'RED', 'AQUA', 'PALEVIOLET', 'SAGEGREEN', 'PALEBLUE2', 'BROWN', 'SPRINGGREEN', 'GOLDEN',
    'HONEY', 'COPPER2', 'MAGENTA', 'MINT', 'EMERALD2', 'PUMPKIN', 'ROSEGOLD',
    'DANDELION', 'INDIGO', 'AMARANTH', 'CORAL', 'DARKGREEN', 'DARKAMBER'
]
little_white = ['LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 'BIB', 'VEE', 'PAWS', 
    'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO', 'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY', 'FRECKLES2', 'WHITEEAR', 'MASK', 'BROWNSPOTS',
    'SNOWBOOT', 'NIGHTMIST', 'SHADOWSIGHT', 'RETSUKO', 'OKAPI', 'CHIN',]
mid_white = ['TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK', 'MITAINE', 'SQUEAKS', 'STAR', 'HALFHEART', 'HUSKY', 'S',
             'SNOWSHOE', 'CHANCE', 'MOSSCLAW', 'DAPPLED', 'TWIST', 'WBELLY1', 'WBELLY2', 'CBELLY1', 'CBELLY2', 'WHITEHEAD']
high_white = ['ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTS2', 
    'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
    'CURVED', 'GLASS', 'MASKMANTLE', 'MOJO', 'SWIFTPAW', 'VENUS', 'FRECKLEMASK', 'DUTCH', 'EYEPATCH', 'SPOTTY', 'COW2']
mostly_white = ['VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE', 'STAINS1', 'STAINS2', 'CRESENT', 'COW',
                'HAWK', 'MOTH', 'DARKTAIL', 'HALFFACE3', 'BLACKSTAR']
point_markings = ['COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'KARPATI', 'SEPIAPOINT', 'MINKPOINT', 
    'SEALPOINT']
vit = ['VITILIGO', 'VITILIGO2', 'VILITIGO3']
white_sprites = [
    little_white, mid_white, high_white, mostly_white, point_markings, vit, 'FULLWHITE', 'EXTRA'
]

skin_sprites = ['BLACK', 'RED', 'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN', 'DARK', 'DARKGREY', 'GREY', 'DARKSALMON',
                'SALMON', 'PEACH', 'DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE']


# CHOOSING PELT
def choose_pelt(colour=None, white=None, pelt=None, length=None, category=None, determined=False):
    colour = colour
    white = white
    pelt = pelt
    length = length
    category = category
    if pelt is None:
        if category != None:
            pelt = choice(category)
    else:
        pelt = pelt
    if length is None:
        length = choice(pelt_length)
    if pelt == 'SingleColour':
        if colour is None and not white:
            return SingleColour(choice(pelt_colours), length)
        elif colour is None:
            return SingleColour("WHITE", length)
        else:
            return SingleColour(colour, length)
    elif pelt == 'TwoColour':
        if colour is None:
            return TwoColour(choice(pelt_c_no_white), length)
        else:
            return TwoColour(colour, length)
    elif pelt == 'Tabby':
        if colour is None and white is None:
            return Tabby(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Tabby(choice(pelt_colours), white, length)
        else:
            return Tabby(colour, white, length)
    elif pelt == 'Marbled':
        if colour is None and white is None:
            return Marbled(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Marbled(choice(pelt_colours), white, length)
        else:
            return Marbled(colour, white, length)
    elif pelt == 'Rosette':
        if colour is None and white is None:
            return Rosette(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Rosette(choice(pelt_colours), white, length)
        else:
            return Rosette(colour, white, length)
    elif pelt == 'Smoke':
        if colour is None and white is None:
            return Smoke(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Smoke(choice(pelt_colours), white, length)
        else:
            return Smoke(colour, white, length)
    elif pelt == 'Ticked':
        if colour is None and white is None:
            return Ticked(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Ticked(choice(pelt_colours), white, length)
        else:
            return Ticked(colour, white, length)
    elif pelt == 'Speckled':
        if colour is None and white is None:
            return Speckled(choice(pelt_colours), choice([False, True]),
                            length)
        elif colour is None:
            return Speckled(choice(pelt_colours), white, length)
        else:
            return Speckled(colour, white, length)
    elif pelt == 'Bengal':
        if colour is None and white is None:
            return Bengal(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Bengal(choice(pelt_colours), white, length)
        else:
            return Bengal(colour, white, length)
    elif pelt == 'Mackerel':
        if colour is None and white is None:
            return Mackerel(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Mackerel(choice(pelt_colours), white, length)
        else:
            return Mackerel(colour, white, length)
    elif pelt == 'Classic':
        if colour is None and white is None:
            return Classic(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Classic(choice(pelt_colours), white, length)
        else:
            return Classic(colour, white, length)
    elif pelt == 'Sokoke':
        if colour is None and white is None:
            return Sokoke(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Sokoke(choice(pelt_colours), white, length)
        else:
            return Sokoke(colour, white, length)
    elif pelt == 'Agouti':
        if colour is None and white is None:
            return Agouti(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Agouti(choice(pelt_colours), white, length)
        else:
            return Agouti(colour, white, length)
    elif pelt == 'Singlestripe':
        if colour is None and white is None:
            return Singlestripe(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Singlestripe(choice(pelt_colours), white, length)
        else:
            return Singlestripe(colour, white, length)
    elif pelt == 'Pinstripe':
        if colour is None and white is None:
            return Pinstripe(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Pinstripe(choice(pelt_colours), white, length)
        else:
            return Pinstripe(colour, white, length)
    elif pelt == 'Ghost':
        if colour is None and white is None:
            return Ghost(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Ghost(choice(pelt_colours), white, length)
        else:
            return Ghost(colour, white, length)
    elif pelt == 'Merle':
        if colour is None and white is None:
            return Merle(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Merle(choice(pelt_colours), white, length)
        else:
            return Merle(colour, white, length)
    elif pelt == 'Snowflake':
        if colour is None and white is None:
            return Snowflake(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Snowflake(choice(pelt_colours), white, length)
        else:
            return Snowflake(colour, white, length)
    elif pelt == 'Cloudy':
        if colour is None and white is None:
            return Cloudy(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Cloudy(choice(pelt_colours), white, length)
        else:
            return Cloudy(colour, white, length)
    elif pelt == 'RTabby':
        if colour is None and white is None:
            return RTabby(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return RTabby(choice(pelt_colours), white, length)
        else:
            return RTabby(colour, white, length)
    elif pelt == 'Pointed':
        if colour is None and white is None:
            return Pointed(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Pointed(choice(pelt_colours), white, length)
        else:
            return Pointed(colour, white, length)
    elif pelt == 'Ragdoll':
        if colour is None and white is None:
            return Ragdoll(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Ragdoll(choice(pelt_colours), white, length)
        else:
            return Ragdoll(colour, white, length)
    elif pelt == 'Shaded':
        if colour is None and white is None:
            return Shaded(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Shaded(choice(pelt_colours), white, length)
        else:
            return Shaded(colour, white, length)
    elif pelt == 'RSingle':
        if colour is None and white is None:
            return RSingle(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return RSingle(choice(pelt_colours), white, length)
        else:
            return RSingle(colour, white, length)
    elif pelt == 'Abyssinian':
        if colour is None and white is None:
            return Abyssinian(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Abyssinian(choice(pelt_colours), white, length)
        else:
            return Abyssinian(colour, white, length)
    elif pelt == 'Spiral':
        if colour is None and white is None:
            return Spiral(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Spiral(choice(pelt_colours), white, length)
        else:
            return Spiral(colour, white, length)
    elif pelt == 'Tortie':
        if white is None:
            return Tortie(colour, choice([False, True]), length)
        else:
            return Tortie(colour, white, length)
    else:
        return Calico(colour, length)

def describe_color(pelt, tortiecolour, tortiepattern, white_patches):
        color_name = ''
        color_name = str(pelt.colour).lower()
        if tortiecolour is not None:
            color_name = str(tortiecolour).lower()
        if color_name == 'palegrey':
            color_name = 'pale grey'
        elif color_name == 'darkgrey':
            color_name = 'dark grey'
        elif color_name == 'ghost':
            color_name = 'dark grey'
        elif color_name == 'paleginger':
            color_name = 'pale ginger'
        elif color_name == 'darkginger':
            color_name = 'dark ginger'
        elif color_name == 'lightbrown':
            color_name = 'light brown'
        elif color_name == 'darkbrown':
            color_name = 'dark brown'
        elif color_name == 'cream':
            color_name = 'cream'
        elif color_name == 'white2':
            color_name = 'white'
        elif color_name == 'black2':
            color_name = 'black'
        elif color_name == 'dark':
            color_name = 'dark grey-brown'
        elif color_name == 'pale':
            color_name = 'pale apricot'
        elif color_name == 'cream2':
            color_name = 'cream'
        elif color_name == 'white3':
            color_name = 'white'
        elif color_name == 'cloud':
            color_name = 'pale gray'
        elif color_name == 'blue2':
            color_name = 'blue'
        elif color_name == 'haze':
            color_name = 'gray'
        elif color_name == 'darkblue':
            color_name = 'dark blue'
        elif color_name == 'soot':
            color_name = 'dark gray-brown'
        elif color_name == 'ivory':
            color_name = 'cream'
        elif color_name == 'sand':
            color_name = 'light brown'
        elif color_name == 'sunburst':
            color_name = 'orange'
        elif color_name == 'russet':
            color_name = 'russet'
        elif color_name == 'bone':
            color_name == 'cream'
        elif color_name == 'lemon':
            color_name == 'yellow'
        elif color_name == 'coffee':
            color_name = 'brown'
        elif color_name == 'marsh':
            color_name = 'brown'
        elif color_name == 'oak':
            color_name = 'mahogany'
        elif color_name == 'ruby':
            color_name == 'dark red'
        elif color_name == 'peach':
            color_name == 'pinkish-red'
        elif color_name == 'scarlet':
            color_name == 'red'
        if pelt.name == "Tabby":
            color_name = color_name + ' tabby'
        elif pelt.name == "Speckled":
            color_name = color_name + ' speckled'
        elif pelt.name == "Bengal":
            color_name = color_name + ' bengal'
        elif pelt.name == "Marbled":
            color_name = color_name + ' marbled tabby'
        elif pelt.name == "Rosette":
            color_name = color_name + ' rosetted'
        elif pelt.name == "Ticked":
            color_name = color_name + ' ticked tabby'
        elif pelt.name == "Smoke":
            color_name = color_name + ' smoke'
        elif pelt.name == "Pinstripe":
            color_name = color_name + ' pinstripe tabby'
        elif pelt.name == "Ghost":
            color_name = color_name + ' ghost tabby'
        elif pelt.name == "Merle":
            color_name = color_name + ' merle'
        elif pelt.name == "Snowflake":
            color_name = color_name + ' snowflake'
        elif pelt.name == "Mackerel":
            color_name = color_name + ' mackerel tabby'
        elif pelt.name == "Sokoke":
            color_name = color_name + ' sokoke tabby'
        elif pelt.name == "Cloudy":
            color_name = color_name + ' cloudy marbled tabby'
        elif pelt.name == "RTabby":
            color_name = color_name + ' realistic tabby'
        elif pelt.name == "Pointed":
            color_name = color_name + ' colourpoint'
        elif pelt.name == "Ragdoll":
            color_name = color_name + ' ragdoll'
        elif pelt.name == "Shaded":
            color_name = color_name + ' shaded tabby'
        elif pelt.name == "Classic":
            color_name = color_name + ' classic tabby'
        elif pelt.name == "RSingle":
            color_name == 'solid ' + color_name
        elif pelt.name == "Agouti":
            color_name == color_name + ' agouti tabby'
        elif pelt.name == "Abyssinian":
            color_name == color_name + ' abyssinian'
        elif pelt.name == "Spiral":
            color_name == color_name + ' sokoke tabby'
        elif pelt.name == "Singlestripe":
            color_name = color_name + ', with a dorsal stripe,'

        elif pelt.name == "Tortie":
            if tortiepattern not in ["tortiesolid", "tortiesmoke"]:
                color_name = color_name + ' torbie'
            else:
                color_name = color_name + ' tortie'
        elif pelt.name == "Calico":
            if tortiepattern not in ["tortiesolid", "tortiesmoke"]:
                color_name = color_name + ' tabico'
            else:
                color_name = color_name + ' calico'
        # enough to comment but not make calico
        if white_patches is not None:
            if white_patches in little_white + mid_white:
                color_name = color_name + ' and white'
            # and white
            elif white_patches in high_white:
                if pelt.name != "Calico":
                    color_name = color_name + ' and white'
            # white and
            elif white_patches in mostly_white:
                color_name = 'white and ' + color_name
            # colorpoint
            elif white_patches in point_markings:
                color_name = color_name + ' point'
                if color_name == 'dark ginger point' or color_name == 'ginger point':
                    color_name = 'flame point'
            # vitiligo
            elif white_patches in vit:
                color_name = color_name + ' with vitiligo'
        else:
            color_name = color_name

        if color_name == 'tortie':
            color_name = 'tortoiseshell'

        if white_patches == 'FULLWHITE':
            color_name = 'white'

        if color_name == 'white and white':
            color_name = 'white'

        return color_name
