from charsheets.abilities import VowOfEmnity
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.paladin import Paladin
from charsheets.spells import Spells


#################################################################################
class PaladinOathOfVengeance(Paladin):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {VowOfEmnity()}
        abilities |= super().class_abilities()
        if self.level >= 3:
            self.prepare_spells(Spells.BANE, Spells.HUNTERS_MARK)
        if self.level >= 5:
            self.prepare_spells(Spells.HOLD_PERSON, Spells.MISTY_STEP)
        return abilities


# EOF
