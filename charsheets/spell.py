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

    ACID_SPLASH = auto()
    AID = auto()
    ALARM = auto()
    ALTER_SELF = auto()
    ANIMAL_FRIENDSHIP = auto()
    ANIMAL_MESSENGER = auto()
    ANIMATE_DEAD = auto()
    ARCANE_EYE = "Arcane Eye"
    ARCANE_LOCK = auto()
    ARCANE_VIGOR = auto()
    ARMOR_OF_AGATHYS = auto()
    ARMS_OF_HADAR = auto()
    AUGURY = auto()
    AURA_OF_LIFE = auto()
    AURA_OF_PURITY = auto()
    AURA_OF_VITALITY = auto()
    BANE = auto()
    BANISHMENT = auto()
    BARKSKIN = auto()
    BEACON_OF_HOPE = auto()
    BEAST_SENSE = auto()
    BESTOW_CURSE = auto()
    BLADE_WARD = auto()
    BLESS = auto()
    BLIGHT = auto()
    BLINDNESS_DEAFNESS = auto()
    BLINDING_SMITE = auto()
    BLINK = auto()
    BLUR = auto()
    BURNING_HANDS = auto()
    CALL_LIGHTNING = auto()
    CALM_EMOTIONS = auto()
    CHARM_MONSTER = "Charm Monster"
    CHARM_PERSON = auto()
    CHILL_TOUCH = auto()
    CHROMATIC_ORB = auto()
    CLAIRVOYANCE = auto()
    CLOUD_OF_DAGGERS = auto()
    COLOR_SPRAY = auto()
    COMMAND = auto()
    COMMUNE_WITH_NATURE = auto()
    COMPELLED_DUEL = auto()
    COMPREHEND_LANGUAGES = auto()
    CONFUSION = auto()
    CONJURE_ANIMALS = auto()
    CONJURE_BARRAGE = auto()
    CONJURE_MINOR_ELEMENTALS = "Conjure Minor Elementals"
    CONJURE_WOODLAND_BEINGS = "Conjure Woodland Beings"
    CONTINUAL_FLAME = auto()
    CONTROL_WATER = auto()
    CORDON_OF_ARROWS = auto()
    COUNTERSPELL = auto()
    CREATE_FOOD_AND_WATER = auto()
    CREATE_OR_DESTROY_WATER = auto()
    CROWN_OF_MADNESS = auto()
    CRUSADERS_MANTLE = auto()
    CURE_WOUNDS = "Cure Wounds"
    DANCING_LIGHTS = auto()
    DARKNESS = auto()
    DARKVISION = auto()
    DAYLIGHT = auto()
    DEATH_WARD = auto()
    DETECT_EVIL_AND_GOOD = auto()
    DETECT_MAGIC = auto()
    DETECT_POISON_AND_DISEASE = auto()
    DETECT_THOUGHTS = auto()
    DIMENSION_DOOR = "Dimension Door"
    DISGUISE_SELF = auto()
    DISPEL_MAGIC = auto()
    DISSONANT_WHISPERS = auto()
    DIVINATION = auto()
    DIVINE_FAVOR = auto()
    DIVINE_SMITE = auto()
    DOMINATE_BEAST = auto()
    DRAGONS_BREATH = auto()
    DRUIDCRAFT = auto()
    ELDRITCH_BLAST = auto()
    ELEMENTALISM = auto()
    ELEMENTAL_WEAPON = auto()
    ENHANCE_ABILITY = auto()
    ENLARGE_REDUCE = auto()
    ENSNARING_STRIKE = auto()
    ENTANGLE = auto()
    ENTHRALL = auto()
    EVARDS_BLACK_TENTACLES = "Evard's Black Tentacles"
    EXPEDITIOUS_RETREAT = auto()
    FABRICATE = auto()
    FAERIE_FIRE = auto()
    FALSE_LIFE = auto()
    FEAR = auto()
    FEATHER_FALL = auto()
    FEIGN_DEATH = auto()
    FIND_FAMILIAR = auto()
    FIND_STEED = auto()
    FIND_TRAPS = auto()
    FIREBALL = auto()
    FIRE_BOLT = auto()
    FIRE_SHIELD = "Fire Shield"
    FLAME_BLADE = auto()
    FLAMING_SPHERE = auto()
    FLY = auto()
    FOG_CLOUD = auto()
    FOUNT_OF_MOONLIGHT = "Fount of Moonlight"
    FREEDOM_OF_MOVEMENT = auto()
    FRIENDS = auto()
    GASEOUS_FORM = auto()
    GENTLE_REPOSE = auto()
    GIANT_INSECT = "Giant Insect"
    GLYPH_OF_WARDING = auto()
    GOODBERRY = auto()
    GRASPING_VINE = "Grasping Vine"
    GREASE = auto()
    GREATER_INVISIBILITY = "Greater Invisibility"
    GREATER_RESTORATION = auto()
    GUARDIAN_OF_FAITH = auto()
    GUIDANCE = auto()
    GUIDING_BOLT = auto()
    GUST_OF_WIND = auto()
    HAIL_OF_THORNS = auto()
    HALLUCINATORY_TERRAIN = "Hallucinatory Terrain"
    HASTE = auto()
    HEALING_WORD = auto()
    HEAT_METAL = auto()
    HELLISH_REBUKE = auto()
    HEROISM = auto()
    HEX = auto()
    HOLD_PERSON = auto()
    HUNGER_OF_HADAR = "Hunger of Hadar"
    HUNTERS_MARK = auto()
    HYPNOTIC_PATTERN = auto()
    ICE_KNIFE = auto()
    ICE_STORM = "Ice Storm"
    IDENTIFY = auto()
    ILLUSORY_SCRIPT = auto()
    INFLICT_WOUNDS = "Inflict Wounds"
    INVISIBILITY = auto()
    JUMP = auto()
    KNOCK = auto()
    LEOMUNDS_SECRET_CHEST = "Leomund's Secret Chest"
    LEOMUNDS_TINY_HUT = auto()
    LESSER_RESTORATION = auto()
    LEVITATE = auto()
    LIGHT = "Light"
    LIGHTNING_ARROW = auto()
    LIGHTNING_BOLT = auto()
    LOCATE_ANIMALS_OR_PLANTS = auto()
    LOCATE_CREATURE = auto()
    LOCATE_OBJECT = auto()
    LONGSTRIDER = auto()
    MAGE_ARMOR = auto()
    MAGE_HAND = auto()
    MAGIC_CIRCLE = auto()
    MAGIC_MISSILE = auto()
    MAGIC_MOUTH = auto()
    MAGIC_WEAPON = auto()
    MAJOR_IMAGE = auto()
    MASS_HEALING_WORD = auto()
    MELD_INTO_STONE = auto()
    MELFS_ACID_ARROW = auto()
    MENDING = auto()
    MESSAGE = "Message"
    MIND_SLIVER = auto()
    MIND_SPIKE = auto()
    MINOR_ILLUSION = auto()
    MIRROR_IMAGE = auto()
    MISTY_STEP = auto()
    MOONBEAM = auto()
    MORDENKAINENS_FAITHFUL_HOUND = "Mordenkainen's Faithful Hound"
    MORDENKAINENS_PRIVATE_SANCTUM = "Mordenkainen's Private Sanctum"
    NONDETECTION = auto()
    NYSTULS_MAGIC_AURA = auto()
    OTILUKES_RESILIENT_SPHERE = "Otiluke's Resilient Sphere"
    PASS_WITHOUT_TRACE = auto()
    PHANTASMAL_FORCE = auto()
    PHANTASMAL_KILLER = auto()
    PHANTOM_STEED = auto()
    PLANT_GROWTH = auto()
    POISON_SPRAY = auto()
    POLYMORPH = auto()
    PRAYER_OF_HEALING = auto()
    PRESTIGITATION = auto()
    PRODUCE_FLAME = auto()
    PROTECTION_FROM_ENERGY = auto()
    PROTECTION_FROM_EVIL_AND_GOOD = auto()
    PROTECTION_FROM_POISON = auto()
    PURIFY_FOOD_AND_DRINK = auto()
    RAY_OF_ENFEEBLEMENT = auto()
    RAY_OF_FROST = auto()
    RAY_OF_SICKNESS = auto()
    REMOVE_CURSE = auto()
    RESISTANCE = auto()
    REVIVIFY = auto()
    ROPE_TRICK = auto()
    SACRED_FLAME = auto()
    SANCTUARY = auto()
    SCORCHING_RAY = auto()
    SEARING_SMITE = auto()
    SEE_INVISIBILITY = auto()
    SENDING = auto()
    SHATTER = auto()
    SHIELD = auto()
    SHIELD_OF_FAITH = auto()
    SHILLELAGH = auto()
    SHINING_SMITE = auto()
    SHOCKING_GRASP = auto()
    SILENCE = auto()
    SILENT_IMAGE = auto()
    SLEEP = auto()
    SLEET_STORM = auto()
    SLOW = auto()
    SOURCEROUS_BURST = auto()
    SPARE_THE_DYING = "Spare the Dying"
    SPEAK_WITH_ANIMALS = "Speak with Animals"
    SPEAK_WITH_DEAD = auto()
    SPEAK_WITH_PLANTS = auto()
    SPIDER_CLIMB = auto()
    SPIKE_GROWTH = auto()
    SPIRITUAL_WEAPON = auto()
    SPIRIT_GUARDIANS = auto()
    STAGGERING_SMITE = auto()
    STARRY_WISP = auto()
    STINKING_CLOUD = auto()
    STONESKIN = auto()
    STONE_SHAPE = auto()
    SUGGESTION = auto()
    SUMMON_ABERRATION = "Summon Aberration"
    SUMMON_BEAST = auto()
    SUMMON_CONSTRUCT = "Summon Construct"
    SUMMON_DRAGON = "Summon Dragon"
    SUMMON_ELEMENTAL = "Summon Elemental"
    SUMMON_FEY = auto()
    SUMMON_UNDEAD = auto()
    TASHAS_HIDEOUS_LAUGHTER = auto()
    TENSERS_FLOATING_DISK = auto()
    THAUMATURGY = auto()
    THORN_WHIP = auto()
    THUNDERCLAP = auto()
    THUNDEROUS_SMITE = auto()
    THUNDERWAVE = auto()
    TOLL_THE_DEAD = auto()
    TONGUES = auto()
    TREE_STRIDE = auto()
    TRUE_STRIKE = auto()
    UNSEEN_SERVANT = auto()
    VAMPIRIC_TOUCH = auto()
    VITRIOLIC_SPHERE = "Vitriolic Sphere"
    WALL_OF_FIRE = "Wall of Fire"
    WARDING_BOND = auto()
    WATER_BREATHING = auto()
    WATER_WALK = auto()
    WEB = auto()
    WIND_WALL = auto()
    WITCH_BOLT = auto()
    WORD_OF_RADIANCE = auto()
    WRATHFUL_SMITE = auto()
    ZONE_OF_TRUTH = auto()


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
    Spell.SUMMON_ELEMENTAL: SDT(4, SpellSchool.CONJURATION, SpellFlag.CONCENTRATION | SpellFlag.MATERIAL),
    Spell.VITRIOLIC_SPHERE: SDT(4, SpellSchool.EVOCATION, SpellFlag.NONE),
    Spell.WALL_OF_FIRE: SDT(4, SpellSchool.EVOCATION, SpellFlag.CONCENTRATION),
    #
    Spell.COMMUNE_WITH_NATURE: SDT(5, SpellSchool.NONE, SpellFlag.NONE),
    Spell.GREATER_RESTORATION: SDT(5, SpellSchool.NONE, SpellFlag.NONE),
    Spell.SUMMON_DRAGON: SDT(5, SpellSchool.NONE, SpellFlag.NONE),
    Spell.TREE_STRIDE: SDT(5, SpellSchool.NONE, SpellFlag.NONE),
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
