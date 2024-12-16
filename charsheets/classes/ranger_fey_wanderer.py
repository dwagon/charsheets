from charsheets.classes.ranger import Ranger
from charsheets.constants import Ability
from charsheets.spells import Spells


#################################################################################
class FeyWanderer(Ranger):
    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = {Ability.DREADFUL_STRIKES, Ability.OTHERWORLDLY_GLAMOUR}
        abilities |= super().class_abilities()
        self.prepare_spells(Spells.CHARM_PERSON)
        return abilities


# EOF
