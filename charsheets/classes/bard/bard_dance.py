from typing import TYPE_CHECKING

from charsheets.classes.bard import Bard
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class BardDanceCollege(Bard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Bard (College of Dance)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {DazzlingFootwork()}
        abilities |= super().class_features()

        return abilities


#################################################################################
class DazzlingFootwork(BaseFeature):
    tag = Feature.DAZZLING_FOOTWORK

    @property
    def desc(self) -> str:
        return f"""While you aren't wearing armor or wielding a Shield, you gain the following benefits.

        Dance Virtuoso. You have Advantage on any Charisma (Performance) check you make that involves you dancing.

        Agile Strikes. When you expend a use of your Bardic Inspiration as part of an action, a Bonus Action, 
        or a Reaction, you can make one Unarmed Strike as part of that action, Bonus Action, or Reaction.

        Bardic Damage. You can use Dexterity instead of Strength for the attack rolls of your Unarmed Strikes. When 
        you deal damage with an Unarmed Strike, you can deal Bludgeoning damage equal to 
        {self.owner.bardic_inspiration_die()} + {self.owner.dexterity.modifier}, instead of the strike's normal damage.
        This roll doesn't expend the die."""

    def mod_ac_bonus(self, character: "Character") -> Reason[int]:
        return Reason("Dazzling Footwork", character.charisma.modifier)


# EOF
