from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability, DamageType
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class EldritchInvocation(BaseAbility):
    tag = Ability.ELDRITCH_INVOCATIONS
    _desc = """You have unearthed Eldritch Invocations, pieces of forbidden knowledge that imbue you with an abiding
    magical ability or other lessons."""


#############################################################################
class PactMagic(BaseAbility):
    tag = Ability.PACT_MAGIC
    _desc = """You know two Warlock cantrips"""


#############################################################################
class MagicalCunning(BaseAbility):
    tag = Ability.MAGICAL_CUNNING
    goes = 1
    _desc = """You can perform an esoteric rite for 1 minute. At the end of it, you regain expended Pact Magic spell
    slots but no more than a numer equal to half your maximum (round up). Once you use this feature, you can't do so
    again until you finish a Long Rest."""


#############################################################################
class StepsOfTheFey(BaseAbility):
    tag = Ability.STEPS_OF_THE_FEY
    _desc = """Your patron grants you the ability to move between the boundaries of the planes. You can cast
    Misty Step without expending a spell slot a number of times equal to your Charisma modifier (min once), and 
    you regain all expended uses when you finish a Long Rest.
    
    In addition, whenever you cast that spell, you can choose one of the following additional effects.
    
    Refreshing Step. Immediately after you teleport, you or one creature you can see within 10 feet of yourself
    gains 1d10 Temporary Hit Points.
    
    Taunting Step. Creatures within 5 feet of the space you left must succeed on a Wisdom saving throw against your
    spell save DC or have Disadvantage on attack rolls against creatures other than you until the start of your
    next turn."""


#############################################################################
class HealingLight(BaseAbility):
    tag = Ability.HEALING_LIGHT
    _desc = """You gain the ability to channel celestial energy to heal wounds. You have a pool of d6s to fuel this
    healing. The number of dice in the pool equals 1 plus your Warlock level.
    
    As a Bonus Action, you can heal yourself or one creature you can see within 60 feet of yourself, expending dice
    from the pool. The maximum number of dice you can expend at once equals your Charisma modifier (minimum of one die).
    Roll the dice you expend, and restore a number of Hit Points equal to the roll's total. Your pool regains all
    expended dice when you finish a Long Rest.
    """


#############################################################################
class DarkOnesBlessing(BaseAbility):
    tag = Ability.DARK_ONES_BLESSING

    @property
    def desc(self) -> str:
        bonus = max(1, self.owner.charisma.modifier + self.owner.level)

        return f"""When you reduce an enemy to 0 Hit Points, you gain {bonus} Temporary Hit Points. You also gain this 
    benefit if someone else reduces an enemy within 10 feet of you to 0 Hit Points."""


#############################################################################
class PsychicSpells(BaseAbility):
    tag = Ability.PSYCHIC_SPELLS
    _desc = """When you cast a Warlock spell that deals damage, you can change its damage type to Psychic. In addition,
    when you cast a Warlock spell that is an Enchantment or Illusion, you can do so without Verbal or Somatic
    components."""


#############################################################################
class MistyEscape(BaseAbility):
    tag = Ability.MISTY_ESCAPE
    _desc = """You can cast Misty Step as a Reaction in response to taking damage.
    
    In addition, the following effects are now among your Steps of the Fey options.
    
    Disappearing Step. You have the Invisible condition until the start of your next turn or until immediate after 
    you make an attack roll, deal damage, or cast a spell.
    
    Dreadful Step. Creatures within 5 feet of the space you left or the space you appear in (your choice) must 
    succeed on a Wisdom saving throw against your spell save DC or take 2d10 Psychic damage."""


#############################################################################
class RadiantSoul(BaseAbility):
    tag = Ability.RADIANT_SOUL
    _desc = """Your link to your patron allows you to serve as a conduit for radiant energy. You have Resistance to 
    Radiant damage. Once per turn, when a spell you cast deals Radiant or Fire damage, you can add your Charisma 
    modifier to that spell's damage against one of the spell's targets."""

    def mod_add_damage_resistances(self, character: "Character") -> Reason[DamageType]:
        return Reason("Radiant Soul", DamageType.RADIANT)


#############################################################################
class DarkOnesOwnLuck(BaseAbility):
    tag = Ability.DARK_ONES_OWN_LUCK

    @property
    def goes(self) -> int:
        return max(1, self.owner.charisma.modifier)

    @property
    def desc(self) -> str:
        return f"""You can call on your fiendish patron to alter fate in your favour. When you make an ability check or a 
    saving throw, you can use this feature to add 1d10 to your roll. You can do so after seeing the roll but before 
    any of the roll's effects occur.
    
    You can use this feature {self.goes} times, but you can use it 
    no more that once per roll. You regain all expended uses when you finish a Long Rest."""


#############################################################################
class ClairvoyantCombatant(BaseAbility):
    tag = Ability.CLAIRVOYANT_COMBATANT
    goes = 1
    _desc = """When you form a telepathic bond with a creature using your Awakened Mind, you can force that creature 
    to make a Wisdom saving throw against your spell save DC. On a failed save, the creature has Disadvantage on 
    attack rolls against you, and you have Advantage on attack rolls against that creature for the duration of the bond.
    
    Once you use this feature, you can't use it again until you finish a Short or Long Rest unless you expend a Pact 
    Magic spell slot (no action required) to restore your use of it."""


# EOF
