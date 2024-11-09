""" Spells"""

from enum import StrEnum, auto


class Spells(StrEnum):
    """All the Spells"""

    AID = auto()
    ALARM = auto()
    ANIMAL_FRIENDSHIP = auto()
    ANIMAL_MESSENGER = auto()
    ARMOR_OF_AGATHYS = auto()
    ARMS_OF_HADAR = auto()
    AUGURY = auto()
    AURA_OF_VITALITY = auto()
    BANE = auto()
    BARKSKIN = auto()
    BEAST_SENSE = auto()
    BLADE_WARD = auto()
    CALL_LIGHTNING = auto()
    CHARM_PERSON = auto()
    CHILL_TOUCH = auto()
    CLOUD_OF_DAGGERS = auto()
    COMMUNE_WITH_NATURE = auto()
    COMPREHEND_LANGUAGES = auto()
    CONJURE_ANIMALS = auto()
    CONJURE_WOODLAND_ANIMALS = auto()
    CONTINUAL_FLAME = auto()
    CORDON_OF_ARROWS = auto()
    CREATE_OR_DESTROY_WATER = auto()
    CROWN_OF_MADNESS = auto()
    CURE_WOUNDS = auto()
    DARKNESS = auto()
    DARKVISION = auto()
    DAYLIGHT = auto()
    DETECT_MAGIC = auto()
    DETECT_POISON_AND_DISEASE = auto()
    DETECT_THOUGHTS = auto()
    DISPEL_MAGIC = auto()
    DISSONANT_WHISPERS = auto()
    DOMINATE_BEAST = auto()
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
    FAIRIE_FIRE = auto()
    FEIGN_DEATH = auto()
    FIND_TRAPS = auto()
    FLAME_BLADE = auto()
    FLAMING_SPHERE = auto()
    FOG_CLOUD = auto()
    FREEDOM_OF_MOVEMENT = auto()
    FRIENDS = auto()
    GOODBERRY = auto()
    GREATER_RESTORATION = auto()
    GUIDANCE = auto()
    GUST_OF_WIND = auto()
    HAIL_OF_THORNS = auto()
    HEALING_WORD = auto()
    HEAT_METAL = auto()
    HELLISH_REBUKE = auto()
    HEX = auto()
    HOLD_PERSON = auto()
    HUNTERS_MARK = auto()
    ICE_KNIFE = auto()
    ILLUSORY_SCRIPT = auto()
    INVISIBILITY = auto()
    JUMP = auto()
    LESSER_RESTORATION = auto()
    LOCATE_ANIMALS_OR_PLANTS = auto()
    LOCATE_CREATURE = auto()
    LOCATE_OBJECT = auto()
    LONGSTRIDER = auto()
    MAGE_HAND = auto()
    MAGIC_WEAPON = auto()
    MELD_INTO_STONE = auto()
    MENDING = auto()
    MESSAGE = auto()
    MIND_SLIVER = auto()
    MIND_SPIKE = auto()
    MINOR_ILLUSION = auto()
    MIRROR_IMAGE = auto()
    MISTY_STEP = auto()
    MOONBEAM = auto()
    NONDETECTION = auto()
    PASS_WITHOUT_TRACE = auto()
    PHANTASMAL_FORCE = auto()
    PLANT_GROWTH = auto()
    POISON_SPRAY = auto()
    PRESTIGITATION = auto()
    PRODUCE_FLAME = auto()
    PROTECTION_FROM_ENERGY = auto()
    PROTECTION_FROM_EVIL_AND_GOOD = auto()
    PROTECTION_FROM_POISON = auto()
    PURIFY_FOOD_AND_DRINK = auto()
    RAY_OF_ENFEEBLEMENT = auto()
    RESISTANCE = auto()
    REVIVIFY = auto()
    SHILLELAGH = auto()
    SILENCE = auto()
    SLEET_STORM = auto()
    SPARE_THE_DYING = auto()
    SPEAK_WITH_ANIMALS = auto()
    SPEAK_WITH_PLANTS = auto()
    SPIDER_CLIMB = auto()
    SPIKE_GROWTH = auto()
    STARRY_WISP = auto()
    STONESKIN = auto()
    SUGGESTION = auto()
    SUMMON_BEAST = auto()
    SUMMON_FEY = auto()
    TASHAS_HIDEOUS_LAUGHTER = auto()
    THORN_WHIP = auto()
    THUNDERCLAP = auto()
    THUNDERWAVE = auto()
    TOLL_THE_DEAD = auto()
    TREE_STRIDE = auto()
    TRUE_STRIKE = auto()
    UNSEEN_SERVANT = auto()
    WATER_BREATHING = auto()
    WATER_WALK = auto()
    WIND_WALL = auto()
    WITCH_BOLT = auto()


SPELL_LEVELS = {
    Spells.AID: 2,
    Spells.ALARM: 1,
    Spells.ANIMAL_FRIENDSHIP: 1,
    Spells.ANIMAL_MESSENGER: 2,
    Spells.ARMOR_OF_AGATHYS: 1,
    Spells.ARMS_OF_HADAR: 1,
    Spells.AUGURY: 2,
    Spells.AURA_OF_VITALITY: 3,
    Spells.BANE: 1,
    Spells.BARKSKIN: 2,
    Spells.BEAST_SENSE: 2,
    Spells.BLADE_WARD: 0,
    Spells.CALL_LIGHTNING: 3,
    Spells.CHARM_PERSON: 1,
    Spells.CHILL_TOUCH: 0,
    Spells.CLOUD_OF_DAGGERS: 2,
    Spells.COMMUNE_WITH_NATURE: 5,
    Spells.COMPREHEND_LANGUAGES: 1,
    Spells.CONJURE_ANIMALS: 3,
    Spells.CONJURE_WOODLAND_ANIMALS: 4,
    Spells.CONTINUAL_FLAME: 2,
    Spells.CORDON_OF_ARROWS: 2,
    Spells.CREATE_OR_DESTROY_WATER: 1,
    Spells.CROWN_OF_MADNESS: 2,
    Spells.CURE_WOUNDS: 1,
    Spells.DARKNESS: 2,
    Spells.DARKVISION: 2,
    Spells.DAYLIGHT: 3,
    Spells.DETECT_MAGIC: 1,
    Spells.DETECT_POISON_AND_DISEASE: 1,
    Spells.DETECT_THOUGHTS: 2,
    Spells.DISPEL_MAGIC: 3,
    Spells.DISSONANT_WHISPERS: 1,
    Spells.DOMINATE_BEAST: 4,
    Spells.DRUIDCRAFT: 0,
    Spells.ELDRITCH_BLAST: 0,
    Spells.ELEMENTALISM: 0,
    Spells.ELEMENTAL_WEAPON: 3,
    Spells.ENHANCE_ABILITY: 2,
    Spells.ENLARGE_REDUCE: 2,
    Spells.ENSNARING_STRIKE: 1,
    Spells.ENTANGLE: 1,
    Spells.ENTHRALL: 2,
    Spells.EXPEDITIOUS_RETREAT: 1,
    Spells.FAIRIE_FIRE: 1,
    Spells.FEIGN_DEATH: 3,
    Spells.FIND_TRAPS: 2,
    Spells.FLAME_BLADE: 2,
    Spells.FLAMING_SPHERE: 2,
    Spells.FOG_CLOUD: 1,
    Spells.FREEDOM_OF_MOVEMENT: 4,
    Spells.FRIENDS: 0,
    Spells.GOODBERRY: 1,
    Spells.GREATER_RESTORATION: 5,
    Spells.GUIDANCE: 0,
    Spells.GUST_OF_WIND: 2,
    Spells.HAIL_OF_THORNS: 1,
    Spells.HEALING_WORD: 1,
    Spells.HEAT_METAL: 2,
    Spells.HELLISH_REBUKE: 1,
    Spells.HEX: 1,
    Spells.HOLD_PERSON: 2,
    Spells.HUNTERS_MARK: 1,
    Spells.ICE_KNIFE: 1,
    Spells.ILLUSORY_SCRIPT: 1,
    Spells.INVISIBILITY: 2,
    Spells.JUMP: 1,
    Spells.LESSER_RESTORATION: 2,
    Spells.LOCATE_ANIMALS_OR_PLANTS: 2,
    Spells.LOCATE_CREATURE: 4,
    Spells.LOCATE_OBJECT: 2,
    Spells.LONGSTRIDER: 1,
    Spells.MAGE_HAND: 0,
    Spells.MAGIC_WEAPON: 2,
    Spells.MELD_INTO_STONE: 3,
    Spells.MENDING: 0,
    Spells.MESSAGE: 0,
    Spells.MIND_SLIVER: 0,
    Spells.MIND_SPIKE: 2,
    Spells.MINOR_ILLUSION: 0,
    Spells.MIRROR_IMAGE: 2,
    Spells.MISTY_STEP: 2,
    Spells.MOONBEAM: 2,
    Spells.NONDETECTION: 3,
    Spells.PASS_WITHOUT_TRACE: 2,
    Spells.PHANTASMAL_FORCE: 2,
    Spells.PLANT_GROWTH: 3,
    Spells.POISON_SPRAY: 0,
    Spells.PRESTIGITATION: 0,
    Spells.PRODUCE_FLAME: 0,
    Spells.PROTECTION_FROM_ENERGY: 3,
    Spells.PROTECTION_FROM_EVIL_AND_GOOD: 1,
    Spells.PROTECTION_FROM_POISON: 2,
    Spells.PURIFY_FOOD_AND_DRINK: 1,
    Spells.RAY_OF_ENFEEBLEMENT: 2,
    Spells.RESISTANCE: 0,
    Spells.REVIVIFY: 3,
    Spells.SHILLELAGH: 0,
    Spells.SILENCE: 2,
    Spells.SLEET_STORM: 3,
    Spells.SPARE_THE_DYING: 0,
    Spells.SPEAK_WITH_ANIMALS: 1,
    Spells.SPEAK_WITH_PLANTS: 3,
    Spells.SPIDER_CLIMB: 2,
    Spells.SPIKE_GROWTH: 2,
    Spells.STARRY_WISP: 0,
    Spells.STONESKIN: 4,
    Spells.SUGGESTION: 2,
    Spells.SUMMON_BEAST: 2,
    Spells.SUMMON_FEY: 3,
    Spells.TASHAS_HIDEOUS_LAUGHTER: 1,
    Spells.THORN_WHIP: 0,
    Spells.THUNDERCLAP: 0,
    Spells.THUNDERWAVE: 1,
    Spells.TOLL_THE_DEAD: 0,
    Spells.TREE_STRIDE: 5,
    Spells.TRUE_STRIKE: 0,
    Spells.UNSEEN_SERVANT: 1,
    Spells.WATER_BREATHING: 3,
    Spells.WATER_WALK: 3,
    Spells.WIND_WALL: 3,
    Spells.WITCH_BOLT: 1,
}
# EOF
