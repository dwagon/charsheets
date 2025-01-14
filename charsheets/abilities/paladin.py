from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability
from charsheets.reason import Reason
from charsheets.spells import Spells

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class LayOnHands(BaseAbility):
    tag = Ability.LAY_ON_HANDS
    _desc = """Your blessed touch can heal wounds. You have a pool of healing power that replenishes when you finish 
    a Long Rest.With that pool, you can restore a total number of Hit Points equal to five times your Paladin level.

    As a Bonus Action, you can touch a creature (which could be yourself) and draw power from the pool of healing to 
    restore a number of Hit Points to that creature, up to the maximum amount remaining in the pool.

    You can also expend 5 Hit Points from the pool of healing power to remove the Poisoned condition from the creature; 
    those points don’t also restore Hit Points to the creature."""


#############################################################################
class PaladinsSmite(BaseAbility):
    tag = Ability.PALADINS_SMITE
    _desc = """You always have the Divine Smite spell prepared. In addition, you can cast it without expending a 
    spell slot, but you must finish a Long Rest before you can cast it in this way again."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        return Reason("Paladin's Smite", Spells.DIVINE_SMITE)


#############################################################################
class SacredWeapon(BaseAbility):
    tag = Ability.SACRED_WEAPON
    _desc = """When you take the Attack action, you can expend one use of your Channel Divinity to imbue one Melee 
    weapon that you are holding with positive energy. For 10 minutes or until you use this feature again, you add your 
    Charisma modifier to attack rolls you make with that weapon (minimum bonus of +1), and each time you hit with it,
    you cause it to deal its normal damage type or Radiant damage. The weapon also emits Bright Light in a 20-foot 
    radius and Dim Light 20 feet beyond that. You can end this effect early (no action required). This effect also 
    ends if you aren't carrying the weapon.
    """


#############################################################################
class PeerlessAthlete(BaseAbility):
    tag = Ability.PEERLESS_ATHLETE
    _desc = """As a Bonus Action, you can expend one use of your Channel Divinity to augment your athleticism. For 1 
    hour, you have Advantage on Strength (Athletics) and Dexterity (Acrobatics) checks, and the distance of your Long 
    and High Jumps increases by 10 feet

    In addition, whenever an ally enters your Aura of Protection for the first time on a turn or starts their turn
    there, the ally's Speed increases by 10 feet until the end of their next turn."""


#############################################################################
class NaturesWrath(BaseAbility):
    tag = Ability.NATURES_WRATH
    _desc = """As a Magic action, you can expend one use of your Channel Divinity to conjure spectral vines around 
    nearby creatures. Each creature of your choice that you can see within 15 feet of yourself must succeed on a 
    Strength saving throw or have the Restrained condition for 1 minute. A Restrained creature repeats the save at the 
    end of each of its turns, ending the effect on itself on a success."""


#############################################################################
class VowOfEmnity(BaseAbility):
    tag = Ability.VOW_OF_EMNITY
    _desc = """When you take the Attack action, you can expend one use of your Channel Divinity to utter a vow of
    enmity against a creature you can see within 30 feet of yourself. You have Advantage on attack rolls
    against the creature for 1 minute or until you use this feature again.

    If the creature drops to O Hit Points before the vow ends, you can transfer the vow to a different creature within 
    30 feet of yourself (no action required)."""


#############################################################################
class InspiringSmite(BaseAbility):
    tag = Ability.INSPIRING_SMITE
    _desc = """Immediately after you cast Divine Smite, you can expend one use of your Channel Divinity and 
    distribute Temporary Hit Points to creatures of your choice within 30 feet of yourself, which can include you. 
    The total number of Temporary Hit Points equals 2d8 plus your Paladin level, divided among the chosen creatures 
    however you like."""


#############################################################################
class FaithfulSteed(BaseAbility):
    tag = Ability.FAITHFUL_STEED
    _desc = """You always have the Find Steed spell prepared. You can also cast the spell once without expending a 
    spell slot, and you regain the ability to do so when you finish a Long Rest."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        return Reason("Faithful Steed", Spells.FIND_STEED)


#############################################################################
class AuraOfProtection(BaseAbility):
    tag = Ability.AURA_OF_PROTECTION
    _desc = """You radiate a protective, unseeable aura in a 10-foot Emanation that originates from you. The aura is 
    inactive while you have the Incapacitated condition.

    You and your allies in the aura gain a bonus to saving throws equal to your Charisma modifier (minimum bonus of +1).

    If another Paladin is present, a creature can benefit from only one Aura of Protection at a time; the creature 
    chooses which aura while in them."""


# EOF
