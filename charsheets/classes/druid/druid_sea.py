from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.druid import Druid
from charsheets.constants import Ability
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class DruidCircleOfTheSea(Druid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Druid (Circle of the Sea)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {
            WrathOfTheSea(),
        }
        self.prepare_spells(Spell.FOG_CLOUD, Spell.GUST_OF_WIND, Spell.RAY_OF_FROST, Spell.SHATTER, Spell.THUNDERWAVE)
        if self.level >= 5:
            self.prepare_spells(Spell.LIGHTNING_BOLT, Spell.WATER_BREATHING)
        if self.level >= 6:
            abilities.add(AquaticAffinity())
        if self.level >= 7:
            self.prepare_spells(Spell.CONTROL_WATER, Spell.ICE_STORM)
        return abilities


#############################################################################
class WrathOfTheSea(BaseAbility):
    tag = Ability.WRATH_OF_THE_SEA

    @property
    def desc(self) -> str:
        dice = max(1, self.owner.wisdom.modifier)
        return f""" As a Bonus Action, you can expend a use of your Wild Shape to manifest a 5-foot Emanation that
        takes the form of ocean spray that surrounds you for 10 minutes. It ends early if you dismiss it (no action
        required), manifest it again, or have the Incapacitated condition.

        When you manifest the Emanation and as a Bonus Action on your subsequent turns, you can choose another
        creature you can see in the Emanation. The target must succeed on a Constitution saving throw against your
        spell save DC or take Cold damage and, if the creature is Large or smaller, be pushed up to 15 feet away from
        you. To determine this damage, roll {dice}d6s"""


#############################################################################
class AquaticAffinity(BaseAbility):
    tag = Ability.AQUATIC_AFFINITY
    _desc = """The size of the Emanation created by your Wrath of the Sea increases to 10 feet.

    In addition, you gain a Swim Speed equal to your Speed."""

    def mod_swim_movement(self, character: "Character") -> Reason[int]:
        return Reason[int]("Aquatic Affinity", character.speed.value)
