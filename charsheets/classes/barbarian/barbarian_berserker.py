from typing import cast, Any

from aenum import extend_enum

from charsheets.classes.barbarian import Barbarian
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature


#################################################################################
class BarbarianPathOfTheBeserker(Barbarian):

    #############################################################################
    def level3(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(Frenzy())

    #############################################################################
    def level6(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(MindlessRage())

    #############################################################################
    def level10(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(Retaliation())


extend_enum(Feature, "FRENZY", "Frenzy")
extend_enum(Feature, "MINDLESS_RAGE", "Mindless Rage")
extend_enum(Feature, "RETALIATION", "Retaliation")


#############################################################################
class Frenzy(BaseFeature):
    tag = Feature.FRENZY
    _desc = """If you use Reckless Attack while your Rage is active, you deal extra damage to the first target you hit
    on your turn with a Strength-based attack. To determine the extra damage, roll a number of d6s equal to your
    Rage Damage bonus, and add them together. The damage has the same type as the weapon or Unarmed Strike used
    for the attack."""

    @property
    def desc(self) -> str:
        rdb = cast(Barbarian, self.owner.barbarian).rage_dmg_bonus
        return f"""If you use Reckless Attack while your Rage is active, you deal extra damage to the first target 
        you hit on your turn with a Strength-based attack. To determine the extra damage, 
        roll {rdb}d6s, and add them together. The damage has the same type as the weapon or Unarmed 
        Strike used for the attack."""


#############################################################################
class MindlessRage(BaseFeature):
    tag = Feature.MINDLESS_RAGE
    _desc = """You have immunity to the Charmed and Frightened conditions while your Rage is active. If you're
    Charmed or Frightened when you enter your Rage, the condition ends on you."""


#############################################################################
class Retaliation(BaseFeature):
    tag = Feature.RETALIATION
    _desc = """When you take damage from a creature that is within 5 feet of you, you can take a Reaction to
            make one melee attack against that creature, using a weapon or an Unarmed Strike."""


# EOF
