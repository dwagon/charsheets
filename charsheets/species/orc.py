from charsheets.constants import Feature, Recovery
from charsheets.features import Darkvision120
from charsheets.features.base_feature import BaseFeature
from charsheets.species.base_species import BaseSpecies


#############################################################################
class Orc(BaseSpecies):
    #########################################################################
    def species_feature(self) -> set[BaseFeature]:
        results: set[BaseFeature] = {RelentlessEndurance(), Darkvision120(), AdrenalinRush()}
        return results


#############################################################################
class RelentlessEndurance(BaseFeature):
    tag = Feature.RELENTLESS_ENDURANCE
    goes = 1
    recovery = Recovery.LONG_REST
    _desc = """When you are reduced to 0 Hit Points but not killed outright, you can drop to 1 Hit Point instead."""


#############################################################################
class AdrenalinRush(BaseFeature):
    tag = Feature.ADRENALIN_RUSH
    recovery = Recovery.SHORT_REST

    @property
    def goes(self) -> int:
        return self.owner.proficiency_bonus

    @property
    def desc(self) -> str:
        return f"""You can take the Dash action as a Bonus Action. When you do so, you gain a Bonus Action. When you do 
    so, you gain {self.owner.proficiency_bonus} Temporary Hit Points."""


# EOF
