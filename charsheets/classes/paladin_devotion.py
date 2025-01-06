from charsheets.abilities import SacredWeapon
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.paladin import Paladin
from charsheets.spells import Spells


#################################################################################
class PaladinOathOfDevotion(Paladin):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {SacredWeapon()}
        abilities |= super().class_abilities()
        if self.level >= 3:
            self.prepare_spells(Spells.PROTECTION_FROM_EVIL_AND_GOOD, Spells.SHIELD_OF_FAITH)
        if self.level >= 5:
            self.prepare_spells(Spells.AID, Spells.ZONE_OF_TRUTH)
        return abilities


# EOF
