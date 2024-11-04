from enum import StrEnum, auto


#############################################################################
class Species(StrEnum):
    HUMAN = auto()
    DWARF = auto()


#############################################################################
class Skill(StrEnum):
    ACROBATICS = auto()
    ANIMAL_HANDLING = auto()
    ARCANA = auto()
    ATHLETICS = auto()
    DECEPTION = auto()
    HISTORY = auto()
    INSIGHT = auto()
    INTIMIDATION = auto()
    INVESTIGATION = auto()
    MEDICINE = auto()
    NATURE = auto()
    PERCEPTION = auto()
    PERFORMANCE = auto()
    PERSUASION = auto()
    RELIGION = auto()
    SLEIGHT_OF_HAND = auto()
    STEALTH = auto()
    SURVIVAL = auto()


#############################################################################
class Stat(StrEnum):
    STRENGTH = auto()
    DEXTERITY = auto()
    CONSTITUTION = auto()
    INTELLIGENCE = auto()
    WISDOM = auto()
    CHARISMA = auto()


#############################################################################
class CharClassName(StrEnum):
    RANGER = auto()
    BARBARIAN = auto()


#############################################################################
class CharSubclassName(StrEnum):
    HUNTER = auto()
    PATH_OF_THE_BESERKER = auto()
    NONE = auto()


#############################################################################
class Armour(StrEnum):
    BREASTPLATE = auto()
    CHAIN = auto()
    HALFPLATE = auto()
    HIDE = auto()
    LEATHER = auto()
    PADDED = auto()
    PLATE = auto()
    RING = auto()
    SCALE = auto()
    SHIELD = auto()
    SPLINT = auto()
    STUDDED = auto()


#############################################################################
class WeaponType(StrEnum):
    BATTLEAXE = auto()
    BLOWGUN = auto()
    CLUB = auto()
    DAGGER = auto()
    DART = auto()
    FLAIL = auto()
    GLAIVE = auto()
    GREATAXE = auto()
    GREATCLUB = auto()
    HALBERD = auto()
    HANDAXE = auto()
    HAND_CROSSBOW = auto()
    HEAVY_CROSSBOW = auto()
    JAVELIN = auto()
    LANCE = auto()
    LIGHT_CROSSBOW = auto()
    LIGHT_HAMMER = auto()
    LONGBOW = auto()
    LONGSWORD = auto()
    MACE = auto()
    MAUL = auto()
    MORNINGSTAR = auto()
    MUSKET = auto()
    PIKE = auto()
    PISTOL = auto()
    QUARTERSTAFF = auto()
    RAPIER = auto()
    SCIMITAR = auto()
    SHORTBOW = auto()
    SHORT_SWORD = auto()
    SICKLE = auto()
    SLING = auto()
    SPEAR = auto()
    TRIDENT = auto()
    UNARMED = auto()
    WARHAMMER = auto()
    WAR_PICK = auto()
    WHIP = auto()


#############################################################################
class Origin(StrEnum):
    GUARD = auto()
    ARTISAN = auto()


#############################################################################
class Ability(StrEnum):
    DEFT_EXPLORER = auto()
    HUNTERS_LORE = auto()
    HUNTERS_PREY = auto()
    COLOSSUS_SLAYER = auto()
    DARKVISION = auto()
    DWARVEN_TOUGHNESS = auto()
    DWARVEN_RESILIANCE = auto()
    DANGER_SENSE = auto()
    FRENZY = auto()
    STONE_CUNNING = auto()
    UNARMORED_DEFENSE = auto()
    RECKLESS_ATTACK = auto()
    WEAPON_MASTERY = auto()
    FAVOURED_ENEMY = auto()
    FIGHTING_STYLE = auto()


#############################################################################
class Feat(StrEnum):
    ALERT = auto()
    ARCHERY = auto()
    HEALER = auto()
    CRAFTER = auto()


#############################################################################
class Proficiencies(StrEnum):
    SIMPLE_WEAPONS = auto()
    MARTIAL_WEAPONS = auto()
    LIGHT_ARMOUR = auto()
    MEDIUM_ARMOUR = auto()
    SHIELDS = auto()


# EOF
