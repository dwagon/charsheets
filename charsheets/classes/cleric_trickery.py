from charsheets.abilities import BlessingOfTheTrickster, InvokeDuplicity, TrickeryDomainSpells
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.cleric import Cleric


#################################################################################
class ClericTrickeryDomain(Cleric):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {BlessingOfTheTrickster(), InvokeDuplicity(), TrickeryDomainSpells()}
        return abilities


# EOF
