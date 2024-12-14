from aenum import StrEnum, auto


#############################################################################
class Movements(StrEnum):
    SPEED = auto()
    SWIM = auto()
    FLY = auto()


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

    ACTION_SURGE = auto()
    ARCANE_RECOVERY = auto()
    BLESSING_OF_THE_TRICKSTER = auto()
    BRAVE = auto()
    BREATH_WEAPON = auto()
    CELESTIAL_RESISTANCE = auto()
    CELESTIAL_REVELATION = auto()
    CHANNEL_DIVINITY = auto()
    CIRCLE_FORMS = auto()
    CLOUDS_JAUNT_GIANT_ANCESTRY = auto()
    COLOSSUS_SLAYER = auto()
    COMBAT_SUPERIORITY = auto()
    DANGER_SENSE = auto()
    DARKVISION120 = auto()
    DARKVISION60 = auto()
    DARK_ONES_BLESSING = auto()
    DEFT_EXPLORER = auto()
    DISCIPLE_OF_LIFE = auto()
    DRACONIC_DAMAGE_RESISTANCE = auto()
    DRACONIC_FLIGHT = auto()
    DRUIDIC = auto()
    DWARVEN_RESILIANCE = auto()
    DWARVEN_TOUGHNESS = auto()
    ELDRITCH_INVOCATIONS = auto()
    FAVOURED_ENEMY = auto()
    FIGHTING_STYLE = auto()
    FRENZY = auto()
    GUIDED_STRIKE = auto()
    HALFLING_NIMBLENESS = auto()
    HEALING_HANDS = auto()
    HEALING_LIGHT = auto()
    HUNTERS_LORE = auto()
    HUNTERS_PREY = auto()
    IMPROVED_CRITICAL = auto()
    INVOKE_DUPLICITY = auto()
    LANDS_AID = auto()
    LAND_SPELL_ARID = auto()
    LAND_SPELL_POLAR = auto()
    LAND_SPELL_TEMPERATE = auto()
    LAND_SPELL_TROPICAL = auto()
    LIFE_DOMAIN_SPELLS = auto()
    LIGHT_BEARER = auto()
    LIGHT_DOMAIN_SPELLS = auto()
    LUCK = auto()
    MAGICAL_CUNNING = auto()
    NATURALLY_STEALTHY = auto()
    NONE = auto()
    PACT_MAGIC = auto()
    PRESERVE_LIFE = auto()
    PRIMAL_KNOWLEDGE = auto()
    PSIONIC_POWER = auto()
    PSYCHIC_SPELLS = auto()
    RADIANCE_OF_THE_DAWN = auto()
    RAGE = auto()
    RECKLESS_ATTACK = auto()
    REMARKABLE_ATHLETE = auto()
    RESOURCEFUL = auto()
    RITUAL_ADEPT = auto()
    SCHOLAR = auto()
    SECOND_WIND = auto()
    SKILLFUL = auto()
    STARRY_FORM = auto()
    STAR_MAP = auto()
    STEPS_OF_THE_FEY = auto()
    STONES_ENDURANCE_GIANT_ANCESTRY = auto()
    STONE_CUNNING = auto()
    STUDENT_OF_WAR = auto()
    TACTICAL_MIND = auto()
    TRICKERY_DOMAIN_SPELLS = auto()
    UNARMORED_DEFENSE = auto()
    WARDING_FLARE = auto()
    WAR_BOND = auto()
    WAR_DOMAIN_SPELLS = auto()
    WAR_PRIEST = auto()
    WEAPON_MASTERY = auto()
    WILD_COMPANION = auto()
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
class Proficiencies(StrEnum):
    SIMPLE_WEAPONS = auto()
    MARTIAL_WEAPONS = auto()
    LIGHT_ARMOUR = auto()
    MEDIUM_ARMOUR = auto()
    HEAVY_ARMOUR = auto()
    SHIELDS = auto()


# EOF
