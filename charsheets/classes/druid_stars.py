from charsheets.abilities import StarMap, StarryForm, CosmicOmen
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.druid import Druid


#################################################################################
class DruidCircleOfTheStars(Druid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Druid (Circle of the Stars)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {StarMap(), StarryForm()}
        abilities |= super().class_abilities()
        if self.level >= 6:
            abilities.add(CosmicOmen())
        return abilities
