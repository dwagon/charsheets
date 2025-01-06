from charsheets.abilities import StarMap, StarryForm
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.druid import Druid


#################################################################################
class DruidCircleOfTheStars(Druid):
    _class_name = "Druid (Circle of the Stars)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {StarMap(), StarryForm()}
        abilities |= super().class_abilities()
        return abilities
