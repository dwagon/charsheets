from aenum import extend_enum

from charsheets.classes.monk import Monk
from charsheets.constants import Feature, Recovery
from charsheets.features.base_feature import BaseFeature


#################################################################################
class MonkWarriorOfTheOpenHand(Monk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Monk (Warrior of the Open Hand)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {OpenHandTechnique()}
        abilities |= super().class_features()
        if self.level >= 6:
            abilities |= {WholenessOfBody()}
        if self.level >= 11:
            abilities |= {FleetStep()}
        return abilities


extend_enum(Feature, "FLEET_STEP", "Fleet Step")
extend_enum(Feature, "OPEN_HAND_TECHNIQUE", "Open Hand Technique")
extend_enum(Feature, "WHOLENESS_OF_BODY", "Wholeness of Body")


#############################################################################
class OpenHandTechnique(BaseFeature):
    tag = Feature.OPEN_HAND_TECHNIQUE

    @property
    def desc(self) -> str:
        return f"""Whenever you hit a creature with an attack granted by your Flurry of Blows, you can impose
        one of the following effects on that target. 

        Addle. The target can’t make Opportunity Attacks until the start of its next turn. 
    
        Push. The target must succeed on a Strength saving throw (DC {self.owner.monk_dc}) or be pushed up to 15 feet
        away from you. 
    
        Topple. The target must succeed on a Dexterity saving throw (DC {self.owner.monk_dc}) or have the
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
        1{self.owner.martial_arts_die}+{wismod} HP (minimum of 1 HP regained)."""


#############################################################################
class FleetStep(BaseFeature):
    tag = Feature.FLEET_STEP
    _desc = """When you take a Bonus Action other than Step of the Wind, you can also use Step of the Wind 
    immediately after that Bonus Action."""


# EOF
