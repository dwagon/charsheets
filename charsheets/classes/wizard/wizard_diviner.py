from charsheets.classes.wizard import Wizard
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature


#################################################################################
class WizardDiviner(Wizard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Diviner"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {DivinationSavant(), Portent()}
        abilities |= super().class_features()
        if self.level >= 6:
            abilities |= {ExpertDivination()}
        return abilities


#############################################################################
class DivinationSavant(BaseFeature):
    tag = Feature.DIVINATION_SAVANT
    _desc = """Choose two Wizard spells from the Divination school, each of which must be no higher than level 2, 
    and add them to your spellbook for free. In addition, whenever you gain access to a new level of spell slots in 
    this class, you can add one Wizard spell from the Divination school to your spellbook for free. The chosen spell 
    must be of a level for which you have spell slots."""


#############################################################################
class Portent(BaseFeature):
    tag = Feature.PORTENT
    _desc = """Glimpses of the future begin to press on your awareness. Whenever you finish a Long Rest, roll two d20s 
    and record the numbers rolled. You can replace any D20 Test made by you or a creature that you can see with one 
    of these foretelling rolls. You must choose to do so before the roll, and you can replace a roll in this way only 
    once per turn.

    Each foretelling roll can be used only once. When you finish a Long Rest, you lose any unused foretelling rolls."""


#############################################################################
class ExpertDivination(BaseFeature):
    tag = Feature.EXPERT_DIVINATION
    _desc = """Casting Divination spells comes so easily to you that it expends only a fraction of your spellcasting 
    efforts. When you cast a Divination spell using a level 2+ spell slot, you regain one expended spell slot. The 
    slot you regain must be of a lower level that the slot you expended and can't be higher than level 5"""


# EOF
