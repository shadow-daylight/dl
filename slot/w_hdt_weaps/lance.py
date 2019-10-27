from slot import *

class Crimsonflame_Lance(WeaponBase):
    ele = 'flame'
    wt = 'lance'
    att = 780
    s3 = {} # Crimson Beacon
    a = [('k', 0.3)]
    ability_desc = {"(Flame) High Midgardsormr's Bane +30%": "If the user is attuned to [[Elements|Flame]]:  increases damage to High Midgardsormr by '''30%'''."}

class Pureflame_Lance(WeaponBase):
    ele = 'flame'
    wt = 'lance'
    att = 1560
    s3 = {} # Crimson Wildfire
    a = []
    ability_desc = {}

class Limpid_Lance(WeaponBase):
    ele = 'water'
    wt = 'lance'
    att = 780
    s3 = {} # Limpid Petals
    a = [('k', 0.3)]
    ability_desc = {"(Water) High Brunhilda's Bane +30%": "If the user is attuned to [[Elements|Water]]:  increases damage to High Brunhilda by '''30%'''."}

class Limpid_Rush(WeaponBase):
    ele = 'water'
    wt = 'lance'
    att = 1560
    s3 = {} # Limpid Shore
    a = []
    ability_desc = {}

class Promising_Breeze(WeaponBase):
    ele = 'wind'
    wt = 'lance'
    att = 757
    s3 = {} # Sworn Gale
    a = [('k', 0.3)]
    ability_desc = {"(Wind) High Mercury's Bane +30% (Alt)": "If the user is attuned to [[Elements|Wind]]:  increases damage to High Mercury by '''30%'''."}

class Guiding_Gale(WeaponBase):
    ele = 'wind'
    wt = 'lance'
    att = 1515
    s3 = {} # Glorious Gale
    a = []
    ability_desc = {}

class Lightflash(WeaponBase):
    ele = 'light'
    wt = 'lance'
    att = 780
    s3 = {} # Flashing Thunder
    a = [('k', 0.3)]
    ability_desc = {"(Light) High Zodiark's Bane +30% (Alt)": "If the user is attuned to [[Elements|Light]]:  increases damage to High Zodiark by '''30%'''."}

class Brilliant_Lightflash(WeaponBase):
    ele = 'light'
    wt = 'lance'
    att = 1560
    s3 = {} # Brilliant Thunder
    a = []
    ability_desc = {}

class Scourge_Lance(WeaponBase):
    ele = 'shadow'
    wt = 'lance'
    att = 719
    s3 = {} # Hazy Hex
    a = [('k', 0.3)]
    ability_desc = {"(Shadow) High Jupiter's Bane +30% (Alt)": "If the user is attuned to [[Elements|Shadow]]:  increases damage to High Jupiter by '''30%'''."}

class Ebon_Scourge_Lance(WeaponBase):
    ele = 'shadow'
    wt = 'lance'
    att = 1439
    s3 = {} # Shadowy Hex
    a = []
    ability_desc = {}


flame = Pureflame_Lance
water = Limpid_Rush
wind = Guiding_Gale
light = Brilliant_Lightflash
shadow = Ebon_Scourge_Lance