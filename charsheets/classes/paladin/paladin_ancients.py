from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.paladin import Paladin
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


extend_enum(Feature, "AURA_OF_WARDING", "Aura of Warding")
extend_enum(Feature, "NATURES_WRATH", "Natures Wrath")
extend_enum(Feature, "OATH_OF_ANCIENTS_SPELLS", "Oath of the Ancients Spells")


#################################################################################
class PaladinOathOfAncients(Paladin):
    _class_name = "Paladin (Oath of the Ancients)"

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(NaturesWrath())
        self.add_feature(OathOfAncientsSpells())
        super().level3(**kwargs)

    #############################################################################
    def level7(self, **kwargs: Any):
        self.add_feature(AuraOfWarding())


#############################################################################
class OathOfAncientsSpells(BaseFeature):
    tag = Feature.OATH_OF_ANCIENTS_SPELLS
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason("Oath of the Ancients", Spell.ENSNARING_STRIKE, Spell.SPEAK_WITH_ANIMALS)
        if character.level >= 5:
            spells |= Reason("Oath of the Ancients", Spell.MISTY_STEP, Spell.MOONBEAM)
        if character.level >= 9:
            spells |= Reason("Oath of the Ancients", Spell.PLANT_GROWTH, Spell.PROTECTION_FROM_ENERGY)
        if character.level >= 13:
            spells |= Reason("Oath of the Ancients", Spell.ICE_STORM, Spell.STONESKIN)
        if character.level >= 17:
            spells |= Reason("Oath of the Ancients", Spell.COMMUNE_WITH_NATURE, Spell.TREE_STRIDE)
        return spells


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
