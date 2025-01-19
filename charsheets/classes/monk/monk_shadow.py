from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.monk import Monk
from charsheets.constants import Ability
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class MonkWarriorOfShadow(Monk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Monk (Warrior of Shadow)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {ShadowArts()}
        abilities |= super().class_abilities()
        if self.level >= 6:
            abilities.add(ShadowStep())
        return abilities


#############################################################################
class ShadowArts(BaseAbility):
    tag = Ability.SHADOW_ARTS
    _desc = """You have learned to draw on the power of the Shadowfell, gaining the following benefits. 

    Darkness. You can expend 1 Focus Point to cast the Darkness spell without spell components. You can see within 
    the spell’s area when you cast it with this feature. While the spell persists, you can move its area of Darkness 
    to a space within 60 feet of yourself at the start of each of your turns.

    Darkvision. You gain Darkvision with a range of 60 feet. If you already have Darkvision, its range increases by 
    60 feet.

    Shadowy Figments. You know the Minor Illusion spell. Wisdom is your spellcasting ability for it."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Shadow Arts", Spell.MINOR_ILLUSION)


#############################################################################
class ShadowStep(BaseAbility):
    tag = Ability.SHADOW_STEP
    _desc = """While entirely within Dim Light or Darkness, you can use a Bonus Action to teleport up to 60 feet to 
    an unoccupied space you can see that is also in Dim Light or Darkness. You then have Advantage on the next melee 
    attack you make before the end of the current turn."""


# EOF
