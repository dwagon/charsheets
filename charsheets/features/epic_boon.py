from aenum import extend_enum

from charsheets.constants import Feature, Stat
from charsheets.features.base_feature import StatIncreaseFeature

extend_enum(Feature, "COMBAT_PROWESS", "Boon of Combat Prowess")
extend_enum(Feature, "DIMENSIONAL_TRAVEL", "Boon of Dimensional Travel")
extend_enum(Feature, "ENERGY_RESISTANCE", "Boon of Energy Resistance")
extend_enum(Feature, "FATE", "Boon of Fate")
extend_enum(Feature, "FORTITUDE", "Boon of Fortitude")
extend_enum(Feature, "IRRESITIBLE_OFFENSE", "Boon of Irresistible Offense")
extend_enum(Feature, "RECOVERY", "Boon of Recovery")
extend_enum(Feature, "SKILL", "Boon of Skill")
extend_enum(Feature, "SPEED", "Boon of Speed")
extend_enum(Feature, "SPELL_RECALL", "Boon of Spell Recall")
extend_enum(Feature, "NIGHT_SPIRIT", "Boon of Night Sprit")
extend_enum(Feature, "TRUESIGHT", "Boon of Truesight")


#############################################################################
class BoonOfCombatProwess(StatIncreaseFeature):
    tag = Feature.COMBAT_PROWESS
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY, Stat.CONSTITUTION, Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]
    _desc = """When you miss with an attack roll, you can hit instead. Once you use this benefit,
    you can't use it again until the start of your next turn.."""


#############################################################################
class BoonOfDimensionalTravel(StatIncreaseFeature):
    tag = Feature.DIMENSIONAL_TRAVEL
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY, Stat.CONSTITUTION, Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]
    _desc = """Immediately after you take the Attack action or the Magic action, you can teleport up to 30 feet to an 
    unoccupied space you can see."""


#############################################################################
class BoonOfEnergyResistance(StatIncreaseFeature):
    tag = Feature.ENERGY_RESISTANCE
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY, Stat.CONSTITUTION, Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]
    _desc = """Energy Resistances. You gain Resistance to two of the following damage types of your choice: Acid, 
    Cold, Fire, Lightning, Necrotic, Poison, Psychic, Radiant, or Thunder. Whenever you finish a Long Rest, 
    you can change your choices.

    Energy Redirection. When you take damage of one of the types chosen for the Energy Resistances benefit, 
    you can take a Reaction to direct damage of the same type toward another creature you can see within 60 feet 
    of yourself that isn’t behind Total Cover. If you do so, that creature must succeed on a Dexterity saving throw 
    (DC8 plus your Constitution modifier and Proficiency Bonus) or take damage equal to 2d12 plus your 
    Constitution modifier."""


#############################################################################
class BoonOfFate(StatIncreaseFeature):
    tag = Feature.FATE
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY, Stat.CONSTITUTION, Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]
    _desc = """When you or another creature within 60 feet of you succeeds on or fails a D20 Test, you can roll 2d4 
    and apply the total rolled as a bonus or penalty to the d20 roll. Once you use this benefit, you can’t use it 
    again until you roll Initiative or finish a Short or Long Rest."""


#############################################################################
class BoonOfFortitude(StatIncreaseFeature):
    tag = Feature.FORTITUDE
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY, Stat.CONSTITUTION, Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]
    _desc = """Your Hit Point maximum increases by 40. In addition, whenever you regain Hit Points, you can regain 
    additional Hit Points equal to your Constitution modifier. Once you've regained these additional Hit Points, 
    you can’t do so again until the start of your next turn."""


#############################################################################
class BoonOfIrresistibleOffense(StatIncreaseFeature):
    tag = Feature.IRRESITIBLE_OFFENSE
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY]
    _desc = """Overcome Defenses. The Bludgeoning, Piercing, and Slashing damage you deal always ignores Resistance.

        Overwhelming Strike. When you roll a 20 on the d20 for an attack roll, you can deal extra damage to the 
        target equal to the ability score increased by this feat. The extra damage's type is the same as the attack's 
        type."""


#############################################################################
class BoonOfRecovery(StatIncreaseFeature):
    tag = Feature.RECOVERY
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY, Stat.CONSTITUTION, Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]
    _desc = """Last Stand. When you would be reduced to 0 Hit Points, you can drop to 1 Hit Point instead and regain 
    a number of Hit Points equal to half your Hit Point maximum. Once you use this benefit, you can't use it again 
    until you finish a Long Rest.

    Recover Vitality. You have a pool of ten d1Os. As a Bonus Action, you can expend dice from the pool, roll those 
    dice, and regain a number of Hit Points equal to the roll's total. You regain all the expended dice when you 
    finish a Long Rest."""


#############################################################################
class BoonOfSkill(StatIncreaseFeature):
    tag = Feature.SKILL
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY, Stat.CONSTITUTION, Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]
    _desc = """All-Around Adept. You gain proficiency in all skills.

    Expertise. Choose one skill in which you lack Expertise. You gain Expertise in that skill."""


#############################################################################
class BoonOfSpeed(StatIncreaseFeature):
    tag = Feature.SPEED
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY, Stat.CONSTITUTION, Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]
    _desc = """Escape Artist. As a Bonus Action, you can take the Disengage action, which also ends the Grappled 
    condition on you.

    Quickness. Your Speed increases by 30 feet."""


#############################################################################
class BoonOfSpellRecall(StatIncreaseFeature):
    tag = Feature.SPELL_RECALL
    _valid_stats = [Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]
    _desc = """Free Casting. Whenever you cast a spell with a level 1-4 spell slot, roll ld4. If the number you roll 
    is the same as the slot's level, the slot isn't expended."""


#############################################################################
class BoonOfNightSpirit(StatIncreaseFeature):
    tag = Feature.NIGHT_SPIRIT
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY, Stat.CONSTITUTION, Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]
    _desc = """Merge with Shadows. While within Dim Light or Darkness, you can give yourself the Invisible condition 
    as a Bonus Action. The condition ends on you immediately after you take an action, a Bonus Action, or a Reaction.

    Shadowy Form. While within Dim Light or Darkness, you have Resistance to all damage except Psychic and 
    Radiant."""


#############################################################################
class BoonOfTruesight(StatIncreaseFeature):
    tag = Feature.TRUESIGHT
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY, Stat.CONSTITUTION, Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]
    _desc = """You have Truesight with a range of 60 feet."""


# EOF
