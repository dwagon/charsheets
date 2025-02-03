""" Spells"""

from enum import StrEnum, Flag, auto
from typing import NamedTuple

from charsheets.exception import NotDefined


#######################################################################
class SpellFlag(Flag):
    CONCENTRATION = auto()
    MATERIAL = auto()
    NONE = auto()
    RITUAL = auto()


#######################################################################
class SpellSchool(StrEnum):
    ABJURATION = auto()
    CONJURATION = auto()
    DIVINATION = auto()
    ENCHANTMENT = auto()
    EVOCATION = auto()
    ILLUSION = auto()
    NECROMANCY = auto()
    NONE = auto()
    TRANSMUTATION = auto()


#######################################################################
class SDT(NamedTuple):
    """Spell Details Type"""

    level: int
    school: SpellSchool
    flags: SpellFlag


#######################################################################
class Spell(StrEnum):
    """All the Spells"""

    # Cantrips
    ACID_SPLASH = auto()
    BLADE_WARD = auto()
    CHILL_TOUCH = auto()
    DRUIDCRAFT = auto()
    ELDRITCH_BLAST = auto()
    ELEMENTALISM = auto()
    FIRE_BOLT = auto()
    FRIENDS = auto()
    GUIDANCE = auto()
    LIGHT = auto()
    MAGE_HAND = auto()
    MENDING = auto()
    MESSAGE = auto()
    MIND_SLIVER = auto()
    MINOR_ILLUSION = auto()
    POISON_SPRAY = auto()
    PRESTIGITATION = auto()
    PRODUCE_FLAME = auto()
    RAY_OF_FROST = auto()
    RESISTANCE = auto()
    SACRED_FLAME = auto()
    SHILLELAGH = auto()
    SHOCKING_GRASP = auto()
    SOURCEROUS_BURST = auto()
    SPARE_THE_DYING = "Spare the Dying"
    STARRY_WISP = auto()
    THAUMATURGY = auto()
    THORN_WHIP = auto()
    THUNDERCLAP = auto()
    TOLL_THE_DEAD = auto()
    TRUE_STRIKE = auto()
    VICIOUS_MOKERY = auto()
    WORD_OF_RADIANCE = auto()

    # Level 1
    ALARM = auto()
    ANIMAL_FRIENDSHIP = auto()
    ARMOR_OF_AGATHYS = auto()
    ARMS_OF_HADAR = auto()
    BANE = auto()
    BLESS = auto()
    BURNING_HANDS = auto()
    CHARM_PERSON = auto()
    CHROMATIC_ORB = auto()
    COLOR_SPRAY = auto()
    COMMAND = auto()
    COMPELLED_DUEL = auto()
    COMPREHEND_LANGUAGES = auto()
    CREATE_OR_DESTROY_WATER = auto()
    CURE_WOUNDS = auto()
    DANCING_LIGHTS = auto()
    DETECT_EVIL_AND_GOOD = auto()
    DETECT_MAGIC = auto()
    DETECT_POISON_AND_DISEASE = auto()
    DISGUISE_SELF = auto()
    DISSONANT_WHISPERS = auto()
    DIVINE_FAVOR = auto()
    DIVINE_SMITE = auto()
    ENSNARING_STRIKE = auto()
    ENTANGLE = auto()
    EXPEDITIOUS_RETREAT = auto()
    FAERIE_FIRE = auto()
    FALSE_LIFE = auto()
    FEATHER_FALL = auto()
    FIND_FAMILIAR = auto()
    FOG_CLOUD = auto()
    GOODBERRY = auto()
    GREASE = auto()
    GUIDING_BOLT = auto()
    HAIL_OF_THORNS = auto()
    HEALING_WORD = auto()
    HELLISH_REBUKE = auto()
    HEROISM = auto()
    HEX = auto()
    HUNTERS_MARK = auto()
    ICE_KNIFE = auto()
    IDENTIFY = auto()
    ILLUSORY_SCRIPT = auto()
    INFLICT_WOUNDS = auto()
    JUMP = auto()
    LONGSTRIDER = auto()
    MAGE_ARMOR = auto()
    MAGIC_MISSILE = auto()
    PROTECTION_FROM_EVIL_AND_GOOD = auto()
    PURIFY_FOOD_AND_DRINK = auto()
    RAY_OF_SICKNESS = auto()
    SANCTUARY = auto()
    SEARING_SMITE = auto()
    SHIELD = auto()
    SHIELD_OF_FAITH = auto()
    SILENT_IMAGE = auto()
    SLEEP = auto()
    SPEAK_WITH_ANIMALS = "Speak with Animals"
    TASHAS_HIDEOUS_LAUGHTER = auto()
    TENSERS_FLOATING_DISK = auto()
    THUNDEROUS_SMITE = auto()
    THUNDERWAVE = auto()
    UNSEEN_SERVANT = auto()
    WITCH_BOLT = auto()
    WRATHFUL_SMITE = auto()

    # Level 2
    AID = auto()
    ALTER_SELF = auto()
    ANIMAL_MESSENGER = auto()
    ARCANE_LOCK = auto()
    ARCANE_VIGOR = auto()
    AUGURY = auto()
    BARKSKIN = auto()
    BEAST_SENSE = auto()
    BLINDNESS_DEAFNESS = auto()
    BLUR = auto()
    CALM_EMOTIONS = auto()
    CLOUD_OF_DAGGERS = auto()
    CONTINUAL_FLAME = auto()
    CORDON_OF_ARROWS = auto()
    CROWN_OF_MADNESS = auto()
    DARKNESS = auto()
    DARKVISION = auto()
    DETECT_THOUGHTS = auto()
    DRAGONS_BREATH = auto()
    ENHANCE_ABILITY = auto()
    ENLARGE_REDUCE = auto()
    ENTHRALL = auto()
    FIND_STEED = auto()
    FIND_TRAPS = auto()
    FLAME_BLADE = auto()
    FLAMING_SPHERE = auto()
    GENTLE_REPOSE = auto()
    GUST_OF_WIND = auto()
    HEAT_METAL = auto()
    HOLD_PERSON = auto()
    INVISIBILITY = auto()
    KNOCK = auto()
    LESSER_RESTORATION = auto()
    LEVITATE = auto()
    LOCATE_ANIMALS_OR_PLANTS = auto()
    LOCATE_OBJECT = auto()
    MAGIC_MOUTH = auto()
    MAGIC_WEAPON = auto()
    MELFS_ACID_ARROW = auto()
    MIND_SPIKE = auto()
    MIRROR_IMAGE = auto()
    MISTY_STEP = auto()
    MOONBEAM = auto()
    NYSTULS_MAGIC_AURA = auto()
    PASS_WITHOUT_TRACE = auto()
    PHANTASMAL_FORCE = auto()
    PRAYER_OF_HEALING = auto()
    PROTECTION_FROM_POISON = auto()
    RAY_OF_ENFEEBLEMENT = auto()
    ROPE_TRICK = auto()
    SCORCHING_RAY = auto()
    SEE_INVISIBILITY = auto()
    SHATTER = auto()
    SHINING_SMITE = auto()
    SILENCE = auto()
    SPIDER_CLIMB = auto()
    SPIKE_GROWTH = auto()
    SPIRITUAL_WEAPON = auto()
    SUGGESTION = auto()
    SUMMON_BEAST = auto()
    WARDING_BOND = auto()
    WEB = auto()
    ZONE_OF_TRUTH = auto()

    # Level 3
    ANIMATE_DEAD = auto()
    AURA_OF_VITALITY = auto()
    BEACON_OF_HOPE = auto()
    BESTOW_CURSE = auto()
    BLINDING_SMITE = auto()
    BLINK = auto()
    CALL_LIGHTNING = auto()
    CLAIRVOYANCE = auto()
    CONJURE_ANIMALS = auto()
    CONJURE_BARRAGE = auto()
    COUNTERSPELL = auto()
    CREATE_FOOD_AND_WATER = auto()
    CRUSADERS_MANTLE = auto()
    DAYLIGHT = auto()
    DISPEL_MAGIC = auto()
    ELEMENTAL_WEAPON = auto()
    FEAR = auto()
    FEIGN_DEATH = auto()
    FIREBALL = auto()
    FLY = auto()
    GASEOUS_FORM = auto()
    GLYPH_OF_WARDING = auto()
    HASTE = auto()
    HUNGER_OF_HADAR = "Hunger of Hadar"
    HYPNOTIC_PATTERN = auto()
    LEOMUNDS_TINY_HUT = auto()
    LIGHTNING_ARROW = auto()
    LIGHTNING_BOLT = auto()
    MAGIC_CIRCLE = auto()
    MAJOR_IMAGE = auto()
    MASS_HEALING_WORD = auto()
    MELD_INTO_STONE = auto()
    NONDETECTION = auto()
    PHANTOM_STEED = auto()
    PLANT_GROWTH = auto()
    PROTECTION_FROM_ENERGY = auto()
    REMOVE_CURSE = auto()
    REVIVIFY = auto()
    SENDING = auto()
    SLEET_STORM = auto()
    SLOW = auto()
    SPEAK_WITH_DEAD = auto()
    SPEAK_WITH_PLANTS = auto()
    SPIRIT_GUARDIANS = auto()
    STINKING_CLOUD = auto()
    SUMMON_FEY = auto()
    SUMMON_UNDEAD = auto()
    TONGUES = auto()
    VAMPIRIC_TOUCH = auto()
    WATER_BREATHING = auto()
    WATER_WALK = auto()
    WIND_WALL = auto()

    # Level 4
    ARCANE_EYE = auto()
    AURA_OF_LIFE = auto()
    AURA_OF_PURITY = auto()
    BANISHMENT = auto()
    BLIGHT = auto()
    CHARM_MONSTER = auto()
    CONFUSION = auto()
    CONJURE_MINOR_ELEMENTALS = auto()
    CONJURE_WOODLAND_BEINGS = auto()
    CONTROL_WATER = auto()
    DEATH_WARD = auto()
    DIMENSION_DOOR = auto()
    DIVINATION = auto()
    DOMINATE_BEAST = auto()
    EVARDS_BLACK_TENTACLES = "Evard's Black Tentacles"
    FABRICATE = auto()
    FIRE_SHIELD = auto()
    FOUNT_OF_MOONLIGHT = "Fount of Moonlight"
    FREEDOM_OF_MOVEMENT = auto()
    GIANT_INSECT = auto()
    GRASPING_VINE = auto()
    GREATER_INVISIBILITY = auto()
    GUARDIAN_OF_FAITH = auto()
    HALLUCINATORY_TERRAIN = auto()
    ICE_STORM = auto()
    LEOMUNDS_SECRET_CHEST = "Leomund's Secret Chest"
    LOCATE_CREATURE = auto()
    MORDENKAINENS_FAITHFUL_HOUND = "Mordenkainen's Faithful Hound"
    MORDENKAINENS_PRIVATE_SANCTUM = "Mordenkainen's Private Sanctum"
    OTILUKES_RESILIENT_SPHERE = "Otiluke's Resilient Sphere"
    PHANTASMAL_KILLER = auto()
    POLYMORPH = auto()
    STAGGERING_SMITE = auto()
    STONESKIN = auto()
    STONE_SHAPE = auto()
    SUMMON_ABERRATION = auto()
    SUMMON_CONSTRUCT = auto()
    SUMMON_ELEMENTAL = auto()
    VITRIOLIC_SPHERE = auto()
    WALL_OF_FIRE = "Wall of Fire"

    # Level 5
    ANTILIFE_SHELL = auto()
    AWAKEN = auto()
    CIRCLE_OF_POWER = auto()
    COMMUNE = auto()
    COMMUNE_WITH_NATURE = auto()
    CONE_OF_COLD = auto()
    CONJURE_ELEMENTAL = auto()
    CONTAGION = auto()
    DISPEL_EVIL_AND_GOOD = auto()
    DOMINATE_PERSON = auto()
    FLAME_STRIKE = auto()
    GEAS = auto()
    GREATER_RESTORATION = auto()
    HALLOW = auto()
    HOLD_MONSTER = auto()
    INSECT_PLAGUE = auto()
    LEGEND_LORE = auto()
    MASS_CURE_WOUNDS = auto()
    MODIFY_MEMORY = auto()
    PLANAR_BINDING = auto()
    RAISE_DEAD = auto()
    REINCARNATE = auto()
    SCRYING = auto()
    STEEL_WIND_STRIKE = auto()
    SUMMON_CELESTIAL = auto()
    SUMMON_DRAGON = auto()
    TREE_STRIDE = auto()
    WALL_OF_STONE = auto()


#######################################################################
SPELL_DETAILS = {
    #
    Spell.ACID_SPLASH: SDT(0, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.BLADE_WARD: SDT(0, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION),
    Spell.CHILL_TOUCH: SDT(0, SpellSchool.NECROMANCY, SpellFlag.NONE),
    Spell.DANCING_LIGHTS: SDT(0, SpellSchool.ILLUSION, SpellFlag.CONCENTRATION),
    Spell.DRUIDCRAFT: SDT(0, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.ELDRITCH_BLAST: SDT(0, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.ELEMENTALISM: SDT(0, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.FIRE_BOLT: SDT(0, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.FRIENDS: SDT(0, SpellSchool.ENCHANTMENT, SpellFlag.CONCENTRATION),
    Spell.GUIDANCE: SDT(0, SpellSchool.DIVINATION, SpellFlag.CONCENTRATION),
    Spell.LIGHT: SDT(0, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.MAGE_HAND: SDT(0, SpellSchool.CONJURATION, SpellFlag.NONE),
    Spell.MENDING: SDT(0, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.MESSAGE: SDT(0, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.MIND_SLIVER: SDT(0, SpellSchool.ENCHANTMENT, SpellFlag.NONE),
    Spell.MINOR_ILLUSION: SDT(0, SpellSchool.ILLUSION, SpellFlag.NONE),
    Spell.POISON_SPRAY: SDT(0, SpellSchool.NECROMANCY, SpellFlag.NONE),
    Spell.PRESTIGITATION: SDT(0, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.PRODUCE_FLAME: SDT(0, SpellSchool.CONJURATION, SpellFlag.NONE),
    Spell.RAY_OF_FROST: SDT(0, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.RESISTANCE: SDT(0, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION),
    Spell.SACRED_FLAME: SDT(0, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.SHILLELAGH: SDT(0, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.SHOCKING_GRASP: SDT(0, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.SOURCEROUS_BURST: SDT(0, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.SPARE_THE_DYING: SDT(0, SpellSchool.NECROMANCY, SpellFlag.NONE),
    Spell.STARRY_WISP: SDT(0, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.THAUMATURGY: SDT(0, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.THORN_WHIP: SDT(0, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.THUNDERCLAP: SDT(0, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.TOLL_THE_DEAD: SDT(0, SpellSchool.NECROMANCY, SpellFlag.NONE),
    Spell.TRUE_STRIKE: SDT(0, SpellSchool.DIVINATION, SpellFlag.NONE),
    Spell.WORD_OF_RADIANCE: SDT(0, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.VICIOUS_MOKERY: SDT(0, SpellSchool.ENCHANTMENT, SpellFlag.NONE),
    #
    Spell.ALARM: SDT(1, SpellSchool.ABJURATION, SpellFlag.RITUAL),
    Spell.ANIMAL_FRIENDSHIP: SDT(1, SpellSchool.ENCHANTMENT, SpellFlag.NONE),
    Spell.ARMOR_OF_AGATHYS: SDT(1, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.ARMS_OF_HADAR: SDT(1, SpellSchool.CONJURATION, SpellFlag.NONE),
    Spell.BANE: SDT(1, SpellSchool.ENCHANTMENT, SpellFlag.CONCENTRATION),
    Spell.BLESS: SDT(1, SpellSchool.ENCHANTMENT, SpellFlag.CONCENTRATION | SpellFlag.MATERIAL),
    Spell.BURNING_HANDS: SDT(1, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.CHARM_PERSON: SDT(1, SpellSchool.ENCHANTMENT, SpellFlag.NONE),
    Spell.CHROMATIC_ORB: SDT(1, SpellSchool.EVOCATION, SpellFlag.MATERIAL),
    Spell.COLOR_SPRAY: SDT(1, SpellSchool.ILLUSION, SpellFlag.NONE),
    Spell.COMMAND: SDT(1, SpellSchool.ENCHANTMENT, SpellFlag.NONE),
    Spell.COMPELLED_DUEL: SDT(1, SpellSchool.ENCHANTMENT, SpellFlag.CONCENTRATION),
    Spell.COMPREHEND_LANGUAGES: SDT(1, SpellSchool.DIVINATION, SpellFlag.RITUAL),
    Spell.CREATE_OR_DESTROY_WATER: SDT(1, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.CURE_WOUNDS: SDT(1, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.DETECT_EVIL_AND_GOOD: SDT(1, SpellSchool.DIVINATION, SpellFlag.CONCENTRATION),
    Spell.DETECT_MAGIC: SDT(1, SpellSchool.DIVINATION, SpellFlag.CONCENTRATION | SpellFlag.RITUAL),
    Spell.DETECT_POISON_AND_DISEASE: SDT(1, SpellSchool.DIVINATION, SpellFlag.CONCENTRATION | SpellFlag.RITUAL),
    Spell.DISGUISE_SELF: SDT(1, SpellSchool.ILLUSION, SpellFlag.NONE),
    Spell.DISSONANT_WHISPERS: SDT(1, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION),
    Spell.DIVINE_FAVOR: SDT(1, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.DIVINE_SMITE: SDT(1, SpellSchool.ENCHANTMENT, SpellFlag.NONE),
    Spell.ENSNARING_STRIKE: SDT(1, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION),
    Spell.ENTANGLE: SDT(1, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION),
    Spell.EXPEDITIOUS_RETREAT: SDT(1, SpellSchool.TRANSMUTATION, SpellFlag.CONCENTRATION),
    Spell.FAERIE_FIRE: SDT(1, SpellSchool.EVOCATION, SpellFlag.CONCENTRATION),
    Spell.FALSE_LIFE: SDT(1, SpellSchool.NECROMANCY, SpellFlag.NONE),
    Spell.FEATHER_FALL: SDT(1, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.FIND_FAMILIAR: SDT(1, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION),
    Spell.FIND_STEED: SDT(1, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION),
    Spell.FOG_CLOUD: SDT(1, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION),
    Spell.GOODBERRY: SDT(1, SpellSchool.CONJURATION, SpellFlag.NONE),
    Spell.GREASE: SDT(1, SpellSchool.CONJURATION, SpellFlag.NONE),
    Spell.GUIDING_BOLT: SDT(1, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.HAIL_OF_THORNS: SDT(1, SpellSchool.CONJURATION, SpellFlag.NONE),
    Spell.HEALING_WORD: SDT(1, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.HELLISH_REBUKE: SDT(1, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.HEROISM: SDT(1, SpellSchool.ENCHANTMENT, SpellFlag.CONCENTRATION),
    Spell.HEX: SDT(1, SpellSchool.ENCHANTMENT, SpellFlag.CONCENTRATION),
    Spell.HUNTERS_MARK: SDT(1, SpellSchool.DIVINATION, SpellFlag.CONCENTRATION),
    Spell.ICE_KNIFE: SDT(1, SpellSchool.CONJURATION, SpellFlag.NONE),
    Spell.IDENTIFY: SDT(1, SpellSchool.DIVINATION, SpellFlag.RITUAL | SpellFlag.MATERIAL),
    Spell.ILLUSORY_SCRIPT: SDT(1, SpellSchool.ILLUSION, SpellFlag.RITUAL | SpellFlag.MATERIAL),
    Spell.INFLICT_WOUNDS: SDT(1, SpellSchool.NECROMANCY, SpellFlag.NONE),
    Spell.JUMP: SDT(1, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.LONGSTRIDER: SDT(1, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.MAGE_ARMOR: SDT(1, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.MAGIC_MISSILE: SDT(1, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.PROTECTION_FROM_EVIL_AND_GOOD: SDT(1, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION | SpellFlag.MATERIAL),
    Spell.PURIFY_FOOD_AND_DRINK: SDT(1, SpellSchool.TRANSMUTATION, SpellFlag.RITUAL),
    Spell.RAY_OF_SICKNESS: SDT(1, SpellSchool.NECROMANCY, SpellFlag.NONE),
    Spell.SANCTUARY: SDT(1, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.SEARING_SMITE: SDT(1, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.SHIELD: SDT(1, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.SHIELD_OF_FAITH: SDT(1, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION),
    Spell.SHINING_SMITE: SDT(1, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION),
    Spell.SILENT_IMAGE: SDT(1, SpellSchool.ILLUSION, SpellFlag.CONCENTRATION),
    Spell.SLEEP: SDT(1, SpellSchool.ENCHANTMENT, SpellFlag.CONCENTRATION),
    Spell.SPEAK_WITH_ANIMALS: SDT(1, SpellSchool.DIVINATION, SpellFlag.RITUAL),
    Spell.TASHAS_HIDEOUS_LAUGHTER: SDT(1, SpellSchool.ENCHANTMENT, SpellFlag.CONCENTRATION),
    Spell.TENSERS_FLOATING_DISK: SDT(1, SpellSchool.CONJURATION, SpellFlag.RITUAL),
    Spell.THUNDEROUS_SMITE: SDT(1, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.THUNDERWAVE: SDT(1, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.UNSEEN_SERVANT: SDT(1, SpellSchool.CONJURATION, SpellFlag.RITUAL),
    Spell.WITCH_BOLT: SDT(1, SpellSchool.EVOCATION, SpellFlag.CONCENTRATION),
    Spell.WRATHFUL_SMITE: SDT(1, SpellSchool.NECROMANCY, SpellFlag.NONE),
    #
    Spell.AID: SDT(2, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.ALTER_SELF: SDT(2, SpellSchool.TRANSMUTATION, SpellFlag.CONCENTRATION),
    Spell.ANIMAL_MESSENGER: SDT(2, SpellSchool.ENCHANTMENT, SpellFlag.RITUAL),
    Spell.ARCANE_LOCK: SDT(2, SpellSchool.ABJURATION, SpellFlag.MATERIAL),
    Spell.ARCANE_VIGOR: SDT(2, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.AUGURY: SDT(2, SpellSchool.DIVINATION, SpellFlag.RITUAL | SpellFlag.MATERIAL),
    Spell.BARKSKIN: SDT(2, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.BEAST_SENSE: SDT(2, SpellSchool.DIVINATION, SpellFlag.CONCENTRATION | SpellFlag.RITUAL),
    Spell.BLINDNESS_DEAFNESS: SDT(2, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.BLUR: SDT(2, SpellSchool.ILLUSION, SpellFlag.CONCENTRATION),
    Spell.CALM_EMOTIONS: SDT(2, SpellSchool.ENCHANTMENT, SpellFlag.CONCENTRATION),
    Spell.CLOUD_OF_DAGGERS: SDT(2, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION),
    Spell.CONTINUAL_FLAME: SDT(2, SpellSchool.EVOCATION, SpellFlag.MATERIAL),
    Spell.CORDON_OF_ARROWS: SDT(2, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.CROWN_OF_MADNESS: SDT(2, SpellSchool.ENCHANTMENT, SpellFlag.CONCENTRATION),
    Spell.DARKNESS: SDT(2, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.DARKVISION: SDT(2, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.DETECT_THOUGHTS: SDT(2, SpellSchool.DIVINATION, SpellFlag.CONCENTRATION),
    Spell.DRAGONS_BREATH: SDT(2, SpellSchool.TRANSMUTATION, SpellFlag.CONCENTRATION),
    Spell.ENHANCE_ABILITY: SDT(2, SpellSchool.TRANSMUTATION, SpellFlag.CONCENTRATION),
    Spell.ENLARGE_REDUCE: SDT(2, SpellSchool.TRANSMUTATION, SpellFlag.CONCENTRATION),
    Spell.ENTHRALL: SDT(2, SpellSchool.ENCHANTMENT, SpellFlag.CONCENTRATION),
    Spell.FIND_TRAPS: SDT(2, SpellSchool.DIVINATION, SpellFlag.NONE),
    Spell.FLAME_BLADE: SDT(2, SpellSchool.EVOCATION, SpellFlag.CONCENTRATION),
    Spell.FLAMING_SPHERE: SDT(2, SpellSchool.EVOCATION, SpellFlag.CONCENTRATION),
    Spell.GENTLE_REPOSE: SDT(2, SpellSchool.NECROMANCY, SpellFlag.RITUAL | SpellFlag.MATERIAL),
    Spell.GUST_OF_WIND: SDT(2, SpellSchool.EVOCATION, SpellFlag.CONCENTRATION),
    Spell.HEAT_METAL: SDT(2, SpellSchool.TRANSMUTATION, SpellFlag.CONCENTRATION),
    Spell.HOLD_PERSON: SDT(2, SpellSchool.ENCHANTMENT, SpellFlag.CONCENTRATION),
    Spell.INVISIBILITY: SDT(2, SpellSchool.ILLUSION, SpellFlag.CONCENTRATION),
    Spell.KNOCK: SDT(2, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.LESSER_RESTORATION: SDT(2, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.LEVITATE: SDT(2, SpellSchool.TRANSMUTATION, SpellFlag.CONCENTRATION),
    Spell.LOCATE_ANIMALS_OR_PLANTS: SDT(2, SpellSchool.DIVINATION, SpellFlag.RITUAL),
    Spell.LOCATE_OBJECT: SDT(2, SpellSchool.DIVINATION, SpellFlag.CONCENTRATION),
    Spell.MAGIC_MOUTH: SDT(2, SpellSchool.ILLUSION, SpellFlag.RITUAL | SpellFlag.MATERIAL),
    Spell.MAGIC_WEAPON: SDT(2, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.MELFS_ACID_ARROW: SDT(2, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.MIND_SPIKE: SDT(2, SpellSchool.DIVINATION, SpellFlag.CONCENTRATION),
    Spell.MIRROR_IMAGE: SDT(2, SpellSchool.ILLUSION, SpellFlag.NONE),
    Spell.MISTY_STEP: SDT(2, SpellSchool.CONJURATION, SpellFlag.NONE),
    Spell.MOONBEAM: SDT(2, SpellSchool.EVOCATION, SpellFlag.CONCENTRATION),
    Spell.NYSTULS_MAGIC_AURA: SDT(2, SpellSchool.ILLUSION, SpellFlag.NONE),
    Spell.PASS_WITHOUT_TRACE: SDT(2, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.PHANTASMAL_FORCE: SDT(2, SpellSchool.ILLUSION, SpellFlag.CONCENTRATION),
    Spell.PRAYER_OF_HEALING: SDT(2, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.PROTECTION_FROM_POISON: SDT(2, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.RAY_OF_ENFEEBLEMENT: SDT(2, SpellSchool.NECROMANCY, SpellFlag.CONCENTRATION),
    Spell.ROPE_TRICK: SDT(2, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.SCORCHING_RAY: SDT(2, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.SEE_INVISIBILITY: SDT(2, SpellSchool.DIVINATION, SpellFlag.NONE),
    Spell.SHATTER: SDT(2, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.SILENCE: SDT(2, SpellSchool.ILLUSION, SpellFlag.CONCENTRATION | SpellFlag.RITUAL),
    Spell.SPIDER_CLIMB: SDT(2, SpellSchool.TRANSMUTATION, SpellFlag.CONCENTRATION),
    Spell.SPIKE_GROWTH: SDT(2, SpellSchool.TRANSMUTATION, SpellFlag.CONCENTRATION),
    Spell.SPIRITUAL_WEAPON: SDT(2, SpellSchool.EVOCATION, SpellFlag.CONCENTRATION),
    Spell.SUGGESTION: SDT(2, SpellSchool.ENCHANTMENT, SpellFlag.CONCENTRATION),
    Spell.SUMMON_BEAST: SDT(2, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION | SpellFlag.MATERIAL),
    Spell.WARDING_BOND: SDT(2, SpellSchool.ABJURATION, SpellFlag.MATERIAL),
    Spell.WEB: SDT(2, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION),
    Spell.ZONE_OF_TRUTH: SDT(2, SpellSchool.ENCHANTMENT, SpellFlag.NONE),
    #
    Spell.ANIMATE_DEAD: SDT(3, SpellSchool.NECROMANCY, SpellFlag.NONE),
    Spell.ARCANE_EYE: SDT(3, SpellSchool.DIVINATION, SpellFlag.CONCENTRATION),
    Spell.AURA_OF_VITALITY: SDT(3, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION),
    Spell.BEACON_OF_HOPE: SDT(3, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION),
    Spell.BESTOW_CURSE: SDT(3, SpellSchool.NECROMANCY, SpellFlag.CONCENTRATION),
    Spell.BLINK: SDT(3, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.BLINDING_SMITE: SDT(3, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.CALL_LIGHTNING: SDT(3, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION),
    Spell.CLAIRVOYANCE: SDT(3, SpellSchool.DIVINATION, SpellFlag.CONCENTRATION | SpellFlag.MATERIAL),
    Spell.CONJURE_ANIMALS: SDT(3, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION),
    Spell.CONJURE_BARRAGE: SDT(3, SpellSchool.CONJURATION, SpellFlag.NONE),
    Spell.COUNTERSPELL: SDT(3, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.CREATE_FOOD_AND_WATER: SDT(3, SpellSchool.CONJURATION, SpellFlag.NONE),
    Spell.CRUSADERS_MANTLE: SDT(3, SpellSchool.TRANSMUTATION, SpellFlag.CONCENTRATION),
    Spell.DAYLIGHT: SDT(3, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.DISPEL_MAGIC: SDT(3, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.ELEMENTAL_WEAPON: SDT(3, SpellSchool.TRANSMUTATION, SpellFlag.CONCENTRATION),
    Spell.FEAR: SDT(3, SpellSchool.ILLUSION, SpellFlag.CONCENTRATION),
    Spell.FEIGN_DEATH: SDT(3, SpellSchool.NECROMANCY, SpellFlag.RITUAL),
    Spell.FIREBALL: SDT(3, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.FLY: SDT(3, SpellSchool.TRANSMUTATION, SpellFlag.CONCENTRATION),
    Spell.GASEOUS_FORM: SDT(3, SpellSchool.TRANSMUTATION, SpellFlag.CONCENTRATION),
    Spell.GLYPH_OF_WARDING: SDT(3, SpellSchool.ABJURATION, SpellFlag.MATERIAL),
    Spell.HASTE: SDT(3, SpellSchool.TRANSMUTATION, SpellFlag.CONCENTRATION),
    Spell.HUNGER_OF_HADAR: SDT(3, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION),
    Spell.HYPNOTIC_PATTERN: SDT(3, SpellSchool.ILLUSION, SpellFlag.CONCENTRATION),
    Spell.LEOMUNDS_TINY_HUT: SDT(3, SpellSchool.EVOCATION, SpellFlag.RITUAL),
    Spell.LIGHTNING_ARROW: SDT(3, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.LIGHTNING_BOLT: SDT(3, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.MAGIC_CIRCLE: SDT(3, SpellSchool.ABJURATION, SpellFlag.MATERIAL),
    Spell.MAJOR_IMAGE: SDT(3, SpellSchool.ILLUSION, SpellFlag.CONCENTRATION),
    Spell.MASS_HEALING_WORD: SDT(3, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.MELD_INTO_STONE: SDT(3, SpellSchool.TRANSMUTATION, SpellFlag.RITUAL),
    Spell.NONDETECTION: SDT(3, SpellSchool.ABJURATION, SpellFlag.MATERIAL),
    Spell.PHANTOM_STEED: SDT(3, SpellSchool.ILLUSION, SpellFlag.RITUAL),
    Spell.PLANT_GROWTH: SDT(3, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.PROTECTION_FROM_ENERGY: SDT(3, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION),
    Spell.REMOVE_CURSE: SDT(3, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.REVIVIFY: SDT(3, SpellSchool.NECROMANCY, SpellFlag.MATERIAL),
    Spell.SENDING: SDT(3, SpellSchool.DIVINATION, SpellFlag.NONE),
    Spell.SLEET_STORM: SDT(3, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION),
    Spell.SLOW: SDT(3, SpellSchool.TRANSMUTATION, SpellFlag.CONCENTRATION),
    Spell.SPEAK_WITH_DEAD: SDT(3, SpellSchool.NECROMANCY, SpellFlag.NONE),
    Spell.SPEAK_WITH_PLANTS: SDT(3, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.SPIRIT_GUARDIANS: SDT(3, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION),
    Spell.STINKING_CLOUD: SDT(3, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION),
    Spell.SUMMON_FEY: SDT(3, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION | SpellFlag.MATERIAL),
    Spell.SUMMON_UNDEAD: SDT(3, SpellSchool.NECROMANCY, SpellFlag.CONCENTRATION | SpellFlag.MATERIAL),
    Spell.TONGUES: SDT(3, SpellSchool.DIVINATION, SpellFlag.NONE),
    Spell.VAMPIRIC_TOUCH: SDT(3, SpellSchool.NECROMANCY, SpellFlag.CONCENTRATION),
    Spell.WATER_BREATHING: SDT(3, SpellSchool.TRANSMUTATION, SpellFlag.RITUAL),
    Spell.WATER_WALK: SDT(3, SpellSchool.TRANSMUTATION, SpellFlag.RITUAL),
    Spell.WIND_WALL: SDT(3, SpellSchool.EVOCATION, SpellFlag.CONCENTRATION),
    #
    Spell.AURA_OF_LIFE: SDT(4, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION),
    Spell.AURA_OF_PURITY: SDT(4, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION),
    Spell.BANISHMENT: SDT(4, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION),
    Spell.BLIGHT: SDT(4, SpellSchool.NECROMANCY, SpellFlag.NONE),
    Spell.CHARM_MONSTER: SDT(4, SpellSchool.ENCHANTMENT, SpellFlag.NONE),
    Spell.CONFUSION: SDT(4, SpellSchool.ENCHANTMENT, SpellFlag.CONCENTRATION),
    Spell.CONJURE_MINOR_ELEMENTALS: SDT(4, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION),
    Spell.CONJURE_WOODLAND_BEINGS: SDT(4, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION),
    Spell.CONTROL_WATER: SDT(4, SpellSchool.TRANSMUTATION, SpellFlag.CONCENTRATION),
    Spell.DEATH_WARD: SDT(4, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.DIMENSION_DOOR: SDT(4, SpellSchool.CONJURATION, SpellFlag.NONE),
    Spell.DIVINATION: SDT(4, SpellSchool.DIVINATION, SpellFlag.RITUAL | SpellFlag.MATERIAL),
    Spell.DOMINATE_BEAST: SDT(4, SpellSchool.ENCHANTMENT, SpellFlag.CONCENTRATION),
    Spell.EVARDS_BLACK_TENTACLES: SDT(4, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION),
    Spell.FABRICATE: SDT(4, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.FIRE_SHIELD: SDT(4, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.FOUNT_OF_MOONLIGHT: SDT(4, SpellSchool.EVOCATION, SpellFlag.CONCENTRATION),
    Spell.FREEDOM_OF_MOVEMENT: SDT(4, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.GIANT_INSECT: SDT(4, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION),
    Spell.GRASPING_VINE: SDT(4, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION),
    Spell.GREATER_INVISIBILITY: SDT(4, SpellSchool.ILLUSION, SpellFlag.CONCENTRATION),
    Spell.GUARDIAN_OF_FAITH: SDT(4, SpellSchool.CONJURATION, SpellFlag.NONE),
    Spell.HALLUCINATORY_TERRAIN: SDT(4, SpellSchool.ILLUSION, SpellFlag.NONE),
    Spell.ICE_STORM: SDT(4, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.LEOMUNDS_SECRET_CHEST: SDT(4, SpellSchool.CONJURATION, SpellFlag.MATERIAL),
    Spell.LOCATE_CREATURE: SDT(4, SpellSchool.DIVINATION, SpellFlag.CONCENTRATION),
    Spell.MORDENKAINENS_FAITHFUL_HOUND: SDT(4, SpellSchool.CONJURATION, SpellFlag.NONE),
    Spell.MORDENKAINENS_PRIVATE_SANCTUM: SDT(4, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.OTILUKES_RESILIENT_SPHERE: SDT(4, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION),
    Spell.PHANTASMAL_KILLER: SDT(4, SpellSchool.ILLUSION, SpellFlag.CONCENTRATION),
    Spell.POLYMORPH: SDT(4, SpellSchool.TRANSMUTATION, SpellFlag.CONCENTRATION),
    Spell.STAGGERING_SMITE: SDT(4, SpellSchool.ENCHANTMENT, SpellFlag.NONE),
    Spell.STONESKIN: SDT(4, SpellSchool.TRANSMUTATION, SpellFlag.CONCENTRATION | SpellFlag.MATERIAL),
    Spell.STONE_SHAPE: SDT(4, SpellSchool.TRANSMUTATION, SpellFlag.NONE),
    Spell.SUMMON_ABERRATION: SDT(4, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION | SpellFlag.MATERIAL),
    Spell.SUMMON_CONSTRUCT: SDT(4, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION | SpellFlag.MATERIAL),
    Spell.SUMMON_ELEMENTAL: SDT(4, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION | SpellFlag.MATERIAL),
    Spell.VITRIOLIC_SPHERE: SDT(4, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.WALL_OF_FIRE: SDT(4, SpellSchool.EVOCATION, SpellFlag.CONCENTRATION),
    #
    Spell.ANTILIFE_SHELL: SDT(5, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION),
    Spell.AWAKEN: SDT(5, SpellSchool.TRANSMUTATION, SpellFlag.MATERIAL),
    Spell.CIRCLE_OF_POWER: SDT(5, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION),
    Spell.COMMUNE: SDT(5, SpellSchool.DIVINATION, SpellFlag.RITUAL),
    Spell.COMMUNE_WITH_NATURE: SDT(5, SpellSchool.DIVINATION, SpellFlag.RITUAL),
    Spell.CONE_OF_COLD: SDT(5, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.CONJURE_ELEMENTAL: SDT(5, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION),
    Spell.CONTAGION: SDT(5, SpellSchool.NECROMANCY, SpellFlag.NONE),
    Spell.DISPEL_EVIL_AND_GOOD: SDT(5, SpellSchool.ABJURATION, SpellFlag.CONCENTRATION),
    Spell.FLAME_STRIKE: SDT(5, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.GEAS: SDT(5, SpellSchool.ENCHANTMENT, SpellFlag.NONE),
    Spell.GREATER_RESTORATION: SDT(5, SpellSchool.ABJURATION, SpellFlag.MATERIAL),
    Spell.HALLOW: SDT(5, SpellSchool.ABJURATION, SpellFlag.MATERIAL),
    Spell.INSECT_PLAGUE: SDT(5, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION),
    Spell.LEGEND_LORE: SDT(5, SpellSchool.DIVINATION, SpellFlag.MATERIAL),
    Spell.MASS_CURE_WOUNDS: SDT(5, SpellSchool.ABJURATION, SpellFlag.NONE),
    Spell.PLANAR_BINDING: SDT(5, SpellSchool.ABJURATION, SpellFlag.MATERIAL),
    Spell.RAISE_DEAD: SDT(5, SpellSchool.NECROMANCY, SpellFlag.MATERIAL),
    Spell.REINCARNATE: SDT(5, SpellSchool.NECROMANCY, SpellFlag.MATERIAL),
    Spell.SCRYING: SDT(5, SpellSchool.DIVINATION, SpellFlag.CONCENTRATION | SpellFlag.MATERIAL),
    Spell.SUMMON_CELESTIAL: SDT(5, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION | SpellFlag.MATERIAL),
    Spell.SUMMON_DRAGON: SDT(5, SpellSchool.NONE, SpellFlag.NONE),
    Spell.TREE_STRIDE: SDT(5, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION),
    Spell.WALL_OF_STONE: SDT(5, SpellSchool.EVOCATION, SpellFlag.CONCENTRATION),
}


#######################################################################
def spell_name(spell: Spell) -> str:
    name = spell.replace("_", " ").title()
    name = name.replace("'S", "'s")
    return name


#########################################################################
def spell_flags(spell: Spell) -> str:
    flags = SPELL_DETAILS[spell].flags
    ans = []
    if flags & SpellFlag.RITUAL:
        ans.append("R")
    if flags & SpellFlag.MATERIAL:
        ans.append("M")
    if flags & SpellFlag.CONCENTRATION:
        ans.append("C")
    if ans:
        return f"[{', '.join(ans)}]"
    else:
        return ""


#######################################################################
def spell_school(spell: Spell) -> str:
    school = SPELL_DETAILS[spell].school
    match school:
        case SpellSchool.ABJURATION:
            return "Abjur"
        case SpellSchool.CONJURATION:
            return "Conj"
        case SpellSchool.DIVINATION:
            return "Div"
        case SpellSchool.ENCHANTMENT:
            return "Ench"
        case SpellSchool.EVOCATION:
            return "Evoc"
        case SpellSchool.ILLUSION:
            return "Illus"
        case SpellSchool.NECROMANCY:
            return "Necro"
        case SpellSchool.TRANSMUTATION:
            return "Trans"
    raise NotDefined(f"Spell {spell.name} doesn't have school defined")


# EOF
