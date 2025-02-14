from charsheets.classes.wizard import Wizard
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature


#################################################################################
class WizardAbjurer(Wizard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Abjurer"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {AbjurationSavant(), ArcaneWard()}
        abilities |= super().class_features()
        if self.level >= 6:
            abilities |= {ProjectedWard()}
        return abilities


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
    _desc = """You can weave magic around yourself for protection. When you cast an Abjuration spell with a spell slot, 
    you can simultaneously use a strand of the spell’s magic to create a magical ward on yourself that lasts until 
    you finish a Long Rest. The ward has a Hit Point maximum equal to twice your Wizard level plus your Intelligence 
    modifier. Whenever you take damage, the ward takes the damage instead, and if you have any Resistances or 
    Vulnerabilities, apply them before reducing the ward’s Hit Points. If the damage reduces the ward to 0 Hit 
    Points, you take any remaining damage. While the ward has O Hit Points, it can’t absorb damage, but its magic 
    remains.

    Whenever you cast an Abjuration spell with a spell slot, the ward regains a number of Hit Points equal to twice 
    the level of the spell slot. Alternatively, as a Bonus Action, you can expend a spell slot, and the ward 
    regains a number of Hit Points equal to twice the level of the spell slot expended. Once you create the ward, 
    you can’t create it again until you finish a Long Rest."""


#############################################################################
class ProjectedWard(BaseFeature):
    tag = Feature.PROJECTED_WARD
    _desc = """When a creature that you can see within 30 feet of yourself takes damage, you can take a Reaction ro 
    cause your Arcane ward to absorb that damage. If this damage reduces the ward to 0 Hit Points, the warded 
    creature takes any remaining damage. If that creature has any Resistances or Vulnerabilities, apply them before 
    reducing the ward's Hit Points."""


# EOF
