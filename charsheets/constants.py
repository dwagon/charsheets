from typing import TypeAlias

from aenum import StrEnum, auto


#############################################################################
class Mod(StrEnum):
    MOD_AC_BONUS = "mod_ac_bonus"
    MOD_ADD_ATTACK = "mod_add_attack"
    MOD_ADD_DAMAGE_RESISTANCES = "mod_add_damage_resistances"
    MOD_ADD_KNOWN_SPELLS = "mod_add_known_spells"
    MOD_ADD_LANGUAGE = "mod_add_language"
    MOD_ADD_MOVEMENT_SPEED = "mod_add_movement_speed"
    MOD_ADD_PREPARED_SPELLS = "mod_add_prepared_spells"
    MOD_ADD_SENSE = "mod_add_sense"
    MOD_ADD_SKILL_EXPERTISE = "mod_add_skill_expertise"
    MOD_ADD_SKILL_PROFICIENCY = "mod_add_skill_proficiency"
    MOD_ADD_TOOL_PROFICIENCY = "mod_add_tool_proficiency"
    MOD_ARMOUR_PROFICIENCY = "mod_armour_proficiency"
    MOD_DESC = "mod_desc"
    MOD_DMG_DICE = "mod_dmg_dice"
    MOD_DMG_TYPE = "mod_dmg_type"
    MOD_EXTRA_ATTACK = "mod_extra_attack"
    MOD_FLY_MOVEMENT = "mod_fly_movement"
    MOD_HP_BONUS = "mod_hp_bonus"
    MOD_INITIATIVE_BONUS = "mod_initiative_bonus"
    MOD_MELEE_ATK_BONUS = "mod_melee_atk_bonus"
    MOD_MELEE_DMG_BONUS = "mod_melee_dmg_bonus"
    MOD_RANGED_ATK_BONUS = "mod_ranged_atk_bonus"
    MOD_RANGED_DMG_BONUS = "mod_ranged_dmg_bonus"
    MOD_SET_MOVEMENT_SPEED = "mod_set_movement_speed"
    MOD_SPECIFIC_WEAPON_PROFICIENCY = "mod_specific_weapon_proficiency"
    MOD_STAT_CHA = "mod_stat_cha"
    MOD_STAT_CHA_SET = "mod_stat_cha_set"
    MOD_STAT_CON = "mod_stat_con"
    MOD_STAT_CON_SET = "mod_stat_con_set"
    MOD_STAT_DEX = "mod_stat_dex"
    MOD_STAT_DEX_SET = "mod_stat_dex_set"
    MOD_STAT_INT = "mod_stat_int"
    MOD_STAT_INT_SET = "mod_stat_int_set"
    MOD_STAT_STR = "mod_stat_str"
    MOD_STAT_STR_SET = "mod_stat_str_set"
    MOD_STAT_WIS = "mod_stat_wis"
    MOD_STAT_WIS_SET = "mod_stat_wis_set"
    MOD_SWIM_MOVEMENT = "mod_swim_movement"
    MOD_WEAPON_PROFICIENCY = "mod_weapon_proficiency"


#############################################################################
class CharacterClass(StrEnum):
    BARBARIAN = auto()
    BARD = auto()
    CLERIC = auto()
    DRUID = auto()
    FIGHTER = auto()
    MONK = auto()
    NONE = auto()
    PALADIN = auto()
    RANGER = auto()
    ROGUE = auto()
    SORCERER = auto()
    WARLOCK = auto()
    WIZARD = auto()


#############################################################################
class Recovery(StrEnum):
    NONE = auto()
    SHORT_REST = auto()
    LONG_REST = auto()
    PARTIAL = auto()  # 1/SR all/LR


#############################################################################
class Sense(StrEnum):
    NORMAL = "Normal"
    DARKVISION60 = "Darkvision 60'"
    DARKVISION120 = "Darkvision 120'"
    BLINDSIGHT = "Blindsight"
    BLINDSIGHT10 = "Blindsight 10'"
    TREMORSENSE = "Tremorsense"
    TRUESIGHT = "Truesight"


#############################################################################
class Language(StrEnum):
    ABYSSAL = auto()
    AQUAN = auto()
    CELESTIAL = auto()
    COMMON = auto()
    DEEP_SPEECH = "Deep Speech"
    DRACONIC = auto()
    DRUIDIC = auto()
    DWARVISH = auto()
    ELVISH = auto()
    GIANT = auto()
    GNOMISH = auto()
    GOBLIN = auto()
    HALFLING = auto()
    INFERNAL = auto()
    ORC = auto()
    PRIMORDIAL = auto()
    SYLVAN = auto()
    THIEVES_CANT = "Thieves' Cant"
    UNDERCOMMON = auto()


#############################################################################
class Tool(StrEnum):
    NONE = auto()

    ARTISAN_TOOLS = "Artisan Tools"
    ALCHEMISTS_SUPPLIES = "Alchemist's Supplies"
    BREWERS_SUPPLIES = "Brewer's Supplies"
    CALLIGRAPHERS_SUPPLIES = "Calligrapher's Supplies"
    CARPENTERS_TOOLS = "Carpenter's Tools"
    CARTOGRAPHERS_TOOLS = "Cartographer's Tools"
    COBBLERS_TOOLS = "Cobbler's Tools"
    COOKS_UTENSILS = "Cook's Utensils"
    GLASSBLOWERS_TOOLS = "Glassblower's Tools"
    JEWELERS_TOOLS = "Jeweler's Tools"
    LEATHERWORKERS_TOOLS = "Leatherworker's Tools"
    MASONS_TOOLS = "Mason's Tools"
    PAINTERS_SUPPLIES = "Painter's Supplies"
    POTTERS_TOOLS = "Potter's Tools"
    SMITHS_TOOLS = "Smith's Tools"
    TINKERS_TOOLS = "Tinker's Tools"
    WEAVERS_TOOLS = "Weaver's Tools"
    WOODCARVERS_TOOLS = "Woodcarver's Tools"

    OTHER_TOOLS = "Other Tools"
    DISGUISE_KIT = "Disguise Kit"
    FORGERY_KIT = "Forgery Kit"
    GAMING_SET = "Gaming Set"
    HERBALISM_KIT = "Herbalism Kit"
    MUSICAL_INSTRUMENT = "Musical Instrument"
    NAVIGATORS_TOOLS = "Navigator's Tools"
    POISONERS_KIT = "Poisoner's Kit"
    THIEVES_TOOLS = "Thieves' Tools"

    VEHICLES_LAND = "Vehicles (Land)"
    VEHICLES_SEA = "Vehicles (Sea)"


ARTISAN_TOOLS = {
    Tool.ALCHEMISTS_SUPPLIES,
    Tool.BREWERS_SUPPLIES,
    Tool.CALLIGRAPHERS_SUPPLIES,
    Tool.CARPENTERS_TOOLS,
    Tool.CARTOGRAPHERS_TOOLS,
    Tool.COBBLERS_TOOLS,
    Tool.COOKS_UTENSILS,
    Tool.GLASSBLOWERS_TOOLS,
    Tool.JEWELERS_TOOLS,
    Tool.LEATHERWORKERS_TOOLS,
    Tool.MASONS_TOOLS,
    Tool.PAINTERS_SUPPLIES,
    Tool.POTTERS_TOOLS,
    Tool.SMITHS_TOOLS,
    Tool.TINKERS_TOOLS,
    Tool.WEAVERS_TOOLS,
    Tool.WOODCARVERS_TOOLS,
}


#############################################################################
class Stat(StrEnum):
    STRENGTH = auto()
    DEXTERITY = auto()
    CONSTITUTION = auto()
    INTELLIGENCE = auto()
    WISDOM = auto()
    CHARISMA = auto()


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


SKILL_STAT_MAP: dict[Skill, Stat] = {
    Skill.ACROBATICS: Stat.DEXTERITY,
    Skill.ANIMAL_HANDLING: Stat.WISDOM,
    Skill.ARCANA: Stat.INTELLIGENCE,
    Skill.ATHLETICS: Stat.STRENGTH,
    Skill.DECEPTION: Stat.CHARISMA,
    Skill.HISTORY: Stat.INTELLIGENCE,
    Skill.INSIGHT: Stat.WISDOM,
    Skill.INTIMIDATION: Stat.CHARISMA,
    Skill.INVESTIGATION: Stat.INTELLIGENCE,
    Skill.MEDICINE: Stat.WISDOM,
    Skill.NATURE: Stat.INTELLIGENCE,
    Skill.PERCEPTION: Stat.WISDOM,
    Skill.PERFORMANCE: Stat.CHARISMA,
    Skill.PERSUASION: Stat.CHARISMA,
    Skill.RELIGION: Stat.INTELLIGENCE,
    Skill.SLEIGHT_OF_HAND: Stat.DEXTERITY,
    Skill.STEALTH: Stat.DEXTERITY,
    Skill.SURVIVAL: Stat.WISDOM,
}


#############################################################################
class Armour(StrEnum):
    NONE = auto()
    BREASTPLATE = auto()
    CHAIN_MAIL = auto()
    CHAIN_SHIRT = auto()
    HALFPLATE = auto()
    HIDE = auto()
    LEATHER = auto()
    PADDED = auto()
    PLATE = auto()
    RING_MAIL = auto()
    SCALE = auto()
    SHIELD = auto()
    SPLINT = auto()
    STUDDED = auto()


#############################################################################
class DamageType(StrEnum):
    ACID = auto()
    BLUDGEONING = auto()
    COLD = auto()
    FIRE = auto()
    FORCE = auto()
    LIGHTNING = auto()
    NECROTIC = auto()
    NONE = auto()
    PIERCING = auto()
    POISON = auto()
    PSYCHIC = auto()
    RADIANT = auto()
    SLASHING = auto()
    THUNDER = auto()


#############################################################################
class ArmourCategory(StrEnum):
    HEAVY = auto()
    LIGHT = auto()
    MEDIUM = auto()
    NONE = auto()
    SHIELD = auto()


#############################################################################
class WeaponCategory(StrEnum):
    SIMPLE_RANGED = auto()
    SIMPLE_MELEE = auto()
    MARTIAL_MELEE = auto()
    MARTIAL_RANGED = auto()


#############################################################################
class WeaponMasteryProperty(StrEnum):
    CLEAVE = auto()
    GRAZE = auto()
    NICK = auto()
    PUSH = auto()
    SAP = auto()
    SLOW = auto()
    TOPPLE = auto()
    VEX = auto()


#############################################################################
class Weapon(StrEnum):
    BATTLEAXE = auto()
    BLOWGUN = auto()
    CLUB = auto()
    DAGGER = auto()
    DART = auto()
    FLAIL = auto()
    GLAIVE = auto()
    GREATAXE = auto()
    GREATCLUB = auto()
    GREATSWORD = auto()
    HALBERD = auto()
    HANDAXE = auto()
    HAND_CROSSBOW = "Hand Crossbow"
    HEAVY_CROSSBOW = "Heavy Crossbow"
    JAVELIN = auto()
    LANCE = auto()
    LIGHT_CROSSBOW = "Light Crossbow"
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
    SHORTSWORD = auto()
    SICKLE = auto()
    SLING = auto()
    SPEAR = auto()
    TEST = auto()  # For testing only
    TRIDENT = auto()
    UNARMED = auto()
    WARHAMMER = auto()
    WAR_PICK = auto()
    WHIP = auto()


#############################################################################
class WeaponProperty(StrEnum):
    AMMUNITION = auto()
    FINESSE = auto()
    HEAVY = auto()
    LIGHT = auto()
    LOADING = auto()
    RANGE = auto()
    REACH = auto()
    THROWN = auto()
    TWO_HANDED = auto()
    VERSATILE = auto()


#############################################################################
class Origin(StrEnum):
    NONE = auto()
    ACOLYTE = auto()
    ARTISAN = auto()
    CHARLATAN = auto()
    CRIMINAL = auto()
    ENTERTAINER = auto()
    FARMER = auto()
    GUARD = auto()
    GUIDE = auto()
    HERMIT = auto()
    MERCHANT = auto()
    NOBLE = auto()
    SAGE = auto()
    SAILOR = auto()
    SCRIBE = auto()
    SOLDIER = auto()
    WAYFARER = auto()


#############################################################################
class Background(StrEnum):
    NONE = auto()
    ACOLYTE = auto()
    CHARLATAN = auto()
    CRIMINAL = auto()
    ENTERTAINER = auto()
    FOLK_HERO = auto()
    GUILD_ARTISAN = auto()
    HERMIT = auto()
    NOBLE = auto()
    OUTLANDER = auto()
    SAGE = auto()
    SAILOR = auto()
    SOLDIER = auto()
    URCHIN = auto()


#############################################################################
# These get defined where the code is rather than centrally.
class Feature(StrEnum):
    NONE = auto()


#############################################################################
class Proficiency(StrEnum):
    SIMPLE_WEAPONS = "Simple Weapons"
    MARTIAL_WEAPONS = "Martial Weapons"
    LIGHT_ARMOUR = "Light Armour"
    MEDIUM_ARMOUR = "Medium Armour"
    HEAVY_ARMOUR = "Heavy Armour"
    SHIELDS = "Shields"


#############################################################################
ProficiencyType: TypeAlias = Tool | Skill


#############################################################################
class SpellNotes(StrEnum):
    STAT = auto()


# EOF
