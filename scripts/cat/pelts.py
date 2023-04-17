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
    
    
class Freckled():
    name = "Freckled"
    sprites = {1: 'freckled', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} freckled{self.length}"
        else:
            return f"{self.colour} freckled{self.length}"

class Mosaic():
    name = "Mosaic"
    sprites = {1: 'mosaic', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} mosaic{self.length}"
        else:
            return f"{self.colour} mosaic{self.length}"

class Lynx():
    name = "Lynx"
    sprites = {1: 'lynx', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} lynx{self.length}"
        else:
            return f"{self.colour} lynx{self.length}"
        
class Moro():
    name = "Moro"
    sprites = {1: 'moro', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} moro{self.length}"
        else:
            return f"{self.colour} moro{self.length}"

class Morotabby():
    name = "Morotabby"
    sprites = {1: 'morotabby', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} morotabby{self.length}"
        else:
            return f"{self.colour} morotabby{self.length}"

class Pointed():
    name = "Pointed"
    sprites = {1: 'pointed', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} pointed{self.length}"
        else:
            return f"{self.colour} pointed{self.length}"

class Abyssinian():
    name = "Abyssinian"
    sprites = {1: 'abyssinian', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} abyssinian{self.length}"
        else:
            return f"{self.colour} abyssinian{self.length}"
    
class Clouded():
    name = "Clouded"
    sprites = {1: 'clouded', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} clouded{self.length}"
        else:
            return f"{self.colour} clouded{self.length}"

class Doberman():
    name = "Doberman"
    sprites = {1: 'doberman', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} doberman{self.length}"
        else:
            return f"{self.colour} doberman{self.length}"

class Ghost():
    name = "Ghost"
    sprites = {1: 'ghost', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} ghost{self.length}"
        else:
            return f"{self.colour} ghost{self.length}"

class Merle():
    name = "Merle"
    sprites = {1: 'merle', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} merle{self.length}"
        else:
            return f"{self.colour} merle{self.length}"

class Monarch():
    name = "Monarch"
    sprites = {1: 'monarch', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} monarch{self.length}"
        else:
            return f"{self.colour} monarch{self.length}"

class Oceloid():
    name = "Oceloid"
    sprites = {1: 'oceloid', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} oceloid{self.length}"
        else:
            return f"{self.colour} oceloid{self.length}"
    
class Pinstripe():
    name = "Pinstripe"
    sprites = {1: 'pinstripe', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} pinstripe{self.length}"
        else:
            return f"{self.colour} pinstripe{self.length}"

class Snowflake():
    name = "Snowflake"
    sprites = {1: 'snowflake', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} snowflake{self.length}"
        else:
            return f"{self.colour} snowflake{self.length}"

class Ghostsmoke():
    name = "Ghostsmoke"
    sprites = {1: 'ghostsmoke', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} ghostsmoke{self.length}"
        else:
            return f"{self.colour} ghostsmoke{self.length}"


# ATTRIBUTES, including non-pelt related
pelt_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN',
    'BLACK',
    'WHITETWO', 'CLOUD', 'BLUE', 'HAZE', 'DARKBLUE', 'SOOT', 'IVORY', 'SAND',
    'SUNBURST', 'RUSSET', 'BONE', 'LEMON', 'COFFEE', 'MARSH', 'OAK', 'RUBY',
    'PEACH', 'SCARLET'
]
pelt_c_no_white = [
    'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'PALEGINGER', 'GOLDEN',
    'GINGER', 'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK',
    'CLOUD', 'BLUE', 'HAZE', 'DARKBLUE', 'SOOT', 'IVORY', 'SAND',
    'SUNBURST', 'RUSSET', 'BONE', 'LEMON', 'COFFEE', 'MARSH', 'OAK', 'RUBY',
    'PEACH', 'SCARLET'
]
pelt_c_no_bw = [
    'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'PALEGINGER', 'GOLDEN', 'GINGER',
    'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN',
    'CLOUD', 'BLUE', 'HAZE', 'DARKBLUE', 'SOOT', 'IVORY', 'SAND',
    'SUNBURST', 'RUSSET', 'BONE', 'LEMON', 'COFFEE', 'MARSH', 'OAK', 'RUBY',
    'PEACH', 'SCARLET'
]

tortiepatterns = ['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH', 'MINIMALONE', 'MINIMALTWO', 'MINIMALTHREE', 'MINIMALFOUR',
                  'OREO', 'SWOOP', 'MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 'STREAMSTRIKE', 'ORIOLE',
                  'ROBIN', 'BRINDLE', 'PAIGE',
                  'CLASSICMASK', 'SINGLESTRIPEMASK', 'AGOUTMASK', 'BENGALMASK', 'TABBYMASK', 'SOKOKEMASK', 
                  'SPECKLEDMASK', 'TICKEDMASK', 'SMOKEMASK', 'ROSETTEMASK', 'MARBLEDMASK', 'MACKERELMASK',
                  'BROKENONE', 'BROKENTWO', 'BROKENTHREE', 'BROKENFOUR', 'GLITCH', 'WAVE', 
                  'STRIPESMASK', 'KOI', 'SKULL', 'LITTLE', 'O', 'TOADSTOOL', 
                  'PONITMASK', 'SPOTSCHAOS', 'FOG', 'SUNSET', 'TAIL', 'MOOSTONE',
]
tortiebases = ['single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette', 'speckled', 'mackerel',
               'classic', 'sokoke', 'agouti', 'singlestripe',
               'freckled', 'mosaic', 'moro', 'morotabby', 'lynx', 'pointed', 'abyssinian', 'clouded', 'doberman', 'ghost',
               'merle', 'monarch', 'oceloid', 'pinstripe', 'snowflake', 'ghostsmoke']

pelt_length = ["short", "medium", "long"]
eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'GREY', 'CYAN', 'EMERALD', 'PALEBLUE', 
    'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT', 'SUNLITICE', 'GREENYELLOW', 'BRONZE', 'SILVER']
yellow_eyes = ['YELLOW', 'AMBER', 'PALEYELLOW', 'GOLD', 'COPPER', 'GREENYELLOW', 'BRONZE', 'SILVER']
blue_eyes = ['BLUE', 'DARKBLUE', 'CYAN', 'PALEBLUE', 'HEATHERBLUE', 'COBALT', 'SUNLITICE', 'GREY']
green_eyes = ['PALEGREEN', 'GREEN', 'EMERALD', 'SAGE', 'HAZEL']
# scars1 is scars from other cats, other animals - scars2 is missing parts - scars3 is "special" scars that could only happen in a special event
# bite scars by @wood pank on discord
scars1 = ["ONE", "TWO", "THREE", "TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY",
          "LEGBITE", "NECKBITE", "FACE", "MANLEG", "BRIGHTHEART", "MANTAIL", "BRIDGE", "RIGHTBLIND", "LEFTBLIND",
          "BOTHBLIND", "BEAKCHEEK", "BEAKLOWER", "CATBITE", "RATBITE", "QUILLCHUNK", "QUILLSCRATCH"]
scars2 = ["LEFTEAR", "RIGHTEAR", "NOTAIL", "HALFTAIL", "NOPAW", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]
scars3 = ["SNAKE", "TOETRAP", "BURNPAWS", "BURNTAIL", "BURNBELLY", "BURNRUMP", "FROSTFACE", "FROSTTAIL", "FROSTMITT",
          "FROSTSOCK"]

# make sure to add plural and singular forms of new accs to acc_display.json so that they will display nicely
plant_accessories = ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL",
                     "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS", "DRY HERBS",
                     "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER",
                     "BARLEY", "SUNFLOWERS", "CORNFLOWER", "DRY THISTLE", "DRAGONFLY WINGS", "PINE WREATH",
                     "ROSE", "HANGING HERBS", "LILY", "HARE TAIL", "WILDFLOWERS WREATH", "SEAGLASS",
                     "PUMPKIN LEAVES", "DRY MOSS", "PINECONE", "THORN COLLAR", "AUTUMN CHAIN", "ROWAN BRANCH",
                     "COLORFUL LEAVES", "ACORN BRANCH", "DRY FIR", "DRY ROSE", "SPIDER'S WEB", "CROW FEATHERS",
                     "IVY WRAP", "HERB WRAP", "PINK HEARTS", "RED HEARTS", "LILIES",
                     
                     "CHERRY BLOSSOM", "TULIP PETALS", "CLOVER FLOWER", "PANSIES", "BELLFLOWERS", "FORSYTHIA",
                     "MINT LEAF", "STICKS", "SPRING FEATHERS", "SNAIL SHELL", "CATKIN", "FERN",
                     "STRAW MANE", "MISTLETOE", "RED POINSETTIA", "WHITE POINSETTIA", "COTONEASTER WREATH", "YEW",
                     "OAK STICK ANTLERS", "BIRCH STICK ANTLERS", "DOGWOOD", "FROSTED IVY", "HEATHER", "FANGS"
                     ]
wild_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS",
                    "MONARCH", "BUTTERFLY", "BROWN HIDE", "GRAY HIDE", "BROWN WRAP", "GRAY WRAP"
                    ]
tail_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS",
                    "BROWN WRAP", "GRAY WRAP", "IVY WRAP", "HERB WRAP", "PINK HEARTS", "RED HEARTS",
                    "DRY THISTLE", "HANGING HERBS", "LILY", "SEAGLASS", "DRY MOSS", "PINECONE",
                    "COLORFUL LEAVES", "SPIDER'S WEB", "CROW FEATHERS",
                    "CHERRY BLOSSOM", "CLOVER FLOWER", "FORSYTHIA",
                    "SPRING FEATHERS", "FERN", "MISTLETOE"]
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
]

tabbies = ["Tabby", "Ticked", "Mackerel", "Classic", "Sokoke", "Agouti", "Pinstripe", "Ghost", "Monarch", "Clouded", "Ghostsmoke"]
spotted = ["Speckled", "Rosette", "Oceloid"]
plain = ["SingleColour", "TwoColour", "Smoke", "Singlestripe"]
exotic = ["Bengal", "Marbled", "Freckled", "Mosaic", "Lynx", "Moro", "Morotabby", "Pointed",
          "Abyssinian", "Doberman", "Merle", "Snowflake"]
torties = ["Tortie", "Calico"]
pelt_categories = [tabbies, spotted, plain, exotic, torties]

# SPRITE NAMES
single_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK',
    'WHITETWO', 'CLOUD', 'BLUE', 'HAZE', 'DARKBLUE', 'SOOT', 'IVORY', 'SAND',
    'SUNBURST', 'RUSSET', 'BONE', 'LEMON', 'COFFEE', 'MARSH', 'OAK', 'RUBY',
    'PEACH', 'SCARLET'
]
ginger_colours = ['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'IVORY', 'SAND', 'SUNBURST', 'BONE', 'LEMON']
black_colours = ['GREY', 'DARKGREY', 'GHOST', 'BLACK','DARKBLUE', 'SOOT']
white_colours = ['WHITE', 'PALEGREY', 'SILVER', 'WHITETWO', 'CLOUD', 'BLUE', 'HAZE']
brown_colours = ['LIGHTBROWN', 'BROWN', 'DARKBROWN', 'SAND', 'COFFEE', 'MARSH', 'OAK']
red_colours = ['RUSSET', 'RUBY', 'PEACH', 'SCARLET']
colour_categories = [ginger_colours, black_colours, white_colours, brown_colours, red_colours]
eye_sprites = [
    'YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'BLUEYELLOW', 'BLUEGREEN',
    'GREY', 'CYAN', 'EMERALD', 'PALEBLUE', 'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT',
    'SUNLITICE', 'GREENYELLOW', 'BRONZE', 'SILVER'
]
little_white = ['LITTLE', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 'BIB', 'VEE', 'PAWS',
                'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO', 'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY', 'LUNA',
                'EXTRA']
mid_white = ['TUXEDO', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK', 'MITAINE', 'SQUEAKS', 'STAR',
             'WINGS']
high_white = ['ANY', 'ANYTWO', 'BROKEN', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTSTWO',
              'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
              'CURVED', 'GLASS', 'MASKMANTLE', 'MAO', 'PAINTED']
mostly_white = ['VAN', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE',
                'CHESTSPECK', 'BLACKSTAR', 'PETAL', 'HEARTTWO']
point_markings = ['COLOURPOINT', 'RAGDOLL', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT']
vit = ['VITILIGO', 'VITILIGOTWO', 'MOON', 'PHANTOM', 'KARPATI', 'POWDER']
white_sprites = [
    little_white, mid_white, high_white, mostly_white, point_markings, vit, 'FULLWHITE']

skin_sprites = ['BLACK', 'RED', 'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN', 'DARK', 'DARKGREY', 'GREY', 'DARKSALMON',
                'SALMON', 'PEACH', 'DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE']
manes = ['BLACKMANE', 'REDMANE', 'PINKMANE', 'DARKBROWNMANE', 'BROWNMANE', 'LIGHTBROWNMANE',
         'DARKMANE', 'DARKGREYMANE', 'GREYMANE', 'COCOMANE', 'WHEATMANE', 'CREAMMANE',
         'DARKMARBLEDMANE', 'MARBLEDMANE', 'LIGHTMARBLEDMANE', 'DARKBLUEMANE', 'BLUEMANE', 'LIGHTBLUEMANE']


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
    elif pelt == 'Freckled':
        if colour is None and white is None:
            return Freckled(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Freckled(choice(pelt_colours), white, length)
        else:
            return Freckled(colour, white, length)
    elif pelt == 'Mosaic':
        if colour is None and white is None:
            return Mosaic(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Mosaic(choice(pelt_colours), white, length)
        else:
            return Mosaic(colour, white, length)
    elif pelt == 'Lynx':
        if colour is None and white is None:
            return Lynx(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Lynx(choice(pelt_colours), white, length)
        else:
            return Lynx(colour, white, length)
    elif pelt == 'Moro':
        if colour is None and white is None:
            return Moro(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Moro(choice(pelt_colours), white, length)
        else:
            return Moro(colour, white, length)
    elif pelt == 'Morotabby':
        if colour is None and white is None:
            return Morotabby(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Morotabby(choice(pelt_colours), white, length)
        else:
            return Morotabby(colour, white, length)
    elif pelt == 'Pointed':
        if colour is None and white is None:
            return Pointed(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Pointed(choice(pelt_colours), white, length)
        else:
            return Pointed(colour, white, length)
    elif pelt == 'Abyssinian':
        if colour is None and white is None:
            return Abyssinian(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Abyssinian(choice(pelt_colours), white, length)
        else:
            return Abyssinian(colour, white, length)
    elif pelt == 'Clouded':
        if colour is None and white is None:
            return Clouded(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Clouded(choice(pelt_colours), white, length)
        else:
            return Clouded(colour, white, length)
    elif pelt == 'Doberman':
        if colour is None and white is None:
            return Doberman(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Doberman(choice(pelt_colours), white, length)
        else:
            return Doberman(colour, white, length)
    elif pelt == 'Ghost':
        if colour is None and white is None:
            return Ghost(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Ghost(choice(pelt_colours), white, length)
        else:
            return Ghost(colour, white, length)
    elif pelt == 'Merle':
        if colour is None and white is None:
            return Merle(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Merle(choice(pelt_colours), white, length)
        else:
            return Merle(colour, white, length)
    elif pelt == 'Monarch':
        if colour is None and white is None:
            return Monarch(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Monarch(choice(pelt_colours), white, length)
        else:
            return Monarch(colour, white, length)
    elif pelt == 'Oceloid':
        if colour is None and white is None:
            return Oceloid(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Oceloid(choice(pelt_colours), white, length)
        else:
            return Oceloid(colour, white, length)
    elif pelt == 'Pinstripe':
        if colour is None and white is None:
            return Pinstripe(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Pinstripe(choice(pelt_colours), white, length)
        else:
            return Pinstripe(colour, white, length)
    elif pelt == 'Snowflake':
        if colour is None and white is None:
            return Snowflake(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Snowflake(choice(pelt_colours), white, length)
        else:
            return Snowflake(colour, white, length)
    elif pelt == 'Ghostsmoke':
        if colour is None and white is None:
            return Ghostsmoke(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Ghostsmoke(choice(pelt_colours), white, length)
        else:
            return Ghostsmoke(colour, white, length)
    elif pelt == 'Tortie':
        if white is None:
            return Tortie(colour, choice([False, True]), length)
        else:
            return Tortie(colour, white, length)
    else:
        return Calico(colour, length)
    
def describe_appearance(cat, short=False):
    
    # Define look-up dictionaries
    if short:
        renamed_colors = {
            "palegrey": "gray",
            "darkgrey": "gray",
            "paleginger": "ginger",
            "darkginger": "ginger",
            "lightbrown": "brown",
            "darkbrown": "brown",
            "ghost": "black",
            "white2": "white",
            "cloud": "gray",
            "blue": "blue",
            "haze": "gray",
            "darkblue": "blue",
            "soot": "gray",
            "ivory": "cream",
            "sand": "brown",
            "sunburst": "orange",
            "russet": "red",
            "bone": "cream",
            "lemon": "yellow",
            "coffee": "brown",
            "marsh": "brown",
            "oak": "brown",
            "ruby": "red",
            "peach": "red",
            "scarlet": "red"
        }
    else:
        renamed_colors = {
            "palegrey": "pale gray",
            "darkgrey": "dark gray",
            "paleginger": "pale ginger",
            "darkginger": "dark ginger",
            "lightbrown": "light brown",
            "darkbrown": "dark brown",
            "ghost": "black",
            "white2": "white",
            "cloud": "pale gray",
            "blue": "blue",
            "haze": "gray",
            "darkblue": "dark blue",
            "soot": "dark gray",
            "ivory": "brownish cream",
            "sand": "sandy brown",
            "sunburst": "bright orange",
            "russet": "russet",
            "bone": "brownish cream",
            "lemon": "yellow",
            "coffee": "brown",
            "marsh": "brown",
            "oak": "russet brown",
            "ruby": "dark red",
            "peach": "pale red",
            "scarlet": "bright red"
        }

    pattern_des = {
        "Tabby": "c_n tabby",
        "Speckled": "speckled c_n",
        "Bengal": "unusually dappled c_n",
        "Marbled": "c_n tabby",
        "Ticked": "c_n ticked",
        "Smoke": "c_n smoke",
        "Mackerel": "c_n tabby",
        "Classic": "c_n tabby",
        "Agouti": "c_n tabby",
        "Singlestripe": "dorsal-striped c_n",
        "Rosette": "unusually spotted c_n",
        "Sokoke": "c_n tabby",
        "Freckled": "unusually dappled c_n",
        "Mosaic": "unusually caped c_n",
        "Lynx": "unusually flecked c_n",
        "Moro": "unusually brindled c_n",
        "Morotabby": "unusually brindled c_n tabby",
        "Pointed": "c_n pointed",
        "Abyssinian": "exotic c_n",
        "Clouded": "c_n tabby",
        "Doberman": "dog-looking c_n",
        "Ghost": "faintly striped c_n",
        "Merle": "unusually patched c_n",
        "Monarch": "unusually striped c_n tabby",
        "Oceloid": "unusually spotted c_n",
        "Snowflake": "unusually dotted c_n",
        "Ghostsmoke": "unusual c_n smoke"
    }

    # Start with determining the base color name. 
    color_name = str(cat.pelt.colour).lower()
    if color_name in renamed_colors:
        color_name = renamed_colors[color_name]
    
    # Replace "white" with "pale" if the cat is 
    if cat.pelt.name not in ["SingleColour", "TwoColour", "Tortie", "Calico"] and color_name == "white":
        color_name = "pale"

    # Time to descibe the pattern and any additional colors. 
    if cat.pelt.name in pattern_des:
        color_name = pattern_des[cat.pelt.name].replace("c_n", color_name)
    elif cat.pelt.name in torties:
        # Calicos and Torties need their own desciptions. 
        if short:
            # If using short, don't add describe the colors of calicos and torties. Just call them calico, tortie, or mottled. 
            # If using short, don't describe the colors of calicos and torties. Just call them calico, tortie, or mottled. 
            if cat.pelt.colour in black_colours + brown_colours + white_colours and \
                cat.tortiecolour in black_colours + brown_colours + white_colours:
                color_name = "mottled"
            else:
                color_name = cat.pelt.name.lower()
        else:
            base = cat.tortiebase.lower()
            if base in tabbies + ['bengal', 'rosette', 'speckled', 'oceloid', 'monarch', 'pinstripe']:
                base = 'tabby'
            else:
                base = ''

            patches_color = cat.tortiecolour.lower()
            if patches_color in renamed_colors:
                patches_color = renamed_colors[patches_color]
            color_name = f"{color_name}/{patches_color}"
            
            if cat.pelt.colour in black_colours + brown_colours + white_colours and \
                cat.tortiecolour in black_colours + brown_colours + white_colours:
                    color_name = f"{color_name} mottled"
            else:
                color_name = f"{color_name} {cat.pelt.name.lower()}"

    if cat.white_patches:
        if cat.white_patches == "FULLWHITE":
            # If the cat is fullwhite, discard all other information. They are just white. 
            color_name = "white"
        if cat.white_patches in mostly_white and cat.pelt.name != "Calico":
            color_name = f"white and {color_name}"
        elif cat.pelt.name != "Calico":
            color_name = f"{color_name} and white"
    
    if cat.points:
        color_name = f"{color_name} point"
        if "ginger point" in color_name:
            color_name.replace("ginger point", "flame point")

    if "white and white" in color_name:
        color_name = color_name.replace("white and white", "white")

    # Now it's time for gender
    if cat.genderalign in ["female", "trans female"]:
        color_name = f"{color_name} she-cat"
    elif cat.genderalign in ["male", "trans male"]:
        color_name = f"{color_name} tom"
    else:
        color_name = f"{color_name} cat"

    # Here is the place where we can add some additional details about the cat, for the full non-short one. 
    # These include notable missing limbs, vitiligo, long-furred-ness, and 3 or more scars. 
    if not short:
        
        scar_details = {
            "NOTAIL": "no tail", 
            "HALFTAIL": "half a tail", 
            "NOPAW": "three legs", 
            "NOLEFTEAR": "a missing ear", 
            "NORIGHTEAR": "a missing ear",
            "NOEAR": "no ears"
        }

        additional_details = []
        if cat.vitiligo:
            additional_details.append("vitiligo")
        for scar in cat.scars:
            if scar in scar_details and scar_details[scar] not in additional_details:
                additional_details.append(scar_details[scar])
        
        if len(additional_details) > 1:
            color_name = f"{color_name} with {', '.join(additional_details[:-1])} and {additional_details[-1]}"
        elif additional_details:
            color_name = f"{color_name} with {additional_details[0]}"
    
    
        if len(cat.scars) >= 3:
            color_name = f"scarred {color_name}"
        if cat.pelt.length == "long":
            color_name = f"long-furred {color_name}"

    return color_name
    