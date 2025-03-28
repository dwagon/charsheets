from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.cleric import Cleric
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "BLESSED_HEALER", "Blessed Healer")
extend_enum(Feature, "DISCIPLE_OF_LIFE", "Disciple of Life")
extend_enum(Feature, "LIFE_DOMAIN_SPELLS", "Life Domain Spells")
extend_enum(Feature, "PRESERVE_LIFE", "Preserve Life")


#################################################################################
class ClericLifeDomain(Cleric):

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(LifeDomainSpells())
        self.add_feature(DiscipleOfLife())
        self.add_feature(PreserveLife())
        super().level3(**kwargs)

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(BlessedHealer())


#############################################################################
class LifeDomainSpells(BaseFeature):
    tag = Feature.LIFE_DOMAIN_SPELLS
    _desc = """Your connection to this divine domain ensures you always have certain spells ready. When you reach a
    Cleric level specified in the Life Domain Spells table, you thereafter always have the listed spells prepared."""
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason("Life Domain Spells", Spell.BLESS, Spell.CURE_WOUNDS, Spell.AID, Spell.LESSER_RESTORATION)
        if character.level >= 5:
            spells |= Reason("Life Domain Spells", Spell.MASS_HEALING_WORD, Spell.REVIVIFY)
        if character.level >= 7:
            spells |= Reason("Life Domain Spells", Spell.AURA_OF_LIFE, Spell.DEATH_WARD)
        if character.level >= 9:
            spells |= Reason("Life Domain Spells", Spell.GREATER_RESTORATION, Spell.MASS_CURE_WOUNDS)
        return spells


#############################################################################
class DiscipleOfLife(BaseFeature):
    tag = Feature.DISCIPLE_OF_LIFE
    _desc = """When a spell you cast with a spell slot restores Hit Points to a creature, that creature regains
    additional Hit Points on the turn you cast the spell. The additional Hit Points equal 2 plus the spell
    slot’s level."""


#############################################################################
class PreserveLife(BaseFeature):
    tag = Feature.PRESERVE_LIFE
    _desc = ""

    @property
    def desc(self) -> str:
        return f"""As a Magic action, you present your Holy Symbol and expend a use of your Channel Divinity to evoke 
        healing energy that can restore {self.owner.level * 5} Hit Points. Choose Bloodied creatures within 30 feet 
        of yourself (which can include you), and divide those Hit Points among them. This feature can
        restore a creature to no more than half its Hit Point maximum."""


#################################################################################
class BlessedHealer(BaseFeature):
    tag = Feature.BLESSED_HEALER
    _desc = """The healing spells you cast on others heal you as well. Immediately after you cast a spell with a spell 
    slot that restores Hit Points to one or more creatures other than yourself, you regain Hit Points equal to 2 plus 
    the spell slot's level."""


# EOF
