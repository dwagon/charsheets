from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability
from charsheets.species import Species
from charsheets.abilities import Darkvision120


#############################################################################
class Orc(Species):
    #########################################################################
    def species_abilities(self) -> set[BaseAbility]:
        results: set[BaseAbility] = {RelentlessEndurance(), Darkvision120(), AdrenalinRush()}
        return results


#############################################################################
class RelentlessEndurance(BaseAbility):
    tag = Ability.RELENTLESS_ENDURANCE
    _desc = """When you are reduced to 0 Hit Points but not killed outright, you can drop to 1 Hit Point instead. 
    Once you use this trait, you can't do so again until you finish a Long Rest."""


#############################################################################
class AdrenalinRush(BaseAbility):
    tag = Ability.ADRENALIN_RUSH
    _desc = """You can take the Dash action as a Bonus Action. When you do so, you gain a Bonus Action. When you do 
    so, you gain a number a number of Temporary Hit Points equal to your Proficiency Bonus. 
    
    You can use this trait a number of times equal to your Proficiency Bonus, and you regain all expended uses when 
    you finish a Short or Long Rest."""


# EOF
