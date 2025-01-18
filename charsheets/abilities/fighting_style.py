from typing import TYPE_CHECKING

from charsheets.constants import Ability, WeaponProperty
from charsheets.abilities.base_ability import BaseAbility
from charsheets.weapons.base_weapon import BaseWeapon

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Archery(BaseAbility):
    tag = Ability.ARCHERY
    desc = """You gain a +2 bonus to attack rolls you make with Ranged weapons."""
    hide = True

    def mod_ranged_atk_bonus(self, character: "Character", _: BaseWeapon):
        return 2


#############################################################################
class BlindFighting(BaseAbility):
    tag = Ability.BLIND_FIGHTING
    desc = """You have Blindsight with a range of 10 feet."""


#############################################################################
class Defense(BaseAbility):
    tag = Ability.DEFENSE
    desc = """While you're wearing Light, Medium, or Heavy armour, you gain a +1 bonus to Armour Class"""
    hide = True

    def mod_ac_bonus(self, character: "Character") -> int:
        return 1


#############################################################################
class Dueling(BaseAbility):
    tag = Ability.DUELING
    desc = """When you're holding a Melee weapon in one hand and no other weapons, you gain
    a +2 bonus to damage rolls with that weapon."""


#############################################################################
class GreatWeaponFighting(BaseAbility):
    tag = Ability.GREAT_WEAPON_FIGHTING
    desc = """When you roll damage for an attack you make with a Melee weapon that you are holding with two hands,
    you can treat any 1 or 2 on a damage due as a 3. The weapon must have the Two-Handed or Versatile property to gain
    this benefit."""


#############################################################################
class Interception(BaseAbility):
    tag = Ability.INTERCEPTION
    desc = """When a creature you can see hits another creature within 5 feet of you with an attack roll, you can take
        a Reaction to reduce the damage dealt to the target by 1d10 plus your Proficiency Bonus. You must be holding a
        Shield or a Simple or Martial weapon to use this Reaction."""


#############################################################################
class Protection(BaseAbility):
    tag = Ability.PROTECTION
    desc = """When a creature you can see attacks a target other than you that is within 5 feet of you, you can take a
    Reaction to interpose your Shield if you're holding one. You impose Disadvantage on the triggering attack roll and
    all other attack rolls against the target until the start of your next turn if you remain within 5 feet of the
    target."""


#############################################################################
class ThrownWeaponFighting(BaseAbility):
    tag = Ability.THROWN_WEAPON_FIGHTING
    hide = True
    desc = """When you hit with a ranged attack roll using a weapon that has the Thrown property,
    you gain a +2 bonus to the damage roll."""

    def mod_ranged_dmg_bonus(self, character: "Character", weapon: BaseWeapon):
        if WeaponProperty.THROWN in weapon.properties:
            return 2


#############################################################################
class TwoWeaponFighting(BaseAbility):
    tag = Ability.TWO_WEAPON_FIGHTING
    desc = """When you make an extra attack as a result of using a weapon that has the Light property, you can add
    your ability modifier to the damage of that attack if you aren't already adding it to the damage."""


#############################################################################
class UnarmedFighting(BaseAbility):
    tag = Ability.UNARMED_FIGHTING
    desc = """When you hit with your Unarmed Strike and deal damage, you can deal Bludgeoning damage equal to 1d6
    plus your Strength modifier instead of the normal damage of an Unarmed Strike. If you aren't holding any weapons
    or a Shield when you make the attack roll, the d6 becomes a d8.

    At the start of each of your turns, you can deal 1d4 Bludgeoning damage to one creature Grappled by you."""


# EOF
