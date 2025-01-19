""" Spells"""

from enum import StrEnum, auto


class Spell(StrEnum):
    """All the Spells"""

    ACID_SPLASH = auto()
    AID = auto()
    ALARM = auto()
    ALTER_SELF = auto()
    ANIMAL_FRIENDSHIP = auto()
    ANIMAL_MESSENGER = auto()
    ANIMATE_DEAD = auto()
    ARCANE_LOCK = auto()
    ARCANE_VIGOR = auto()
    ARMOR_OF_AGATHYS = auto()
    ARMS_OF_HADAR = auto()
    AUGURY = auto()
    AURA_OF_VITALITY = auto()
    BANE = auto()
    BARKSKIN = auto()
    BEACON_OF_HOPE = auto()
    BEAST_SENSE = auto()
    BESTOW_CURSE = auto()
    BLADE_WARD = auto()
    BLESS = auto()
    BLINDNESS_DEAFNESS = auto()
    BLINK = auto()
    BLUR = auto()
    BURNING_HANDS = auto()
    CALL_LIGHTNING = auto()
    CALM_EMOTIONS = auto()
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
    CONJURE_ANIMALS = auto()
    CONJURE_WOODLAND_ANIMALS = auto()
    CONTINUAL_FLAME = auto()
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
    DETECT_EVIL_AND_GOOD = auto()
    DETECT_MAGIC = auto()
    DETECT_POISON_AND_DISEASE = auto()
    DETECT_THOUGHTS = auto()
    DISGUISE_SELF = auto()
    DISPEL_MAGIC = auto()
    DISSONANT_WHISPERS = auto()
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
    EXPEDITIOUS_RETREAT = auto()
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
    FLAME_BLADE = auto()
    FLAMING_SPHERE = auto()
    FLY = auto()
    FOG_CLOUD = auto()
    FREEDOM_OF_MOVEMENT = auto()
    FRIENDS = auto()
    GASEOUS_FORM = auto()
    GENTLE_REPOSE = auto()
    GLYPH_OF_WARDING = auto()
    GOODBERRY = auto()
    GREASE = auto()
    GREATER_RESTORATION = auto()
    GUIDANCE = auto()
    GUIDING_BOLT = auto()
    GUST_OF_WIND = auto()
    HAIL_OF_THORNS = auto()
    HASTE = auto()
    HEALING_WORD = auto()
    HEAT_METAL = auto()
    HELLISH_REBUKE = auto()
    HEROISM = auto()
    HEX = auto()
    HOLD_PERSON = auto()
    HUNGER_OF_HADAR = auto()
    HUNTERS_MARK = auto()
    HYPNOTIC_PATTERN = auto()
    ICE_KNIFE = auto()
    IDENTIFY = auto()
    ILLUSORY_SCRIPT = auto()
    INFLICT_WOUNDS = auto()
    INVISIBILITY = auto()
    JUMP = auto()
    KNOCK = auto()
    LEOMUNDS_TINY_HUT = auto()
    LESSER_RESTORATION = auto()
    LEVITATE = auto()
    LIGHT = "Light"
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
    NONDETECTION = auto()
    NYSTULS_MAGIC_AURA = auto()
    PASS_WITHOUT_TRACE = auto()
    PHANTASMAL_FORCE = auto()
    PHANTOM_STEED = auto()
    PLANT_GROWTH = auto()
    POISON_SPRAY = auto()
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
    SPARE_THE_DYING = "Spare the Dying"
    SPEAK_WITH_ANIMALS = "Speak with Animals"
    SPEAK_WITH_DEAD = auto()
    SPEAK_WITH_PLANTS = auto()
    SPIDER_CLIMB = auto()
    SPIKE_GROWTH = auto()
    SPIRITUAL_WEAPON = auto()
    SPIRIT_GUARDIANS = auto()
    STARRY_WISP = auto()
    STINKING_CLOUD = auto()
    STONESKIN = auto()
    SUGGESTION = auto()
    SUMMON_BEAST = auto()
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
    WARDING_BOND = auto()
    WATER_BREATHING = auto()
    WATER_WALK = auto()
    WEB = auto()
    WIND_WALL = auto()
    WITCH_BOLT = auto()
    WORD_OF_RADIANCE = auto()
    WRATHFUL_SMITE = auto()
    ZONE_OF_TRUTH = auto()


SPELL_LEVELS = {
    Spell.ACID_SPLASH: 0,
    Spell.AID: 2,
    Spell.ALARM: 1,
    Spell.ALTER_SELF: 2,
    Spell.ANIMAL_FRIENDSHIP: 1,
    Spell.ANIMAL_MESSENGER: 2,
    Spell.ANIMATE_DEAD: 3,
    Spell.ARCANE_LOCK: 2,
    Spell.ARCANE_VIGOR: 2,
    Spell.ARMOR_OF_AGATHYS: 1,
    Spell.ARMS_OF_HADAR: 1,
    Spell.AUGURY: 2,
    Spell.AURA_OF_VITALITY: 3,
    Spell.BANE: 1,
    Spell.BARKSKIN: 2,
    Spell.BEACON_OF_HOPE: 3,
    Spell.BEAST_SENSE: 2,
    Spell.BESTOW_CURSE: 3,
    Spell.BLADE_WARD: 0,
    Spell.BLESS: 1,
    Spell.BLINDNESS_DEAFNESS: 2,
    Spell.BLINK: 3,
    Spell.BLUR: 2,
    Spell.BURNING_HANDS: 1,
    Spell.CALL_LIGHTNING: 3,
    Spell.CALM_EMOTIONS: 2,
    Spell.CHARM_PERSON: 1,
    Spell.CHILL_TOUCH: 0,
    Spell.CHROMATIC_ORB: 1,
    Spell.CLAIRVOYANCE: 3,
    Spell.CLOUD_OF_DAGGERS: 2,
    Spell.COLOR_SPRAY: 1,
    Spell.COMMAND: 1,
    Spell.COMMUNE_WITH_NATURE: 5,
    Spell.COMPELLED_DUEL: 1,
    Spell.COMPREHEND_LANGUAGES: 1,
    Spell.CONJURE_ANIMALS: 3,
    Spell.CONJURE_WOODLAND_ANIMALS: 4,
    Spell.CONTINUAL_FLAME: 2,
    Spell.CORDON_OF_ARROWS: 2,
    Spell.COUNTERSPELL: 3,
    Spell.CREATE_FOOD_AND_WATER: 3,
    Spell.CREATE_OR_DESTROY_WATER: 1,
    Spell.CROWN_OF_MADNESS: 2,
    Spell.CRUSADERS_MANTLE: 3,
    Spell.CURE_WOUNDS: 1,
    Spell.DANCING_LIGHTS: 0,
    Spell.DARKNESS: 2,
    Spell.DARKVISION: 2,
    Spell.DAYLIGHT: 3,
    Spell.DETECT_EVIL_AND_GOOD: 1,
    Spell.DETECT_MAGIC: 1,
    Spell.DETECT_POISON_AND_DISEASE: 1,
    Spell.DETECT_THOUGHTS: 2,
    Spell.DISGUISE_SELF: 1,
    Spell.DISPEL_MAGIC: 3,
    Spell.DISSONANT_WHISPERS: 1,
    Spell.DIVINE_FAVOR: 1,
    Spell.DIVINE_SMITE: 1,
    Spell.DOMINATE_BEAST: 4,
    Spell.DRAGONS_BREATH: 2,
    Spell.DRUIDCRAFT: 0,
    Spell.ELDRITCH_BLAST: 0,
    Spell.ELEMENTALISM: 0,
    Spell.ELEMENTAL_WEAPON: 3,
    Spell.ENHANCE_ABILITY: 2,
    Spell.ENLARGE_REDUCE: 2,
    Spell.ENSNARING_STRIKE: 1,
    Spell.ENTANGLE: 1,
    Spell.ENTHRALL: 2,
    Spell.EXPEDITIOUS_RETREAT: 1,
    Spell.FAERIE_FIRE: 1,
    Spell.FALSE_LIFE: 1,
    Spell.FEAR: 3,
    Spell.FEATHER_FALL: 1,
    Spell.FEIGN_DEATH: 3,
    Spell.FIND_FAMILIAR: 1,
    Spell.FIND_STEED: 1,
    Spell.FIND_TRAPS: 2,
    Spell.FIREBALL: 3,
    Spell.FIRE_BOLT: 0,
    Spell.FLAME_BLADE: 2,
    Spell.FLAMING_SPHERE: 2,
    Spell.FLY: 3,
    Spell.FOG_CLOUD: 1,
    Spell.FREEDOM_OF_MOVEMENT: 4,
    Spell.FRIENDS: 0,
    Spell.GASEOUS_FORM: 3,
    Spell.GENTLE_REPOSE: 2,
    Spell.GLYPH_OF_WARDING: 3,
    Spell.GOODBERRY: 1,
    Spell.GREASE: 1,
    Spell.GREATER_RESTORATION: 5,
    Spell.GUIDANCE: 0,
    Spell.GUIDING_BOLT: 1,
    Spell.GUST_OF_WIND: 2,
    Spell.HAIL_OF_THORNS: 1,
    Spell.HASTE: 3,
    Spell.HEALING_WORD: 1,
    Spell.HEAT_METAL: 2,
    Spell.HELLISH_REBUKE: 1,
    Spell.HEROISM: 1,
    Spell.HEX: 1,
    Spell.HOLD_PERSON: 2,
    Spell.HUNGER_OF_HADAR: 3,
    Spell.HUNTERS_MARK: 1,
    Spell.HYPNOTIC_PATTERN: 3,
    Spell.ICE_KNIFE: 1,
    Spell.IDENTIFY: 1,
    Spell.ILLUSORY_SCRIPT: 1,
    Spell.INFLICT_WOUNDS: 1,
    Spell.INVISIBILITY: 2,
    Spell.JUMP: 1,
    Spell.KNOCK: 2,
    Spell.LEOMUNDS_TINY_HUT: 3,
    Spell.LESSER_RESTORATION: 2,
    Spell.LEVITATE: 2,
    Spell.LIGHT: 0,
    Spell.LIGHTNING_BOLT: 3,
    Spell.LOCATE_ANIMALS_OR_PLANTS: 2,
    Spell.LOCATE_CREATURE: 4,
    Spell.LOCATE_OBJECT: 2,
    Spell.LONGSTRIDER: 1,
    Spell.MAGE_ARMOR: 1,
    Spell.MAGE_HAND: 0,
    Spell.MAGIC_CIRCLE: 3,
    Spell.MAGIC_MISSILE: 1,
    Spell.MAGIC_MOUTH: 2,
    Spell.MAGIC_WEAPON: 2,
    Spell.MAJOR_IMAGE: 3,
    Spell.MASS_HEALING_WORD: 3,
    Spell.MELD_INTO_STONE: 3,
    Spell.MELFS_ACID_ARROW: 2,
    Spell.MENDING: 0,
    Spell.MESSAGE: 0,
    Spell.MIND_SLIVER: 0,
    Spell.MIND_SPIKE: 2,
    Spell.MINOR_ILLUSION: 0,
    Spell.MIRROR_IMAGE: 2,
    Spell.MISTY_STEP: 2,
    Spell.MOONBEAM: 2,
    Spell.NONDETECTION: 3,
    Spell.NYSTULS_MAGIC_AURA: 2,
    Spell.PASS_WITHOUT_TRACE: 2,
    Spell.PHANTASMAL_FORCE: 2,
    Spell.PHANTOM_STEED: 3,
    Spell.PLANT_GROWTH: 3,
    Spell.POISON_SPRAY: 0,
    Spell.PRAYER_OF_HEALING: 2,
    Spell.PRESTIGITATION: 0,
    Spell.PRODUCE_FLAME: 0,
    Spell.PROTECTION_FROM_ENERGY: 3,
    Spell.PROTECTION_FROM_EVIL_AND_GOOD: 1,
    Spell.PROTECTION_FROM_POISON: 2,
    Spell.PURIFY_FOOD_AND_DRINK: 1,
    Spell.RAY_OF_ENFEEBLEMENT: 2,
    Spell.RAY_OF_FROST: 0,
    Spell.RAY_OF_SICKNESS: 1,
    Spell.REMOVE_CURSE: 3,
    Spell.RESISTANCE: 0,
    Spell.REVIVIFY: 3,
    Spell.ROPE_TRICK: 2,
    Spell.SACRED_FLAME: 0,
    Spell.SANCTUARY: 1,
    Spell.SCORCHING_RAY: 2,
    Spell.SEARING_SMITE: 1,
    Spell.SEE_INVISIBILITY: 2,
    Spell.SENDING: 3,
    Spell.SHATTER: 2,
    Spell.SHIELD: 1,
    Spell.SHIELD_OF_FAITH: 1,
    Spell.SHILLELAGH: 0,
    Spell.SHINING_SMITE: 1,
    Spell.SHOCKING_GRASP: 0,
    Spell.SILENCE: 2,
    Spell.SILENT_IMAGE: 1,
    Spell.SLEEP: 1,
    Spell.SLEET_STORM: 3,
    Spell.SLOW: 3,
    Spell.SPARE_THE_DYING: 0,
    Spell.SPEAK_WITH_ANIMALS: 1,
    Spell.SPEAK_WITH_DEAD: 3,
    Spell.SPEAK_WITH_PLANTS: 3,
    Spell.SPIDER_CLIMB: 2,
    Spell.SPIKE_GROWTH: 2,
    Spell.SPIRITUAL_WEAPON: 2,
    Spell.SPIRIT_GUARDIANS: 3,
    Spell.STARRY_WISP: 0,
    Spell.STINKING_CLOUD: 3,
    Spell.STONESKIN: 4,
    Spell.SUGGESTION: 2,
    Spell.SUMMON_BEAST: 2,
    Spell.SUMMON_FEY: 3,
    Spell.SUMMON_UNDEAD: 3,
    Spell.TASHAS_HIDEOUS_LAUGHTER: 1,
    Spell.TENSERS_FLOATING_DISK: 1,
    Spell.THAUMATURGY: 0,
    Spell.THORN_WHIP: 0,
    Spell.THUNDERCLAP: 0,
    Spell.THUNDEROUS_SMITE: 1,
    Spell.THUNDERWAVE: 1,
    Spell.TOLL_THE_DEAD: 0,
    Spell.TONGUES: 3,
    Spell.TREE_STRIDE: 5,
    Spell.TRUE_STRIKE: 0,
    Spell.UNSEEN_SERVANT: 1,
    Spell.VAMPIRIC_TOUCH: 3,
    Spell.WARDING_BOND: 2,
    Spell.WATER_BREATHING: 3,
    Spell.WATER_WALK: 3,
    Spell.WEB: 2,
    Spell.WIND_WALL: 3,
    Spell.WITCH_BOLT: 1,
    Spell.WORD_OF_RADIANCE: 0,
    Spell.WRATHFUL_SMITE: 1,
    Spell.ZONE_OF_TRUTH: 2,
}
