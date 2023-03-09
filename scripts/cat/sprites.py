import pygame

try:
    import ujson
except ImportError:
    import json as ujson


class Sprites():
    cat_tints = {}

    def __init__(self, original_size, new_size=None):
        self.size = original_size  # size of a single sprite in a spritesheet
        self.new_size = self.size * 2 if new_size is None else new_size
        self.spritesheets = {}
        self.images = {}
        self.groups = {}
        self.sprites = {}

        self.load_tints()

    def load_tints(self):
        try:
            with open("sprites/dicts/tint.json", 'r') as read_file:
                Sprites.cat_tints = ujson.loads(read_file.read())
        except:
            print("ERROR: Reading Tints")

    def spritesheet(self, a_file, name):
        """
        Add spritesheet called name from a_file.

        Parameters:
        a_file -- Path to the file to create a spritesheet from.
        name -- Name to call the new spritesheet.
        """
        self.spritesheets[name] = pygame.image.load(a_file).convert_alpha()

    def find_sprite(self, group_name, x, y):
        """
        Find singular sprite from a group.

        Parameters:
        group_name -- Name of Pygame group to find sprite from.
        x -- X-offset of the sprite to get. NOT pixel offset, but offset of other sprites.
        y -- Y-offset of the sprite to get. NOT pixel offset, but offset of other sprites.
        """
        # pixels will be calculated automatically, so for x and y, just use 0, 1, 2, 3 etc.
        new_sprite = pygame.Surface((self.size, self.size),
                                    pygame.HWSURFACE | pygame.SRCALPHA)
        new_sprite.blit(self.groups[group_name], (0, 0),
                        (x * self.size, y * self.size, (x + 1) * self.size,
                         (y + 1) * self.size))
        return new_sprite

    def make_group(self,
                   spritesheet,
                   pos,
                   name,
                   sprites_x=3,
                   sprites_y=3):  # pos = ex. (2, 3), no single pixels
        """
        Divide sprites on a sprite-sheet into groups of sprites that are easily accessible.

        Parameters:
        spritesheet -- Name of spritesheet.
        pos -- (x,y) tuple of offsets. NOT pixel offset, but offset of other sprites.
        name -- Name of group to make.
        
        Keyword Arguments
        sprites_x -- Number of sprites horizontally (default: 3)
        sprites_y -- Number of sprites vertically (default: 3)
        """

        # making the group
        new_group = pygame.Surface(
            (self.size * sprites_x, self.size * sprites_y),
            pygame.HWSURFACE | pygame.SRCALPHA)
        new_group.blit(
            self.spritesheets[spritesheet], (0, 0),
            (pos[0] * sprites_x * self.size, pos[1] * sprites_y * self.size,
             (pos[0] + sprites_x) * self.size,
             (pos[1] + sprites_y) * self.size))

        self.groups[name] = new_group

        # splitting group into singular sprites and storing into self.sprites section
        x_spr = 0
        y_spr = 0
        for x in range(sprites_x * sprites_y):
            new_sprite = pygame.Surface((self.size, self.size),
                                        pygame.HWSURFACE | pygame.SRCALPHA)
            new_sprite.blit(new_group, (0, 0),
                            (x_spr * self.size, y_spr * self.size,
                             (x_spr + 1) * self.size, (y_spr + 1) * self.size))
            self.sprites[name + str(x)] = new_sprite
            x_spr += 1
            if x_spr == sprites_x:
                x_spr = 0
                y_spr += 1

    def load_scars(self):
        """
        Loads scar sprites and puts them into groups.
        """
        scars = 'scars'

        for a, i in enumerate(
                ["ONE", "TWO", "THREE", "LEFTEAR", "RIGHTEAR", "NOTAIL"]):
            sprites.make_group('scars', (a, 0), f'scars{i}')
            sprites.make_group('scarsextra', (a, 0),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(
                ["MANLEG", "BRIGHTHEART", "MANTAIL", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]):
            sprites.make_group('scars', (a, 1), f'scars{i}')
            sprites.make_group('scarsextra', (a, 1),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(
                ["BRIDGE", "RIGHTBLIND", "LEFTBLIND", "BOTHBLIND", "BURNPAWS", "BURNTAIL"]):
            sprites.make_group('scars', (a, 2), f'scars{i}')
            sprites.make_group('scarsextra', (a, 2),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(
                ["BURNBELLY", "BEAKCHEEK", "BEAKLOWER", "BURNRUMP", "CATBITE", "RATBITE"]):
            sprites.make_group('scars', (a, 3), f'scars{i}')
            sprites.make_group('scarsextra', (a, 3),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(
                ["TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE"]):
            sprites.make_group('Newscars', (a, 0), f'scars{i}')
            sprites.make_group('Newscarsextra', (a, 0),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(["BELLY", "TOETRAP", "SNAKE"]):
            sprites.make_group('Newscars', (a, 1), f'scars{i}')
            sprites.make_group('Newscarsextra', (a, 1),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(["LEGBITE", "NECKBITE", "FACE", "HALFTAIL", "NOPAW"]):
            sprites.make_group('Newscars', (a, 2), f'scars{i}')
            sprites.make_group('Newscarsextra', (a, 2),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(["FROSTFACE", "FROSTTAIL", "FROSTMITT", "FROSTSOCK", "QUILLCHUNK", "QUILLSCRATCH"]):
            sprites.make_group('Newscars', (a, 3), f'scars{i}')
            sprites.make_group('Newscarsextra', (a, 3),
                               f'scarsextra{i}',
                               sprites_y=2)

            # Accessories
        for a, i in enumerate([
            "MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL"]):
            sprites.make_group('medcatherbs', (a, 0), f'acc_herbs{i}')
            sprites.make_group('medcatherbsextra', (a, 0), f'acc_herbsextra{i}', sprites_y=2)
        for a, i in enumerate([
            "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS"]):
            sprites.make_group('medcatherbs', (a, 1), f'acc_herbs{i}')
            sprites.make_group('medcatherbsextra', (a, 1), f'acc_herbsextra{i}', sprites_y=2)
        for a, i in enumerate([
            "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"]):
            sprites.make_group('medcatherbs', (a, 3), f'acc_herbs{i}')
            sprites.make_group('medcatherbsextra', (a, 3), f'acc_herbsextra{i}', sprites_y=2)
        sprites.make_group('medcatherbs', (5, 2), 'acc_herbsDRY HERBS')
        sprites.make_group('medcatherbsextra', (5, 2), 'acc_herbsextraDRY HERBS', sprites_y=2)

        for a, i in enumerate([
            "RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"]):
            sprites.make_group('medcatherbs', (a, 2), f'acc_wild{i}')
            sprites.make_group('medcatherbsextra', (a, 2), f'acc_wildextra{i}', sprites_y=2)
        for a, i in enumerate(["CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME"]):
            sprites.make_group('collars', (a, 0), f'collars{i}')
            sprites.make_group('collarsextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["GREEN", "RAINBOW", "BLACK", "SPIKES", "WHITE"]):
            sprites.make_group('collars', (a, 1), f'collars{i}')
            sprites.make_group('collarsextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINK", "PURPLE", "MULTI", "INDIGO"]):
            sprites.make_group('collars', (a, 2), f'collars{i}')
            sprites.make_group('collarsextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate([
            "CRIMSONBELL", "BLUEBELL", "YELLOWBELL", "CYANBELL", "REDBELL",
            "LIMEBELL"
        ]):
            sprites.make_group('bellcollars', (a, 0), f'collars{i}')
            sprites.make_group('bellcollarsextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(
                ["GREENBELL", "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "WHITEBELL"]):
            sprites.make_group('bellcollars', (a, 1), f'collars{i}')
            sprites.make_group('bellcollarsextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINKBELL", "PURPLEBELL", "MULTIBELL", "INDIGOBELL"]):
            sprites.make_group('bellcollars', (a, 2), f'collars{i}')
            sprites.make_group('bellcollarsextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate([
            "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
            "LIMEBOW"
        ]):
            sprites.make_group('bowcollars', (a, 0), f'collars{i}')
            sprites.make_group('bowcollarsextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(
                ["GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "WHITEBOW"]):
            sprites.make_group('bowcollars', (a, 1), f'collars{i}')
            sprites.make_group('bowcollarsextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINKBOW", "PURPLEBOW", "MULTIBOW", "INDIGOBOW"]):
            sprites.make_group('bowcollars', (a, 2), f'collars{i}')
            sprites.make_group('bowcollarsextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate([
            "CRIMSONNYLON", "BLUENYLON", "YELLOWNYLON", "CYANNYLON", "REDNYLON",
            "LIMENYLON"
        ]):
            sprites.make_group('nyloncollars', (a, 0), f'collars{i}')
            sprites.make_group('nyloncollarsextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(
                ["GREENNYLON", "RAINBOWNYLON", "BLACKNYLON", "SPIKESNYLON", "WHITENYLON"]):
            sprites.make_group('nyloncollars', (a, 1), f'collars{i}')
            sprites.make_group('nyloncollarsextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINKNYLON", "PURPLENYLON", "MULTINYLON", "INDIGONYLON"]):
            sprites.make_group('nyloncollars', (a, 2), f'collars{i}')
            sprites.make_group('nyloncollarsextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
        
# new accessories
        
        for a, i in enumerate(["WHITEYARN", "BLUEYARN", "YELLOWYARN", "PURPLEYARN", "PINKYARN", "MINTYARN"]):
            sprites.make_group('yarn', (a, 0), f'collars{i}')
            sprites.make_group('yarnextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["GREYYARN", "RAINBOWYARN", "GREENYARN", "REDYARN"]):
            sprites.make_group('yarn', (a, 1), f'collars{i}')
            sprites.make_group('yarnextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["FADEDYARN", "ORANGEYARN", "GRADIENTYARN"]):
            sprites.make_group('yarn', (a, 2), f'collars{i}')
            sprites.make_group('yarnextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
        
        for a, i in enumerate([
                "WHITEMANE", "PALEGRAYMANE", "SILVERMANE", "GRAYMANE", "DARKGRAYMANE",
                "BLACKMANE"]):
            sprites.make_group('manes', (a, 0), f'collars{i}')
            sprites.make_group('manesextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(
            ["PALEGINGERMANE", "GOLDENMANE", "GINGERMANE", "DARKGINGERMANE"]):
            sprites.make_group('manes', (a, 1), f'collars{i}')
            sprites.make_group('manesextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["LIGHTBROWNMANE", "BROWNMANE", "DARKBROWNMANE"]):
            sprites.make_group('manes', (a, 2), f'collars{i}')
            sprites.make_group('manesextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
        
        for a, i in enumerate(["REDSCARF", "BLUESCARF", "YELLOWSCARF", "CYANSCARF", "CRIMSONSCARF", "LIMESCARF"]):
            sprites.make_group('scarf', (a, 0), f'collars{i}')
            sprites.make_group('scarfextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["GREENSCARF", "RAINBOWSCARF", "GREYSCARF", "GOLDSCARF"]):
            sprites.make_group('scarf', (a, 1), f'collars{i}')
            sprites.make_group('scarfextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINKSCARF", "PURPLESCARF", "ORANGESCARF"]):
            sprites.make_group('scarf', (a, 2), f'collars{i}')
            sprites.make_group('scarfextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
        
        for a, i in enumerate(["REDSCARFS", "BLUESCARFS", "ORANGESCARFS", "MINTSCARFS", "CRIMSONSCARFS", "GREENSCARFS"]):
            sprites.make_group('scarfstripe', (a, 0), f'collars{i}')
            sprites.make_group('scarfstripeextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["CYANSCARFS", "BLUE2SCARFS", "PURPLESCARFS", "GOLDSCARFS"]):
            sprites.make_group('scarfstripe', (a, 1), f'collars{i}')
            sprites.make_group('scarfstripeextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINKSCARFS", "YELLOWSCARFS", "BLACKSCARFS"]):
            sprites.make_group('scarfstripe', (a, 2), f'collars{i}')
            sprites.make_group('scarfstripeextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
            
        for a, i in enumerate(["CRIMSONSPIKE", "BLUESPIKE", "YELLOWSPIKE", "CYANSPIKE", "REDSPIKE", "LIMESPIKE"]):
            sprites.make_group('collarspiky', (a, 0), f'collars{i}')
            sprites.make_group('collarspikyextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["GREENSPIKE", "RAINBOWSPIKE", "BLACKSPIKE", "GOLDSPIKE"]):
            sprites.make_group('collarspiky', (a, 1), f'collars{i}')
            sprites.make_group('collarspikyextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINKSPIKE", "PURPLESPIKE", "MULTISPIKE"]):
            sprites.make_group('collarspiky', (a, 2), f'collars{i}')
            sprites.make_group('collarspikyextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
        
        for a, i in enumerate([
                "POPPY2", "JUNIPER2", "DAISY", "BORAGE", "OAK LEAF",
                "BEECH LEAF"]):
            sprites.make_group('plants', (a, 0), f'acc_herbs{i}')
            sprites.make_group('plantsextra', (a, 0),
                               f'acc_herbsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(
            ["LAUREL2", "COLTSFOOT", "BINDWEED", "TORMENTIL"]):
            sprites.make_group('plants', (a, 1), f'acc_herbs{i}')
            sprites.make_group('plantsextra', (a, 1),
                               f'acc_herbsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["BRIGHT-EYE", "LAVENDER2", "YARROW"]):
            sprites.make_group('plants', (a, 2), f'acc_herbs{i}')
            sprites.make_group('plantsextra', (a, 2),
                               f'acc_herbsextra{i}',
                               sprites_y=2)
        
        for a, i in enumerate(["REDBANDANA", "BLUEBANDANA", "YELLOWBANDANA", "CYANBANDANA", "REDBANDANA", "LIMEBANDANA"]):
            sprites.make_group('bandanas', (a, 0), f'collars{i}')
            sprites.make_group('bandanasextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["GREENBANDANA", "RAINBOWBANDANA", "BLACKBANDANA", "GOLDBANDANA"]):
            sprites.make_group('bandanas', (a, 1), f'collars{i}')
            sprites.make_group('bandanasextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINKBANDANA", "PURPLEBANDANA", "MULTIBANDANA"]):
            sprites.make_group('bandanas', (a, 2), f'collars{i}')
            sprites.make_group('bandanasextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
            
        for a, i in enumerate(["CLOVERS", "SEAWEED", "PUMPKINS", "STICKS", "SNAKEROOT"]):
            sprites.make_group('ohdan', (a, 0), f'acc_herbs{i}')
            sprites.make_group('ohdanextra', (a, 0),
                               f'acc_herbsextra{i}',
                               sprites_y=2)
        sprites.make_group('ohdan', (4, 0), 'collarsCAPE')
        sprites.make_group('ohdanextra', (4, 0), 'collarsextraCAPE', sprites_y=2)
        for a, i in enumerate(["BEE", "BROWN SNAIL", "SNAKE", "WORM", "RED SNAIL"]):
            sprites.make_group('ohdan', (a, 1), f'acc_animal{i}')
            sprites.make_group('ohdanextra', (a, 1),
                               f'acc_animalextra{i}',
                               sprites_y=2)
    
        for a, i in enumerate([
            "MONARCH", "BUTTERFLY", "BROWN HIDE", "GRAY HIDE", "BROWN WRAP", "GRAY WRAP"]):
            sprites.make_group('superartsi', (a, 0), f'acc_wild{i}')
            sprites.make_group('superartsiextra', (a, 0), f'acc_wildextra{i}', sprites_y=2)
        for a, i in enumerate(["IVY WRAP", "HERB WRAP", "PINK HEARTS", "RED HEARTS", "LILIES"]):
            sprites.make_group('superartsi', (a, 1), f'acc_herbs{i}')
            sprites.make_group('superartsiextra', (a, 1),
                               f'acc_herbsextra{i}',
                               sprites_y=2)
            
        for a, i in enumerate([
                "BROWN FROG", "SNAIL", "BUMBLEBEE", "GREEN FROG"]):
            sprites.make_group('toasters', (a, 0), f'acc_animal{i}')
            sprites.make_group('toastersextra', (a, 0),
                               f'acc_animalextra{i}',
                               sprites_y=2)
        for a, i in enumerate(
            ["ORANGE LILY", "HONEY", "HONEYCOMB", "RED MUSHROOMS", "BROWN MUSHROOMS"]):
            sprites.make_group('toasters', (a, 1), f'acc_herbs{i}')
            sprites.make_group('toastersextra', (a, 1),
                               f'acc_herbsextra{i}',
                               sprites_y=2)
        
        for a, i in enumerate([
                "BARLEY", "SUNFLOWERS", "CORNFLOWER", "DRY THISTLE", "DRAGONFLY WINGS", "PINE WREATH"]):
            sprites.make_group('summerfall', (a, 0), f'acc_herbs{i}')
            sprites.make_group('summerfallextra', (a, 0),
                               f'acc_herbsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(
            ["ROSE", "HANGING HERBS", "LILY", "COLORFUL LEAVES", "ACORN BRANCH", "DRY FIR"]):
            sprites.make_group('summerfall', (a, 1), f'acc_herbs{i}')
            sprites.make_group('summerfallextra', (a, 1),
                               f'acc_herbsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PUMPKIN LEAVES", "DRY MOSS", "PINECONE", "THORN COLLAR", "AUTUMN CHAIN", "ROWAN BRANCH"]):
            sprites.make_group('summerfall', (a, 2), f'acc_herbs{i}')
            sprites.make_group('summerfallextra', (a, 2),
                               f'acc_herbsextra{i}',
                               sprites_y=2)
        
        for a, i in enumerate([
                "ROSES", "BLUEMOON", "BUTTERCUPS", "ORCHIDS", "AUTUMN", "VINES"]):
            sprites.make_group('angelflowers', (a, 0), f'acc_wild{i}')
            sprites.make_group('angelflowersextra', (a, 0),
                               f'acc_wildextra{i}',
                               sprites_y=2)
        for a, i in enumerate(
            ["GRASS", "RAINBOW FLOWERS", "PETUNIA", "CHRYSANTHEMUM"]):
            sprites.make_group('angelflowers', (a, 1), f'acc_wild{i}')
            sprites.make_group('angelflowersextra', (a, 1),
                               f'acc_wildextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["CHERRY BLOSSOM", "HELIOTROPES", "VALLEY LILIES"]):
            sprites.make_group('angelflowers', (a, 2), f'acc_wild{i}')
            sprites.make_group('angelflowersextra', (a, 2),
                               f'acc_wildextra{i}',
                               sprites_y=2)


sprites = Sprites(50)
#tiles = Sprites(64)

for x in [
    'lineart', 'singlecolours', 'speckledcolours', 'tabbycolours',
    'whitepatches', 'eyes', 'singleextra', 'tabbyextra', 'eyes2',
    'speckledextra', 'whiteextra', 'eyesextra', 'eyesextra2', 'skin',
    'skinextra', 'scars', 'scarsextra', 'whitenewextra', 'whitepatchesnew',
    'scarsdark', 'scarsdarkextra', 'collars', 'collarsextra', 'nyloncollars', 'nyloncollarsextra',
    'bellcollars', 'bellcollarsextra', 'bowcollars', 'bowcollarsextra',
    'speckledcolours2', 'speckledextra2', 'tabbycolours2', 'tabbyextra2',
    'rosettecolours', 'rosetteextra', 'smokecolours', 'smokeextra', 'tickedcolours', 'tickedextra',
    'mackerelcolours', 'classiccolours', 'sokokecolours', 'agouticolours', 'singlestripecolours',
    'mackerelextra', 'classicextra', 'sokokeextra', 'agoutiextra', 'singlestripeextra',
    'whitepatches3', 'whitepatches3extra', 'whitepatches4', 'whitepatches4extra',
    'Newscars', 'Newscarsextra', 'shadersnewwhite', 'lineartdead',
    'tortiecolourssolid', 'tortiecolourstabby', 'tortiecoloursbengal', 'tortiecoloursmarbled',
    'tortiecoloursticked', 'tortiecolourssmoke', 'tortiecoloursrosette', 'tortiecoloursspeckled',
    'tortiecoloursmackerel', 'tortiecoloursclassic', 'tortiecolourssokoke', 'tortiecoloursagouti',
    'tortiesextrasolid', 'tortiesextratabby', 'tortiesextrabengal', 'tortiesextramarbled', 'tortiesextraticked',
    'tortiesextrasmoke', 'tortiesextrarosette', 'tortiesextraspeckled',
    'tortiesextramackerel', 'tortiesextraclassic', 'tortiesextrasokoke', 'tortiesextraagouti',
    'medcatherbs', 'medcatherbsextra', 'lineartdf', 'eyes_df', 'eyesextra_df', 'lightingnew', 'fademask',
    'fadestarclan', 'fadedarkforest', 'eyes3', 'eyesextra3',
    # modded stuff
    'bengalcolours', 'bengalextra', 'bengalcolours2', 'bengalextra2',
    'ghosttabby', 'ghosttabbyextra', 'manes', 'manesextra', 'marbledcolours', 'marbledextra', 'marbledcolours2', 'marbledextra2', 'merle', 'merleextra',
    'pinstripetabby', 'pinstripetabbyextra', 'rosettecolours2', 'rosetteextra2', 'singlecolours2', 'singleextra2',
    'smokecolours2', 'smokeextra2', 'snowflake', 'snowflakeextra', 'speckledcolours2', 'speckledextra2',
    'tabbycolours2', 'tabbyextra2', 'tickedcolors2', 'tickedextra2', 'yarn', 'yarnextra', 'mackerel2', 'mackerel2extra', 'mackerel3', 'mackerelextra3',
    'sokokecolours', 'sokokeextra', 'singlecolours3', 'singleextra3', 'scarf', 'scarfextra', 'scarfstripe', 'scarfstripeextra',
    'collarspiky', 'collarspikyextra', 'cloudy', 'cloudyextra', 'plants', 'plantsextra', 'bandanas', 'bandanasextra', 'points',
    'pointsextra', 'ragdolls', 'ragdollsextra', 'shadedtabby', 'shadedextra', 'rsinglecolours', 'rsingleextra', 'tortiecoloursrsolid', 'tortieextrarsolid', 'tortiecoloursrtabby', 'tortieextrartabby',
    'tortiebrindle', 'tortiebrindleextra', 'whitepatchesmore', 'whiteextramore', 'whitepatchesmoss', 'whitemossextra', 'sokoke2', 'sokoke2extra', 'sokoke3',
    'abyssinian', 'abyssinianextra', 'rsinglecolours', 'rsingleextra', 'tortieghost', 'tortieghostextra', 'tortiemerle', 'tortiemerleextra', 'tortiepinstripe', 'tortiepinstripeextra',
    'tortiesnowflake', 'tortiesnowflakeextra', 'rtabby', 'rtabbyextra', 'whitegoogaoo', 'whiteextragoogaoo',
    'agouticolours2', 'agoutiextra2', 'bengalcolours3', 'bengalextra3', 'classiccolours2', 'classicextra2', 'marbledcolours3', 'marbledextra3', 'rosettecolours3', 'rosetteextra3',
    'singlestripe2', 'singlestripeextra2', 'smokecolours3', 'smokeextra3', 'sokokeextra3', 'speckledcolours3', 'speckledextra3', 'tabbycolours3', 'tabbyextra3', 'tickedcolors3', 'tickedextra3',
    'moresokoke', 'moresokokeextra', 'angelflowers', 'angelflowersextra', 'toasters', 'toastersextra', 'ohdan', 'ohdanextra', 'superartsi', 'superartsiextra', 'summerfall', 'summerfallextra'

]:
    sprites.spritesheet(f"sprites/{x}.png", x)

for sprite in [
    'Paralyzed_lineart', 'singleparalyzed', 'speckledparalyzed',
    'tabbyparalyzed', 'whiteallparalyzed', 'eyesparalyzed',
    'tabbyparalyzed', 'tortiesparalyzed', 'scarsparalyzed', 'skinparalyzed',
    'medcatherbsparalyzed'

]:
    sprites.spritesheet(f"sprites/paralyzed/{sprite}.png", sprite)

# for x in ['dithered']:
#     tiles.spritesheet(f"sprites/{x}.png", x)

# Line art
sprites.make_group('lineart', (0, 0), 'lines', sprites_y=5)
sprites.make_group('Paralyzed_lineart', (0, 0),
                   'p_lines',
                   sprites_x=1,
                   sprites_y=1)
sprites.make_group('shadersnewwhite', (0, 0), 'shaders', sprites_y=5)
sprites.make_group('lightingnew', (0, 0), 'lighting', sprites_y=5)

sprites.make_group('lineartdead', (0, 0), 'lineartdead', sprites_y=5)
sprites.make_group('lineartdf', (0, 0), 'lineartdf', sprites_y=5)

# Fading Fog
sprites.make_group('fademask', (0, 0), 'fademask', sprites_y=15)
sprites.make_group('fadestarclan', (0, 0), 'fadestarclan', sprites_y=15)
sprites.make_group('fadedarkforest', (0, 0), 'fadedf', sprites_y=15)

for a, i in enumerate(
        ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE']):
    sprites.make_group('eyes', (a, 0), f'eyes{i}')
    sprites.make_group('eyesextra', (a, 0), f'eyesextra{i}', sprites_y=2)
for a, i in enumerate(
        ['DARKBLUE', 'GREY', 'CYAN', 'EMERALD', 'HEATHERBLUE', 'SUNLITICE']):
    sprites.make_group('eyes', (a, 1), f'eyes{i}')
    sprites.make_group('eyesextra', (a, 1), f'eyesextra{i}', sprites_y=2)
for a, i in enumerate(
        ['COPPER', 'SAGE', 'BLUE2', 'PALEBLUE', 'BLUEYELLOW', 'BLUEGREEN']):
    sprites.make_group('eyes', (a, 2), f'eyes{i}')
    sprites.make_group('eyesextra', (a, 2), f'eyesextra{i}', sprites_y=2)
for a, i in enumerate(
        ['PALEYELLOW', 'GOLD', 'GREENYELLOW', 'PINK', 'SCARLET', 'VIOLET']):
    sprites.make_group('eyes', (a, 3), f'eyes{i}')
    sprites.make_group('eyesextra', (a, 3), f'eyesextra{i}', sprites_y=2)
for a, i in enumerate(
        ['PALEYELLOW2', 'RED', 'AQUA', 'PALEVIOLET', 'SAGEGREEN', 'PALEBLUE2']):
    sprites.make_group('eyes', (a, 4), f'eyes{i}')
    sprites.make_group('eyesextra', (a, 4), f'eyesextra{i}', sprites_y=2)
for a, i in enumerate(
        ['BROWN', 'SPRINGGREEN', 'GOLDEN', 'HONEY', 'COPPER2', 'MAGENTA']):
    sprites.make_group('eyes2', (a, 0), f'eyes{i}')
    sprites.make_group('eyesextra2', (a, 0), f'eyesextra{i}', sprites_y=2)
for a, i in enumerate(
        ['MINT', 'EMERALD2', 'PUMPKIN', 'ROSEGOLD', 'GREENGOLD', 'PINKBLUE']):
    sprites.make_group('eyes2', (a, 1), f'eyes{i}')
    sprites.make_group('eyesextra2', (a, 1), f'eyesextra{i}', sprites_y=2)
for a, i in enumerate(
        ['DANDELION', 'INDIGO', 'AMARANTH', 'CORAL', 'DARKGREEN', 'DARKAMBER']):
    sprites.make_group('eyes2', (a, 2), f'eyes{i}')
    sprites.make_group('eyesextra2', (a, 2), f'eyesextra{i}', sprites_y=2)

# white patches
for a, i in enumerate(['FULLWHITE', 'ANY', 'TUXEDO', 'LITTLE', 'COLOURPOINT', 'VAN', 'ANY2']):
    sprites.make_group('whitepatches', (a, 0), f'white{i}')
    sprites.make_group('whiteextra', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate([
    'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
    'LIGHTSONG', 'VITILIGO'
]):
    sprites.make_group('whitepatchesnew', (a, 0), f'white{i}')
    sprites.make_group('whitenewextra', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate([
    'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY', 'COLOURPOINTCREAMY',
    'VANCREAMY', 'ANY2CREAMY'
]):
    sprites.make_group('whitepatches', (a, 1), f'white{i}')
    sprites.make_group('whiteextra', (a, 1), f'whiteextra{i}', sprites_y=2)
# extra
sprites.make_group('whitepatches', (0, 2), 'whiteEXTRA')
sprites.make_group('whiteextra', (0, 2), 'whiteextraEXTRA', sprites_y=2)

# ryos white patches
for a, i in enumerate(
        ['TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTS2', 'GOATEE', 'VITILIGO2']):
    sprites.make_group('whitepatches3', (a, 0), f'white{i}')
    sprites.make_group('whitepatches3extra', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(['TAIL', 'BLAZE', 'PRINCE', 'BIB', 'VEE', 'UNDERS', 'PAWS', 'MITAINE']):
    sprites.make_group('whitepatches3', (a, 1), f'white{i}')
    sprites.make_group('whitepatches3extra', (a, 1), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(
        ['FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'SCOURGE']):
    sprites.make_group('whitepatches3', (a, 2), f'white{i}')
    sprites.make_group('whitepatches3extra', (a, 2), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(
        ['APRON', 'CAPSADDLE', 'MASKMANTLE', 'SQUEAKS', 'STAR', 'TOESTAIL', 'RAVENPAW', 'HONEY']):
    sprites.make_group('whitepatches3', (a, 3), f'white{i}')
    sprites.make_group('whitepatches3extra', (a, 3), f'whiteextra{i}', sprites_y=2)

# beejeans white patches + perrio's point marks, painted, and heart2 + anju's new marks + key's blackstar
for a, i in enumerate(['PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED']):
    sprites.make_group('whitepatches4', (a, 0), 'white' + i)
    sprites.make_group('whitepatches4extra', (a, 0), 'whiteextra' + i, sprites_y=2)
for a, i in enumerate(['HEART', 'LILTWO', 'GLASS', 'MOORISH', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT']):
    sprites.make_group('whitepatches4', (a, 1), 'white' + i)
    sprites.make_group('whitepatches4extra', (a, 1), 'whiteextra' + i, sprites_y=2)
for a, i in enumerate(['MAO', 'LUNA', 'CHESTSPECK', 'WINGS', 'PAINTED', 'HEART2', 'BLACKSTAR']):
    sprites.make_group('whitepatches4', (a, 2), 'white' + i)
    sprites.make_group('whitepatches4extra', (a, 2), 'whiteextra' + i, sprites_y=2)

# era's white patches
for a, i in enumerate(['MOJO', 'STAINS1', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESENT', 'HUSKY']):
    sprites.make_group('whitepatchesmore', (a, 0), 'white' + i)
    sprites.make_group('whiteextramore', (a, 0), 'whiteextra' + i, sprites_y=2)
for a, i in enumerate(['COW', 'MASK', 'S', 'BROWNSPOTS', 'SWIFTPAW']):
    sprites.make_group('whitepatchesmore', (a, 1), 'white' + i)
    sprites.make_group('whiteextramore', (a, 1), 'whiteextra' + i, sprites_y=2)

# moss' white patches
for a, i in enumerate(['SNOWSHOE', 'VENUS', 'SNOWBOOT', 'CHANCE', 'MOSSCLAW', 'DAPPLED', 'NIGHTMIST', 'HAWK']):
    sprites.make_group('whitepatchesmoss', (a, 0), 'white' + i)
    sprites.make_group('whitemossextra', (a, 0), 'whiteextra' + i, sprites_y=2)
for a, i in enumerate(['SHADOWSIGHT', 'TWIST', 'RETSUKO', 'OKAPI', 'FRECKLEMASK', 'MOTH']):
    sprites.make_group('whitepatchesmoss', (a, 1), 'white' + i)
    sprites.make_group('whitemossextra', (a, 1), 'whiteextra' + i, sprites_y=2)
    
# googaoo's white patches
for a, i in enumerate(['CHIN', 'DUTCH', 'EYEPATCH', 'WBELLY1', 'WBELLY2', 'CBELLY1', 'CBELLY2', 'DARKTAIL']):
    sprites.make_group('whitegoogaoo', (a, 0), 'white' + i)
    sprites.make_group('whiteextragoogaoo', (a, 0), 'whiteextra' + i, sprites_y=2)
for a, i in enumerate(['HALFFACE3', 'BLACKSTAR', 'SPOTTY', 'VILITIGO3', 'WHITEHEAD', 'COW2']):
    sprites.make_group('whitegoogaoo', (a, 1), 'white' + i)
    sprites.make_group('whiteextragoogaoo', (a, 1), 'whiteextra' + i, sprites_y=2)

# single (solid)
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('singlecolours', (a, 0), f'single{i}')
    sprites.make_group('singleextra', (a, 0), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('singlecolours', (a, 1), f'single{i}')
    sprites.make_group('singleextra', (a, 1), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK']):
    sprites.make_group('singlecolours', (a, 2), f'single{i}')
    sprites.make_group('singleextra', (a, 2), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK']):
    sprites.make_group('singlecolours2', (a, 0), f'single{i}')
    sprites.make_group('singleextra2', (a, 0), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['PALE', 'CREAM2', 'APRICOT', 'ORANGE']):
    sprites.make_group('singlecolours2', (a, 1), f'single{i}')
    sprites.make_group('singleextra2', (a, 1), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN', 'CINNAMON', 'CHOCOLATE']):
    sprites.make_group('singlecolours2', (a, 2), f'single{i}')
    sprites.make_group('singleextra2', (a, 2), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'CLOUD', 'BLUE2', 'HAZE', 'DARKBLUE', 'SOOT']):
    sprites.make_group('singlecolours3', (a, 0), f'single{i}')
    sprites.make_group('singleextra3', (a, 0), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['IVORY', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON']):
    sprites.make_group('singlecolours3', (a, 1), f'single{i}')
    sprites.make_group('singleextra3', (a, 1), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET']):
    sprites.make_group('singlecolours3', (a, 2), f'single{i}')
    sprites.make_group('singleextra3', (a, 2), f'singleextra{i}', sprites_y=2)
# tabby
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('tabbycolours', (a, 0), f'tabby{i}')
    sprites.make_group('tabbyextra', (a, 0), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('tabbycolours', (a, 1), f'tabby{i}')
    sprites.make_group('tabbyextra', (a, 1), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK']):
    sprites.make_group('tabbycolours', (a, 2), f'tabby{i}')
    sprites.make_group('tabbyextra', (a, 2), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK']):
    sprites.make_group('tabbycolours2', (a, 0), f'tabby{i}')
    sprites.make_group('tabbyextra2', (a, 0), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['PALE', 'CREAM2', 'APRICOT', 'ORANGE']):
    sprites.make_group('tabbycolours2', (a, 1), f'tabby{i}')
    sprites.make_group('tabbyextra2', (a, 1), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN', 'CINNAMON', 'CHOCOLATE']):
    sprites.make_group('tabbycolours2', (a, 2), f'tabby{i}')
    sprites.make_group('tabbyextra2', (a, 2), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'CLOUD', 'BLUE2', 'HAZE', 'DARKBLUE', 'SOOT']):
    sprites.make_group('tabbycolours3', (a, 0), f'tabby{i}')
    sprites.make_group('tabbyextra3', (a, 0), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['IVORY', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON']):
    sprites.make_group('tabbycolours3', (a, 1), f'tabby{i}')
    sprites.make_group('tabbyextra3', (a, 1), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET']):
    sprites.make_group('tabbycolours3', (a, 2), f'tabby{i}')
    sprites.make_group('tabbyextra3', (a, 2), f'tabbyextra{i}', sprites_y=2)
# marbled
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('marbledcolours', (a, 0), f'marbled{i}')
    sprites.make_group('marbledextra', (a, 0), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('marbledcolours', (a, 1), f'marbled{i}')
    sprites.make_group('marbledextra', (a, 1), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK']):
    sprites.make_group('marbledcolours', (a, 2), f'marbled{i}')
    sprites.make_group('marbledextra', (a, 2), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK']):
    sprites.make_group('marbledcolours2', (a, 0), f'marbled{i}')
    sprites.make_group('marbledextra2', (a, 0), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['PALE', 'CREAM2', 'APRICOT', 'ORANGE']):
    sprites.make_group('marbledcolours2', (a, 1), f'marbled{i}')
    sprites.make_group('marbledextra2', (a, 1), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN', 'CINNAMON', 'CHOCOLATE']):
    sprites.make_group('marbledcolours2', (a, 2), f'marbled{i}')
    sprites.make_group('marbledextra2', (a, 2), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'CLOUD', 'BLUE2', 'HAZE', 'DARKBLUE', 'SOOT']):
    sprites.make_group('marbledcolours3', (a, 0), f'marbled{i}')
    sprites.make_group('marbledextra3', (a, 0), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['IVORY', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON']):
    sprites.make_group('marbledcolours3', (a, 1), f'marbled{i}')
    sprites.make_group('marbledextra3', (a, 1), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET']):
    sprites.make_group('marbledcolours3', (a, 2), f'marbled{i}')
    sprites.make_group('marbledextra3', (a, 2), f'marbledextra{i}', sprites_y=2)
# rosette
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('rosettecolours', (a, 0), f'rosette{i}')
    sprites.make_group('rosetteextra', (a, 0), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('rosettecolours', (a, 1), f'rosette{i}')
    sprites.make_group('rosetteextra', (a, 1), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK']):
    sprites.make_group('rosettecolours', (a, 2), f'rosette{i}')
    sprites.make_group('rosetteextra', (a, 2), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK']):
    sprites.make_group('rosettecolours2', (a, 0), f'rosette{i}')
    sprites.make_group('rosetteextra2', (a, 0), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['PALE', 'CREAM2', 'APRICOT', 'ORANGE']):
    sprites.make_group('rosettecolours2', (a, 1), f'rosette{i}')
    sprites.make_group('rosetteextra2', (a, 1), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN', 'CINNAMON', 'CHOCOLATE']):
    sprites.make_group('rosettecolours2', (a, 2), f'rosette{i}')
    sprites.make_group('rosetteextra2', (a, 2), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'CLOUD', 'BLUE2', 'HAZE', 'DARKBLUE', 'SOOT']):
    sprites.make_group('rosettecolours3', (a, 0), f'rosette{i}')
    sprites.make_group('rosetteextra3', (a, 0), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['IVORY', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON']):
    sprites.make_group('rosettecolours3', (a, 1), f'rosette{i}')
    sprites.make_group('rosetteextra3', (a, 1), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET']):
    sprites.make_group('rosettecolours3', (a, 2), f'rosette{i}')
    sprites.make_group('rosetteextra3', (a, 2), f'rosetteextra{i}', sprites_y=2)
# smoke
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('smokecolours', (a, 0), f'smoke{i}')
    sprites.make_group('smokeextra', (a, 0), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('smokecolours', (a, 1), f'smoke{i}')
    sprites.make_group('smokeextra', (a, 1), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK']):
    sprites.make_group('smokecolours', (a, 2), f'smoke{i}')
    sprites.make_group('smokeextra', (a, 2), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK']):
    sprites.make_group('smokecolours2', (a, 0), f'smoke{i}')
    sprites.make_group('smokeextra2', (a, 0), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['PALE', 'CREAM2', 'APRICOT', 'ORANGE']):
    sprites.make_group('smokecolours2', (a, 1), f'smoke{i}')
    sprites.make_group('smokeextra2', (a, 1), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN', 'CINNAMON', 'CHOCOLATE']):
    sprites.make_group('smokecolours2', (a, 2), f'smoke{i}')
    sprites.make_group('smokeextra2', (a, 2), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'CLOUD', 'BLUE2', 'HAZE', 'DARKBLUE', 'SOOT']):
    sprites.make_group('smokecolours3', (a, 0), f'smoke{i}')
    sprites.make_group('smokeextra3', (a, 0), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['IVORY', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON']):
    sprites.make_group('smokecolours3', (a, 1), f'smoke{i}')
    sprites.make_group('smokeextra3', (a, 1), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET']):
    sprites.make_group('smokecolours3', (a, 2), f'smoke{i}')
    sprites.make_group('smokeextra3', (a, 2), f'smokeextra{i}', sprites_y=2)
# ticked
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('tickedcolours', (a, 0), f'ticked{i}')
    sprites.make_group('tickedextra', (a, 0), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('tickedcolours', (a, 1), f'ticked{i}')
    sprites.make_group('tickedextra', (a, 1), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK']):
    sprites.make_group('tickedcolours', (a, 2), f'ticked{i}')
    sprites.make_group('tickedextra', (a, 2), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK']):
    sprites.make_group('tickedcolors2', (a, 0), f'ticked{i}')
    sprites.make_group('tickedextra2', (a, 0), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['PALE', 'CREAM2', 'APRICOT', 'ORANGE']):
    sprites.make_group('tickedcolors2', (a, 1), f'ticked{i}')
    sprites.make_group('tickedextra2', (a, 1), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN', 'CINNAMON', 'CHOCOLATE']):
    sprites.make_group('tickedcolors2', (a, 2), f'ticked{i}')
    sprites.make_group('tickedextra2', (a, 2), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'CLOUD', 'BLUE2', 'HAZE', 'DARKBLUE', 'SOOT']):
    sprites.make_group('tickedcolors3', (a, 0), f'ticked{i}')
    sprites.make_group('tickedextra3', (a, 0), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['IVORY', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON']):
    sprites.make_group('tickedcolors3', (a, 1), f'ticked{i}')
    sprites.make_group('tickedextra3', (a, 1), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET']):
    sprites.make_group('tickedcolors3', (a, 2), f'ticked{i}')
    sprites.make_group('tickedextra3', (a, 2), f'tickedextra{i}', sprites_y=2)
# speckled
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('speckledcolours', (a, 0), f'speckled{i}')
    sprites.make_group('speckledextra', (a, 0), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('speckledcolours', (a, 1), f'speckled{i}')
    sprites.make_group('speckledextra', (a, 1), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK']):
    sprites.make_group('speckledcolours', (a, 2), f'speckled{i}')
    sprites.make_group('speckledextra', (a, 2), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK']):
    sprites.make_group('speckledcolours2', (a, 0), f'speckled{i}')
    sprites.make_group('speckledextra2', (a, 0), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['PALE', 'CREAM2', 'APRICOT', 'ORANGE']):
    sprites.make_group('speckledcolours2', (a, 1), f'speckled{i}')
    sprites.make_group('speckledextra2', (a, 1), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN', 'CINNAMON', 'CHOCOLATE']):
    sprites.make_group('speckledcolours2', (a, 2), f'speckled{i}')
    sprites.make_group('speckledextra2', (a, 2), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'CLOUD', 'BLUE2', 'HAZE', 'DARKBLUE', 'SOOT']):
    sprites.make_group('speckledcolours3', (a, 0), f'speckled{i}')
    sprites.make_group('speckledextra3', (a, 0), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['IVORY', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON']):
    sprites.make_group('speckledcolours3', (a, 1), f'speckled{i}')
    sprites.make_group('speckledextra3', (a, 1), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET']):
    sprites.make_group('speckledcolours3', (a, 2), f'speckled{i}')
    sprites.make_group('speckledextra3', (a, 2), f'speckledextra{i}', sprites_y=2)
# bengal
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('bengalcolours', (a, 0), f'bengal{i}')
    sprites.make_group('bengalextra', (a, 0), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('bengalcolours', (a, 1), f'bengal{i}')
    sprites.make_group('bengalextra', (a, 1), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK']):
    sprites.make_group('bengalcolours', (a, 2), f'bengal{i}')
    sprites.make_group('bengalextra', (a, 2), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK']):
    sprites.make_group('bengalcolours2', (a, 0), f'bengal{i}')
    sprites.make_group('bengalextra2', (a, 0), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['PALE', 'CREAM2', 'APRICOT', 'ORANGE']):
    sprites.make_group('bengalcolours2', (a, 1), f'bengal{i}')
    sprites.make_group('bengalextra2', (a, 1), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN', 'CINNAMON', 'CHOCOLATE']):
    sprites.make_group('bengalcolours2', (a, 2), f'bengal{i}')
    sprites.make_group('bengalextra2', (a, 2), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'CLOUD', 'BLUE2', 'HAZE', 'DARKBLUE', 'SOOT']):
    sprites.make_group('bengalcolours3', (a, 0), f'bengal{i}')
    sprites.make_group('bengalextra3', (a, 0), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['IVORY', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON']):
    sprites.make_group('bengalcolours3', (a, 1), f'bengal{i}')
    sprites.make_group('bengalextra3', (a, 1), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET']):
    sprites.make_group('bengalcolours3', (a, 2), f'bengal{i}')
    sprites.make_group('bengalextra3', (a, 2), f'bengalextra{i}', sprites_y=2)
# mackerel
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('mackerelcolours', (a, 0), f'mackerel{i}')
    sprites.make_group('mackerelextra', (a, 0), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('mackerelcolours', (a, 1), f'mackerel{i}')
    sprites.make_group('mackerelextra', (a, 1), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK']):
    sprites.make_group('mackerelcolours', (a, 2), f'mackerel{i}')
    sprites.make_group('mackerelextra', (a, 2), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK']):
    sprites.make_group('mackerel2', (a, 0), f'mackerel{i}')
    sprites.make_group('mackerel2extra', (a, 0), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['PALE', 'CREAM2', 'APRICOT', 'ORANGE']):
    sprites.make_group('mackerel2', (a, 1), f'mackerel{i}')
    sprites.make_group('mackerel2extra', (a, 1), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN', 'CINNAMON', 'CHOCOLATE']):
    sprites.make_group('mackerel2', (a, 2), f'mackerel{i}')
    sprites.make_group('mackerel2extra', (a, 2), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'CLOUD', 'BLUE2', 'HAZE', 'DARKBLUE', 'SOOT']):
    sprites.make_group('mackerel3', (a, 0), f'mackerel{i}')
    sprites.make_group('mackerelextra3', (a, 0), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['IVORY', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON']):
    sprites.make_group('mackerel3', (a, 1), f'mackerel{i}')
    sprites.make_group('mackerelextra3', (a, 1), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET']):
    sprites.make_group('mackerel3', (a, 2), f'mackerel{i}')
    sprites.make_group('mackerelextra3', (a, 2), f'mackerelextra{i}', sprites_y=2)
# classic
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('classiccolours', (a, 0), f'classic{i}')
    sprites.make_group('classicextra', (a, 0), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('classiccolours', (a, 1), f'classic{i}')
    sprites.make_group('classicextra', (a, 1), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK']):
    sprites.make_group('classiccolours', (a, 2), f'classic{i}')
    sprites.make_group('classicextra', (a, 2), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'CLOUD', 'BLUE2', 'HAZE', 'DARKBLUE', 'SOOT']):
    sprites.make_group('classiccolours2', (a, 0), f'classic{i}')
    sprites.make_group('classicextra2', (a, 0), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['IVORY', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON']):
    sprites.make_group('classiccolours2', (a, 1), f'classic{i}')
    sprites.make_group('classicextra2', (a, 1), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET']):
    sprites.make_group('classiccolours2', (a, 2), f'classic{i}')
    sprites.make_group('classicextra2', (a, 2), f'classicextra{i}', sprites_y=2)
# sokoke
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('sokokecolours', (a, 0), f'sokoke{i}')
    sprites.make_group('sokokeextra', (a, 0), f'sokokeextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('sokokecolours', (a, 1), f'sokoke{i}')
    sprites.make_group('sokokeextra', (a, 1), f'sokokeextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK']):
    sprites.make_group('sokokecolours', (a, 2), f'sokoke{i}')
    sprites.make_group('sokokeextra', (a, 2), f'sokokeextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'CLOUD', 'BLUE2', 'HAZE', 'DARKBLUE', 'SOOT']):
    sprites.make_group('sokoke3', (a, 0), f'sokoke{i}')
    sprites.make_group('sokokeextra3', (a, 0), f'sokokeextra{i}', sprites_y=2)
for a, i in enumerate(['IVORY', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON']):
    sprites.make_group('sokoke3', (a, 1), f'sokoke{i}')
    sprites.make_group('sokokeextra3', (a, 1), f'sokokeextra{i}', sprites_y=2)
for a, i in enumerate(['COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH' , 'SCARLET']):
    sprites.make_group('sokoke3', (a, 2), f'sokoke{i}')
    sprites.make_group('sokokeextra3', (a, 2), f'sokokeextra{i}', sprites_y=2)
# agouti
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('agouticolours', (a, 0), f'agouti{i}')
    sprites.make_group('agoutiextra', (a, 0), f'agoutiextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('agouticolours', (a, 1), f'agouti{i}')
    sprites.make_group('agoutiextra', (a, 1), f'agoutiextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK']):
    sprites.make_group('agouticolours', (a, 2), f'agouti{i}')
    sprites.make_group('agoutiextra', (a, 2), f'agoutiextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'CLOUD', 'BLUE2', 'HAZE', 'DARKBLUE', 'SOOT']):
    sprites.make_group('agouticolours2', (a, 0), f'agouti{i}')
    sprites.make_group('agoutiextra2', (a, 0), f'agoutiextra{i}', sprites_y=2)
for a, i in enumerate(['IVORY', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON']):
    sprites.make_group('agouticolours2', (a, 1), f'agouti{i}')
    sprites.make_group('agoutiextra2', (a, 1), f'agoutiextra{i}', sprites_y=2)
for a, i in enumerate(['COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH' , 'SCARLET']):
    sprites.make_group('agouticolours2', (a, 2), f'agouti{i}')
    sprites.make_group('agoutiextra2', (a, 2), f'agoutiextra{i}', sprites_y=2)
# singlestripe
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('singlestripecolours', (a, 0), f'singlestripe{i}')
    sprites.make_group('singlestripeextra', (a, 0), f'singlestripeextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('singlestripecolours', (a, 1), f'singlestripe{i}')
    sprites.make_group('singlestripeextra', (a, 1), f'singlestripeextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK']):
    sprites.make_group('singlestripecolours', (a, 2), f'singlestripe{i}')
    sprites.make_group('singlestripeextra', (a, 2), f'singlestripeextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'CLOUD', 'BLUE2', 'HAZE', 'DARKBLUE', 'SOOT']):
    sprites.make_group('singlestripe2', (a, 0), f'singlestripe{i}')
    sprites.make_group('singlestripeextra2', (a, 0), f'singlestripeextra{i}', sprites_y=2)
for a, i in enumerate(['IVORY', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON']):
    sprites.make_group('singlestripe2', (a, 1), f'singlestripe{i}')
    sprites.make_group('singlestripeextra2', (a, 1), f'singlestripeextra{i}', sprites_y=2)
for a, i in enumerate(['COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH' , 'SCARLET']):
    sprites.make_group('singlestripe2', (a, 2), f'singlestripe{i}')
    sprites.make_group('singlestripeextra2', (a, 2), f'singlestripeextra{i}', sprites_y=2)
# new pelts
#merle
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('merle', (a, 0), f'merle{i}')
    sprites.make_group('merleextra', (a, 0), f'merleextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('merle', (a, 1), f'merle{i}')
    sprites.make_group('merleextra', (a, 1), f'merleextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('merle', (a, 2), f'merle{i}')
    sprites.make_group('merleextra', (a, 2), f'merleextra{i}', sprites_y=2)
#snowflake
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('snowflake', (a, 0), f'snowflake{i}')
    sprites.make_group('snowflakeextra', (a, 0), f'snowflakeextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('snowflake', (a, 1), f'snowflake{i}')
    sprites.make_group('snowflakeextra', (a, 1), f'snowflakeextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('snowflake', (a, 2), f'snowflake{i}')
    sprites.make_group('snowflakeextra', (a, 2), f'snowflakeextra{i}', sprites_y=2)
#ghost
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('ghosttabby', (a, 0), f'ghost{i}')
    sprites.make_group('ghosttabbyextra', (a, 0), f'ghostextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('ghosttabby', (a, 1), f'ghost{i}')
    sprites.make_group('ghosttabbyextra', (a, 1), f'ghostextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('ghosttabby', (a, 2), f'ghost{i}')
    sprites.make_group('ghosttabbyextra', (a, 2), f'ghostextra{i}', sprites_y=2)
#pinstripe
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('pinstripetabby', (a, 0), f'pinstripe{i}')
    sprites.make_group('pinstripetabbyextra', (a, 0), f'pinstripeextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('pinstripetabby', (a, 1), f'pinstripe{i}')
    sprites.make_group('pinstripetabbyextra', (a, 1), f'pinstripeextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('pinstripetabby', (a, 2), f'pinstripe{i}')
    sprites.make_group('pinstripetabbyextra', (a, 2), f'pinstripeextra{i}', sprites_y=2)
#cloudy marbled
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('cloudy', (a, 0), f'cloudy{i}')
    sprites.make_group('cloudyextra', (a, 0), f'cloudyextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('cloudy', (a, 1), f'cloudy{i}')
    sprites.make_group('mackerelextra', (a, 1), f'cloudyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('cloudy', (a, 2), f'cloudy{i}')
    sprites.make_group('cloudyextra', (a, 2), f'cloudyextra{i}', sprites_y=2)
#colorpoints
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('points', (a, 0), f'points{i}')
    sprites.make_group('pointsextra', (a, 0), f'pointsextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('points', (a, 1), f'points{i}')
    sprites.make_group('pointsextra', (a, 1), f'pointsextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('points', (a, 2), f'points{i}')
    sprites.make_group('pointsextra', (a, 2), f'pointsextra{i}', sprites_y=2)
#realistic tabbies
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('rtabby', (a, 0), f'rtabby{i}')
    sprites.make_group('rtabbyextra', (a, 0), f'rtabbyextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('rtabby', (a, 1), f'rtabby{i}')
    sprites.make_group('rtabbyextra', (a, 1), f'rtabbyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('rtabby', (a, 2), f'rtabby{i}')
    sprites.make_group('rtabbyextra', (a, 2), f'rtabbyextra{i}', sprites_y=2)
#ragdolls
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('ragdolls', (a, 0), f'ragdolls{i}')
    sprites.make_group('ragdollsextra', (a, 0), f'ragdollsextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('ragdolls', (a, 1), f'ragdolls{i}')
    sprites.make_group('ragdollsextra', (a, 1), f'ragdollsextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('ragdolls', (a, 2), f'ragdolls{i}')
    sprites.make_group('ragdollsextra', (a, 2), f'ragdollsextra{i}', sprites_y=2)
#shaded tabby
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('shadedtabby', (a, 0), f'shaded{i}')
    sprites.make_group('shadedextra', (a, 0), f'shadedextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('shadedtabby', (a, 1), f'shaded{i}')
    sprites.make_group('shadedextra', (a, 1), f'shadedextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('shadedtabby', (a, 2), f'shaded{i}')
    sprites.make_group('shadedextra', (a, 2), f'shadedextra{i}', sprites_y=2)
#realistic singles
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('rsinglecolours', (a, 0), f'rsingle{i}')
    sprites.make_group('rsingleextra', (a, 0), f'rsingleextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('rsinglecolours', (a, 1), f'rsingle{i}')
    sprites.make_group('rsingleextra', (a, 1), f'rsingleextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('rsinglecolours', (a, 2), f'rsingle{i}')
    sprites.make_group('rsingleextra', (a, 2), f'rsingleextra{i}', sprites_y=2)
# abyssinian
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST']):
    sprites.make_group('abyssinian', (a, 0), f'abyssinian{i}')
    sprites.make_group('abyssinianextra', (a, 0), f'abyssinianextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('abyssinian', (a, 1), f'abyssinian{i}')
    sprites.make_group('abyssinianextra', (a, 1), f'abyssinianextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('abyssinian', (a, 2), f'abyssinian{i}')
    sprites.make_group('abyssinianextra', (a, 2), f'abyssinianextra{i}', sprites_y=2)
# spiral sokoke
for a, i in enumerate(['WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK']):
    sprites.make_group('sokoke2', (a, 0), f'spiral{i}')
    sprites.make_group('sokoke2extra', (a, 0), f'spiralextra{i}', sprites_y=2)
for a, i in enumerate(['PALE', 'CREAM2', 'APRICOT', 'ORANGE']):
    sprites.make_group('sokoke2', (a, 1), f'spiral{i}')
    sprites.make_group('sokoke2extra', (a, 1), f'spiralextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN', 'CINNAMON', 'CHOCOLATE']):
    sprites.make_group('sokoke2', (a, 2), f'spiral{i}')
    sprites.make_group('sokoke2extra', (a, 2), f'spiralextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'CLOUD', 'BLUE2', 'HAZE', 'DARKBLUE', 'SOOT']):
    sprites.make_group('moresokoke', (a, 0), f'spiral{i}')
    sprites.make_group('moresokokeextra', (a, 0), f'spiralextra{i}', sprites_y=2)
for a, i in enumerate(['IVORY', 'SAND', 'SUNBURST', 'RUSSET', 'BONE', 'LEMON']):
    sprites.make_group('moresokoke', (a, 1), f'spiral{i}')
    sprites.make_group('moresokokeextra', (a, 1), f'spiralextra{i}', sprites_y=2)
for a, i in enumerate(['COFFEE', 'MARSH', 'OAK', 'RUBY', 'PEACH', 'SCARLET']):
    sprites.make_group('moresokoke', (a, 2), f'spiral{i}')
    sprites.make_group('moresokokeextra', (a, 2), f'spiralextra{i}', sprites_y=2)

# new torties
# solids
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 0), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 0), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 1), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 1), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 2), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 2), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 3), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 3), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 4), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 4), f'tortiesolidextra{i}', sprites_y=2)
# tabby
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecolourstabby', (a, 0), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby', (a, 0), f'tortietabbyextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecolourstabby', (a, 1), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby', (a, 1), f'tortietabbyextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecolourstabby', (a, 2), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby', (a, 2), f'tortietabbyextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecolourstabby', (a, 3), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby', (a, 3), f'tortietabbyextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecolourstabby', (a, 4), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby', (a, 4), f'tortietabbyextra{i}', sprites_y=2)
# bengal
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursbengal', (a, 0), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal', (a, 0), f'tortiebengalextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursbengal', (a, 1), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal', (a, 1), f'tortiebengalextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursbengal', (a, 2), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal', (a, 2), f'tortiebengalextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursbengal', (a, 3), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal', (a, 3), f'tortiebengalextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursbengal', (a, 4), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal', (a, 4), f'tortiebengalextra{i}', sprites_y=2)
# marbled
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 0), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 0), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 1), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 1), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 2), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 2), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 3), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 3), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 4), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 4), f'tortiemarbledextra{i}', sprites_y=2)
# ticked
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 0), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 0), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 1), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 1), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 2), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 2), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 3), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 3), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 4), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 4), f'tortietickedextra{i}', sprites_y=2)
# smoke
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecolourssmoke', (a, 0), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke', (a, 0), f'tortiesmokeextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecolourssmoke', (a, 1), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke', (a, 1), f'tortiesmokeextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecolourssmoke', (a, 2), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke', (a, 2), f'tortiesmokeextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecolourssmoke', (a, 3), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke', (a, 3), f'tortiesmokeextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecolourssmoke', (a, 4), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke', (a, 4), f'tortiesmokeextra{i}', sprites_y=2)
# rosette
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursrosette', (a, 0), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette', (a, 0), f'tortierosetteextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursrosette', (a, 1), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette', (a, 1), f'tortierosetteextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursrosette', (a, 2), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette', (a, 2), f'tortierosetteextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursrosette', (a, 3), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette', (a, 3), f'tortierosetteextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursrosette', (a, 4), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette', (a, 4), f'tortierosetteextra{i}', sprites_y=2)
# speckled
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursspeckled', (a, 0), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled', (a, 0), f'tortiespeckledextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursspeckled', (a, 1), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled', (a, 1), f'tortiespeckledextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursspeckled', (a, 2), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled', (a, 2), f'tortiespeckledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursspeckled', (a, 3), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled', (a, 3), f'tortiespeckledextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursspeckled', (a, 4), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled', (a, 4), f'tortiespeckledextra{i}', sprites_y=2)
# mackerel
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursmackerel', (a, 0), f'tortiemackerel{i}')
    sprites.make_group('tortiesextramackerel', (a, 0), f'tortiemackerelextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursmackerel', (a, 1), f'tortiemackerel{i}')
    sprites.make_group('tortiesextramackerel', (a, 1), f'tortiemackerelextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursmackerel', (a, 2), f'tortiemackerel{i}')
    sprites.make_group('tortiesextramackerel', (a, 2), f'tortiemackerelextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursmackerel', (a, 3), f'tortiemackerel{i}')
    sprites.make_group('tortiesextramackerel', (a, 3), f'tortiemackerelextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursmackerel', (a, 4), f'tortiemackerel{i}')
    sprites.make_group('tortiesextramackerel', (a, 4), f'tortiemackerelextra{i}', sprites_y=2)
# classic
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursclassic', (a, 0), f'tortieclassic{i}')
    sprites.make_group('tortiesextraclassic', (a, 0), f'tortieclassicextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursclassic', (a, 1), f'tortieclassic{i}')
    sprites.make_group('tortiesextraclassic', (a, 1), f'tortieclassicextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursclassic', (a, 2), f'tortieclassic{i}')
    sprites.make_group('tortiesextraclassic', (a, 2), f'tortieclassicextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursclassic', (a, 3), f'tortieclassic{i}')
    sprites.make_group('tortiesextraclassic', (a, 3), f'tortieclassicextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursclassic', (a, 4), f'tortieclassic{i}')
    sprites.make_group('tortiesextraclassic', (a, 4), f'tortieclassicextra{i}', sprites_y=2)
# sokoke
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecolourssokoke', (a, 0), f'tortiesokoke{i}')
    sprites.make_group('tortiesextrasokoke', (a, 0), f'tortiesokokeextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecolourssokoke', (a, 1), f'tortiesokoke{i}')
    sprites.make_group('tortiesextrasokoke', (a, 1), f'tortiesokokeextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecolourssokoke', (a, 2), f'tortiesokoke{i}')
    sprites.make_group('tortiesextrasokoke', (a, 2), f'tortiesokokeextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecolourssokoke', (a, 3), f'tortiesokoke{i}')
    sprites.make_group('tortiesextrasokoke', (a, 3), f'tortiesokokeextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecolourssokoke', (a, 4), f'tortiesokoke{i}')
    sprites.make_group('tortiesextrasokoke', (a, 4), f'tortiesokokeextra{i}', sprites_y=2)
# agouti
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursagouti', (a, 0), f'tortieagouti{i}')
    sprites.make_group('tortiesextraagouti', (a, 0), f'tortieagoutiextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursagouti', (a, 1), f'tortieagouti{i}')
    sprites.make_group('tortiesextraagouti', (a, 1), f'tortieagoutiextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursagouti', (a, 2), f'tortieagouti{i}')
    sprites.make_group('tortiesextraagouti', (a, 2), f'tortieagoutiextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursagouti', (a, 3), f'tortieagouti{i}')
    sprites.make_group('tortiesextraagouti', (a, 3), f'tortieagoutiextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursagouti', (a, 4), f'tortieagouti{i}')
    sprites.make_group('tortiesextraagouti', (a, 4), f'tortieagoutiextra{i}', sprites_y=2)
# new torties
# rsolid
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursrsolid', (a, 0), f'tortiersolid{i}')
    sprites.make_group('tortieextrarsolid', (a, 0), f'tortiersolidextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursrsolid', (a, 1), f'tortiersolid{i}')
    sprites.make_group('tortieextrarsolid', (a, 1), f'tortiersolidextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursrsolid', (a, 2), f'tortiersolid{i}')
    sprites.make_group('tortieextrarsolid', (a, 2), f'tortiersolidextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursrsolid', (a, 3), f'tortiersolid{i}')
    sprites.make_group('tortieextrarsolid', (a, 3), f'tortiersolidextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursrsolid', (a, 4), f'tortiersolid{i}')
    sprites.make_group('tortieextrarsolid', (a, 4), f'tortiersolidextra{i}', sprites_y=2)
# rtabby
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursrtabby', (a, 0), f'tortiertabby{i}')
    sprites.make_group('tortieextrartabby', (a, 0), f'tortiertabbyextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursrtabby', (a, 1), f'tortiertabby{i}')
    sprites.make_group('tortieextrartabby', (a, 1), f'tortiertabbyextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursrtabby', (a, 2), f'tortiertabby{i}')
    sprites.make_group('tortieextrartabby', (a, 2), f'tortiertabbyextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursrtabby', (a, 3), f'tortiertabby{i}')
    sprites.make_group('tortieextrartabby', (a, 3), f'tortiertabbyextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursrtabby', (a, 4), f'tortiertabby{i}')
    sprites.make_group('tortieextrartabby', (a, 4), f'tortiertabbyextra{i}', sprites_y=2)
# brindle
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiebrindle', (a, 0), f'tortiebrindle{i}')
    sprites.make_group('tortiebrindleextra', (a, 0), f'tortiebrindleextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiebrindle', (a, 1), f'tortiebrindle{i}')
    sprites.make_group('tortiebrindleextra', (a, 1), f'tortiebrindleextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiebrindle', (a, 2), f'tortiebrindle{i}')
    sprites.make_group('tortiebrindleextra', (a, 2), f'tortiebrindleextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiebrindle', (a, 3), f'tortiebrindle{i}')
    sprites.make_group('tortiebrindleextra', (a, 3), f'tortiebrindleextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiebrindle', (a, 4), f'tortiebrindle{i}')
    sprites.make_group('tortiebrindleextra', (a, 4), f'tortiebrindleextra{i}', sprites_y=2)
# ghost
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortieghost', (a, 0), f'tortieghost{i}')
    sprites.make_group('tortieghostextra', (a, 0), f'tortieghostextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortieghost', (a, 1), f'tortieghost{i}')
    sprites.make_group('tortieghostextra', (a, 1), f'tortieghostextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortieghost', (a, 2), f'tortieghost{i}')
    sprites.make_group('tortieghostextra', (a, 2), f'tortieghostextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortieghost', (a, 3), f'tortieghost{i}')
    sprites.make_group('tortieghostextra', (a, 3), f'tortieghostextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortieghost', (a, 4), f'tortieghost{i}')
    sprites.make_group('tortieghostextra', (a, 4), f'tortieghostextra{i}', sprites_y=2)
# pinstripe
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiepinstripe', (a, 0), f'tortiepinstripe{i}')
    sprites.make_group('tortiepinstripeextra', (a, 0), f'tortiepinstripeextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiepinstripe', (a, 1), f'tortiepinstripe{i}')
    sprites.make_group('tortiepinstripeextra', (a, 1), f'tortiepinstripeextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiepinstripe', (a, 2), f'tortiepinstripe{i}')
    sprites.make_group('tortiepinstripeextra', (a, 2), f'tortiepinstripeextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiepinstripe', (a, 3), f'tortiepinstripe{i}')
    sprites.make_group('tortiepinstripeextra', (a, 3), f'tortiepinstripeextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiepinstripe', (a, 4), f'tortiepinstripe{i}')
    sprites.make_group('tortiepinstripeextra', (a, 4), f'tortiepinstripeextra{i}', sprites_y=2)
# snowflake
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiesnowflake', (a, 0), f'tortiesnowflake{i}')
    sprites.make_group('tortiesnowflakeextra', (a, 0), f'tortiesnowflakeextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiesnowflake', (a, 1), f'tortiesnowflake{i}')
    sprites.make_group('tortiesnowflakeextra', (a, 1), f'tortiesnowflakeextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiesnowflake', (a, 2), f'tortiesnowflake{i}')
    sprites.make_group('tortiesnowflakeextra', (a, 2), f'tortiesnowflakeextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiesnowflake', (a, 3), f'tortiesnowflake{i}')
    sprites.make_group('tortiesnowflakeextra', (a, 3), f'tortiesnowflakeextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiesnowflake', (a, 4), f'tortiesnowflake{i}')
    sprites.make_group('tortiesnowflakeextra', (a, 4), f'tortiesnowflakeextra{i}', sprites_y=2)
# merle
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiemerle', (a, 0), f'tortiemerle{i}')
    sprites.make_group('tortiemerleextra', (a, 0), f'tortiemerleextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiemerle', (a, 1), f'tortiemerle{i}')
    sprites.make_group('tortiemerleextra', (a, 1), f'tortiemerleextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiemerle', (a, 2), f'tortiemerle{i}')
    sprites.make_group('tortiemerleextra', (a, 2), f'tortiemerleextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiemerle', (a, 3), f'tortiemerle{i}')
    sprites.make_group('tortiemerleextra', (a, 3), f'tortiemerleextra{i}', sprites_y=2)
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiemerle', (a, 4), f'tortiemerle{i}')
    sprites.make_group('tortiemerleextra', (a, 4), f'tortiemerleextra{i}', sprites_y=2)


# SKINS
sprites.make_group('skin', (0, 0), 'skinBLACK')
sprites.make_group('skin', (1, 0), 'skinRED')
sprites.make_group('skin', (2, 0), 'skinPINK')
sprites.make_group('skin', (3, 0), 'skinDARKBROWN')
sprites.make_group('skin', (4, 0), 'skinBROWN')
sprites.make_group('skin', (5, 0), 'skinLIGHTBROWN')
sprites.make_group('skin', (0, 1), 'skinDARK')
sprites.make_group('skin', (1, 1), 'skinDARKGREY')
sprites.make_group('skin', (2, 1), 'skinGREY')
sprites.make_group('skin', (3, 1), 'skinDARKSALMON')
sprites.make_group('skin', (4, 1), 'skinSALMON')
sprites.make_group('skin', (5, 1), 'skinPEACH')
sprites.make_group('skin', (0, 2), 'skinDARKMARBLED')
sprites.make_group('skin', (1, 2), 'skinMARBLED')
sprites.make_group('skin', (2, 2), 'skinLIGHTMARBLED')
sprites.make_group('skin', (3, 2), 'skinDARKBLUE')
sprites.make_group('skin', (4, 2), 'skinBLUE')
sprites.make_group('skin', (5, 2), 'skinLIGHTBLUE')
sprites.make_group('skinparalyzed', (0, 0),
                   'skinparalyzedPINK',
                   sprites_x=1,
                   sprites_y=1)
sprites.make_group('skinparalyzed', (1, 0),
                   'skinparalyzedRED',
                   sprites_x=1,
                   sprites_y=1)
sprites.make_group('skinparalyzed', (2, 0),
                   'skinparalyzedBLACK',
                   sprites_x=1,
                   sprites_y=1)

sprites.make_group('skinextra', (0, 0), 'skinextraBLACK', sprites_y=2)
sprites.make_group('skinextra', (1, 0), 'skinextraRED', sprites_y=2)
sprites.make_group('skinextra', (2, 0), 'skinextraPINK', sprites_y=2)
sprites.make_group('skinextra', (3, 0), 'skinextraDARKBROWN', sprites_y=2)
sprites.make_group('skinextra', (4, 0), 'skinextraBROWN', sprites_y=2)
sprites.make_group('skinextra', (5, 0), 'skinextraLIGHTBROWN', sprites_y=2)
sprites.make_group('skinextra', (0, 1), 'skinextraDARK', sprites_y=2)
sprites.make_group('skinextra', (1, 1), 'skinextraDARKGREY', sprites_y=2)
sprites.make_group('skinextra', (2, 1), 'skinextraGREY', sprites_y=2)
sprites.make_group('skinextra', (3, 1), 'skinextraDARKSALMON', sprites_y=2)
sprites.make_group('skinextra', (4, 1), 'skinextraSALMON', sprites_y=2)
sprites.make_group('skinextra', (5, 1), 'skinextraPEACH', sprites_y=2)
sprites.make_group('skinextra', (0, 2), 'skinextraDARKMARBLED', sprites_y=2)
sprites.make_group('skinextra', (1, 2), 'skinextraMARBLED', sprites_y=2)
sprites.make_group('skinextra', (2, 2), 'skinextraLIGHTMARBLED', sprites_y=2)
sprites.make_group('skinextra', (3, 2), 'skinextraDARKBLUE', sprites_y=2)
sprites.make_group('skinextra', (4, 2), 'skinextraBLUE', sprites_y=2)
sprites.make_group('skinextra', (5, 2), 'skinextraLIGHTBLUE', sprites_y=2)

# tiles.make_group('dithered', (0, 0), 'terrain')
# tiles.make_group('dithered', (1, 0), 'terraintwo')

sprites.load_scars()
