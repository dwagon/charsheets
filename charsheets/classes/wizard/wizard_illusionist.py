from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.wizard import Wizard
from charsheets.constants import Feature, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "ILLUSION_SAVANT", "Illuion Savant")
extend_enum(Feature, "ILLUSORY_SELF", "Illusory Self")
extend_enum(Feature, "IMPROVED_ILLUSIONS", "Improved Illusions")
extend_enum(Feature, "PHANTASMAL_CREATURES", "Phantasmal Creatures")


#################################################################################
class WizardIllusionist(Wizard):

    #############################################################################
    def level3(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(IllusionSavant())
        self.add_feature(ImprovedIllusions())

    #############################################################################
    def level6(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(PhantasmalCreatures())

    #############################################################################
    def level10(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(IllusorySelf())


#############################################################################
class IllusionSavant(BaseFeature):
    tag = Feature.ILLUSION_SAVANT
    hide = True
    _desc = """Choose two Wizard spells from the Illusion school, each of which must be no higher than level 2, 
    and add them to your spellbook for free. In addition, whenever you gain access to a new level of spell slots in 
    this class, you can add one Wizard spell from the Illusion school to your spellbook for free. The chosen spell 
    must be of a level for which you have spell slots."""


#############################################################################
class ImprovedIllusions(BaseFeature):
    tag = Feature.IMPROVED_ILLUSIONS
    _desc = """You can cast Illusion spells without providing Verbal components, and if an Illusion spell you cast has 
    a range 10+ feet, the range is increased by 60 feet.

    You also know the Minor Illusion cantrip. If you already know it, you learn a different Wizard cantrip of your 
    choice. The cantrip doesn't count against your number of cantrips known. You can create both a sound and an image 
    with a single casting of Minor Illusion, and you can cast it as a Bonus Action."""

    def mod_add_known_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Improved Illusions", Spell.MINOR_ILLUSION)


#############################################################################
class PhantasmalCreatures(BaseFeature):
    tag = Feature.PHANTASMAL_CREATURES
    goes = 1
    _desc = """You always have the Summon Beast and Summon Fey spells prepared. Whenever you cast either spell, 
    you can change its school to Illusion, which causes the summoned creature to appear spectral. You can cast the 
    Illusion version of each spell without expending a spell slot, but casting it without a slot halves the 
    creature's Hit Points. Once you cast either spell without a spell slot, you must finish a Long Rest before you 
    can cast the spell in that way again."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Phantasmal Creatures", Spell.SUMMON_FEY, Spell.SUMMON_BEAST)


#############################################################################
class IllusorySelf(BaseFeature):
    tag = Feature.ILLUSORY_SELF
    _goes = 1
    recovery = Recovery.SHORT_REST
    _desc = """When a creature hits you with an attack roll, you can take a Reaction to interpose an illusory 
    duplicate of yourself between the attacker and yourself. The attack automatically misses you, then the illusion 
    dissipates.

    You can restore your use of it by expending a level 2+ spell slot (no action required)."""


# EOF
