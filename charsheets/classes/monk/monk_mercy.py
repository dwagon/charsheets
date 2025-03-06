from typing import TYPE_CHECKING

from aenum import extend_enum

from charsheets.classes.monk import Monk
from charsheets.constants import Feature, Skill, Tool, Recovery
from charsheets.features.base_feature import BaseFeature
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
            abilities |= {PhysiciansTouch()}
        if self.level >= 11:
            abilities |= {FlurryOfHealingAndHarm()}

        return abilities


extend_enum(Feature, "FLURRY_OF_HEALING_AND_HARM", "Flurry of Healing and Harm")
extend_enum(Feature, "HAND_OF_HARM", "Hand of Harm")
extend_enum(Feature, "HAND_OF_HEALING", "Hand of Healing")
extend_enum(Feature, "IMPLEMENTS_OF_MERCY", "Implements of Mercy")
extend_enum(Feature, "PHYSICIANS_TOUCH", "Physicians Touch")


#############################################################################
class HandOfHarm(BaseFeature):
    tag = Feature.HAND_OF_HARM

    @property
    def desc(self) -> str:
        result = f"""Once per turn when you hit a creature with an Unarmed Strike and deal damage, you can expend 1 Focus 
        Point to deal an extra 1{self.owner.martial_arts_die}+{self.owner.wisdom.modifier} Necrotic damage. """
        if self.owner.level >= 6:  # Physicians Touch
            result += """You can also give that creature the Poisoned condition until the end of your next turn."""
        return result


#############################################################################
class HandOfHealing(BaseFeature):
    tag = Feature.HAND_OF_HEALING

    @property
    def desc(self) -> str:
        result = f"""As a Magic action, you can expend 1 Focus Point to touch a creature and restore
        1{self.owner.martial_arts_die}+{self.owner.wisdom.modifier} HP. When you use your Flurry of Blows,
        you can replace one of the Unarmed Strikes with a use of this feature without expending a Focus Point
        for the healing. """
        if self.owner.level >= 6:  # Physicians Touch
            result += """You can also end on of the following conditions on the creature 
    you heal: Blinded, Deafened, Paralyzed, Poisoned or Stunned."""
        return result


#############################################################################
class ImplementsOfMercy(BaseFeature):
    tag = Feature.IMPLEMENTS_OF_MERCY
    hide = True
    _desc = """You gain proficiency in the Insight and Medicine skills and proficiency with the Herbalism Kit."""

    def mod_add_tool_proficiency(self, character: "Character") -> Reason[Skill]:
        return Reason("Implements of Mercy", Tool.HERBALISM_KIT)

    def mod_add_skill_proficiency(self, character: "Character") -> Reason[Skill]:
        return Reason("Implements of Mercy", Skill.INSIGHT, Skill.MEDICINE)


#############################################################################
class PhysiciansTouch(BaseFeature):
    tag = Feature.PHYSICIANS_TOUCH
    hide = True
    _desc = ""


#############################################################################
class FlurryOfHealingAndHarm(BaseFeature):
    tag = Feature.FLURRY_OF_HEALING_AND_HARM
    recovery = Recovery.LONG_REST

    @property
    def goes(self) -> int:
        return min(1, self.owner.wisdom.modifier)

    _desc = """When you use Flurry of Blows, you can replace each of the Unarmed Strikes with a use of Hand of 
    Healing without expending Focus Points for the healing.

    In addition, when you make an Unarmed Strike with Flurry of Blows and deal damage, you can use Hand of Harm with 
    that strike without expending a Focus Point for Hand of Harm. You can still use Hand of Harm only once per turn."""


# EOF
