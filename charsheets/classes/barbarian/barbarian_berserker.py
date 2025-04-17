from typing import cast, Any

from aenum import extend_enum

from charsheets.classes.barbarian import Barbarian
from charsheets.constants import Feature, Recovery, Stat
from charsheets.features.base_feature import BaseFeature

extend_enum(Feature, "FRENZY", "Frenzy")
extend_enum(Feature, "INTIMIDATING_PRESENCE", "Intimidating Presence")
extend_enum(Feature, "MINDLESS_RAGE", "Mindless Rage")
extend_enum(Feature, "RETALIATION", "Retaliation")


#################################################################################
class BarbarianPathOfTheBerserker(Barbarian):
    _class_name = "Berserker"
    _sub_class = True

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
        self.add_feature(Retaliation())

    #############################################################################
    def level14(self, **kwargs: Any):
        self.add_feature(IntimidatingPresence())


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


#############################################################################
class IntimidatingPresence(BaseFeature):
    tag = Feature.INTIMIDATING_PRESENCE
    recovery = Recovery.LONG_REST
    _goes = 1

    @property
    def desc(self) -> str:
        dc = 8 + self.owner.stats[Stat.STRENGTH].modifier + self.owner.proficiency_bonus
        return f"""As a Bonus Action, you can strike terror into others with your menacing presence and primal power. 
        When you do so, each creature of your choice in a 30-foot Emanation originating from ycm must make a Wisdom 
        saving throw (DC {dc}). On a failed save, a creature has the Frightened condition for 1 minute. At the end of 
        each of the Frightened creature's turns, the creature repeats the save, ending the effect on itself on a 
        success.
    
    Once you use this feature, you can't use it again until you finish a Long Rest unless you expend a use of your 
    Rage (no action required) to restore your use of it."""


# EOF
