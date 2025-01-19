from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.ranger import Ranger
from charsheets.constants import Ability
from charsheets.reason import Reason
from charsheets.spells import Spells

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class RangerFeyWanderer(Ranger):
    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {DreadfulStrikes(), OtherworldlyGlamour(), FeyWandererSpells()}
        abilities |= super().class_abilities()
        return abilities


#############################################################################
class DreadfulStrikes(BaseAbility):
    tag = Ability.DREADFUL_STRIKES
    _desc = """You can augment your weapon strikes with mind-scarring magic drawn from the murky hollows of the
    Fey wild. When you hit a creature with a weapon, you can deal an extra 1d4 Psychic damage to the target,
    which can take this extra damage only once per turn."""


#############################################################################
class OtherworldlyGlamour(BaseAbility):
    tag = Ability.OTHERWORLDLY_GLAMOUR
    _desc = """Whenever you make a Charisma check, you gain a bonus to the check equal to your Wisdom modifier (min +1).
    You also gain proficiency in one of these skills of your choice: Deception, Performance or Persuasion"""
    # TODO - select skill


#############################################################################
class FeyWandererSpells(BaseAbility):
    tag = Ability.FEY_WANDERER_SPELLS
    _desc = """Feywild Gifts

    1 Illusory butterflies flutter around you while you take aShort or Long Rest.

    2 Flowers bloom from your hair each dawn.

    3 You faintly smell of cinnamon, lavender, nutmeg, or another comforting herb or spice.

    4 Your shadow dances while noone is looking directly at it.

    5 Horns or antlers sprout from your head.

    6 Your skin and hair change color each dawn."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        spells = Reason("Fey Wanderer", Spells.CHARM_PERSON)
        if character.level >= 5:
            spells = Reason("Fey Wanderer", Spells.MISTY_STEP)
        return spells


# EOF
