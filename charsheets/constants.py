from typing import TypeAlias

from aenum import StrEnum, auto


#############################################################################
class Mod(StrEnum):
    MOD_ADD_ATTACK = "mod_add_attack"
    MOD_ADD_DAMAGE_RESISTANCES = "mod_add_damage_resistances"
    MOD_ADD_KNOWN_SPELLS = "mod_add_known_spells"
    MOD_ADD_LANGUAGE = "mod_add_language"
    MOD_ADD_MOVEMENT_SPEED = "mod_add_movement_speed"
    MOD_ADD_PREPARED_SPELLS = "mod_add_prepared_spells"
    MOD_ADD_SENSE = "mod_add_sense"
    MOD_ADD_SKILL_PROFICIENCY = "mod_add_skill_proficiency"
    MOD_ADD_TOOL_PROFICIENCY = "mod_add_tool_proficiency"
    MOD_ARMOUR_PROFICIENCY = "mod_armour_proficiency"
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
class Sense(StrEnum):
    NORMAL = "Normal"
    DARKVISION60 = "Darkvision 60'"
    DARKVISION120 = "Darkvision 120'"
    BLINDSIGHT = "Blindsight"
    TREMORSENSE = "Tremorsense"
    TRUESIGHT = "Truesight"


#############################################################################
class Language(StrEnum):
    ABYSSAL = auto()
    CELESTIAL = auto()
    COMMON = auto()
    DEEP_SPEECH = auto()
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
    THIEVES_CANT = auto()
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
class Ability(StrEnum):
    ABERRANT_SORCERY = auto()
    ABILITY_SCORE_IMPROVEMENT = auto()
    ABJURATION_SAVANT = auto()
    ACTION_SURGE = auto()
    ADRENALIN_RUSH = auto()
    ANIMAL_SPEAKER = auto()
    AQUATIC_AFFINITY = auto()
    ARCANE_RECOVERY = auto()
    ARCANE_WARD = auto()
    ASPECTS_OF_THE_WILDS = auto()
    ASSASSINATE = auto()
    ASSASSINS_TOOLS = auto()
    AURA_OF_PROTECTION = auto()
    BASTION_OF_LAW = auto()
    BEND_LUCK = auto()
    BLESSED_HEALER = auto()
    BLESSING_OF_THE_TRICKSTER = auto()
    BRANCHES_OF_THE_TREE = auto()
    BRAVE = auto()
    BREATH_WEAPON = auto()
    CELESTIAL_RESISTANCE = auto()
    CELESTIAL_REVELATION = auto()
    CHANNEL_DIVINITY = auto()
    CIRCLE_FORMS = auto()
    CLAIRVOYANT_COMBATANT = auto()
    CLOCKWORK_SPELLS = auto()
    COLOSSUS_SLAYER = auto()
    COMBAT_SUPERIORITY = auto()
    COSMIC_OMEN = auto()
    CUNNING_ACTION = auto()
    CUNNING_STRIKE = auto()
    DANGER_SENSE = auto()
    DARKVISION120 = auto()
    DARKVISION60 = auto()
    DARK_ONES_BLESSING = auto()
    DARK_ONES_OWN_LUCK = auto()
    DEFLECT_ATTACKS = auto()
    DEFT_EXPLORER = auto()
    DISCIPLE_OF_LIFE = auto()
    DIVINATION_SAVANT = auto()
    DIVINE_FURY = auto()
    DIVINE_ORDER_PROTECTOR = auto()
    DIVINE_ORDER_THAUMATURGE = auto()
    DRACONIC_DAMAGE_RESISTANCE = auto()
    DRACONIC_FLIGHT = auto()
    DRACONIC_RESILIENCE = auto()
    DREADFUL_STRIKES = auto()
    DREAD_AMBUSHER = auto()
    DRUIDIC = auto()
    DWARVEN_RESILIENCE = auto()
    DWARVEN_TOUGHNESS = auto()
    ELDRITCH_INVOCATIONS = auto()
    ELEMENTAL_AFFINITY = auto()
    ELEMENTAL_ATTUNEMENT = auto()
    ELEMENTAL_BURST = auto()
    EMPOWERED_STRIKES = auto()
    EVOCATION_SAVANT = auto()
    EXPERTISE = auto()
    EXPERT_DIVINATION = auto()
    EXTRA_ATTACK = auto()
    FAITHFUL_STEED = auto()
    FANATICAL_FOCUS = auto()
    FAST_HANDS = auto()
    FAST_MOVEMENT = auto()
    FAVOURED_ENEMY = auto()
    FEYWILD_GIFTS = auto()
    FEY_ANCESTRY = auto()
    FEY_WANDERER_SPELLS = auto()
    FIENDISH_LEGACY = auto()
    FIGHTING_STYLE = auto()
    FONT_OF_MAGIC = auto()
    FRENZY = auto()
    GIANT_ANCESTRY = auto()
    GIANT_CLOUDS_JAUNT = "Cloud’s Jaunt"
    GIANT_FIRES_BURN = "Fire’s Burn"
    GIANT_FROSTS_CHILL = "Frost's Chill"
    GIANT_HILLS_TUMBLE = "Hill’s Tumble"
    GIANT_STONES_ENDURANCE = "Stone's Endurance"
    GIANT_STORMS_THUNDER = "Storm's Thunder"
    GNOMISH_CUNNING = auto()
    GNOMISH_LINEAGE = auto()
    GUIDED_STRIKE = auto()
    HALFLING_NIMBLENESS = auto()
    HAND_OF_HARM = auto()
    HAND_OF_HEALING = auto()
    HEALING_HANDS = auto()
    HEALING_LIGHT = auto()
    HUNTERS_LORE = auto()
    HUNTERS_PREY = auto()
    ILLUSION_SAVANT = auto()
    IMPLEMENTS_OF_MERCY = auto()
    IMPROVED_CIRCLE_FORMS = auto()
    IMPROVED_CRITICAL = auto()
    IMPROVED_ILLUSIONS = auto()
    IMPROVED_WARDING_FLARE = auto()
    INNATE_SORCERY = auto()
    INSPIRING_SMITE = auto()
    INVOKE_DUPLICITY = auto()
    KEEN_SENSES = auto()
    LANDS_AID = auto()
    LAND_SPELL_ARID = auto()
    LAND_SPELL_POLAR = auto()
    LAND_SPELL_TEMPERATE = auto()
    LAND_SPELL_TROPICAL = auto()
    LAY_ON_HANDS = auto()
    LIFE_DOMAIN_SPELLS = auto()
    LIGHT_BEARER = auto()
    LIGHT_DOMAIN_SPELLS = auto()
    LUCK = auto()
    MAGE_HAND_LEGERDERMAIN = auto()
    MAGICAL_CUNNING = auto()
    MAGICIAN = auto()
    MANIPULATE_ELEMENTS = auto()
    MARTIAL_ARTS = auto()
    MEMORIZE_SPELL = auto()
    METAMAGIC = auto()
    MINDLESS_RAGE = auto()
    MISTY_ESCAPE = auto()
    MONKS_FOCUS = auto()
    NATURALLY_STEALTHY = auto()
    NATURAL_RECOVERY = auto()
    NATURES_WRATH = auto()
    NONE = auto()
    OPEN_HAND_TECHNIQUE = auto()
    OTHERWORLDLY_GLAMOUR = auto()
    OTHERWORLDLY_PRESENCE = auto()
    PACT_MAGIC = auto()
    PALADINS_SMITE = auto()
    PEERLESS_ATHLETE = auto()
    PHANTASMAL_CREATURES = auto()
    PHYSICIANS_TOUCH = auto()
    PORTENT = auto()
    POTENT_CANTRIP = auto()
    PRESERVE_LIFE = auto()
    PRIMAL_COMPANION = auto()
    PRIMAL_KNOWLEDGE = auto()
    PROJECTED_WARD = auto()
    PSIONIC_POWER_FIGHTER = auto()
    PSIONIC_POWER_ROGUE = auto()
    PSIONIC_SORCERY = auto()
    PSYCHIC_BLADES = auto()
    PSYCHIC_DEFENSES = auto()
    PSYCHIC_SPELLS = auto()
    RADIANCE_OF_THE_DAWN = auto()
    SCULPT_SPELLS = auto()
    RADIANT_SOUL = auto()
    RAGE = auto()
    RAGE_OF_THE_WILDS = auto()
    RECKLESS_ATTACK = auto()
    RELENTLESS_ENDURANCE = auto()
    REMARKABLE_ATHLETE = auto()
    RESOURCEFUL = auto()
    RESTORE_BALANCE = auto()
    RITUAL_ADEPT = auto()
    ROVING = auto()
    SACRED_WEAPON = auto()
    SCHOLAR = auto()
    SEAR_UNDEAD = auto()
    SECOND_STORY_WORK = auto()
    SECOND_WIND = auto()
    SHADOW_ARTS = auto()
    SHADOW_STEP = auto()
    SKILLFUL = auto()
    SLOW_FALL = auto()
    SNEAK_ATTACK = auto()
    SORCEROUS_RESTORATION = auto()
    STARRY_FORM = auto()
    STAR_MAP = auto()
    STEADY_AIM = auto()
    STEPS_OF_THE_FEY = auto()
    STONE_CUNNING = auto()
    STUDENT_OF_WAR = auto()
    STUNNING_STRIKE = auto()
    TACTICAL_MIND = auto()
    TACTICAL_SHIFT = auto()
    TELEPATHIC_SPEECH = auto()
    THIEVES_CANT = auto()
    TIDES_OF_CHAOS = auto()
    TRANCE = auto()
    TRICKERY_DOMAIN_SPELLS = auto()
    TRICKSTERS_TRANSPOSITION = auto()
    UMBRAL_SIGHT = auto()
    UNARMORED_DEFENSE_BARBARIAN = "Unarmored Defense"
    UNARMORED_DEFENSE_MONK = "Unarmored Defense"
    UNARMORED_MOVEMENT = auto()
    UNCANNY_DODGE = auto()
    UNCANNY_METABOLISM = auto()
    VITALITY_OF_THE_TREE = auto()
    VOW_OF_EMNITY = auto()
    WARDEN = auto()
    WARDING_FLARE = auto()
    WARRIOR_OF_THE_GODS = auto()
    WAR_BOND = auto()
    WAR_DOMAIN_SPELLS = auto()
    WAR_GODS_BLESSING = auto()
    WAR_PRIEST = auto()
    WEAPON_MASTERY = auto()
    WHOLENESS_OF_BODY = auto()
    WILD_COMPANION = auto()
    WILD_MAGIC_SURGE = auto()
    WILD_RESURGENCE = auto()
    WILD_SHAPE = auto()
    WRATH_OF_THE_SEA = auto()


#############################################################################
class Feat(StrEnum):
    NONE = auto()
    ALERT = auto()
    CRAFTER = auto()
    HEALER = auto()
    LUCKY = auto()
    MAGIC_INITIATE_CLERIC = auto()
    MAGIC_INITIATE_DRUID = auto()
    MAGIC_INITIATE_WIZARD = auto()
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
    BLIND_FIGHTING = auto()
    DEFENSE = auto()
    DUELING = auto()
    GREAT_WEAPON_FIGHTING = auto()
    INTERCEPTION = auto()
    PROTECTION = auto()
    THROWN_WEAPON_FIGHTING = auto()
    TWO_WEAPON_FIGHTING = auto()
    UNARMED_FIGHTING = auto()


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
