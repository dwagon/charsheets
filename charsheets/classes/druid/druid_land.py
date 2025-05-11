import math
from typing import TYPE_CHECKING, Any

from aenum import extend_enum
from charsheets.classes.druid import Druid
from charsheets.constants import Feature, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


extend_enum(Feature, "LANDS_AID", "Lands Aid")
extend_enum(Feature, "LAND_SPELL_ARID", "Circle of the Land Spell (Arid)")
extend_enum(Feature, "LAND_SPELL_POLAR", "Circle of the Land Spell (Polar)")
extend_enum(Feature, "LAND_SPELL_TEMPERATE", "Circle of the Land Spell (Temperate)")
extend_enum(Feature, "LAND_SPELL_TROPICAL", "Circle of the Land Spell (Tropical)")
extend_enum(Feature, "NATURAL_RECOVERY", "Natural Recovery")
extend_enum(Feature, "NATURES_WARD", "Natures Ward")
extend_enum(Feature, "NATURES_SANCTUARY", "Natures Sanctuary")


#################################################################################
class DruidCircleOfTheLand(Druid):
    _class_name = "Circle of the Land Druid"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(LandsAid())
        self.add_feature(LandSpellArid())
        self.add_feature(LandSpellTropical())
        self.add_feature(LandSpellPolar())
        self.add_feature(LandSpellTemperate())

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(NaturalRecovery())

    #############################################################################
    def level10(self, **kwargs: Any):
        self.add_feature(NaturesWard())

    #############################################################################
    def level14(self, **kwargs: Any):
        self.add_feature(NaturesSanctuary())


#############################################################################
class LandsAid(BaseFeature):
    tag = Feature.LANDS_AID
    _desc = """As a Magic action, you can expend a use of your Wild Shape and choose a point within 60 feet of yourself.
    Vitality-giving flowers and life-draining thorns appear for a moment in a 10-foot-radius Sphere centered on
    that point. Each creature of your choice in the Sphere must make a Constitution saving throw against your
    spell save DC, taking 2d6 Necrotic damage on a failed save or half as much damage on a successful one. One
    creature of your choice in that area regains 2d6 Hit Points."""


#############################################################################
class LandSpellArid(BaseFeature):
    tag = Feature.LAND_SPELL_ARID
    _desc = """Arid Land"""

    @property
    def desc(self) -> str:
        assert self.owner.druid is not None
        spells = ["Blur", "Burning Hands", "Fire Bolt"]
        if self.owner.druid.level >= 5:
            spells.append("Fireball")
        if self.owner.druid.level >= 7:
            spells.append("Blight")
        if self.owner.druid.level >= 9:
            spells.append("Wall of Stone")
        spell_list = ", ".join(f"'{_}'" for _ in spells)
        return f"If you pick Arid you have the following spells prepared: {spell_list}."

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        assert character.druid is not None
        spells = Reason("Arid Land", Spell.BLUR, Spell.BURNING_HANDS, Spell.FIRE_BOLT)
        if character.druid.level >= 5:
            spells |= Reason("Arid Land", Spell.FIREBALL)
        if character.druid.level >= 7:
            spells |= Reason("Arid Land", Spell.BLIGHT)
        if character.druid.level >= 9:
            spells |= Reason("Arid Land", Spell.WALL_OF_STONE)
        return spells


#############################################################################
class LandSpellTropical(BaseFeature):
    tag = Feature.LAND_SPELL_TROPICAL
    _desc = """Tropical Land"""

    @property
    def desc(self) -> str:
        assert self.owner.druid is not None
        spells = ["Acid Splash", "Ray of Sickness", "Web"]
        if self.owner.druid.level >= 5:
            spells.append("Stinking Cloud")
        if self.owner.druid.level >= 7:
            spells.append("Polymorph")
        if self.owner.druid.level >= 9:
            spells.append("Insect Plague")
        spell_list = ", ".join(f"'{_}'" for _ in spells)
        return f"If you pick Tropical you have the following spells prepared: {spell_list}."

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        assert character.druid is not None

        spells = Reason("Tropical Land", Spell.ACID_SPLASH, Spell.RAY_OF_SICKNESS, Spell.WEB)
        if character.druid.level >= 5:
            spells |= Reason("Tropical Land", Spell.STINKING_CLOUD)
        if character.druid.level >= 7:
            spells |= Reason("Tropical Land", Spell.POLYMORPH)
        if character.druid.level >= 9:
            spells |= Reason("Tropical Land", Spell.INSECT_PLAGUE)
        return spells


#############################################################################
class LandSpellPolar(BaseFeature):
    tag = Feature.LAND_SPELL_POLAR
    _desc = """Polar Land"""

    @property
    def desc(self) -> str:
        assert self.owner.druid is not None
        spells = ["Fog Cloud", "Hold Person", "Ray of Frost"]
        if self.owner.druid.level >= 5:
            spells.append("Sleet Storm")
        if self.owner.druid.level >= 7:
            spells.append("Ice Storm")
        if self.owner.druid.level >= 9:
            spells.append("Cone of Cold")
        spell_list = ", ".join(f"'{_}'" for _ in spells)
        return f"If you pick Polar you have the following spells prepared: {spell_list}."

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        assert character.druid is not None

        spells = Reason("Polar Land", Spell.FOG_CLOUD, Spell.HOLD_PERSON, Spell.RAY_OF_FROST)
        if character.druid.level >= 5:
            spells |= Reason("Polar Land", Spell.SLEET_STORM)
        if character.druid.level >= 5:
            spells |= Reason("Polar Land", Spell.ICE_STORM)
        if character.druid.level >= 9:
            spells |= Reason("Polar Land", Spell.CONE_OF_COLD)
        return spells


#############################################################################
class LandSpellTemperate(BaseFeature):
    tag = Feature.LAND_SPELL_TEMPERATE
    _desc = """ Temperate Land"""

    @property
    def desc(self) -> str:
        assert self.owner.druid is not None
        spells = ["Misty Step", "Shocking Grasp", "Sleep"]
        if self.owner.druid.level >= 5:
            spells.append("Lightning Bolt")
        if self.owner.druid.level >= 7:
            spells.append("Freedom of Movement")
        if self.owner.druid.level >= 9:
            spells.append("Tree Stride")
        spell_list = ", ".join(f"'{_}'" for _ in spells)
        return f"If you pick Temperate you have the following spells prepared: {spell_list}."

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        assert character.druid is not None

        spells = Reason("Temperate Land", Spell.MISTY_STEP, Spell.SHOCKING_GRASP, Spell.SLEEP)
        if character.druid.level >= 5:
            spells |= Reason("Temperate Land", Spell.LIGHTNING_BOLT)
        if character.druid.level >= 7:
            spells |= Reason("Temperate Land", Spell.FREEDOM_OF_MOVEMENT)
        if character.druid.level >= 9:
            spells |= Reason("Temperate Land", Spell.TREE_STRIDE)
        return spells


#############################################################################
class NaturalRecovery(BaseFeature):
    tag = Feature.NATURAL_RECOVERY
    goes = 1
    recovery = Recovery.LONG_REST

    @property
    def desc(self) -> str:
        slots = math.ceil(self.owner.level / 2)
        return f"""You can cast one of the level 1+ spells that you have prepared from your Circle Spells feature 
        without expending a spell slot, and you must finish a Long rest before you do so again.

        In addition, when you finish a Short Rest, you can choose expended spell slots to recover. The spell slots 
        can have a combined level that is equal to or less than {slots}, and none of them can be level 6+. Once you 
        recover spell slots with this feature, you can't do so again until you finish a Long Rest."""


#############################################################################
class NaturesWard(BaseFeature):
    tag = Feature.NATURES_WARD
    _desc = """You are immune to the Poisoned condition, and you have Resistance to a damage type associated with 
    your current land choice in the Circle Spells feature. 
    
    Arid -> Fire,
    Temperate -> Lightning,
    Polar -> Cold,
    Tropical -> Poison"""


#############################################################################
class NaturesSanctuary(BaseFeature):
    tag = Feature.NATURES_SANCTUARY
    _desc = """As a Magic action, you can expend a use of your Wild Shape and cause spectral trees and vines to 
    appear in a 15-foot Cube on the ground within 120 feet of yourself. They last there for 1 minute or until you 
    have the Incapacitated condition or die. You and your allies have Half Cover while in that area, and your allies 
    gain the current Resistance of your Nature's Ward while there.

    As a Bonus Action, you can move the Cube up to 60 feet to ground within 120 feet of yourself."""


# EOF
