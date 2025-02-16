from charsheets.classes.barbarian import Barbarian
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature


#################################################################################
class BarbarianPathOfTheBeserker(Barbarian):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Barbarian (Path of the Beserker)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        features: set[BaseFeature] = {Frenzy()}
        if self.level >= 6:
            features.add(MindlessRage())
        if self.level >= 10:
            features.add(Retaliation())
        features |= super().class_features()
        return features


#############################################################################
class Frenzy(BaseFeature):
    tag = Feature.FRENZY
    _desc = """If you use Reckless Attack while your Rage is active, you deal extra damage to the first target you hit
    on your turn with a Strength-based attack. To determine the extra damage, roll a number of d6s equal to your
    Rage Damage bonus, and add them together. The damage has the same type as the weapon or Unarmed Strike used
    for the attack."""

    @property
    def desc(self) -> str:
        return f"""If you use Reckless Attack while your Rage is active, you deal extra damage to the first target 
        you hit on your turn with a Strength-based attack. To determine the extra damage, 
        roll {self.owner.rage_dmg_bonus}d6s, and add them together. The damage has the same type as the weapon or Unarmed 
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
