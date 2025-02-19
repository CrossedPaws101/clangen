import random
from random import choice
from re import sub

from scripts.cat.sprites import sprites
from scripts.game_structure.game_essentials import game


class Pelt:
    sprites_names = {
        "SingleColour": 'single',
        'TwoColour': 'single',
        'Tabby': 'tabby',
        'Marbled': 'marbled',
        'Rosette': 'rosette',
        'Smoke': 'smoke',
        'Ticked': 'ticked',
        'Speckled': 'speckled',
        'Bengal': 'bengal',
        'Mackerel': 'mackerel',
        'Classic': 'classic',
        'Sokoke': 'sokoke',
        'Agouti': 'agouti',
        'Singlestripe': 'singlestripe',
        'Masked': 'masked',
        'Tortie': None,
        'Calico': None,
        'Abyssinian': 'abyssinian',
        'Clouded': 'clouded',
        'Doberman': 'doberman',
        'Merle': 'merle',
        'Snowflake': 'snowflake',
        'Lynx': 'lynx',
        'Wildcat': 'wildcat',
        'Wolf': 'wolf',
        'Smokepoint': 'smokepoint',
        'Brindle': 'brindle',
        'Finleap': 'finleap',
        'Spots': 'spots',
        'Braided': 'braided',
        'Brokenbraided': 'brokenbraided',
        'Brokenmackerel': 'brokenmackerel',
        'Charcoal': 'charcoal',
    }

    # ATTRIBUTES, including non-pelt related
    pelt_colours = [
        'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'BLACK', 'CREAM', 'PALEGINGER',
        'GOLDEN', 'GINGER', 'DARKGINGER', 'SIENNA', 'LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN',
        'CHOCOLATE',
        # era
        'PALE', 'CLOUD', 'BLUE', 'HAZE', 'DARKBLUE', 'SMOG',
        'TAN', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON',
        'COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET',
        # doe
        'ICE', 'SKY', 'SLATE', 'ASHBROWN', 'STORM', 'CLAY', 'UMBER',
        'SHELL', 'SALMON', 'BUTTERSCOTCH', 'TANGERINE', 'CHILI', 'TOFFEE',
        'FAWN', 'TAUPE', 'CAMEL', 'PEANUT', 'MOLE', 'WALNUT'
    ]
    
    default_colors = [
        'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'BLACK', 'CREAM', 'PALEGINGER',
        'GOLDEN', 'GINGER', 'DARKGINGER', 'SIENNA', 'LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN',
        'CHOCOLATE'
    ]
    era_colors = ['PALE', 'CLOUD', 'BLUE', 'HAZE', 'DARKBLUE', 'SMOG',
        'TAN', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON',
        'COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET']
    doe_colors = ['ICE', 'SKY', 'SLATE', 'ASHBROWN', 'STORM', 'CLAY', 'UMBER',
        'SHELL', 'SALMON', 'BUTTERSCOTCH', 'TANGERINE', 'CHILI', 'TOFFEE',
        'FAWN', 'TAUPE', 'CAMEL', 'PEANUT', 'MOLE', 'WALNUT']
    
    pelt_c_no_white = [
        'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'BLACK', 'CREAM', 'PALEGINGER',
        'GOLDEN', 'GINGER', 'DARKGINGER', 'SIENNA', 'LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN',
        'CHOCOLATE',
        # era
        'CLOUD', 'BLUE', 'HAZE', 'DARKBLUE', 'SMOG',
        'TAN', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON',
        'COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET',
        # doe
        'ICE', 'SKY', 'SLATE', 'ASHBROWN', 'STORM', 'CLAY', 'UMBER',
        'SHELL', 'SALMON', 'BUTTERSCOTCH', 'TANGERINE', 'CHILI', 'TOFFEE',
        'FAWN', 'TAUPE', 'CAMEL', 'PEANUT', 'MOLE', 'WALNUT'

    ]
    pelt_c_no_bw = [
        'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'CREAM', 'PALEGINGER',
        'GOLDEN', 'GINGER', 'DARKGINGER', 'SIENNA', 'LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN',
        'CHOCOLATE',
        # era
        'CLOUD', 'BLUE', 'HAZE', 'DARKBLUE',
        'TAN', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON',
        'COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET',
        # doe
        'ICE', 'SKY', 'SLATE', 'ASHBROWN', 'STORM', 'CLAY', 'UMBER',
        'SHELL', 'SALMON', 'BUTTERSCOTCH', 'TANGERINE', 'CHILI', 'TOFFEE',
        'FAWN', 'TAUPE', 'CAMEL', 'PEANUT', 'MOLE', 'WALNUT'
    ]

    tortiepatterns = ['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH', 'MINIMALONE', 'MINIMALTWO', 'MINIMALTHREE',
                      'MINIMALFOUR', 'HALF',
                      'OREO', 'SWOOP', 'MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 'STREAMSTRIKE', 'ORIOLE',
                      'CHIMERA', 'DAUB', 'EMBER', 'BLANKET',
                      'ROBIN', 'BRINDLE', 'PAIGE', 'ROSETAIL', 'SAFI', 'SMUDGED', 'DAPPLENIGHT', 'STREAK', 'MASK',
                      'CHEST', 'ARMTAIL', 'SMOKE', 'GRUMPYFACE',
                      'BRIE', 'BELOVED', 'BODY', 'SHILOH', 'FRECKLED', 'HEARTBEAT',
                      # white patches --> tortie masks
                    'FULLWHITE', 'ANY', 'TUXEDO', 'LITTLE', 'COLOURPOINT', 'VAN', 'ANYTWO', 'MOON', 'PHANTOM', 'POWDER',
                     'BLEACHED', 'SAVANNAH', 'FADESPOTS', 'PEBBLESHINE',
                    'EXTRA', 'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL', 'LIGHTSONG', 'VITILIGO', 'BLACKSTAR',
                     'PIEBALD', 'CURVED', 'PETAL', 'SHIBAINU', 'OWL',
                    'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTSTWO', 'GOATEE', 'VITILIGOTWO', 'PAWS', 'MITAINE',
                     'BROKENBLAZE', 'SCOURGE', 'DIVA', 'BEARD',
                    'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'VEE', 'UNDERS', 'HONEY', 'FAROFA', 'DAMIEN', 'MISTER', 'BELLY',
                     'TAILTIP', 'TOES', 'TOPCOVER',
                    'APRON', 'CAPSADDLE', 'MASKMANTLE', 'SQUEAKS', 'STAR', 'TOESTAIL', 'RAVENPAW', 'PANTS', 'REVERSEPANTS',
                     'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 'DAPPLEPAW',
                    'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT', 'MAO', 'LUNA', 'CHESTSPECK',
                     'WINGS', 'PAINTED', 'HEARTTWO', 'WOODPECKER',
                    'BOOTS', 'MISS', 'COW', 'COWTWO', 'BUB', 'BOWTIE', 'MUSTACHE', 'REVERSEHEART', 'SPARROW', 'VEST',
                     'LOVEBUG', 'TRIXIE', 'SAMMY', 'SPARKLE',
                    'RIGHTEAR', 'LEFTEAR', 'ESTRELLA', 'SHOOTINGSTAR', 'EYESPOT', 'REVERSEEYE', 'FADEBELLY', 'FRONT',
                     'BLOSSOMSTEP', 'PEBBLE', 'TAILTWO', 'BUDDY', 'BACKSPOT', 'EYEBAGS',
                    'BULLSEYE', 'FINN', 'DIGIT', 'KROPKA', 'FCTWO', 'FCONE', 'MIA', 'SCAR', 'BUSTER', 'SMOKEY', 'HAWKBLAZE',
                     'CAKE', 'ROSINA', 'PRINCESS',
                    'LOCKET', 'BLAZEMASK', 'TEARS', 'DOUGIE',
                      # new torties
                      'CLASSICMASK', 'SINGLESTRIPEMASK', 'AGOUTMASK', 'BENGALMASK', 'TABBYMASK', 'SOKOKEMASK', 
                      'SPECKLEDMASK', 'TICKEDMASK', 'SMOKEMASK', 'ROSETTEMASK', 'MARBLEDMASK', 'MACKERELMASK',
                      'BROKENONE', 'BROKENTWO', 'BROKENTHREE', 'BROKENFOUR', 'GLITCH', 'WAVE', 
                      'STRIPESMASK', 'KOI', 'SKULL', 'LITTLE', 'O', 'TOADSTOOL', 
                      'POINTMASK', 'SPOTSCHAOS', 'FOG', 'SUNSET', 'TAIL', 'MOOSTONE'
                  ]
    tortiebases = ['single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette', 'speckled', 'mackerel',
                   'classic', 'sokoke', 'agouti', 'singlestripe', 'masked', 'abyssinian', 'clouded', 'doberman',
                   'merle', 'snowflake', 'spots', 'lynx', 'smokepoint', 'wildcat', 'wolf', 'finleap', 'brindle',
                   'braided', 'brokenbraided', 'brokenmackerel', 'charcoal']

    pelt_length = ["short", "medium", "long"]
    eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'GREY', 'CYAN', 'EMERALD',
                   'PALEBLUE',
                   'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT', 'SUNLITICE', 'GREENYELLOW',
                   'BRONZE', 'SILVER',
                   # era eyes
                   'DARK HAZEL', 'GOLD ROSE', 'ROSE', 'REVERSE SUNLIT', 'ICY', 'SUNSET', 'LAVENDER', 'ECLIPSE', 'BLACK', 'MUDDY',
                   'TURQUOISE', 'VIOLET',
                   'RUST', 'PASTEL', 'AVOCADO', 'PASTEL LAVENDER', 'ALBINO', 'WINTER ROSE', 'PINK', 'MORNING', 'DARK BROWN',
                   # beetle eyes
                   'ROSY', 'ALGAE', 'SEAFOAM', 'LIGHT FLAME', 'CLOUDY', 'RED', 'SEA', 'SWAMP', 'RAINY', 'AQUAMARINE', 'EARTH', 'PUMPKIN',
                   'LILAC', 'PERIWINKLE', 'GALAXY', 'POND', 'DIRT', 'BROWN', 'CEDAR', 'CHRISTMAS', 'COTTON CANDY', 'VALENTINE', 'FIREWORK', 'LUCKY',
                   'DARK PINE', 'FALL', 'FOREST FIRE', 'GOLD MOON', 'HALLOWEEN', 'LOBELIA', 'MIDNIGHT', 'MOONSTONE', 'OXIDIZED', 'SNOW', 'BERRY BANANA', 'DAWN SKY',
                   'TWILIGHT SKY', 'WORMY', 'BLUE HAZEL', 'THUNDERBOLT', 'VOLCANO', 'SEASHELL', 'PARADOX', 'CURSE', 'BLESSING', 'LIME', 'PALE BROWN', 'CRIMSON',
                   'FOXGLOVE', 'OLIVE', 'EASTER',
                   ]
    yellow_eyes = ['YELLOW', 'AMBER', 'PALEYELLOW', 'GOLD', 'GREENYELLOW', 'REVERSE SUNLIT', 'MORNING', 'PUMPKIN', 'GOLD MOON',
                   'WORMY']
    blue_eyes = ['BLUE', 'DARKBLUE', 'CYAN', 'PALEBLUE', 'HEATHERBLUE', 'COBALT', 'SUNLITICE', 'GREY', 'ICY', 'TURQUOISE',
                 'WINTER ROSE', 'SEAFOAM', 'SEA', 'RAINY', 'POND', 'LOBELIA', 'MOONSTONE'] 
    green_eyes = ['PALEGREEN', 'GREEN', 'EMERALD', 'SAGE', 'HAZEL', 'DARK HAZEL', 'MUDDY', 'AVOCADO', 'ALGAE',
                  'AQUAMARINE', 'EARTH', 'LUCKY', 'FOREST FIRE', 'THUNDERBOLT', 'LIME']
    red_eyes = ['COPPER', 'ROSE', 'SUNSET', 'ECLIPSE', 'RUST', 'RED', 'CEDAR', 'CHRISTMAS', 'VALENTINE', 'FALL', 'OXIDIZED',
                'VOLCANO', 'BLESSING', 'CRIMSON']
    pink_eyes = ['GOLD ROSE', 'PASTEL', 'ALBINO', 'PINK', 'ROSY', 'LIGHT FLAME', 'COTTON CANDY', 'BERRY BANANA', 'SEASHELL']
    purple_eyes = ['LAVENDER', 'VIOLET', 'PASTEL LAVENDER', 'LILAC', 'PERIWINKLE', 'GALAXY', 'FIREWORK', 'HALLOWEEN', 'DAWN SKY',
                   'TWILIGHT SKY', 'PARADOX', 'CURSE']
    dull_eyes = ['BRONZE', 'BLACK', 'MUDDY', 'DARK BROWN', 'SWAMP', 'DIRT', 'BROWN', 'DARK PINE', 'MIDNIGHT', 'PALE BROWN']
    pale_eyes = ['SILVER', 'GREY', 'CLOUDY', 'SNOW', 'BLUE HAZEL']
    
    physical_trait_teeth = ['TEETHUPPER', 'TEETHSABRE', 'TEETHUNDERBITE']
    physical_trait_ear_type = ['EARSMALL', 'EARBIG', 'EARTALL', 'EARPANTHER']
    physical_trait_ear_fold = ['FOLDBOTH', 'FOLDONE']
    physical_trait_headfur = ['HEADFORELOCK', 'HEADCOWLICK', 'HEADMOHAWK', 'HEADTUFT', 'HEADEMO']
    physical_trait_cheekfur = ['CHEEKLONG', 'CHEEKPOINTED', 'CHEEKFLUFF', 'CHEEKCURL']
    physical_trait_mane = ['MANESILKY', 'MANEFLUFFY', 'MANERUFF', 'MANEHORSE']
    physical_trait_muzzle_type = ['MUZZLESHORT', 'MUZZLEBROAD', 'MUZZLELONG']
    physical_trait_tail = ['TAILCROOKED', 'TAILLONG', 'TAILFEATHER', 'TAILCURL', 'TAILTUFT']
    physical_trait_bodyfur = ['BACKFLUFF', 'BACKRIDGE', 'SHOULDERTUFT']
    physical_trait_misc = ['EARTUFTS', 'POLYDACTYL', 'LASHESUPPER', 'LASHESLOWER', 'WHISKERSLONG', 'CLAWSLONG', 'LEGTUFT']    
    

    # bite scars by @wood pank on discord

    # scars from other cats, other animals
    scars1 = ["ONE", "TWO", "THREE", "TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY",
              "LEGBITE", "NECKBITE", "FACE", "MANLEG", "BRIGHTHEART", "MANTAIL", "BRIDGE", "RIGHTBLIND", "LEFTBLIND",
              "BOTHBLIND", "BEAKCHEEK", "BEAKLOWER", "CATBITE", "RATBITE", "QUILLCHUNK", "QUILLSCRATCH", "HINDLEG",
              "BACK", "QUILLSIDE", "SCRATCHSIDE", "BEAKSIDE", "CATBITETWO", "FOUR"]

    # missing parts
    scars2 = ["LEFTEAR", "RIGHTEAR", "NOTAIL", "HALFTAIL", "NOPAW", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]

    # "special" scars that could only happen in a special event
    scars3 = ["SNAKE", "TOETRAP", "BURNPAWS", "BURNTAIL", "BURNBELLY", "BURNRUMP", "FROSTFACE", "FROSTTAIL",
              "FROSTMITT", "FROSTSOCK", "TOE", "SNAKETWO"]

    # make sure to add plural and singular forms of new accs to acc_display.json so that they will display nicely
    plant_accessories = ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL",
                         "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS", "DRY HERBS",
                         "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER",
                         # new clangen
                         "CATTAIL", "ORANGE POPPY", "CYAN POPPY", "WHITE POPPY", "PINK POPPY",
                         "LILY OF THE VALLEY", "SNAPDRAGON", "HEATHER", "GORSE", "JUNIPER", "RASPBERRY", 
                         "BULB WHITE", "BULB YELLOW", "BULB ORANGE", "BULB PINK", "BULB BLUE", "CLOVER", "DAISY",
                         "DRY CATMINT", "DRY NETTLES", "DRY LAURELS",
                         # new accessories
                         # eragona
                         "BARLEY", "SUNFLOWERS", "CORNFLOWER", "DRY THISTLE", "DRAGONFLY WINGS", "PINE WREATH",
                         "ROSE", "HANGING HERBS", "LILY", "HARE TAIL", "WILDFLOWERS WREATH", "SEAGLASS",
                         "PUMPKIN LEAVES", "DRY MOSS", "PINECONE", "THORN COLLAR", "AUTUMN CHAIN", "ROWAN BRANCH",
                         "COLORFUL LEAVES", "ACORN BRANCH", "DRY FIR", "DRY ROSE", "SPIDER'S WEB", "CROW FEATHERS",
                         "CHERRY BLOSSOM", "TULIP PETALS", "CLOVER FLOWER", "PANSIES", "BELLFLOWERS", "FORSYTHIA",
                         "MINT LEAF", "STICKS", "SPRING FEATHERS", "SNAIL SHELL", "CATKIN", "FERN",
                         "STRAW MANE", "MISTLETOE", "RED POINSETTIA", "WHITE POINSETTIA", "COTONEASTER WREATH", "YEW",
                         "OAK STICK ANTLERS", "BIRCH STICK ANTLERS", "DOGWOOD", "FROSTED IVY", "HEATHERTWO", "FANGS",
                         # superartsi
                         "IVY WRAP", "HERB WRAP", "PINK HEARTS", "RED HEARTS", "LILIES"
                         ]

    wild_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS",
                        # new clangen
                        "GULL FEATHERS", "SPARROW FEATHERS", "ROSY MOTH WINGS", "MORPHO BUTTERFLY", "MONARCH BUTTERFLY", "BLACK CICADA",
                        # superartsi
                        "MONARCH", "BUTTERFLY", "BROWN HIDE", "GRAY HIDE", "BROWN WRAP", "GRAY WRAP"]
    tail_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS",
                        # new clangen
                        "GULL FEATHERS", "SPARROW FEATHERS", "CLOVER", "DAISY",
                        # superartsi
                        "BROWN WRAP", "GRAY WRAP", "IVY WRAP", "HERB WRAP", "PINK HEARTS", "RED HEARTS",
                        # eragona
                        "DRY THISTLE", "HANGING HERBS", "LILY", "SEAGLASS", "DRY MOSS", "PINECONE",
                        "COLORFUL LEAVES", "SPIDER'S WEB", "CROW FEATHERS",
                        "CHERRY BLOSSOM", "CLOVER FLOWER", "FORSYTHIA",
                        "SPRING FEATHERS", "FERN", "MISTLETOE"
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
    ]

    tabbies = ["Tabby", "Ticked", "Mackerel", "Classic", "Sokoke", "Agouti", "Braided", "Brokenbraided", "Brokenmackerel"]
    spotted = ["Speckled", "Rosette", "Spots"]
    plain = ["SingleColour", "TwoColour", "Smoke", "Singlestripe", "Abyssinian", "Doberman", "Smokepoint"]
    exotic = ["Bengal", "Marbled", "Masked", "Clouded", "Merle", "Snowflake", "Brindle", "Wildcat", "Wolf", "Lynx", "Finleap", "Charcoal"]
    torties = ["Tortie", "Calico"]
    pelt_categories = [tabbies, spotted, plain, exotic, torties]
    new_pelts = ["Abyssinian", "Clouded", "Merle", "Doberman", "Snowflake", "Lynx",
                 "Wildcat", "Wolf", "Smokepoint", "Brindle", "Finleap", "Spots",
                 "Braided", "Brokenbraided", "Brokenmackerel", "Charcoal"]

    # SPRITE NAMES
    single_colours = [
        'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'BLACK', 'CREAM', 'PALEGINGER',
        'GOLDEN', 'GINGER', 'DARKGINGER', 'SIENNA', 'LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN',
        'CHOCOLATE',
        # era
        'PALE', 'CLOUD', 'BLUE', 'HAZE', 'DARKBLUE', 'SMOG',
        'TAN', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON',
        'COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET',
        # doe
        'ICE', 'SKY', 'SLATE', 'ASHBROWN', 'STORM', 'CLAY', 'UMBER',
        'SHELL', 'SALMON', 'BUTTERSCOTCH', 'TANGERINE', 'CHILI', 'TOFFEE',
        'FAWN', 'TAUPE', 'CAMEL', 'PEANUT', 'MOLE', 'WALNUT'
    ]
    ginger_colours = ['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'SIENNA', 'SUNBURST', 'TANGERINE', 'CHILI', 'TOFFEE']
    black_colours = ['GREY', 'DARKGREY', 'GHOST', 'BLACK', 'DARKBLUE', 'SMOG', 'SLATE']
    white_colours = ['WHITE', 'PALEGREY', 'SILVER', 'PALE', 'CLOUD', 'BLUE', 'HAZE', 'ICE', 'SKY', 'STORM']
    brown_colours = ['LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN', 'CHOCOLATE',
                     'COFFEE', 'MARSH', 'ASHBROWN', 'CLAY', 'TAUPE', 'UMBER', 'CAMEL', 'PEANUT',
                     'MOLE', 'WALNUT']
    cream_colours = ['CREAM', 'TAN', 'SAND', 'BONE', 'LEMON', 'SHELL', 'BUTTERSCOTCH', 'FAWN']
    red_colours = ['SIENNA', 'RUSSET', 'OAK', 'RUBY', 'PEACH', 'SCARLET', 'SALMON']
    colour_categories = [ginger_colours, black_colours, white_colours, brown_colours, cream_colours, red_colours]
    eye_sprites = [
        'YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'BLUEYELLOW', 'BLUEGREEN',
        'GREY', 'CYAN', 'EMERALD', 'PALEBLUE', 'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT',
        'SUNLITICE', 'GREENYELLOW', 'BRONZE', 'SILVER',
        # era eyes
        'DARK HAZEL', 'GOLD ROSE', 'ROSE', 'REVERSE SUNLIT', 'ICY', 'SUNSET', 'LAVENDER', 'ECLIPSE', 'BLACK', 'MUDDY',
        'TURQUOISE', 'VIOLET',
        'RUST', 'PASTEL', 'AVOCADO', 'PASTEL LAVENDER', 'ALBINO', 'WINTER ROSE', 'PINK', 'MORNING', 'DARK BROWN',
        # beetle eyes
        'ROSY', 'ALGAE', 'SEAFOAM', 'LIGHT FLAME', 'CLOUDY', 'RED', 'SEA', 'SWAMP', 'RAINY', 'AQUAMARINE', 'EARTH', 'PUMPKIN', 'LILAC',
        'PERIWINKLE', 'GALAXY', 'POND', 'DIRT', 'BROWN', 'CEDAR', 'CHRISTMAS', 'COTTON CANDY', 'DARK PINE', 'FALL', 'FOREST FIRE',
        'GOLD MOON', 'HALLOWEEN', 'LOBELIA', 'MIDNIGHT', 'MOONSTONE', 'OXIDIZED', 'SNOW', 'BERRY BANANA', 'DAWN SKY', 'TWILIGHT SKY',
        'WORMY', 'BLUE HAZEL', 'THUNDERBOLT', 'VOLCANO', 'SEASHELL', 'PARADOX', 'CURSE', 'BLESSING', 'FOXGLOVE', 'OLIVE', 'EASTER',
        'VALENTINE', 'FIREWORK', 'LUCKY', 'LIME', 'PALE BROWN', 'CRIMSON'
    ]
    little_white = ['LITTLE', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 'BIB', 'VEE', 'PAWS',
                    'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO', 'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
                    'LUNA',
                    'EXTRA', 'MUSTACHE', 'REVERSEHEART', 'SPARKLE', 'RIGHTEAR', 'LEFTEAR', 'ESTRELLA', 'REVERSEEYE',
                    'BACKSPOT',
                    'EYEBAGS', 'LOCKET', 'BLAZEMASK', 'TEARS']
    mid_white = ['TUXEDO', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK', 'MITAINE', 'SQUEAKS', 'STAR', 'WINGS',
                 'DIVA', 'SAVANNAH', 'FADESPOTS', 'BEARD', 'DAPPLEPAW', 'TOPCOVER', 'WOODPECKER', 'MISS', 'BOWTIE',
                 'VEST',
                 'FADEBELLY', 'DIGIT', 'FCTWO', 'FCONE', 'MIA', 'ROSINA', 'PRINCESS', 'DOUGIE']
    high_white = ['ANY', 'ANYTWO', 'BROKEN', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTSTWO',
                  'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
                  'CURVED', 'GLASS', 'MASKMANTLE', 'MAO', 'PAINTED', 'SHIBAINU', 'OWL', 'BUB', 'SPARROW', 'TRIXIE',
                  'SAMMY', 'FRONT', 'BLOSSOMSTEP', 'BULLSEYE', 'FINN', 'SCAR', 'BUSTER', 'HAWKBLAZE', 'CAKE']
    mostly_white = ['VAN', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE',
                    'CHESTSPECK', 'BLACKSTAR', 'PETAL', 'HEARTTWO', 'PEBBLESHINE', 'BOOTS', 'COW', 'COWTWO', 'LOVEBUG',
                    'SHOOTINGSTAR', 'EYESPOT', 'PEBBLE', 'TAILTWO', 'BUDDY', 'KROPKA']
    point_markings = ['COLOURPOINT', 'RAGDOLL', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT']
    vit = ['VITILIGO', 'VITILIGOTWO', 'MOON', 'PHANTOM', 'KARPATI', 'POWDER', 'BLEACHED', 'SMOKEY']
    white_sprites = [
        little_white, mid_white, high_white, mostly_white, point_markings, vit, 'FULLWHITE']

    skin_sprites = ['BLACK', 'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN', 'DARK', 'DARKGREY', 'GREY', 'DARKSALMON',
                    'SALMON', 'PEACH', 'DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE', 'RED']

    """Holds all appearance information for a cat. """

    def __init__(self,
                 name: str = "SingleColour",
                 length: str = "short",
                 colour: str = "WHITE",
                 white_patches: list = None,
                 eye_color: str = "BLUE",
                 eye_colour2: str = None,
                 tortiebase: str = None,
                 tortiecolour: str = None,
                 pattern: list = None,
                 tortiepattern: str = None,
                 vitiligo: str = None,
                 points: str = None,
                 accessory: str = None,
                 paralyzed: bool = False,
                 opacity: int = 100,
                 scars: list = None,
                 tint: str = "none",
                 skin: str = "BLACK",
                 white_patches_tint: str = "none",
                 kitten_sprite: int = None,
                 adol_sprite: int = None,
                 adult_sprite: int = None,
                 senior_sprite: int = None,
                 para_adult_sprite: int = None,
                 reverse: bool = False,
                 fur_texture: str = None,
                 build: str = None,
                 height: str = None,
                 physical_trait_1: str = None,
                 physical_trait_2: str = None,
                 physical_trait_3: str = None,
                 physical_trait_4: str = None,
                 physical_trait_hidden: str = None,
                 physical_trait_hidden_2: str = None,
                 physical_trait_hidden_3: str = None,
                 physical_trait_hidden_4: str = None
                 ) -> None:
        self.name = name
        self.colour = colour
        self.white_patches = white_patches
        self.eye_colour = eye_color
        self.eye_colour2 = eye_colour2
        self.tortiebase = tortiebase
        self.pattern = pattern
        self.tortiepattern = tortiepattern
        self.tortiecolour = tortiecolour
        self.vitiligo = vitiligo
        self.length = length
        self.points = points
        self.accessory = accessory
        self.paralyzed = paralyzed
        self.opacity = opacity
        self.scars = scars if isinstance(scars, list) else []
        self.tint = tint
        self.white_patches_tint = white_patches_tint
        self.cat_sprites = {"kitten": kitten_sprite if kitten_sprite is not None else 0,
                            "adolescent": adol_sprite if adol_sprite is not None else 0,
                            "young adult": adult_sprite if adult_sprite is not None else 0,
                            "adult": adult_sprite if adult_sprite is not None else 0,
                            "senior adult": adult_sprite if adult_sprite is not None else 0,
                            "senior": senior_sprite if senior_sprite is not None else 0,
                            "para_adult": para_adult_sprite if para_adult_sprite is not None else 0,
                            'newborn': 20,
                            'para_young': 17,
                            "sick_adult": 18,
                            "sick_young": 19}

        self.reverse = reverse
        self.skin = skin
        
        self.fur_texture = fur_texture if fur_texture is not None else choice(["soft", "curly", "rough", "silky", "sleek", "wavy", "sparse", "tangled", "fuzzy", "spiky"])
        self.build = build if build is not None else choice(["stocky", "slender", "lithe", "wiry", "muscular", "lanky", "delicate"])
        self.height = height if height is not None else choice(["petite", "short", "average", "average", "tall", "towering"])
        
        self.physical_trait_1 = physical_trait_1
        self.physical_trait_2 = physical_trait_2
        self.physical_trait_3 = physical_trait_3
        self.physical_trait_4 = physical_trait_4
        self.physical_trait_hidden = physical_trait_hidden
        self.physical_trait_hidden_2 = physical_trait_hidden_2
        self.physical_trait_hidden_3 = physical_trait_hidden_3
        self.physical_trait_hidden_4 = physical_trait_hidden_4

    @staticmethod
    def generate_new_pelt(gender: str, parents: tuple = (), age: str = "adult"):
        new_pelt = Pelt()

        pelt_white = new_pelt.init_pattern_color(parents, gender)
        new_pelt.init_white_patches(pelt_white, parents)
        new_pelt.init_sprite()
        new_pelt.init_scars(age)
        new_pelt.init_accessories(age)
        new_pelt.init_eyes(parents)
        new_pelt.init_pattern()
        new_pelt.init_tint()
        new_pelt.init_physical_traits(parents)

        return new_pelt

    def check_and_convert(self, convert_dict):
        """Checks for old-type properties for the appearance-related properties
        that are stored in Pelt, and converts them. To be run when loading a cat in. """
        
        # First, convert from some old names that may be in white_patches. 
        if self.white_patches == 'POINTMARK':
            self.white_patches = "SEALPOINT"
        elif self.white_patches == 'PANTS2':
            self.white_patches = 'PANTSTWO'
        elif self.white_patches == 'ANY2':
            self.white_patches = 'ANYTWO'
        elif self.white_patches == "VITILIGO2":
            self.white_patches = "VITILIGOTWO"
            
        if self.vitiligo == "VITILIGO2":
            self.vitiligo = "VITILIGOTWO"

        # Move white_patches that should be in vit or points. 
        if self.white_patches in Pelt.vit:
            self.vitiligo = self.white_patches
            self.white_patches = None
        elif self.white_patches in Pelt.point_markings:
            self.points = self.white_patches
            self.white_patches = None

        if self.tortiepattern and "tortie" in self.tortiepattern:
            self.tortiepattern = sub("tortie", "", self.tortiepattern.lower())
            if self.tortiepattern == "solid":
                self.tortiepattern = "single"

        '''if self.white_patches in convert_dict["old_creamy_patches"]:
            self.white_patches = convert_dict["old_creamy_patches"][self.white_patches]
            self.white_patches_tint = "darkcream"
        elif self.white_patches in ['SEPIAPOINT', 'MINKPOINT', 'SEALPOINT']:
            self.white_patches_tint = "none" '''

        # Eye Color Convert Stuff
        if self.eye_colour == "BLUE2":
            self.eye_colour = "COBALT"
        if self.eye_colour2 == "BLUE2":
            self.eye_colour2 = "COBALT"

        if self.eye_colour in ["BLUEYELLOW", "BLUEGREEN"]:
            if self.eye_colour == "BLUEYELLOW":
                self.eye_colour2 = "YELLOW"
            elif self.eye_colour == "BLUEGREEN":
                self.eye_colour2 = "GREEN"
            self.eye_colour = "BLUE"

        if self.length == 'long':
            if self.cat_sprites['adult'] not in [9, 10, 11]:
                if self.cat_sprites['adult'] == 0:
                    self.cat_sprites['adult'] = 9
                elif self.cat_sprites['adult'] == 1:
                    self.cat_sprites['adult'] = 10
                elif self.cat_sprites['adult'] == 2:
                    self.cat_sprites['adult'] = 11
                self.cat_sprites['young adult'] = self.cat_sprites['adult']
                self.cat_sprites['senior adult'] = self.cat_sprites['adult']
                self.cat_sprites['para_adult'] = 16
        else:
            self.cat_sprites['para_adult'] = 15
        if self.cat_sprites['senior'] not in [12, 13, 14]:
            if self.cat_sprites['senior'] == 3:
                self.cat_sprites['senior'] = 12
            elif self.cat_sprites['senior'] == 4:
                self.cat_sprites['senior'] = 13
            elif self.cat_sprites['senior'] == 5:
                self.cat_sprites['senior'] = 14
            
        if self.pattern == "MINIMAL1":
            self.pattern = "MINIMALONE"
        elif self.pattern == "MINIMAL2":
            self.pattern = "MINIMALTWO"
        elif self.pattern == "MINIMAL3":
            self.pattern = "MINIMALTHREE"
        elif self.pattern == "MINIMAL4":
            self.pattern = "MINIMALFOUR"
        
    def init_eyes(self, parents):
        if not parents:
            self.eye_colour = choice(Pelt.eye_colours)
        else:
            self.eye_colour = choice([i.pelt.eye_colour for i in parents] + [choice(Pelt.eye_colours)])

        # White patches must be initalized before eye color.
        num = game.config["cat_generation"]["base_heterochromia"]
        if self.white_patches:
            if any(white in [Pelt.high_white, Pelt.mostly_white, 'FULLWHITE'] for white in self.white_patches) or self.colour == 'WHITE':
                num = num - 90
            if any(white in 'FULLWHITE' for white in self.white_patches) or self.colour == 'WHITE':
                num -= 10
        if num < 0:
            num = 1

        if not random.randint(0, num):
            colour_wheel = [Pelt.yellow_eyes, Pelt.blue_eyes, Pelt.green_eyes, Pelt.red_eyes, Pelt.pink_eyes, Pelt.purple_eyes, Pelt.dull_eyes, Pelt.pale_eyes]
            for colour in colour_wheel[:]:
                if self.eye_colour in colour:
                    colour_wheel.remove(colour) # removes the selected list from the options
                    self.eye_colour2 = choice(choice(colour_wheel)) # choose from the remaining two lists
                    break

    def pattern_color_inheritance(self, parents: tuple = (), gender="female"):
        # setting parent pelt categories
        # We are using a set, since we don't need this to be ordered, and sets deal with removing duplicates.
        par_peltlength = set()
        par_peltcolours = set()
        par_peltnames = set()
        par_pelts = []
        par_white = []
        for p in parents:
            if p:
                # Gather pelt color.
                par_peltcolours.add(p.pelt.colour)

                # Gather pelt length
                par_peltlength.add(p.pelt.length)

                # Gather pelt name
                if p.pelt.name in Pelt.torties:
                    par_peltnames.add(p.pelt.tortiebase.capitalize())
                else:
                    par_peltnames.add(p.pelt.name)

                # Gather exact pelts, for direct inheritance.
                par_pelts.append(p.pelt)

                # Gather if they have white in their pelt.
                par_white.append(p.pelt.white)
            else:
                # If order for white patches to work correctly, we also want to randomly generate a "pelt_white"
                # for each "None" parent (missing or unknown parent)
                par_white.append(bool(random.getrandbits(1)))

                # Append None
                # Gather pelt color.
                par_peltcolours.add(None)
                par_peltlength.add(None)
                par_peltnames.add(None)

        # If this list is empty, something went wrong.
        if not par_peltcolours:
            print("Warning - no parents: pelt randomized")
            return self.randomize_pattern_color(gender)

        # There is a 1/10 chance for kits to have the exact same pelt as one of their parents
        if not random.randint(0, game.config["cat_generation"]["direct_inheritance"]):  # 1/10 chance
            selected = choice(par_pelts)
            self.name = selected.name
            self.length = selected.length
            self.colour = selected.colour
            self.tortiebase = selected.tortiebase
            return selected.white
        
        if self.name in Pelt.new_pelts and self.name not in ["Braided", "Brokenbraided", "Brokenmackerel", "Charcoal"]:
            self.colour = random.choice(Pelt.default_colors)
        else:
            self.colour = random.choice(Pelt.doe_colors)
        
        while self.tortiebase in ['abyssinian', 'clouded', 'doberman', 'merle', 'snowflake',
                                  'spots', 'lynx', 'smokepoint', 'wildcat', 'wolf', 'finleap', 'brindle'] and self.color not in Pelt.default_colors:
            self.tortiebase = random.choice(Pelt.tortiebases)
        
        while self.tortiebase in ['braided', 'brokenbraided', 'brokenmackerel', 'charcoal'] and self.color not in Pelt.doe_colors:
            self.tortiebase = random.choice(Pelt.tortiebases)

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT
        # ------------------------------------------------------------------------------------------------------------#

        # Determine pelt.
        weights = [0, 0, 0, 0]  # Weights for each pelt group. It goes: (tabbies, spotted, plain, exotic)
        for p_ in par_peltnames:
            if p_ in Pelt.tabbies:
                add_weight = (50, 10, 5, 7)
            elif p_ in Pelt.spotted:
                add_weight = (10, 50, 5, 5)
            elif p_ in Pelt.plain:
                add_weight = (5, 5, 50, 0)
            elif p_ in Pelt.exotic:
                add_weight = (15, 15, 1, 45)
            elif p_ is None:  # If there is at least one unknown parent, a None will be added to the set.
                add_weight = (35, 20, 30, 15)
            else:
                add_weight = (0, 0, 0, 0)

            for x in range(0, len(weights)):
                weights[x] += add_weight[x]

        # A quick check to make sure all the weights aren't 0
        if all([x == 0 for x in weights]):
            weights = [1, 1, 1, 1]

        # Now, choose the pelt category and pelt. The extra 0 is for the tortie pelts,
        chosen_pelt = choice(
            random.choices(Pelt.pelt_categories, weights=weights + [0], k=1)[0]
        )

        # Tortie chance
        tortie_chance_f = game.config["cat_generation"][
            "base_female_tortie"]  # There is a default chance for female tortie
        tortie_chance_m = game.config["cat_generation"]["base_male_tortie"]
        for p_ in par_pelts:
            if p_.name in Pelt.torties:
                tortie_chance_f = int(tortie_chance_f / 2)
                tortie_chance_m = tortie_chance_m - 1
                break

        # Determine tortie:
        if gender == "female":
            torbie = random.getrandbits(tortie_chance_f) == 1
        else:
            torbie = random.getrandbits(tortie_chance_m) == 1

        chosen_tortie_base = None
        if torbie:
            # If it is tortie, the chosen pelt above becomes the base pelt.
            chosen_tortie_base = chosen_pelt
            if chosen_tortie_base in ["TwoColour", "SingleColour"]:
                chosen_tortie_base = "Single"
            chosen_tortie_base = chosen_tortie_base.lower()
            chosen_pelt = random.choice(Pelt.torties)

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT COLOUR
        # ------------------------------------------------------------------------------------------------------------#
        # Weights for each colour group. It goes: (ginger_colours, black_colours, white_colours, brown_colours)
        weights = [0, 0, 0, 0, 0, 0]
        for p_ in par_peltcolours:
            if p_ in Pelt.ginger_colours:
                add_weight = (40, 0, 0, 2, 5, 5)
            elif p_ in Pelt.black_colours:
                add_weight = (0, 40, 2, 5, 0, 2)
            elif p_ in Pelt.white_colours:
                add_weight = (0, 5, 40, 0, 0, 0)
            elif p_ in Pelt.brown_colours:
                add_weight = (5, 5, 0, 35, 0, 5)
            elif p_ in Pelt.cream_colours:
                add_weight = (5, 0, 2, 2, 35, 2)
            elif p_ in Pelt.red_colours:
                add_weight = (10, 0, 0, 2, 2, 35)
            elif p_ is None:
                add_weight = (40, 40, 40, 40, 40, 40)
            else:
                add_weight = (0, 0, 0, 0, 0, 0)

            for x in range(0, len(weights)):
                weights[x] += add_weight[x]

            # A quick check to make sure all the weights aren't 0
            if all([x == 0 for x in weights]):
                weights = [1, 1, 1, 1, 1, 1]
        
        if chosen_pelt == "Masked":
            chosen_pelt_color = choice([
                random.choice(Pelt.default_colors),
                random.choice(Pelt.era_colors)
            ])
        elif chosen_pelt in ["Abyssinian", "Clouded", "Doberman", "Merle", "Snowflake",
                             "Finleap", "Wolf", "Smokepoint", "Lynx", "Brindle", "Wildcat", "Spots"]:
            chosen_pelt_color = random.choice(Pelt.default_colors)
        elif chosen_pelt in ["Braided", "Brokenbraided", "Brokenmackerel", "Charcoal"]:
            chosen_pelt_color = random.choice(Pelt.doe_colors)
        else:
            chosen_pelt_color = choice(
                random.choices(Pelt.colour_categories, weights=weights, k=1)[0]
            )

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT LENGTH
        # ------------------------------------------------------------------------------------------------------------#

        weights = [0, 0, 0]  # Weights for each length. It goes (short, medium, long)
        for p_ in par_peltlength:
            if p_ == "short":
                add_weight = (50, 10, 2)
            elif p_ == "medium":
                add_weight = (25, 50, 25)
            elif p_ == "long":
                add_weight = (2, 10, 50)
            elif p_ is None:
                add_weight = (10, 10, 10)
            else:
                add_weight = (0, 0, 0)

            for x in range(0, len(weights)):
                weights[x] += add_weight[x]

        # A quick check to make sure all the weights aren't 0
        if all([x == 0 for x in weights]):
            weights = [1, 1, 1]

        chosen_pelt_length = random.choices(Pelt.pelt_length, weights=weights, k=1)[0]

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT WHITE
        # ------------------------------------------------------------------------------------------------------------#

        # There are 94 percentage points that can be added by
        # parents having white. If we have more than two, this
        # will keep that the same.
        percentage_add_per_parent = int(94 / len(par_white))
        chance = 3
        for p_ in par_white:
            if p_:
                chance += percentage_add_per_parent

        chosen_white = random.randint(1, 100) <= chance

        # Adjustments to pelt chosen based on if the pelt has white in it or not.
        if chosen_pelt in ["TwoColour", "SingleColour"]:
            if chosen_white:
                chosen_pelt = "TwoColour"
            else:
                chosen_pelt = "SingleColour"
        elif chosen_pelt == "Calico":
            if not chosen_white:
                chosen_pelt = "Tortie"

        # SET THE PELT
        self.name = chosen_pelt
        self.colour = chosen_pelt_color
        self.length = chosen_pelt_length
        self.tortiebase = chosen_tortie_base  # This will be none if the cat isn't a tortie.
        return chosen_white

    def randomize_pattern_color(self, gender):
        # ------------------------------------------------------------------------------------------------------------#
        #   PELT
        # ------------------------------------------------------------------------------------------------------------#

        # Determine pelt.
        chosen_pelt = choice(
            random.choices(Pelt.pelt_categories, weights=(35, 20, 30, 15, 0), k=1)[0]
        )

        # Tortie chance
        # There is a default chance for female tortie, slightly increased for completely random generation.
        tortie_chance_f = game.config["cat_generation"]["base_female_tortie"] - 1
        tortie_chance_m = game.config["cat_generation"]["base_male_tortie"]
        if gender == "female":
            torbie = random.getrandbits(tortie_chance_f) == 1
        else:
            torbie = random.getrandbits(tortie_chance_m) == 1

        chosen_tortie_base = None
        if torbie:
            # If it is tortie, the chosen pelt above becomes the base pelt.
            chosen_tortie_base = chosen_pelt
            if chosen_tortie_base in ["TwoColour", "SingleColour"]:
                chosen_tortie_base = "Single"
            chosen_tortie_base = chosen_tortie_base.lower()
            chosen_pelt = random.choice(Pelt.torties)

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT COLOUR
        # ------------------------------------------------------------------------------------------------------------#

        if chosen_pelt == "Masked":
            chosen_pelt_color = choice([
                random.choice(Pelt.default_colors),
                random.choice(Pelt.era_colors)
            ])
        elif chosen_pelt in ["Abyssinian", "Clouded", "Doberman", "Merle", "Snowflake",
                             "Finleap", "Wolf", "Smokepoint", "Lynx", "Brindle", "Wildcat", "Spots"]:
            chosen_pelt_color = random.choice(Pelt.default_colors)
        elif chosen_pelt in ["Braided", "Brokenbraided", "Brokenmackerel", "Charcoal"]:
            chosen_pelt_color = random.choice(Pelt.doe_colors)
        else:
            chosen_pelt_color = choice(
                random.choices(Pelt.colour_categories, k=1)[0]
            )

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT LENGTH
        # ------------------------------------------------------------------------------------------------------------#

        chosen_pelt_length = random.choice(Pelt.pelt_length)

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT WHITE
        # ------------------------------------------------------------------------------------------------------------#

        chosen_white = random.randint(1, 100) <= 40

        # Adjustments to pelt chosen based on if the pelt has white in it or not.
        if chosen_pelt in ["TwoColour", "SingleColour"]:
            if chosen_white:
                chosen_pelt = "TwoColour"
            else:
                chosen_pelt = "SingleColour"
        elif chosen_pelt == "Calico":
            if not chosen_white:
                chosen_pelt = "Tortie"

        self.name = chosen_pelt
        self.colour = chosen_pelt_color
        self.length = chosen_pelt_length
        self.tortiebase = chosen_tortie_base  # This will be none if the cat isn't a tortie.
        return chosen_white

    def init_pattern_color(self, parents, gender) -> bool:
        """Inits self.name, self.colour, self.length, 
            self.tortiebase and determines if the cat 
            will have white patche or not. 
            Return TRUE is the cat should have white patches, 
            false is not. """

        if parents:
            # If the cat has parents, use inheritance to decide pelt.
            chosen_white = self.pattern_color_inheritance(parents, gender)
        else:
            chosen_white = self.randomize_pattern_color(gender)

        return chosen_white

    def init_sprite(self):
        self.cat_sprites = {
            'newborn': 20,
            'kitten': random.randint(0, 2),
            'adolescent': random.randint(3, 5),
            'senior': random.randint(12, 14),
            'sick_young': 19,
            'sick_adult': 18
        }
        self.reverse = bool(random.getrandbits(1))
        # skin chances
        self.skin = choice(Pelt.skin_sprites)

        if self.length != 'long':
            self.cat_sprites['adult'] = random.randint(6, 8)
            self.cat_sprites['para_adult'] = 16
        else:
            self.cat_sprites['adult'] = random.randint(9, 11)
            self.cat_sprites['para_adult'] = 15
        self.cat_sprites['young adult'] = self.cat_sprites['adult']
        self.cat_sprites['senior adult'] = self.cat_sprites['adult']

    def init_scars(self, age):
        if age == "newborn":
            return

        if age in ['kitten', 'adolescent']:
            scar_choice = random.randint(0, 50)  # 2%
        elif age in ['young adult', 'adult']:
            scar_choice = random.randint(0, 20)  # 5%
        else:
            scar_choice = random.randint(0, 15)  # 6.67%

        if scar_choice == 1:
            self.scars.append(choice([
                choice(Pelt.scars1),
                choice(Pelt.scars3)
            ]))

        if 'NOTAIL' in self.scars and 'HALFTAIL' in self.scars:
            self.scars.remove('HALFTAIL')

    def init_accessories(self, age):
        if age == "newborn":
            self.accessory = None
            return

        acc_display_choice = random.randint(0, 80)
        if age in ['kitten', 'adolescent']:
            acc_display_choice = random.randint(0, 180)
        elif age in ['young adult', 'adult']:
            acc_display_choice = random.randint(0, 100)

        if acc_display_choice == 1:
            self.accessory = choice([
                choice(Pelt.plant_accessories),
                choice(Pelt.wild_accessories)
            ])
        else:
            self.accessory = None

    def init_pattern(self):
        if self.name in Pelt.torties:
            if not self.tortiebase:
                self.tortiebase = choice(Pelt.tortiebases)
            if not self.pattern:
                chosen_pattern = set()
                chosen_pattern.add(choice(Pelt.tortiepatterns))
                num = game.config["cat_generation"]["base_extra_tortie"]
                for x in range(game.config["cat_generation"]["max_tortie_amount"] - 1):
                    if not random.randint(0, num):
                        chosen_pattern.add(choice(Pelt.tortiepatterns))
                        num += 3
                if len(chosen_pattern) >= 2:
                    print("DoublePatches: "+str(len(chosen_pattern))+" tortie patches!")
                self.pattern = list(chosen_pattern)

            wildcard_chance = game.config["cat_generation"]["wildcard_tortie"]
            if self.colour:
                # The "not wildcard_chance" allows users to set wildcard_tortie to 0
                # and always get wildcard torties.
                if not wildcard_chance or random.getrandbits(wildcard_chance) == 1:
                    # This is the "wildcard" chance, where you can get funky combinations.
                    # people are fans of the print message, so I'm putting it back
                    print("Wildcard tortie!")

                    # Allow any pattern:
                    self.tortiepattern = choice(Pelt.tortiebases)

                    # Allow any colors that aren't the base color.
                    if self.tortiepattern == 'masked':
                        possible_colors = Pelt.default_colors.copy()
                        possible_colors.extend(Pelt.era_colors)
                        possible_colors.remove(self.colour)
                        self.tortiecolour = choice(possible_colors)
                    elif self.tortiepattern in ['abyssinian', 'clouded', 'doberman', 'merle', 'snowflake',
                                                'spots', 'lynx', 'smokepoint', 'wildcat', 'wolf', 'finleap', 'brindle']:
                        possible_colors = Pelt.default_colors.copy()
                        possible_colors.remove(self.colour)
                        self.tortiecolour = choice(possible_colors)
                    elif self.tortiepattern in ['braided', 'brokenbraided', 'brokenmackerel', 'charcoal']:
                        possible_colors = Pelt.doe_colors.copy()
                        possible_colors.remove(self.colour)
                        self.tortiecolour = choice(possible_colors)
                    else:
                        possible_colors = Pelt.pelt_colours.copy()
                        possible_colors.remove(self.colour)
                        self.tortiecolour = choice(possible_colors)

                else:
                    # Normal generation
                    if self.tortiebase in ["singlestripe", "smoke", "single"]:
                        self.tortiepattern = choice(['tabby', 'mackerel', 'classic', 'single', 'smoke', 'agouti',
                                                     'ticked', 'abyssinian', 'clouded', 'doberman', 'merle', 'snowflake',
                                                     'spots', 'lynx', 'smokepoint', 'wildcat', 'wolf', 'finleap', 'brindle',
                                                     'braided', 'brokenbraided', 'brokenmackerel', 'charcoal'])
                    else:
                        self.tortiepattern = random.choices([self.tortiebase, 'single'], weights=[97, 3], k=1)[0]

                    if self.tortiepattern in ['abyssinian', 'clouded', 'doberman', 'merle', 'snowflake', 'spots', 'lynx', 'smokepoint', 'wildcat', 'wolf', 'finleap', 'brindle']:
                        possible_colors = Pelt.default_colors.copy()
                        self.colour = choice(possible_colors)
                    
                    if self.tortiepattern in ['braided', 'brokenbraided', 'brokenmackerel', 'charcoal']:
                        possible_colors = Pelt.doe_colors.copy()
                        self.colour = choice(possible_colors)
                        
                    if self.colour == "WHITE" or "PALE" or "ICE":
                        possible_colors = Pelt.white_colours.copy()
                        possible_colors.remove("WHITE")
                        possible_colors.remove("PALE")
                        possible_colors.remove("ICE")
                        if self.tortiepattern == 'masked':
                            possible_colors.remove("SKY")
                            possible_colors.remove("STORM")
                        if self.tortiepattern in ['braided', 'brokenbraided', 'brokenmackerel', 'charcoal']:
                            possible_colors.remove("PALEGREY")
                            possible_colors.remove("SILVER")
                            possible_colors.remove("CLOUD")
                            possible_colors.remove("BLUE")
                            possible_colors.remove("HAZE")
                        if self.tortiepattern in ['abyssinian', 'clouded', 'doberman', 'merle', 'snowflake', 'spots', 'lynx', 'smokepoint', 'wildcat', 'wolf', 'finleap', 'brindle']:
                            possible_colors.remove("CLOUD")
                            possible_colors.remove("BLUE")
                            possible_colors.remove("HAZE")
                            possible_colors.remove("SKY")
                            possible_colors.remove("STORM")
                        self.colour = choice(possible_colors)

                    # Ginger is often duplicated to increase its chances
                    if (self.colour in Pelt.black_colours) or (self.colour in Pelt.white_colours):
                        self.tortiecolour = choice((Pelt.ginger_colours * 2) + Pelt.red_colours + Pelt.cream_colours + Pelt.brown_colours)
                    elif self.colour in Pelt.ginger_colours:
                        self.tortiecolour = choice(Pelt.brown_colours + Pelt.black_colours * 2)
                    elif self.colour in Pelt.brown_colours:
                        possible_colors = Pelt.brown_colours.copy()
                        possible_colors.remove(self.colour)
                        possible_colors.extend(Pelt.black_colours + (Pelt.ginger_colours * 2) + (Pelt.cream_colours * 2) + Pelt.red_colours)
                        self.tortiecolour = choice(possible_colors)
                    else:
                        self.tortiecolour = "GOLDEN"
                    
                    if self.tortiepattern in ['abyssinian', 'clouded', 'doberman', 'merle', 'snowflake',
                                              'spots', 'lynx', 'smokepoint', 'wildcat', 'wolf', 'finleap', 'brindle']:
                        possible_colors = Pelt.default_colors.copy()
                        if self.colour in possible_colors:
                            possible_colors.remove(self.colour)
                        self.tortiecolour = choice(possible_colors)
                    if self.tortiepattern in ['braided', 'brokenbraided', 'brokenmackerel', 'charcoal']:
                        possible_colors = Pelt.doe_colors.copy()
                        if self.colour in possible_colors:
                            possible_colors.remove(self.colour)
                        self.tortiecolour = choice(possible_colors)
                    if self.tortiepattern == 'masked':
                        possible_colors = Pelt.default_colors.copy()
                        possible_colors.extend(Pelt.era_colors)
                        if self.colour in possible_colors:
                            possible_colors.remove(self.colour)
                        self.tortiecolour = choice(possible_colors)
            else:
                self.tortiecolour = "GOLDEN"
        else:
            self.tortiebase = None
            self.tortiepattern = None
            self.tortiecolour = None
            self.pattern = None

    def white_patches_inheritance(self, parents: tuple):

        par_whitepatches = set()
        par_points = []
        for p in parents:
            if p:
                if p.pelt.white_patches:
                    par_whitepatches.add(choice(p.pelt.white_patches))
                if p.pelt.points:
                    par_points.append(p.pelt.points)

        if not parents:
            print("Error - no parents. Randomizing white patches.")
            self.randomize_white_patches()
            return

        # Direct inheritance. Will only work if at least one parent has white patches, otherwise continue on.
        if par_whitepatches and not random.randint(0, game.config["cat_generation"]["direct_inheritance"]):
            # This ensures Torties and Calicos won't get direct inheritance of incorrect white patch types
            _temp = par_whitepatches.copy()
            if self.name == "Tortie":
                for p in _temp.copy():
                    if p in Pelt.high_white + Pelt.mostly_white + ["FULLWHITE"]:
                        _temp.remove(p)
            elif self.name == "Calico":
                for p in _temp.copy():
                    if p in Pelt.little_white + Pelt.mid_white:
                        _temp.remove(p)
                        
            chosen_white_patches = set()
            
            # Only proceed with the direct inheritance if there are white patches that match the pelt.
            if _temp:
                chosen_white_patches.add(choice(list(_temp)))
                for x in range(game.config["cat_generation"]["max_white_amount"] - 1):
                    if not random.randint(0, game.config["cat_generation"]["base_extra_white"]):
                        for p in chosen_white_patches:
                            if p in _temp:
                                _temp.remove(p)
                        if _temp:
                            chosen_white_patches.add(choice(list(_temp)))
                if len(chosen_white_patches) >= 2:
                    print("DoublePatches: "+str(len(chosen_white_patches))+" white patches!")
                self.white_patches = list(chosen_white_patches)

                # Direct inheritance also effect the point marking.
                if par_points and self.name != "Tortie":
                    self.points = choice(par_points)
                else:
                    self.points = None

                return

        # dealing with points
        if par_points:
            chance = 10 - len(par_points)
        else:
            chance = 40
        # Chance of point is 1 / chance.
        if self.name != "Tortie" and not int(random.random() * chance):
            self.points = choice(Pelt.point_markings)
        else:
            self.points = None

        white_list = [Pelt.little_white, Pelt.mid_white, Pelt.high_white, Pelt.mostly_white, ['FULLWHITE']]

        weights = [0, 0, 0, 0, 0]  # Same order as white_list
        for p_ in par_whitepatches:
            if p_ in Pelt.little_white:
                add_weights = (40, 20, 15, 5, 0)
            elif p_ in Pelt.mid_white:
                add_weights = (10, 40, 15, 10, 0)
            elif p_ in Pelt.high_white:
                add_weights = (15, 20, 40, 10, 1)
            elif p_ in Pelt.mostly_white:
                add_weights = (5, 15, 20, 40, 5)
            elif p_ == "FULLWHITE":
                add_weights = (0, 5, 15, 40, 10)
            else:
                add_weights = (0, 0, 0, 0, 0)

            for x in range(0, len(weights)):
                weights[x] += add_weights[x]

        # If all the weights are still 0, that means none of the parents have white patches.
        if not any(weights):
            if not all(parents):  # If any of the parents are None (unknown), use the following distribution:
                weights = [20, 10, 10, 5, 0]
            else:
                # Otherwise, all parents are known and don't have any white patches. Focus distribution on little_white.
                weights = [50, 5, 0, 0, 0]

        # Adjust weights for torties, since they can't have anything greater than mid_white:
        if self.name == "Tortie":
            weights = weights[:2] + [0, 0, 0]
            # Another check to make sure not all the values are zero. This should never happen, but better
            # safe than sorry.
            if not any(weights):
                weights = [2, 1, 0, 0, 0]
        elif self.name == "Calico":
            weights = [0, 0, 0] + weights[3:]
            # Another check to make sure not all the values are zero. This should never happen, but better
            # safe than sorry.
            if not any(weights):
                weights = [2, 1, 0, 0, 0]

        chosen_white_patches = set()
        chosen_white_patches.add(choice(
            random.choices(white_list, weights=weights, k=1)[0]
        ))
        
        num = game.config["cat_generation"]["base_extra_white"]
        
        if any(white in Pelt.high_white for white in chosen_white_patches):
            num -= 2
        elif any(white in Pelt.little_white for white in chosen_white_patches) or any(white in Pelt.mid_white for white in chosen_white_patches):
            num -= 5
        for p in parents:
            if p:
                if not p.pelt.white_patches:
                    num += 1
                elif len(p.pelt.white_patches) >= 2:
                    num -= 1
        if num < 0:
            num = 1

        for x in range(game.config["cat_generation"]["max_white_amount"] - 1):
            if not random.randint(0, num):
                weights = (12, 10, 3, 0, 0)
                chosen_white_patches.add(choice(
                    random.choices(white_list, weights=weights, k=1)[0]
                ))
                num += 1
        if len(chosen_white_patches) >= 2:
            print("DoublePatches: "+str(len(chosen_white_patches))+" white patches!")
        self.white_patches = list(chosen_white_patches)
        
        if self.points and self.white_patches in [Pelt.high_white, Pelt.mostly_white, 'FULLWHITE']:
            self.points = None

    def randomize_white_patches(self):

        # Points determination. Tortie can't be pointed
        if self.name != "Tortie" and not random.getrandbits(game.config["cat_generation"]["random_point_chance"]):
            # Cat has colorpoint!
            self.points = choice(Pelt.point_markings)
        else:
            self.points = None

        # Adjust weights for torties, since they can't have anything greater than mid_white:
        if self.name == "Tortie":
            weights = (2, 1, 0, 0, 0)
        elif self.name == "Calico":
            weights = (0, 0, 20, 15, 1)
        else:
            weights = (10, 10, 10, 10, 1)
        
        chosen_white_patches = set()
    
        white_list = [Pelt.little_white, Pelt.mid_white, Pelt.high_white, Pelt.mostly_white, ['FULLWHITE']]
        
        chosen_white_patches.add(choice(
            random.choices(white_list, weights=weights, k=1)[0]
        ))
        
        num = game.config["cat_generation"]["base_extra_white"]
        
        if any(white in Pelt.high_white for white in chosen_white_patches):
            num -= 2
        elif any(white in Pelt.little_white for white in chosen_white_patches) or any(white in Pelt.mid_white for white in chosen_white_patches):
            num -= 5
        if num < 0:
            num = 1
        for x in range(game.config["cat_generation"]["max_white_amount"] - 1):
            if not random.randint(0, num):
                weights = (12, 10, 3, 0, 0)
                chosen_white_patches.add(choice(
                    random.choices(white_list, weights=weights, k=1)[0]
                ))
                num += 1
        if len(chosen_white_patches) >= 2:
            print("DoublePatches: "+str(len(chosen_white_patches))+" white patches!")

        self.white_patches = list(chosen_white_patches)
        
        if self.points and self.white_patches in [Pelt.high_white, Pelt.mostly_white, 'FULLWHITE']:
            self.points = None

    def init_white_patches(self, pelt_white, parents: tuple):
        # Vit can roll for anyone, not just cats who rolled to have white in their pelt. 
        par_vit = []
        for p in parents:
            if p:
                if p.pelt.vitiligo:
                    par_vit.append(p.pelt.vitiligo)

        vit_chance = max(game.config["cat_generation"]["vit_chance"] - len(par_vit), 0)
        if not random.getrandbits(vit_chance):
            self.vitiligo = choice(Pelt.vit)

        # If the cat was rolled previously to have white patches, then determine the patch they will have
        # these functions also handle points. 
        if pelt_white:
            if parents:
                self.white_patches_inheritance(parents)
            else:
                self.randomize_white_patches()
        else:
            self.white_patches = None
            self.points = None

    def init_tint(self):
        """Sets tint for pelt and white patches"""

        # PELT TINT
        # Basic tints as possible for all colors.
        base_tints = sprites.cat_tints["possible_tints"]["basic"]
        if self.colour in sprites.cat_tints["colour_groups"]:
            color_group = sprites.cat_tints["colour_groups"].get(self.colour, "warm")
            color_tints = sprites.cat_tints["possible_tints"][color_group]
        else:
            color_tints = []

        if base_tints or color_tints:
            self.tint = choice(base_tints + color_tints)
        else:
            self.tint = "none"

        # WHITE PATCHES TINT
        if self.white_patches or self.points:
            # Now for white patches
            base_tints = sprites.white_patches_tints["possible_tints"]["basic"]
            if self.colour in sprites.cat_tints["colour_groups"]:
                color_group = sprites.white_patches_tints["colour_groups"].get(self.colour, "white")
                color_tints = sprites.white_patches_tints["possible_tints"][color_group]
            else:
                color_tints = []

            if base_tints or color_tints:
                self.white_patches_tint = choice(base_tints + color_tints)
            else:
                self.white_patches_tint = "none"
        else:
            self.white_patches_tint = "none"
    
    def init_physical_traits(self, parents: tuple=()):
        
        trait_categories = [
            Pelt.physical_trait_teeth,
            Pelt.physical_trait_ear_type,
            Pelt.physical_trait_ear_fold,
            Pelt.physical_trait_headfur,
            Pelt.physical_trait_cheekfur,
            Pelt.physical_trait_mane,
            Pelt.physical_trait_muzzle_type,
            Pelt.physical_trait_tail,
            Pelt.physical_trait_bodyfur,
            Pelt.physical_trait_misc
        ]
        
        trait_pool = [(trait, category) for category in trait_categories for trait in category]
        
        par_traits = set()
        for p in parents:
                par_traits.add(p.pelt.physical_trait_1)
                par_traits.add(p.pelt.physical_trait_2)
                par_traits.add(p.pelt.physical_trait_3)
                par_traits.add(p.pelt.physical_trait_4)
                par_traits.add(p.pelt.physical_trait_hidden)
                par_traits.add(p.pelt.physical_trait_hidden_2)
                par_traits.add(p.pelt.physical_trait_hidden_3)
                par_traits.add(p.pelt.physical_trait_hidden_4)
        
        # Remove any None values from par_traits
        par_traits.discard(None)
        
        if par_traits:
            # Check for conflicting traits from the same category
            for category in trait_categories:
                clash_traits = par_traits.intersection(category)
                if len(clash_traits) > 1:
                    chosen_trait = random.choice(list(clash_traits))
                    par_traits = par_traits.difference(clash_traits)
                    par_traits.add(chosen_trait)
            inherit_trait_chance = int(random.random() * 100)
            if inherit_trait_chance <= game.config["cat_generation"]["physical_trait_inherit_chance"]:
                #Roll to inherit first trait, and if so, remove it from the list
                self.physical_trait_1 = random.choice(list(par_traits))
                par_traits.remove(self.physical_trait_1)
                if len(par_traits) > 0:
                    #If we have a first trait, roll to inherit a second, and if we do, remove it from the list
                    inherit_trait_chance = int(random.random() * 100)
                    if inherit_trait_chance <= game.config["cat_generation"]["physical_trait_inherit_chance"]:
                        self.physical_trait_2 = random.choice(list(par_traits))
                        par_traits.remove(self.physical_trait_2)
                        if len(par_traits) > 0:
                            #If we have a second trait, roll to inherit a third, and if we do, remove it from the list
                            inherit_trait_chance = int(random.random() * 100)
                            if inherit_trait_chance <= game.config["cat_generation"]["physical_trait_inherit_chance"]:
                                self.physical_trait_3 = random.choice(list(par_traits))
                                par_traits.remove(self.physical_trait_3)
                                if len(par_traits) > 0:
                                    #If we have a third trait, roll to inherit a fourth, and if we do, remove it from the list
                                    inherit_trait_chance = int(random.random() * 100)
                                    if inherit_trait_chance <= game.config["cat_generation"]["physical_trait_inherit_chance"]:
                                        self.physical_trait_4 = random.choice(list(par_traits))
                                        par_traits.remove(self.physical_trait_4)
            if len(par_traits) > 0:
                #If there are still leftover traits, roll to inherit as hidden with a +50% chance
                inherit_trait_chance = int((random.random() * 100) - 50)
                if inherit_trait_chance <= game.config["cat_generation"]["physical_trait_inherit_chance"]:
                    self.physical_trait_hidden = random.choice(list(par_traits))
                    par_traits.remove(self.physical_trait_hidden)
                    if len(par_traits) > 0:
                        #If there are still leftover traits, roll to inherit as hidden with a +50% chance
                        inherit_trait_chance = int((random.random() * 100) - 50)
                        if inherit_trait_chance <= game.config["cat_generation"]["physical_trait_inherit_chance"]:
                            self.physical_trait_hidden_2 = random.choice(list(par_traits))
                            par_traits.remove(self.physical_trait_hidden_2)
                            if len(par_traits) > 0:
                                #If there are still leftover traits, roll to inherit as hidden with a +50% chance
                                inherit_trait_chance = int((random.random() * 100) - 50)
                                if inherit_trait_chance <= game.config["cat_generation"]["physical_trait_inherit_chance"]:
                                    self.physical_trait_hidden_3 = random.choice(list(par_traits))
                                    par_traits.remove(self.physical_trait_hidden_3)
                                    if len(par_traits) > 0:
                                        #If there are still leftover traits, roll to inherit as hidden with a +50% chance
                                        inherit_trait_chance = int((random.random() * 100) - 50)
                                        if inherit_trait_chance <= game.config["cat_generation"]["physical_trait_inherit_chance"]:
                                            self.physical_trait_hidden_4 = random.choice(list(par_traits))
                                            par_traits.remove(self.physical_trait_hidden_4)
            
        # Giving cats that inherited nothing a 50% of base chance roll for new traits
        if not self.physical_trait_1:
            trait_chance = int(random.random() * 100)
            if trait_chance <= game.config["cat_generation"]["physical_trait_chance"]:
                if trait_chance <= (0.5 * game.config["cat_generation"]["physical_trait_chance"]):
                    traitcount = 2
                    trait_chance = int(random.random() * 100)
                    if trait_chance <= (0.25 * game.config["cat_generation"]["physical_trait_chance"]):
                        traitcount = 3
                        trait_chance = int(random.random() * 100)
                        if trait_chance <= (0.1 * game.config["cat_generation"]["physical_trait_chance"]):
                            traitcount = 4
                else:
                    traitcount = 1
            else:
                traitcount = 0
                
            if traitcount > 0:
                # Select the first trait and its category
                trait1, category1 = random.choice(trait_pool)
                print("Trait 1:", trait1)
                self.physical_trait_1 = trait1
                
                # Remove traits from the same category as the first trait
                trait_pool = [(trait, category) for trait, category in trait_pool if category != category1]
                
                if traitcount >= 2 and trait_pool:
                    # Select the second trait from the remaining pool
                    trait2, category2 = random.choice(trait_pool)
                    print("Trait 2:", trait2)
                    self.physical_trait_2 = trait2
                    
                    # Remove traits from the same category as the second trait
                    trait_pool = [(trait, category) for trait, category in trait_pool if category != category2]
                    
                    if traitcount >= 3 and trait_pool:
                        # Select the third trait from the remaining pool
                        trait3, category3 = random.choice(trait_pool)
                        print("Trait 3:", trait3)
                        self.physical_trait_3 = trait3
                        
                        # Remove traits from the same category as the third trait
                        trait_pool = [(trait, category) for trait, category in trait_pool if category != category3]
                        
                        if traitcount == 4 and trait_pool:
                            # Select the fourth trait from the remaining pool
                            trait4, category4 = random.choice(trait_pool)
                            print("Trait 4:", trait4)
                            self.physical_trait_4 = trait4
                        else:
                            self.physical_trait_4 = None
                    else:
                        self.physical_trait_3 = None
                        self.physical_trait_4 = None
                else:
                    self.physical_trait_2 = None
                    self.physical_trait_3 = None
                    self.physical_trait_4 = None
            else:
                self.physical_trait_1 = None
                self.physical_trait_2 = None
                self.physical_trait_3 = None
                self.physical_trait_4 = None

    @property
    def white(self):
        return self.white_patches or self.points

    @white.setter
    def white(self, val):
        print("Can't set pelt.white")
        return

    @staticmethod
    def describe_appearance(cat, short=False):
        """Return a description of a cat

        :param Cat cat: The cat to describe
        :param bool short: Whether to return a heavily-truncated description, default False
        :return str: The cat's description
        """

        # Define look-up dictionaries
        if short:
            renamed_colors = {
                "white": "pale",
                "palegrey": "gray",
                "darkgrey": "gray",
                "grey": "gray",
                "paleginger": "ginger",
                "darkginger": "ginger",
                "sienna": "ginger",
                "lightbrown": "brown",
                "lilac": "brown",
                "golden-brown": "brown",
                "darkbrown": "brown",
                "chocolate": "brown",
                "ghost": "black",
                "pale": "pale",
                "cloud": "gray",
                "blue": "blue",
                "haze": "gray",
                "darkblue": "blue",
                "smog": "gray",
                "tan": "cream",
                "sand": "brown",
                "sunburst": "ginger",
                "russet": "ginger",
                "bone": "cream",
                "lemon": "yellow",
                "coffee": "brown",
                "marsh": "brown",
                "oak": "brown",
                "ruby": "red",
                "peach": "red",
                "scarlet": "red",
                "icy": "gray",
                "sky": "gray",
                "slate": "silver",
                "ashbrown": "brown",
                "storm": "blue",
                "clay": "brown",
                "umber": "brown",
                "shell": "cream",
                "salmon": "ginger",
                "butterscotch": "golden",
                "tangerine": "ginger",
                "chili": "ginger",
                "toffee": "ginger",
                "fawn": "cream",
                "taupe": "brown",
                "camel": "brown",
                "peanut": "brown",
                "mole": "brown",
                "walnut": "brown",
            }
        else:
            renamed_colors = {
                "white": "pale",
                "palegrey": "pale gray",
                "grey": "gray",
                "darkgrey": "dark gray",
                "paleginger": "pale ginger",
                "darkginger": "dark ginger",
                "sienna": "dark ginger",
                "lightbrown": "light brown",
                "lilac": "light brown",
                "golden-brown": "golden brown",
                "darkbrown": "dark brown",
                "chocolate": "dark brown",
                "ghost": "black",
                "pale": "pale gray",
                "cloud": "gray",
                "blue": "blue",
                "haze": "gray",
                "darkblue": "dark blue",
                "smog": "dark gray",
                "tan": "tan",
                "sand": "light brown",
                "sunburst": "ginger",
                "russet": "dark ginger",
                "bone": "beige",
                "lemon": "yellow",
                "coffee": "brown",
                "marsh": "brown",
                "oak": "reddish-brown",
                "ruby": "red",
                "peach": "pale red",
                "scarlet": "bright red",
                "icy": "pale gray",
                "sky": "pale gray",
                "slate": "silver",
                "ashbrown": "gray-brown",
                "storm": "blue",
                "clay": "dark brown",
                "umber": "dark brown",
                "shell": "cream",
                "salmon": "pale ginger",
                "butterscotch": "golden",
                "tangerine": "ginger",
                "chili": "dark ginger",
                "toffee": "ginger",
                "fawn": "cream",
                "taupe": "lilac",
                "camel": "brown",
                "peanut": "brown",
                "mole": "dark brown",
                "walnut": "dark brown",
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
            "Masked": "masked c_n tabby",
            "Abyssinian": "c_n abyssinian",
            "Clouded": "clouded c_n tabby",
            "Doberman": "c_n dog-like",
            "Merle": "c_n merle",
            "Snowflake": "unusually specked c_n",
            "Lynx": "unusually speckled c_n",
            "Wildcat": "unusually striped c_n",
            "Wolf": "c_n wolf-like",
            "Smokepoint": "c_n pointed smoke",
            "Brindle": "c_n brindled",
            "Finleap": "darker-legged c_n",
            "Spots": "c_n spotted",
            "Braided": "c_n tabby",
            "Brokenbraided": "c_n broken tabby",
            "Brokenmackerel": "c_n broken tabby",
            "Charcoal": "unusually dappled c_n",
        }

        # Start with determining the base color name
        color_name = str(cat.pelt.colour).lower()
        if color_name in renamed_colors:
            color_name = renamed_colors[color_name]

        # Replace "white" with "pale" if the cat is white
        if cat.pelt.name not in ["SingleColour", "TwoColour", "Tortie", "Calico"] and color_name == "white":
            color_name = "pale"

        # Time to describe the pattern and any additional colors
        if cat.pelt.name in pattern_des:
            if cat.pelt.colour in Pelt.default_colors and cat.pelt.name == "Rosette":
                cat.pelt.name = "Abyssinian"
            color_name = pattern_des[cat.pelt.name].replace("c_n", color_name) 
        elif cat.pelt.name in Pelt.torties:
            # Calicos and Torties need their own desciptions
            if short:
                # If using short, don't describe the colors of calicos and torties.
                # Just call them calico, tortie, or mottled
                if cat.pelt.colour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours and \
                        cat.pelt.tortiecolour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours:
                    color_name = "mottled"
                else:
                    color_name = cat.pelt.name.lower()
            else:
                base = cat.pelt.tortiebase.lower()
                if base in [tabby.lower() for tabby in Pelt.tabbies] + ['bengal', 'rosette', 'speckled']:
                    base = ' tabby'  # the extra space is intentional
                else:
                    base = ''

                patches_color = cat.pelt.tortiecolour.lower()
                if patches_color in renamed_colors:
                    patches_color = renamed_colors[patches_color]
                color_name = f"{color_name}/{patches_color}"

                if cat.pelt.colour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours and \
                        cat.pelt.tortiecolour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours:
                    color_name = f"{color_name} mottled{base}"
                else:
                    color_name = f"{color_name} {cat.pelt.name.lower()}{base}"

        if cat.pelt.white_patches:
            if cat.pelt.white_patches == "FULLWHITE":
                # If the cat is fullwhite, discard all other information. They are just white
                color_name = "white"
                
            if any(white in Pelt.mostly_white for white in cat.pelt.white_patches) and cat.pelt.name != "Calico":
                
                color_name = f"white and {color_name}"
            elif cat.pelt.name != "Calico":
                color_name = f"{color_name} and white"

        if cat.pelt.points:
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

        # Here is the place where we can add some additional details about the cat, for the full non-short one
        # These include notable missing limbs, vitiligo, long-furred-ness, and 3 or more scars
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
            if cat.pelt.vitiligo:
                additional_details.append("vitiligo")
            for scar in cat.pelt.scars:
                if scar in scar_details and scar_details[scar] not in additional_details:
                    additional_details.append(scar_details[scar])

            if len(additional_details) > 2:
                color_name = f"{color_name} with {', '.join(additional_details[:-1])}, and {additional_details[-1]}"
            elif len(additional_details) == 2:
                color_name = f"{color_name} with {' and '.join(additional_details)}"
            elif additional_details:
                color_name = f"{color_name} with {additional_details[0]}"

            if len(cat.pelt.scars) >= 3:
                color_name = f"scarred {color_name}"
            if cat.pelt.length == "long":
                color_name = f"long-furred {color_name}"

        return color_name

    def get_sprites_name(self):
        return Pelt.sprites_names[self.name]
