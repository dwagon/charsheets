from typing import TYPE_CHECKING

from charsheets.classes.druid import Druid
from charsheets.constants import Feature, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class DruidCircleOfTheLand(Druid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Druid (Circle of the Land)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        """Only one of these should be active at one time"""
        abilities: set[BaseFeature] = set()
        abilities |= super().class_features()
        abilities |= {
            LandsAid(),
            LandSpellArid(),
            LandSpellTropical(),
            LandSpellPolar(),
            LandSpellTemperate(),
        }
        if self.level >= 6:
            abilities.add(NaturalRecovery())
        if self.level >= 10:
            abilities.add(NaturesWard())
        return abilities


#############################################################################
class LandsAid(BaseFeature):
    tag = Feature.LANDS_AID
    _desc = """As a Magic action, you can expend a use of your Wild Shape a choose a point within 60 feet of yourself.
    Vitality-giving flowers and life-draining thorns appear for a moment in a 10-foot-radius Sphere centered on
    that point. Each creature of your choice in the Sphere must make a Constitution saving throw against your
    spell save DC, taking 2d6 Necrotic damage on a failed save or half as much damage on a successful one. One
    creature of your choice in that area regains 2d6 Hit Points."""


#############################################################################
class LandSpellArid(BaseFeature):
    tag = Feature.LAND_SPELL_ARID
    _desc = """Arid Land"""
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason("Arid Land", Spell.BLUR, Spell.BURNING_HANDS, Spell.FIRE_BOLT)
        if character.level >= 5:
            spells |= Reason("Arid Land", Spell.FIREBALL)
        if character.level >= 7:
            spells |= Reason("Arid Land", Spell.BLIGHT)
        if character.level >= 9:
            spells |= Reason("Arid Land", Spell.WALL_OF_STONE)
        return spells


#############################################################################
class LandSpellTropical(BaseFeature):
    tag = Feature.LAND_SPELL_TROPICAL
    _desc = """Tropical Land"""
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason("Tropical Land", Spell.ACID_SPLASH, Spell.RAY_OF_SICKNESS, Spell.WEB)
        if character.level >= 5:
            spells |= Reason("Tropical Land", Spell.STINKING_CLOUD)
        if character.level >= 7:
            spells |= Reason("Tropical Land", Spell.POLYMORPH)
        if character.level >= 9:
            spells |= Reason("Tropical Land", Spell.INSECT_PLAGUE)
        return spells


#############################################################################
class LandSpellPolar(BaseFeature):
    tag = Feature.LAND_SPELL_POLAR
    _desc = """Polar Land"""
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason("Polar Land", Spell.FOG_CLOUD, Spell.HOLD_PERSON, Spell.RAY_OF_FROST)
        if character.level >= 5:
            spells |= Reason("Polar Land", Spell.SLEET_STORM)
        if character.level >= 5:
            spells |= Reason("Polar Land", Spell.ICE_STORM)
        if character.level >= 9:
            spells |= Reason("Polar Land", Spell.CONE_OF_COLD)
        return spells


#############################################################################
class LandSpellTemperate(BaseFeature):
    tag = Feature.LAND_SPELL_TEMPERATE
    _desc = """ Temperate Land"""
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason("Temperate Land", Spell.MISTY_STEP, Spell.SHOCKING_GRASP, Spell.SLEEP)
        if character.level >= 5:
            spells |= Reason("Temperate Land", Spell.LIGHTNING_BOLT)
        if character.level >= 7:
            spells |= Reason("Temperate Land", Spell.FREEDOM_OF_MOVEMENT)
        if character.level >= 9:
            spells |= Reason("Temperate Land", Spell.TREE_STRIDE)
        return spells


#############################################################################
class NaturalRecovery(BaseFeature):
    tag = Feature.NATURAL_RECOVERY
    goes = 1
    recovery = Recovery.LONG_REST
    _desc = """You can cast one of the level 1+ spells that you have prepared from your Circle Spells feature without
    expending a spell slot, and you must finish a Long rest before you do so again.

    In addition, when you finish a Short Rest, you can choose expended spell slots to recover. The spell slots can
    have a combined level that is equal to or less than half your Druid level (round up), and none of them can be
    level 6+. Once you recover spell slots with this feature, you can't do so again until you finish a Long Rest."""


#############################################################################
class NaturesWard(BaseFeature):
    tag = Feature.NATURES_WARD
    _desc = """You are immune to the Poisoned condition, and you have Resistance to a damage type associated with 
    your current land choice in the Circle Spells feature, as shown in the Nature's Ward table. 
    
    NATURE'S WARD 
    Land Type Resistance Land Type Resistance 
    Arid Fire 
    Temperate Lightning 
    Polar Cold 
    Tropical Poison"""


# EOF
