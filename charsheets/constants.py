from enum import StrEnum, auto


#############################################################################
class CharSpecies(StrEnum):
    AASIMAR = auto()
    DRAGONBORN = auto()
    DWARF = auto()
    ELF = auto()
    GNOME = auto()
    GOLIATH = auto()
    HALFLING = auto()
    HUMAN = auto()
    ORC = auto()
    TIEFLING = auto()


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
    BARBARIAN = auto()
    BARD = auto()
    CLERIC = auto()
    DRUID = auto()
    FIGHTER = auto()
    MONK = auto()
    PALADIN = auto()
    RANGER = auto()
    ROGUE = auto()
    SORCERER = auto()
    WARLOCK = auto()
    WIZARD = auto()


#############################################################################
class CharSubclassName(StrEnum):
    CIRCLE_OF_THE_LAND = auto()
    CIRCLE_OF_THE_MOON = auto()
    CIRCLE_OF_THE_SEA = auto()
    CIRCLE_OF_THE_STARS = auto()
    HUNTER = auto()
    NONE = auto()
    PATH_OF_THE_BESERKER = auto()


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
    ARTISAN = auto()
    GUARD = auto()
    NOBLE = auto()


#############################################################################
class Ability(StrEnum):
    COLOSSUS_SLAYER = auto()
    DANGER_SENSE = auto()
    DARKVISION60 = auto()
    DARKVISION120 = auto()
    DRUIDIC = auto()
    DEFT_EXPLORER = auto()
    DWARVEN_RESILIANCE = auto()
    DWARVEN_TOUGHNESS = auto()
    FAVOURED_ENEMY = auto()
    FIGHTING_STYLE = auto()
    FRENZY = auto()
    HUNTERS_LORE = auto()
    HUNTERS_PREY = auto()
    PRIMAL_KNOWLEDGE = auto()
    PRIMAL_ORDER = auto()
    RAGE = auto()
    RECKLESS_ATTACK = auto()
    RESOURCEFUL = auto()
    SKILLFUL = auto()
    STONE_CUNNING = auto()
    UNARMORED_DEFENSE = auto()
    WEAPON_MASTERY = auto()
    WILD_COMPANION = auto()
    WILD_SHAPE = auto()


#############################################################################
class Feat(StrEnum):
    ALERT = auto()
    CRAFTER = auto()
    HEALER = auto()
    LUCKY = auto()
    MAGIC_INITIATE = auto()
    MUSICIAN = auto()
    SAVAGE_ATTACKER = auto()
    SKILLED = auto()
    TAVERN_BRAWLER = auto()
    TOUGH = auto()

    ABILITY_SCORE_IMPROVEMENT = auto()
    ACTOR = auto()
    ATHLETE = auto()
    CHARGER = auto()
    CHEF = auto()
    CROSSBOW_EXPERT = auto()
    CRUSHER = auto()
    DEFENSIVE_DUELIST = auto()
    DUAL_WIELDER = auto()
    DURABLE = auto()
    ELEMENTAL_ADEPT = auto()
    FEY_TOUCHED = auto()
    GRAPPLER = auto()
    GREAT_WEAPON_MASTER = auto()
    HEAVILY_ARMORED = auto()
    HEAVY_ARMOR_MASTER = auto()
    INSPIRING_LEADER = auto()
    KEEN_MIND = auto()
    LIGHTLY_ARMORED = auto()
    MAGE_SLAYER = auto()
    MARTIAL_WEAPON_TRAINING = auto()
    MEDIUM_ARMOR_MASTER = auto()
    MODERATELY_ARMORED = auto()
    MOUNTED_COMBATANT = auto()
    OBSERVANT = auto()
    PIERCER = auto()
    POISONER = auto()
    POLEARM_MASTER = auto()
    RESILIENT = auto()
    RITUAL_CASTER = auto()
    SENTINEL = auto()
    SHADOW_TOUCHED = auto()
    SHARPSHOOTER = auto()
    SHIELD_MASTER = auto()
    SKILL_EXPERT = auto()
    SKULKER = auto()
    SLASHER = auto()
    SPEEDY = auto()
    SPELL_SNIPER = auto()
    TELEKINETIC = auto()
    TELEPATHIC = auto()
    WAR_CASTER = auto()
    WEAPON_MASTER = auto()

    ARCHERY = auto()


#############################################################################
class Proficiencies(StrEnum):
    SIMPLE_WEAPONS = auto()
    MARTIAL_WEAPONS = auto()
    LIGHT_ARMOUR = auto()
    MEDIUM_ARMOUR = auto()
    SHIELDS = auto()


# EOF
