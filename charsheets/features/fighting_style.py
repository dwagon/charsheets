from typing import TYPE_CHECKING

from aenum import extend_enum
from charsheets.constants import Feature, WeaponProperty
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.weapons.base_weapon import BaseWeapon

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "ARCHERY", "Archery")
extend_enum(Feature, "BLIND_FIGHTING", "Blind Fighting")
extend_enum(Feature, "DEFENSE", "Defense")
extend_enum(Feature, "DUELING", "Dueling")
extend_enum(Feature, "GREAT_WEAPON_FIGHTING", "Great Weapon Fighting")
extend_enum(Feature, "INTERCEPTION", "Interception")
extend_enum(Feature, "PROTECTION", "Protection")
extend_enum(Feature, "THROWN_WEAPON_FIGHTING", "Thrown Weapon Fighting")
extend_enum(Feature, "TWO_WEAPON_FIGHTING", "Two Weapon Fighting")
extend_enum(Feature, "UNARMED_FIGHTING", "Unarmed Fighting")


#############################################################################
class Archery(BaseFeature):
    tag = Feature.ARCHERY
    desc = """You gain a +2 bonus to attack rolls you make with Ranged weapons."""
    hide = True

    def mod_ranged_atk_bonus(self, weapon: BaseWeapon, character: "BaseCharacter") -> Reason[int]:
        return Reason("Archery", 2)


#############################################################################
class BlindFighting(BaseFeature):
    tag = Feature.BLIND_FIGHTING
    desc = """You have Blindsight with a range of 10 feet."""


#############################################################################
class Defense(BaseFeature):
    tag = Feature.DEFENSE
    desc = """While you're wearing Light, Medium, or Heavy armour, you gain a +1 bonus to Armour Class"""
    hide = True

    def mod_ac_bonus(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Defense", 1)


#############################################################################
class Dueling(BaseFeature):
    tag = Feature.DUELING
    desc = """When you're holding a Melee weapon in one hand and no other weapons, you gain
    a +2 bonus to damage rolls with that weapon."""


#############################################################################
class GreatWeaponFighting(BaseFeature):
    tag = Feature.GREAT_WEAPON_FIGHTING
    desc = """When you roll damage for an attack you make with a Melee weapon that you are holding with two hands,
    you can treat any 1 or 2 on a damage die as a 3. The weapon must have the Two-Handed or Versatile property to gain
    this benefit."""


#############################################################################
class Interception(BaseFeature):
    tag = Feature.INTERCEPTION
    desc = """When a creature you can see hits another creature within 5 feet of you with an attack roll, you can take
        a Reaction to reduce the damage dealt to the target by 1d10 plus your Proficiency Bonus. You must be holding a
        Shield or a Simple or Martial weapon to use this Reaction."""


#############################################################################
class Protection(BaseFeature):
    tag = Feature.PROTECTION
    desc = """When a creature you can see attacks a target other than you that is within 5 feet of you, you can take a
    Reaction to interpose your Shield if you're holding one. You impose Disadvantage on the triggering attack roll and
    all other attack rolls against the target until the start of your next turn if you remain within 5 feet of the
    target."""


#############################################################################
class ThrownWeaponFighting(BaseFeature):
    tag = Feature.THROWN_WEAPON_FIGHTING
    hide = True
    desc = """When you hit with a ranged attack roll using a weapon that has the Thrown property,
    you gain a +2 bonus to the damage roll."""

    def mod_ranged_dmg_bonus(self, weapon: BaseWeapon, character: "BaseCharacter") -> Reason[int]:
        if WeaponProperty.THROWN in weapon.properties:
            return Reason("Thrown Weapon Fighting", 2)
        return Reason()


#############################################################################
class TwoWeaponFighting(BaseFeature):
    tag = Feature.TWO_WEAPON_FIGHTING
    desc = """When you make an extra attack as a result of using a weapon that has the Light property, you can add
    your ability modifier to the damage of that attack if you aren't already adding it to the damage."""


#############################################################################
class UnarmedFighting(BaseFeature):
    tag = Feature.UNARMED_FIGHTING
    desc = """When you hit with your Unarmed Strike and deal damage, you can deal Bludgeoning damage equal to 1d6
    plus your Strength modifier instead of the normal damage of an Unarmed Strike. If you aren't holding any weapons
    or a Shield when you make the attack roll, the d6 becomes a d8.

    At the start of each of your turns, you can deal 1d4 Bludgeoning damage to one creature Grappled by you."""


# EOF