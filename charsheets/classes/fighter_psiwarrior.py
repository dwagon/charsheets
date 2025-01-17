from charsheets.abilities import PsionicPowerFighter
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.fighter import Fighter


#################################################################################
class FighterPsiWarrior(Fighter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Psi Warrior"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {PsionicPowerFighter()}
        return abilities

    #############################################################################
    @property
    def energy_dice(self) -> str:
        if self.level >= 17:
            return "12 x d12"
        elif self.level >= 13:
            return "10 x d10"
        elif self.level >= 11:
            return "8 x d10"
        elif self.level >= 9:
            return "8 x d8"
        elif self.level >= 5:
            return "6 x d8"
        return "4 x d6"

    #############################################################################
    @property
    def class_special(self) -> str:
        return f"Energy Dice: {self.energy_dice}\n"


# EOF
