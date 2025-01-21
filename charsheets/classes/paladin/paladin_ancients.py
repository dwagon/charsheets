from charsheets.features.base_feature import BaseFeature
from charsheets.classes.paladin import Paladin
from charsheets.constants import Feature
from charsheets.spell import Spell


#################################################################################
class PaladinOathOfAncients(Paladin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Paladin (Oath of the Ancients)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {NaturesWrath()}
        abilities |= super().class_features()
        self.prepare_spells(Spell.ENSNARING_STRIKE, Spell.SPEAK_WITH_ANIMALS)
        if self.level >= 5:
            self.prepare_spells(Spell.MISTY_STEP, Spell.MOONBEAM)
        if self.level >= 7:
            abilities |= {AuraOfWarding()}
        return abilities


#############################################################################
class NaturesWrath(BaseFeature):
    tag = Feature.NATURES_WRATH
    _desc = """As a Magic action, you can expend one use of your Channel Divinity to conjure spectral vines around 
    nearby creatures. Each creature of your choice that you can see within 15 feet of yourself must succeed on a 
    Strength saving throw or have the Restrained condition for 1 minute. A Restrained creature repeats the save at the 
    end of each of its turns, ending the effect on itself on a success."""


#############################################################################
class AuraOfWarding(BaseFeature):
    tag = Feature.AURA_OF_WARDING
    _desc = """Ancient magic lies so heavily upon you that it forms an eldritch ward, blunting energy from beyond the 
    Material Plane; you and your allies have Resistance to Necrotic, Psychic, and Radiant damage while in your Aura 
    of Protection."""


# EOF
