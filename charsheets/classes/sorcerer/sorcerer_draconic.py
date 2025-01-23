from typing import TYPE_CHECKING

from charsheets.classes.sorcerer import Sorcerer
from charsheets.constants import Feature, Armour
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class SorcererDraconic(Sorcerer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Draconic Sorceror"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {DraconicResilience()}
        abilities |= super().class_features()
        self.prepare_spells(Spell.ALTER_SELF, Spell.CHROMATIC_ORB, Spell.COMMAND)
        if self.level >= 5:
            self.prepare_spells(Spell.FEAR, Spell.FLY)
        if self.level >= 6:
            abilities |= {ElementalAffinity()}
        if self.level >= 7:
            self.prepare_spells(Spell.ARCANE_EYE, Spell.CHARM_MONSTER)

        return abilities


#############################################################################
class DraconicResilience(BaseFeature):
    tag = Feature.DRACONIC_RESILIENCE
    _desc = """The magic in your body manifests physical traits of your draconic gift. Parts of you are covered by 
    dragon-like scales."""
    hide = True

    #############################################################################
    def mod_hp_bonus(self, character: "Character") -> Reason[int]:
        return Reason("Draconic Resilience", character.level)

    #############################################################################
    def mod_ac_bonus(self, character: "Character") -> Reason[int]:
        if character.armour.tag == Armour.NONE and not character.shield:
            return Reason("Draconic Resilience", character.charisma.modifier)  # Dex is already included
        return Reason("Draconic Resilience", 0)


#############################################################################
class ElementalAffinity(BaseFeature):
    tag = Feature.ELEMENTAL_AFFINITY
    _desc = """Your draconic magic has an affinity with a damage type associated with dragons. Choose one of those 
    types: Acid, Cold, Fire, Lightning or Poison.

    You have Resistance to that damage type, and when you cast a spell that deals damage of that type you can add 
    your Charisma modifier to one damage roll of that spell."""

    # TODO - select damage type


# EOF
