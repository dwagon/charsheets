from typing import Any

from aenum import extend_enum

from charsheets.classes.monk import Monk
from charsheets.constants import Feature, Recovery
from charsheets.features.base_feature import BaseFeature

extend_enum(Feature, "FLEET_STEP", "Fleet Step")
extend_enum(Feature, "OPEN_HAND_TECHNIQUE", "Open Hand Technique")
extend_enum(Feature, "QUIVERING_PALM", "Quivering Palm")
extend_enum(Feature, "WHOLENESS_OF_BODY", "Wholeness of Body")


#################################################################################
class MonkWarriorOfTheOpenHand(Monk):
    _class_name = "Warrior of the Open Hand"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(OpenHandTechnique())
        super().level3(**kwargs)

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(WholenessOfBody())
        super().level6(**kwargs)

    #############################################################################
    def level11(self, **kwargs: Any):
        self.add_feature(FleetStep())

    #############################################################################
    def level17(self, **kwargs: Any):
        self.add_feature(QuiveringPalm())


#############################################################################
class OpenHandTechnique(BaseFeature):
    tag = Feature.OPEN_HAND_TECHNIQUE

    @property
    def desc(self) -> str:
        return f"""Whenever you hit a creature with an attack granted by your Flurry of Blows, you can impose
        one of the following effects on that target. 

        Addle. The target can’t make Opportunity Attacks until the start of its next turn. 
    
        Push. The target must succeed on a Strength saving throw (DC {self.owner.monk.monk_dc}) or be pushed up to 15 feet
        away from you. 
    
        Topple. The target must succeed on a Dexterity saving throw (DC {self.owner.monk.monk_dc}) or have the
        Prone condition."""


#############################################################################
class WholenessOfBody(BaseFeature):
    tag = Feature.WHOLENESS_OF_BODY
    recovery = Recovery.LONG_REST

    @property
    def goes(self) -> int:
        return min(1, self.owner.wisdom.modifier)

    @property
    def desc(self) -> str:
        wismod = self.owner.wisdom.modifier

        return f"""You gain the ability to heal yourself. As a Bonus Action, you can regain
        1{self.owner.monk.martial_arts_die}+{wismod} HP (minimum of 1 HP regained)."""


#############################################################################
class FleetStep(BaseFeature):
    tag = Feature.FLEET_STEP
    _desc = """When you take a Bonus Action other than Step of the Wind, you can also use Step of the Wind 
    immediately after that Bonus Action."""


#############################################################################
class QuiveringPalm(BaseFeature):
    tag = Feature.QUIVERING_PALM
    _desc = """You gain the ability to set up lethal vibrations in someone's body. When you hit a creature with an 
    Unarmed Strike, you can expend 4 Focus Points to start these imperceptible vibrations, which last for a number 
    of days equal to your Monk level. The vibrations are harmless unless you take an action to end them. 
    Alternatively, when you take the Attack action on your turn, you can forgo one of the attacks to end the 
    vibrations. To end them, you and the target must be on the same plane of existence.

    When you end them, the target must make a Constitution saving throw, taking 10d12 Force damage on a failed save 
    or half as much damage on a successful one.

    You can have only one creature under the effect of this feature at a time. You can end the vibrations harmlessly 
    (no action required)."""


# EOF
