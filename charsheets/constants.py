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
    MOD_ADD_SKILL_PROFICIENCY = "mod_add_skill_proficiency"
    MOD_ADD_SKILL_EXPERTISE = "mod_add_skill_expertise"
    MOD_ADD_TOOL_PROFICIENCY = "mod_add_tool_proficiency"
    MOD_ARMOUR_PROFICIENCY = "mod_armour_proficiency"
    MOD_EXTRA_ATTACK = "mod_extra_attack"
    MOD_HP_BONUS = "mod_hp_bonus"
    MOD_INITIATIVE_BONUS = "mod_initiative_bonus"
    MOD_SET_MOVEMENT_SPEED = "mod_set_movement_speed"
    MOD_STAT_CHA = "mod_stat_cha"
    MOD_STAT_CON = "mod_stat_con"
    MOD_STAT_DEX = "mod_stat_dex"
    MOD_STAT_INT = "mod_stat_int"
    MOD_STAT_STR = "mod_stat_str"
    MOD_STAT_WIS = "mod_stat_wis"
    MOD_WEAPON_PROFICIENCY = "mod_weapon_proficiency"


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
class Feature(StrEnum):
    ABERRANT_SORCERY = auto()
    ABILITY_SCORE_IMPROVEMENT = auto()
    ABJURATION_SAVANT = auto()
    ABJURE_FOES = auto()
    ACROBATIC_MOVEMENT = auto()
    ACTOR = auto()
    ADRENALIN_RUSH = auto()
    ALERT = auto()
    ARCANE_RECOVERY = auto()
    ARCANE_WARD = auto()
    ARCHERY = auto()
    ASSASSINATE = auto()
    ASSASSINS_TOOLS = auto()
    ATHLETE = auto()
    AURA_OF_ALACRITY = auto()
    AURA_OF_COURAGE = auto()
    AURA_OF_DEVOTION = auto()
    AURA_OF_PROTECTION = auto()
    AURA_OF_WARDING = auto()
    BASTION_OF_LAW = auto()
    BEGUILING_TWIST = auto()
    BEND_LUCK = auto()
    BESTIAL_FURY = auto()
    BLIND_FIGHTING = auto()
    BRAVE = auto()
    BREATH_WEAPON = auto()
    CELESTIAL_RESISTANCE = auto()
    CELESTIAL_REVELATION = auto()
    CHANNEL_DIVINITY_PALADIN = "Channel Divinity"
    CHARGER = auto()
    CHEF = auto()
    CLOCKWORK_SPELLS = auto()
    COLOSSUS_SLAYER = auto()
    CRAFTER = auto()
    CROSSBOW_EXPERT = auto()
    CRUSHER = auto()
    CUNNING_ACTION = auto()
    CUNNING_STRIKE = auto()
    DARKVISION120 = auto()
    DARKVISION60 = auto()
    DEFENSE = auto()
    DEFENSIVE_DUELIST = auto()
    DEFENSIVE_TACTICS = auto()
    DEFLECT_ATTACKS = auto()
    DEFT_EXPLORER = auto()
    DIVINATION_SAVANT = auto()
    DRACONIC_DAMAGE_RESISTANCE = auto()
    DRACONIC_FLIGHT = auto()
    DRACONIC_RESILIENCE = auto()
    DREADFUL_STRIKES = auto()
    DREAD_AMBUSHER = auto()
    DRUIDIC_WARRIOR = auto()
    DUAL_WIELDER = auto()
    DUELING = auto()
    DURABLE = auto()
    DWARVEN_RESILIENCE = auto()
    DWARVEN_TOUGHNESS = auto()
    ELEMENTAL_ADEPT = auto()
    ELEMENTAL_AFFINITY = auto()
    ELEMENTAL_ATTUNEMENT = auto()
    ELEMENTAL_BURST = auto()
    EMPOWERED_EVOCATION = auto()
    EMPOWERED_STRIKES = auto()
    EVASION = auto()
    EVOCATION_SAVANT = auto()
    EXCEPTIONAL_TRAINING = auto()
    EXPERTISE = auto()
    EXPERT_DIVINATION = auto()
    EXTRA_ATTACK = auto()
    FAITHFUL_STEED = auto()
    FAST_HANDS = auto()
    FAVOURED_ENEMY = auto()
    FEYWILD_GIFTS = auto()
    FEY_ANCESTRY = auto()
    FEY_REINFORCEMENTS = auto()
    FEY_TOUCHED = auto()
    FEY_WANDERER_SPELLS = auto()
    FIENDISH_LEGACY = auto()
    FIGHTING_STYLE_PALADIN = "Fighting Style"
    FIGHTING_STYLE_RANGER = "Fighting Style"
    FLEET_STEP = auto()
    FLURRY_OF_HEALING_AND_HARD = auto()
    FONT_OF_MAGIC = auto()
    GIANT_ANCESTRY = auto()
    GIANT_CLOUDS_JAUNT = "Cloud’s Jaunt"
    GIANT_FIRES_BURN = "Fire’s Burn"
    GIANT_FROSTS_CHILL = "Frost's Chill"
    GIANT_HILLS_TUMBLE = "Hill’s Tumble"
    GIANT_STONES_ENDURANCE = "Stone's Endurance"
    GIANT_STORMS_THUNDER = "Storm's Thunder"
    GNOMISH_CUNNING = auto()
    GNOMISH_LINEAGE = auto()
    GRAPPLER = auto()
    GREAT_WEAPON_FIGHTING = auto()
    GREAT_WEAPON_MASTER = auto()
    HALFLING_NIMBLENESS = auto()
    HAND_OF_HARM = auto()
    HAND_OF_HEALING = auto()
    HEALER = auto()
    HEALING_HANDS = auto()
    HEAVILY_ARMORED = auto()
    HEAVY_ARMOR_MASTER = auto()
    HIGHTENED_FOCUS = auto()
    HUNTERS_LORE = auto()
    HUNTERS_PREY = auto()
    ILLUSION_SAVANT = auto()
    ILLUSORY_SELF = auto()
    IMPLEMENTS_OF_MERCY = auto()
    IMPROVED_CUNNING_STRIKE = auto()
    IMPROVED_SHADOW_STEP = auto()
    IMPROVED_ILLUSIONS = auto()
    INFILTRATION_EXPERTISE = auto()
    INNATE_SORCERY = auto()
    INSPIRING_LEADER = auto()
    INSPIRING_SMITE = auto()
    INTERCEPTION = auto()
    IRON_MIND = auto()
    KEEN_MIND = auto()
    KEEN_SENSES = auto()
    LAY_ON_HANDS = auto()
    LIGHTLY_ARMORED = auto()
    LIGHT_BEARER = auto()
    LUCK = auto()
    LUCKY = auto()
    MAGE_HAND_LEGERDERMAIN = auto()
    MAGE_SLAYER = auto()
    MAGICAL_AMBUSH = auto()
    MAGIC_INITIATE_CLERIC = "Magic Initiate (Cleric)"
    MAGIC_INITIATE_DRUID = "Magic Initiate (Druid)"
    MAGIC_INITIATE_WIZARD = "Magic Initiate (Wizard)"
    MANIPULATE_ELEMENTS = auto()
    MARTIAL_ARTS = auto()
    MARTIAL_WEAPON_TRAINING = auto()
    MEDIUM_ARMOR_MASTER = auto()
    MEMORIZE_SPELL = auto()
    METAMAGIC = auto()
    MODERATELY_ARMORED = auto()
    MONKS_FOCUS = auto()
    MOUNTED_COMBATANT = auto()
    MUSICIAN = auto()
    NATURALLY_STEALTHY = auto()
    NATURES_WRATH = auto()
    NONE = auto()
    OBSERVANT = auto()
    OPEN_HAND_TECHNIQUE = auto()
    OTHERWORLDLY_GLAMOUR = auto()
    OTHERWORLDLY_PRESENCE = auto()
    PALADINS_SMITE = auto()
    PEERLESS_ATHLETE = auto()
    PHANTASMAL_CREATURES = auto()
    PHYSICIANS_TOUCH = auto()
    PIERCER = auto()
    POISONER = auto()
    POLEARM_MASTER = auto()
    PORTENT = auto()
    POTENT_CANTRIP = auto()
    PRIMAL_COMPANION = auto()
    PROJECTED_WARD = auto()
    PROTECTION = auto()
    PSIONIC_POWER_ROGUE = auto()
    PSIONIC_SORCERY = auto()
    PSYCHIC_BLADES = auto()
    PSYCHIC_DEFENSES = auto()
    RADIANT_STRIKES = auto()
    RELENTLESS_AVENGER = auto()
    RELENTLESS_ENDURANCE = auto()
    RELIABLE_TALENT = auto()
    RESILIENT = auto()
    RESOURCEFUL = auto()
    RESTORE_BALANCE = auto()
    RITUAL_ADEPT = auto()
    RITUAL_CASTER = auto()
    ROVING = auto()
    SACRED_WEAPON = auto()
    SAVAGE_ATTACKER = auto()
    SCHOLAR = auto()
    SCULPT_SPELLS = auto()
    SECOND_STORY_WORK = auto()
    SELF_RESTORATION = auto()
    SENTINEL = auto()
    SHADOW_ARTS = auto()
    SHADOW_STEP = auto()
    SHADOW_TOUCHED = auto()
    SHARPSHOOTER = auto()
    SHIELD_MASTER = auto()
    SKILLED = auto()
    SKILLFUL = auto()
    SKILL_EXPERT = auto()
    SKULKER = auto()
    SLASHER = auto()
    SLOW_FALL = auto()
    SNEAK_ATTACK = auto()
    SORCEROUS_RESTORATION = auto()
    SORCERY_INCARNATE = auto()
    SOUL_BLADES = auto()
    SPEEDY = auto()
    SPELL_BREAKER = auto()
    SPELL_SNIPER = auto()
    STALKERS_FLURRY = auto()
    STEADY_AIM = auto()
    STONE_CUNNING = auto()
    STRIDE_OF_THE_ELEMENTS = auto()
    STUNNING_STRIKE = auto()
    SUPERIOR_HUNTERS_PREY = auto()
    SUPREME_SNEAK = auto()
    TAVERN_BRAWLER = auto()
    TELEKINETIC = auto()
    TELEPATHIC = auto()
    TELEPATHIC_SPEECH = auto()
    THE_THIRD_EYE = auto()
    THIEVES_CANT = "Thieves' Cant"
    THROWN_WEAPON_FIGHTING = auto()
    TIDES_OF_CHAOS = auto()
    TIRELESS = auto()
    TOUGH = auto()
    TRANCE = auto()
    TWO_EXTRA_ATTACKS = auto()
    TWO_WEAPON_FIGHTING = auto()
    UMBRAL_SIGHT = auto()
    UNARMED_FIGHTING = auto()
    UNARMORED_DEFENSE_MONK = "Unarmored Defense"
    UNARMORED_MOVEMENT = auto()
    UNCANNY_DODGE = auto()
    UNCANNY_METABOLISM = auto()
    VERSATILE = auto()
    VOW_OF_EMNITY = auto()
    WAR_CASTER = auto()
    WEAPON_MASTER = auto()
    WEAPON_MASTERY = auto()
    WHOLENESS_OF_BODY = auto()
    WILD_MAGIC_SURGE = auto()


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

# EOF
