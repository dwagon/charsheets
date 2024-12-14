from charsheets.classes.fighter import Fighter
from charsheets.constants import Ability


#################################################################################
class PsiWarrior(Fighter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.energy_dice = self.get_energy_dice()
        self._class_name = "Psi Warrior"

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {Ability.PSIONIC_POWER}
        return abilities

    #############################################################################
    def get_energy_dice(self) -> str:
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
