from enum import StrEnum, auto


#############################################################################
class Species(StrEnum):
    HUMAN = auto()


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


#############################################################################
class Armour(StrEnum):
    SHIELD = auto()
    LEATHER = auto()


#############################################################################
class WeaponType(StrEnum):
    CLUB = auto()
    LONGBOW = auto()
    SHORT_SWORD = auto()


#############################################################################
class Feat(StrEnum):
    ALERT = auto()
    ARCHERY = auto()
    HEALER = auto()


# EOF
