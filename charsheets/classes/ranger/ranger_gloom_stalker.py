from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.ranger import Ranger
from charsheets.constants import Ability
from charsheets.spells import Spells

if TYPE_CHECKING:  # pragma: no coverage
    pass


#################################################################################
class RangerGloomStalker(Ranger):
    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {DreadAmbusher(), UmbralSight()}
        abilities |= super().class_abilities()

        self.prepare_spells(Spells.DISGUISE_SELF)
        if self.level >= 5:
            self.prepare_spells(Spells.ROPE_TRICK)

        return abilities


#############################################################################
class DreadAmbusher(BaseAbility):
    tag = Ability.DREAD_AMBUSHER
    _desc = """You have mastered the art of creating fearsome ambushes, granting you the following benefits.

    Ambusher's Leap.  At the start of your first turn of each combat, your Speed increases by 10 feet until the end 
    of that turn.

    Dreadful Strike. When you attack a creature and hit it with a weapon, you can deal an extra 2d6 Psychic damage. 
    You can use this benefit only once per turn, you can use it a number of times equal to your Wisdom modifier (
    minimum of once), and you regain all expended uses when you finish a Long Rest.

    Initiative Bonus. When you roll Initiative, you can add your Wisdom modifier to the roll."""


#############################################################################
class UmbralSight(BaseAbility):
    tag = Ability.UMBRAL_SIGHT
    _desc = """You gain Darkvision with a range of 60 feet. If you already have Darkvision, its range increases by 60
    feet.

    You are also adept at evading creatures that rely on Darkvision. While entirely in Darkness, you have the
    Invisible condition to any creature that relies on Darkvision to see you in that Darkness."""

    # TODO - darkvision


# EOF
