from typing import TYPE_CHECKING

from charsheets.features.base_feature import BaseFeature
from charsheets.classes.monk import Monk
from charsheets.constants import Feature, Skill, Tool
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class MonkWarriorOfMercy(Monk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Monk (Warrior of Mercy)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {HandOfHarm(), HandOfHealing(), ImplementsOfMercy()}
        abilities |= super().class_features()

        if self.level >= 6:
            abilities.add(PhysiciansTouch())

        return abilities


#############################################################################
class HandOfHarm(BaseFeature):
    tag = Feature.HAND_OF_HARM
    _desc = """Once per turn when you hit a creature with an Unarmed Strike and deal damage, you can expend 1 Focus 
    Point to deal extra Necrotic damage equal to one roll of your Martial Arts die plus your Wisdom modifier."""


#############################################################################
class HandOfHealing(BaseFeature):
    tag = Feature.HAND_OF_HEALING
    _desc = """As a Magic action, you can expend 1 Focus Point to touch a creature and restore a number of Hit Points 
    equal to a roll of your Martial Arts die plus your Wisdom modifier. When you use your Flurry of Blows, 
    you can replace one of the Unarmed Strikes with a use of this feature without expending a Focus Point for the 
    healing."""


#############################################################################
class ImplementsOfMercy(BaseFeature):
    tag = Feature.IMPLEMENTS_OF_MERCY
    _desc = """You gain proficiency in the Insight and Medicine skills and proficiency with the Herbalism Kit."""

    def mod_add_tool_proficiency(self, character: "Character") -> Reason[Skill]:
        return Reason("Implements of Mercy", Tool.HERBALISM_KIT)

    def mod_add_skill_proficiency(self, character: "Character") -> Reason[Skill]:
        return Reason("Implements of Mercy", Skill.INSIGHT, Skill.MEDICINE)


#############################################################################
class PhysiciansTouch(BaseFeature):
    tag = Feature.PHYSICIANS_TOUCH
    _desc = """Your Hand of Harm and Hand of Healing improve, as detailed below.

    Hand of Harm. When you use Hand of Harm on a creature, you can also give that creature the Poisoned condition 
    until the end of your next turn.

    Hand of Healing. When you use Hand of Healing, you can also end on of the following conditions on the creature 
    you heal: Blinded, Deafened, Paralyzed, Poisoned or Stunned."""


# EOF
