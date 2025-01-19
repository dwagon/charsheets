from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.wizard import Wizard
from charsheets.constants import Ability
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class WizardIllusionist(Wizard):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {IllusionSavant(), ImprovedIllusions()}
        abilities |= super().class_abilities()
        if self.level >= 6:
            abilities |= {PhantasmalCreatures()}
        return abilities


#############################################################################
class IllusionSavant(BaseAbility):
    tag = Ability.ILLUSION_SAVANT
    _desc = """Choose two Wizard spells from the Illusion school, each of which must be no higher than level 2, 
    and add them to your spellbook for free. In addition, whenever you gain access to a new level of spell slots in 
    this class, you can add one Wizard spell from the Illusion school to your spellbook for free. The chosen spell 
    must be of a level for which you have spell slots."""


#############################################################################
class ImprovedIllusions(BaseAbility):
    tag = Ability.IMPROVED_ILLUSIONS
    _desc = """You can cast Illusion spells without providing Verbal components, and if an Illusion spell you cast has 
    a range 10+ feet, the range is increased by 60 feet.

    You also know the Minor Illusion cantrip. If you already know it, you learn a different Wizard cantrip of your 
    choice. The cantrip doesn't count against your number of cantrips known. You can create both a sound and an image 
    with a single casting of Minor Illusion, and you can cast it as a Bonus Action."""

    def mod_add_known_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Improved Illusions", Spell.MINOR_ILLUSION)


#############################################################################
class PhantasmalCreatures(BaseAbility):
    tag = Ability.PHANTASMAL_CREATURES
    goes = 1
    _desc = """You always have the Summon Beast and Summon Fey spells prepared. Whenever you cast either spell, 
    you can change its school to Illusion, which causes the summoned creature to appear spectral. You can cast the 
    Illusion version of each spell without expending a spell slot, but casting it without a slot halves the 
    creature's Hit Points. Once you cast either spell without a spell slot, you must finish a Long Rest before you 
    can cast the spell in that way again."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Phantasmal Creatures", Spell.SUMMON_FEY, Spell.SUMMON_BEAST)


# EOF
