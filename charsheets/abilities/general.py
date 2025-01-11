from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability, Sense
from charsheets.reason import Reason

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class Darkvision120(BaseAbility):
    tag = Ability.DARKVISION120
    _desc = """You have Darkvision with a range of 120 feet"""
    hide = True

    def mod_add_sense(self, character: "Character") -> Reason[Sense]:
        return Reason("Darkvsion120", Sense.DARKVISION120)


#############################################################################
class Darkvision60(BaseAbility):
    tag = Ability.DARKVISION60
    _desc = """You have Darkvision with a range of 60 feet"""
    hide = True

    def mod_add_sense(self, character: "Character") -> Reason[Sense]:
        return Reason("Darkvsion60", Sense.DARKVISION60)


#############################################################################
class ExtraAttack(BaseAbility):
    tag = Ability.EXTRA_ATTACK
    _desc = """You can attack twice instead of once whenever you take the Attack action on your turn."""


#############################################################################
class WeaponMastery(BaseAbility):
    tag = Ability.WEAPON_MASTERY
    _desc = """Your training with weapons allows you to use the mastery properties of two kinds of weapons of your
    choice with which you have proficiency. Whenever you finish a Long Rest, you can change the kinds of weapons
    you choose."""


# EOF
