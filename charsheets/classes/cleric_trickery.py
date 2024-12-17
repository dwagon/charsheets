from charsheets.classes.cleric import Cleric
from charsheets.constants import Ability


#################################################################################
class TrickeryDomain(Cleric):
    pass

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {Ability.BLESSING_OF_THE_TRICKSTER, Ability.INVOKE_DUPLICITY, Ability.TRICKERY_DOMAIN_SPELLS}
        return abilities


# EOF
