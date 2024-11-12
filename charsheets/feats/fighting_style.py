from typing import TYPE_CHECKING

from charsheets.constants import Feat
from charsheets.feat import BaseFeat

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class FeatArchery(BaseFeat):
    tag = Feat.ARCHERY
    desc = """You gain a +2 bonus to attack rolls you make with Ranged weapons."""

    @classmethod
    def ranged_atk_bonus(cls, character: "Character"):
        return 2


#############################################################################
class FeatBlindFighting(BaseFeat):
    tag = Feat.BLIND_FIGHTING
    desc = """You have Blindsight with a range of 10 feet."""


#############################################################################
class FeatDefense(BaseFeat):
    tag = Feat.DEFENSE
    desc = """While you're wearing Light, Medium, or Heavy armour, you gain a +1 bonus to Armour Class"""


#############################################################################
class FeatDueling(BaseFeat):
    tag = Feat.DUELING
    desc = """When you're holding a Melee weapon in one hand and no other weapons, you gain
    a +2 bonus to damage rolls with that weapon."""


#############################################################################
class FeatGreatWeaponFighting(BaseFeat):
    tag = Feat.GREAT_WEAPON_FIGHTING
    desc = """When you roll damage for an attack you make with a Melee weapon that you are holding with two hands,
    you can treat any 1 or 2 on a damage due as a 3. The weapon must have the Two-Handed or Versatile property to gain
    this benefit."""


#############################################################################
class FeatInterception(BaseFeat):
    tag = Feat.INTERCEPTION
    desc = """When a creature you can see his another creature within 5 feet of you with an attack roll, you can take a
    Reaction to reduce the damage dealth to the target by 1d10 plus your Proficiency Bonus. You must be holding a
    Shield or a Simple or Martial weapon to use this Reaction."""


#############################################################################
class FeatProtection(BaseFeat):
    tag = Feat.PROTECTION
    desc = """When a creature you can see attacks a target other than you that is within 5 feet of you, you can take a
    Reaction to interpose your Shield if you're holding one. You impose Disadvantage on the triggering attack roll and
    all other attack rolls against the target until the start of your next turn if you remain within 5 feet of the
    target."""


#############################################################################
class FeatThrownWeaponFighting(BaseFeat):
    tag = Feat.THROWN_WEAPON_FIGHTING
    desc = """When you hit with a ranged attack roll using a weapon that has the Thrown property,
    you gain a +2 bonus to the damage roll."""


#############################################################################
class FeatTwoWeaponFighting(BaseFeat):
    tag = Feat.TWO_WEAPON_FIGHTING
    desc = """When you make an extra attack as a result of using a weapon that has the Light property, you can add 
    your ability modifier to the damage of that attack if you aren't already adding it to the damage."""


#############################################################################
class FeatUnarmedFighting(BaseFeat):
    tag = Feat.UNARMED_FIGHTING
    desc = """When you hit with your Unarmed Strike and deal damage, you can deal Bludgeoning damage equal to 1d6
    plus your Strength modifier instrad of the normal damage of an Unarmed Strike. If you aren't holding any weapons
    or a Shield when you make the attack roll, the d6 becomes a d8.
    At the start of each of your turns, you can deal 1d4 Bludgeoning damage to one creature Grappled by you."""


# EOF
