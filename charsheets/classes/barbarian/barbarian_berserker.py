from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.barbarian import Barbarian
from charsheets.constants import Ability


#################################################################################
class BarbarianPathOfTheBeserker(Barbarian):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Barbarian (Path of the Beserker)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {Frenzy()}
        if self.level >= 6:
            abilities.add(MindlessRage())
        abilities |= super().class_abilities()
        return abilities


#############################################################################
class Frenzy(BaseAbility):
    tag = Ability.FRENZY
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
class MindlessRage(BaseAbility):
    tag = Ability.MINDLESS_RAGE
    _desc = """You have immunity to the Charmed and Frightened conditions while your Rage is active. If you're
    Charmed or Frightened when you enter your Rage, the condition ends on you."""


# EOF
