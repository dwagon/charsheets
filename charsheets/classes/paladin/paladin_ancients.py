from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.paladin import Paladin
from charsheets.constants import Ability
from charsheets.spell import Spell


#################################################################################
class PaladinOathOfAncients(Paladin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Paladin (Oath of the Ancients)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {NaturesWrath()}
        abilities |= super().class_abilities()
        self.prepare_spells(Spell.ENSNARING_STRIKE, Spell.SPEAK_WITH_ANIMALS)
        if self.level >= 5:
            self.prepare_spells(Spell.MISTY_STEP, Spell.MOONBEAM)
        return abilities


#############################################################################
class NaturesWrath(BaseAbility):
    tag = Ability.NATURES_WRATH
    _desc = """As a Magic action, you can expend one use of your Channel Divinity to conjure spectral vines around 
    nearby creatures. Each creature of your choice that you can see within 15 feet of yourself must succeed on a 
    Strength saving throw or have the Restrained condition for 1 minute. A Restrained creature repeats the save at the 
    end of each of its turns, ending the effect on itself on a success."""


# EOF
