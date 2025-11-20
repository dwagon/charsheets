from typing import Any

from aenum import extend_enum
from charsheets.classes.wizard import Wizard
from charsheets.constants import Feature, Stat
from charsheets.features.base_feature import BaseFeature

extend_enum(Feature, "ABJURATION_SAVANT", "Abjuration Savant")
extend_enum(Feature, "ARCANE_WARD", "Arcane Ward")
extend_enum(Feature, "PROJECTED_WARD", "Projected Ward")
extend_enum(Feature, "SPELL_BREAKER", "Spell Breaker")
extend_enum(Feature, "SPELL_RESISTANCE", "Spell Resistance")


#################################################################################
class WizardAbjurer(Wizard):
    _class_name = "Abjurer"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(AbjurationSavant())
        self.add_feature(ArcaneWard())

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(ProjectedWard())

    #############################################################################
    def level10(self, **kwargs: Any):
        self.add_feature(SpellBreaker())

    #############################################################################
    def level14(self, **kwargs: Any):
        self.add_feature(SpellResistance())


#############################################################################
class AbjurationSavant(BaseFeature):
    tag = Feature.ABJURATION_SAVANT
    hide = True
    _desc = """Choose two Wizard spells from the Abjuration school, each of which must be no higher than level 2,
    and add them to your spellbook for free. In addition, whenever you gain access to a new level of spell slots in
    this class, you can add one Wizard spell from the Abjuration school to your spellbook for free. The chosen spell
    must be of a level for which you have spell slots."""


#############################################################################
class ArcaneWard(BaseFeature):
    tag = Feature.ARCANE_WARD

    @property
    def desc(self) -> str:
        hit_points = self.owner.level * 2 + self.owner.intelligence.modifier
        return f"""You can weave magic around yourself for protection. When you cast an Abjuration spell with a spell
        slot, you can simultaneously use a strand of the spell’s magic to create a magical ward on yourself that
        lasts until you finish a Long Rest. The ward has {hit_points} Hit Points. Whenever you take damage, the ward takes
        the damage instead, and if you have any Resistances or Vulnerabilities, apply them before reducing the ward’s
        Hit Points. If the damage reduces the ward to 0 Hit Points, you take any remaining damage. While the ward
        has O Hit Points, it can’t absorb damage, but its magic remains.

        Whenever you cast an Abjuration spell with a spell slot, the ward regains a number of Hit Points equal to twice
        the level of the spell slot. Alternatively, as a Bonus Action, you can expend a spell slot, and the ward
        regains a number of Hit Points equal to twice the level of the spell slot expended. Once you create the ward,
        you can’t create it again until you finish a Long Rest."""


#############################################################################
class ProjectedWard(BaseFeature):
    tag = Feature.PROJECTED_WARD
    _desc = """When a creature that you can see within 30 feet of yourself takes damage, you can take a Reaction or
    cause your Arcane ward to absorb that damage. If this damage reduces the ward to 0 Hit Points, the warded
    creature takes any remaining damage. If that creature has any Resistances or Vulnerabilities, apply them before
    reducing the ward's Hit Points."""


#############################################################################
class SpellBreaker(BaseFeature):
    tag = Feature.SPELL_BREAKER
    _desc = """You always have the 'Counterspell' and 'Dispel Magic' spells prepared. In addition, you can cast 
    'Dispel Magic' as a Bonus Action, and you can add your Proficiency Bonus to its ability check. When you cast 
    either spell with a spell slot, that slot isn't expended if the spell fails to stop a spell."""


#############################################################################
class SpellResistance(BaseFeature):
    tag = Feature.SPELL_RESISTANCE
    _desc = """You have Advantage on saving throws against spells, and you have Resistance to the damage of spells."""


# EOF
