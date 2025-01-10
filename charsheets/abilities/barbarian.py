from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability, Skill
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Rage(BaseAbility):
    tag = Ability.RAGE
    _desc = """Damage Resistance
    Rage Damage
    Strength Advantage"""


#############################################################################
class UnarmoredDefenseBarbarian(BaseAbility):
    tag = Ability.UNARMORED_DEFENSE_BARBARIAN
    _desc = """While you aren't wearing any armor, your base Armor Class equals 10 plus your Constitution and Dexterity 
    modifiers. You can use a Shield and still gain this benefit."""


#############################################################################
class DangerSense(BaseAbility):
    tag = Ability.DANGER_SENSE
    _desc = """You gain an uncanny sense of when things aren't as they should be, giving you an edge when you 
    dodge perils. You have Advantage on Dexterity saving throws unless you have the Incapacitated condition."""


#############################################################################
class RecklessAttack(BaseAbility):
    tag = Ability.RECKLESS_ATTACK
    _desc = """You can throw aside all concern for defense to attack with increased ferocity.
    When you make your first attack roll on your turn, you can decide to attack recklessly. Doing so gives you 
    Advantage on attack rolls using Strength until the start of your next turn, but attack rolls against you have 
    Advantage during that time."""


#############################################################################
class PrimalKnowledge(BaseAbility):
    tag = Ability.PRIMAL_KNOWLEDGE
    _desc = """You gain proficiency in one skill of your choice."""
    hide = True

    def __init__(self, skill: Skill):
        super().__init__()
        self.skill = skill

    def mod_add_skill_proficiency(self, character: "Character") -> Reason[Skill]:
        return Reason("Primal Knowledge", self.skill)


#############################################################################
class Frenzy(BaseAbility):
    tag = Ability.FRENZY
    _desc = """If you use Reckless Attack while your Rage is active, you deal extra damage to the first target you hit
    on your turn with a Strength-based attack. To determine the extra damage, roll a number of d6s equal to your
    Rage Damage bonus, and add them together. The damage has the same type as the weapon or Unarmed Strike used
    for the attack."""


#############################################################################
class AnimalSpeaker(BaseAbility):
    tag = Ability.ANIMAL_SPEAKER
    _desc = """You can cast the Beast Sense and Speak with Animals spells but only as Rituals. Wisdom is your
    spellcasting Ability for them."""


#############################################################################
class RageOfTheWilds(BaseAbility):
    tag = Ability.RAGE_OF_THE_WILDS
    _desc = """Your Rage taps into the primal power of animals. Whenever you activate your Rage, you gain one of the
    following options of your choice.
    
    Bear. While your Rage is active, you have Resistance to every damage type except Force, Necrotic, Psychic and
    Radiant.
    
    Eagle. When you activate your Rage, you can take the Disengage and Dash actions as part of that Bonus Action.
    While yourRage is active, you can take a Bonus Action to take both of those actions.
    
    Wolf. While your Rage is active, your allies have Advantage on attack rolls against any enemy of yours with 5 feet
    of you."""


#############################################################################
class VitalityOfTheTree(BaseAbility):
    tag = Ability.VITALITY_OF_THE_TREE
    _desc = """Your Rage taps into the life force of the World Tree. You gain the following benefits.
    
    Vitality Surge. When you activate your Rage, you gain a number of Temporary Hit Points equal to your
    Barbarian Level.
    
    Life-Giving Force. At the start of each of your turns while your Rage is active, you can choose another
    creature within 10 feet of yourself to gain Temporary Hit Points. To determine the number of Temporary Hit
    Points, roll a number of d6s equal to your Rage Damage bonus, and add them together. If any of these
    Temporary Hit Points remain when your Rage ends, they vanish."""


#############################################################################
class DivineFury(BaseAbility):
    tag = Ability.DIVINE_FURY
    _desc = """You can channel divine power into your strikes. On each of your turns while your Rage is active, the
    first creature you hit with a weapon or an Unarmed Strike takes extra damage equal to 1d6 plus half your
    Barbarian level (rounded down). The extra damage is Necrotic or Radiant; you choose the type each time you deal
    the damage."""


#############################################################################
class WarriorOfTheGods(BaseAbility):
    tag = Ability.WARRIOR_OF_THE_GODS
    _desc = """A divine entity helps ensure you can continue the fight. You have a pool of four d12s that you
    can spend to heal yourself. As a Bonus Action, you can expend dice from the pool, roll them, and regain a number
    of Hit Points equal to the roll's total.
    
    Your pool regains all expended dice when you finish a Long Rest."""


#############################################################################
class FastMovement(BaseAbility):
    tag = Ability.FAST_MOVEMENT
    _desc = """Your speed increases by 10 feet while you aren't wearing Heavy Armor."""

    def mod_add_movement_speed(self, character: "Character") -> Reason[int]:
        return Reason("Fast Movement", 10)


# EOF
