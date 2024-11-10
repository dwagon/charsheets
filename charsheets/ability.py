""" Abilities"""

from charsheets.constants import Ability
from charsheets.exception import UnhandledException


#############################################################################
class BaseAbility:
    desc = "Unspecified"


#############################################################################
class AbilityDeftExplorer(BaseAbility):
    desc = """Thanks to your travels, you gain the following benefits.
    
    Expertise. Choose one of your skill proficiencies with which you lack Expertise. You gain Expertise in that skill.
    
    Languages. You know two languages of your choice"""


#############################################################################
class AbilityColossusSlayer(BaseAbility):
    desc = """Your tenacity can wear down even the most resilient foes.
    When you hit a creature with a weapon, the weapon deals an extra 1d8 damage to the target if it’s missing any
    of its Hit Points. You can deal this extra damage only once per turn."""


#############################################################################
class AbilityFightingStyle(BaseAbility):
    desc = """You gain a Fighting Style fear of your choice. Instead of choosing one of those feats you can choose the
    option below.
    
    Druidic Warrior. You learn two Druid cantrips of your choice. The chosen cantrips count as Ranger spells for you,
    and Wisdom is your spellcasting ability for them. Whenever you gain a Ranger level, you can replace one of these
    cantrips with another Druid cantrip."""


#############################################################################
class AbilityHuntersLore(BaseAbility):
    desc = """You can call on the forces of nature to reveal certain strengths and weaknesses of your prey.
    While a creature is marked by your Hunter’s Mark, you know whether that creature has any
    Immunities, Resistances, or Vulnerabilities, and if the creature has any, you know what they are."""


#############################################################################
class AbilityUnarmoredDefense(BaseAbility):
    desc = """While you aren't wearing any armor, your base Armor Class equals 10 plus your Constitution and Dexterity 
    modifiers. You can use a Shield and still gain this benefit."""


#############################################################################
class AbilityDangerSense(BaseAbility):
    desc = """You gain an uncanny sense of when things aren't as they should be, giving you an edge when you 
    dodge perils. You have Advantage on Dexterity saving throws unless you have the Incapacitated condition."""


#############################################################################
class AbilityResourceful(BaseAbility):
    desc = """You gain Heroic Inspiration whenever you finish a Long Rest."""


#############################################################################
class AbilitySkillful(BaseAbility):
    desc = """You gain proficiency in one skill of your choice."""


#############################################################################
class AbilityDarkvision120(BaseAbility):
    desc = """You have Darkvision with a range of 120 feet"""


#############################################################################
class AbilityDarkvision60(BaseAbility):
    desc = """You have Darkvision with a range of 60 feet"""


#############################################################################
class AbilityDwarvenResilience(BaseAbility):
    desc = """You have Resistance to Poison damage. You also have Advantage on saving throws you make to avoid or
    end the Poisoned condition,."""


#############################################################################
class AbilityDwarvenToughness(BaseAbility):
    desc = """Your Hit Point maximum increases by 1, and it increases by 1 again whenever you gain a level."""


#############################################################################
class AbilityEldritchInvocation(BaseAbility):
    desc = ""


#############################################################################
class AbilityHuntersPrey(BaseAbility):
    desc = """You gain one of the following. Whenever you finish a Long Rest you can replace the option.
    
    Colossus Slayer. Your tenacity can wear down even the most resilient foes. When you hit a creature with a weapon,
    the weapon deals an extra 1d8 damage to the target if its missing any of its Hit Points. You can deal this extra 
    damage only once per turn.
    
    Horde Breaker. Once on each of your turns when you make an attack with a weapon, you can make another attack with 
    the same weapon against a different creature that is within 5 feet of the original target, that is within the 
    weapon's range, and you haven't attacked this turn.
    """


#############################################################################
class AbilityStonecunning(BaseAbility):
    desc = """As a Bonus Action, you gain Tremorsense with a range of 60 feet for 10 minutes.
    You must be on a stone surface or touching a stone surface to use this Tremorsense. 
    The stone can be natural or worked. You can use this Bonus Action a number of times equal to your Proficiency Bonus,
     and you regain expended uses when you finish a Long Rest."""


#############################################################################
class AbilityRage(BaseAbility):
    desc = """Damage Resistance
    Rage Damage
    Strength Advantage"""


#############################################################################
class AbilityRecklessAttack(BaseAbility):
    desc = """You can throw aside all concern for defense to attack with increased ferocity.
    When you make your first attack roll on your turn, you can decide to attack recklessly. Doing so gives you 
    Advantage on attack rolls using Strength until the start of your next turn, but attack rolls against you have 
    Advantage during that time."""


#############################################################################
class AbilityPrimalKnowledge(BaseAbility):
    desc = """You gain proficiency in one skill of your choice."""


#############################################################################
class AbilityDruidic(BaseAbility):
    desc = """You know Druidic, the secret language of Druids."""


#############################################################################
class AbilityPrimalOrder(BaseAbility):
    desc = """You have dedicated yourself to one of the following sacred roles: Magician, Warden."""


#############################################################################
class AbilityWildShape(BaseAbility):
    desc = """The power of nature allows you to assume the form of an animal.
    As a Bonus Action, you shape-shift into a Beast form that you have learned for this feature."""


#############################################################################
class AbilityWildCompanion(BaseAbility):
    desc = """You can summon a nature spirit that assumes an animal form to aid you. As a Magic action,
    you can expend a spell slot or a use of Wild Shape to cast the Find Familiar spell without Material components.
    When you cast the spell in this way, the familiar is Fey and disappears when you finish a long rest."""


#############################################################################
class AbilityPactMagic(BaseAbility):
    desc = """You know two Warlock cantrips"""


#############################################################################
class AbilityMagicalCunning(BaseAbility):
    desc = """You can perform an esoteric rite for 1 minute. At the end of it, you regain expended Pact Magic spell
    slots but no more than a numer equal to half your maximum (round up). Once you use this feature, you can't do so
    again until you finish a Long Rest."""


#############################################################################
class AbilityWeaponMastery(BaseAbility):
    desc = """Your training with weapons allows you to use the mastery properties of two kinds of weapons of your choice with which you have proficiency.
     Whenever you finish a Long Rest, you can change the kinds of weapons you choose."""


#############################################################################
class AbilityFavoredEnemy(BaseAbility):
    desc = """You always have the Hunter's Mark spell prepared. You can cast it twice without expending a spell slot
    and you regain all expended uses of this ability when you finish a Long Rest.
    """


#############################################################################
class AbilitySecondWind(BaseAbility):
    desc = """You have a limited well of physical and mental stamina that you can draw on. As a Bonus Action,
    you can use it to regain Hit Points equal to 1d10 plus your Fighter Level.
    
    You can use this feature twice. You regain one expended use when you finish a Short Rest, and you regain all
    expended uses when you finish a Long Rest.
    """


############################################################################
class AbilityActionSurge(BaseAbility):
    desc = """You can push yourself beyond your normal limits for a moment. On your turn, you can take one additional
    action, except the Magic action.
    
    Once you use this feature, you can't do so again until you finish a Short or Long Rest.
    """


############################################################################
class AbilityTacticalMind(BaseAbility):
    desc = """You have a mind for tactics on and off the battlefield. When you fail an ability check you can expend
     a use of your Second Wind to push yourself toward success. Rather than regaining Hit Points, you roll 1d10 and add
      the number tolled to the ability check, potentially turning it into a success. If the check still fails, this use
       of Second Wind isn't expended.
    """


############################################################################
class AbilityImprovedCritical(BaseAbility):
    desc = "Your attack rolls with weapons and Unarmed Strikes can score a Critical Hit on a roll of 19 or 20 on the d20"


############################################################################
class AbilityRemarkableAthlete(BaseAbility):
    desc = """Thanks to your athleticism, you have Advantage on Initiative rolls and Strength(Athletics) checks.
    
    In addition, immediately after you score a Critical Hit, you can move up to half your Speed without provoking 
    Opportunity Attacks."""


#############################################################################
ability_mapping = {
    Ability.DRUIDIC: AbilityDruidic,
    Ability.WILD_SHAPE: AbilityWildShape,
    Ability.WILD_COMPANION: AbilityWildCompanion,
    Ability.DARKVISION60: AbilityDarkvision60,
    Ability.DANGER_SENSE: AbilityDangerSense,
    Ability.FIGHTING_STYLE: AbilityFightingStyle,
    Ability.WEAPON_MASTERY: AbilityWeaponMastery,
    Ability.FAVOURED_ENEMY: AbilityFavoredEnemy,
    Ability.UNARMORED_DEFENSE: AbilityUnarmoredDefense,
    Ability.DEFT_EXPLORER: AbilityDeftExplorer,
    Ability.COLOSSUS_SLAYER: AbilityColossusSlayer,
    Ability.HUNTERS_LORE: AbilityHuntersLore,
    Ability.HUNTERS_PREY: AbilityHuntersPrey,
    Ability.RESOURCEFUL: AbilityResourceful,
    Ability.SKILLFUL: AbilitySkillful,
    Ability.DARKVISION120: AbilityDarkvision120,
    Ability.DWARVEN_RESILIANCE: AbilityDwarvenResilience,
    Ability.DWARVEN_TOUGHNESS: AbilityDwarvenToughness,
    Ability.RECKLESS_ATTACK: AbilityRecklessAttack,
    Ability.STONE_CUNNING: AbilityStonecunning,
    Ability.PRIMAL_KNOWLEDGE: AbilityPrimalKnowledge,
    Ability.PRIMAL_ORDER: AbilityPrimalOrder,
    Ability.ELDRITCH_INVOCATIONS: AbilityEldritchInvocation,
    Ability.PACT_MAGIC: AbilityPactMagic,
    Ability.MAGICAL_CUNNING: AbilityMagicalCunning,
    Ability.SECOND_WIND: AbilitySecondWind,
    Ability.ACTION_SURGE: AbilityActionSurge,
    Ability.TACTICAL_MIND: AbilityTacticalMind,
    Ability.IMPROVED_CRITICAL: AbilityImprovedCritical,
    Ability.REMARKABLE_ATHLETE: AbilityRemarkableAthlete,
}


#############################################################################
def get_ability(ability: Ability):
    try:
        return ability_mapping[ability]
    except KeyError:
        raise UnhandledException(f"Unknown ability {ability}")


# EOF
