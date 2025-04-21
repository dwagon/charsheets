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
extend_enum(Feature, "UNDYING_SENTINEL", "Undying Sentinel")
extend_enum(Feature, "ELDER_CHAMPION", "Elder Champion")


#################################################################################
class PaladinOathOfAncients(Paladin):
    _class_name = "Paladin (Oath of the Ancients)"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(NaturesWrath())
        self.add_feature(OathOfAncientsSpells())
        super().level3(**kwargs)

    #############################################################################
    def level7(self, **kwargs: Any):
        self.add_feature(AuraOfWarding())

    #############################################################################
    def level15(self, **kwargs: Any):
        self.add_feature(UndyingSentinel())

    #############################################################################
    def level20(self, **kwargs: Any):
        self.add_feature(ElderChampion())


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


#############################################################################
class UndyingSentinel(BaseFeature):
    tag = Feature.UNDYING_SENTINEL
    _desc = """When you are reduced to O Hit Points and not killed outright, you can drop to 1 Hit Point instead, 
    and you regain a number of Hit Points equal to three times your Paladin level. Once you use this feature, 
    you can't do so again until you finish a Long Rest. Additionally, you can't be aged magically, and you cease 
    visibly aging."""


#############################################################################
class ElderChampion(BaseFeature):
    tag = Feature.ELDER_CHAMPION
    _desc = """As a Bonus Action, you can imbue your Aura of Protection with primal power, granting the benefits 
    below for 1 minute or until you end them (no action required). Once you use this feature, you can't use it again 
    until you finish a Long Rest. You can also restore your use of it by expending a level 5 spell slot (no action 
    required).

    Diminish Defiance. Enemies in the aura have Disadvantage on saving throws against your spells and Channel 
    Divinity options.

    Regeneration. At the start of each of your turns, you regain 10 Hit Points.

    Swift Spells. Whenever you cast a spell that has a casting time of an action, you can cast it using a Bonus 
    Action instead."""


# EOF
