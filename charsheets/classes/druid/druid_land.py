from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.druid import Druid
from charsheets.constants import Ability
from charsheets.reason import Reason
from charsheets.spells import Spells

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class DruidCircleOfTheLand(Druid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Druid (Circle of the Land)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        """Only one of these should be active at one time"""
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {
            LandsAid(),
            LandSpellArid(),
            LandSpellTropical(),
            LandSpellPolar(),
            LandSpellTemperate(),
        }
        if self.level >= 6:
            abilities.add(NaturalRecovery())
        return abilities


#############################################################################
class LandsAid(BaseAbility):
    tag = Ability.LANDS_AID
    _desc = """As a Magic action, you can expend a use of your Wild Shape a choose a point within 60 feet of yourself.
    Vitality-giving flowers and life-draining thorns appear for a moment in a 10-foot-radius Sphere centered on
    that point. Each creature of your choice in the Sphere must make a Constitution saving throw against your
    spell save DC, taking 2d6 Necrotic damage on a failed save or half as much damage on a successful one. One
    creature of your choice in that area regains 2d6 Hit Points."""


#############################################################################
class LandSpellArid(BaseAbility):
    tag = Ability.LAND_SPELL_ARID
    _desc = """Arid Land"""
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        spells = Reason("Arid Land", Spells.BLUR, Spells.BURNING_HANDS, Spells.FIRE_BOLT)
        if character.level >= 5:
            spells |= Reason("Arid Land", Spells.FIREBALL)
        return spells


#############################################################################
class LandSpellTropical(BaseAbility):
    tag = Ability.LAND_SPELL_TROPICAL
    _desc = """Tropical Land"""
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        spells = Reason("Tropical Land", Spells.ACID_SPLASH, Spells.RAY_OF_SICKNESS, Spells.WEB)
        if character.level >= 5:
            spells |= Reason("Tropical Land", Spells.STINKING_CLOUD)
        return spells


#############################################################################
class LandSpellPolar(BaseAbility):
    tag = Ability.LAND_SPELL_POLAR
    _desc = """Polar Land"""
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        spells = Reason("Polar Land", Spells.FOG_CLOUD, Spells.HOLD_PERSON, Spells.RAY_OF_FROST)
        if character.level >= 5:
            spells |= Reason("Polar Land", Spells.SLEET_STORM)
        return spells


#############################################################################
class LandSpellTemperate(BaseAbility):
    tag = Ability.LAND_SPELL_TEMPERATE
    _desc = """ Temperate Land"""
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        spells = Reason("Temperate Land", Spells.MISTY_STEP, Spells.SHOCKING_GRASP, Spells.SLEEP)
        if character.level >= 5:
            spells |= Reason("Temperate Land", Spells.LIGHTNING_BOLT)
        return spells


#############################################################################
class NaturalRecovery(BaseAbility):
    tag = Ability.NATURAL_RECOVERY
    goes = 1
    _desc = """You can cast one of the level 1+ spells that you have prepared from your Circle Spells feature without
    expending a spell slot, and you must finish a Long rest before you do so again.

    In addition, when you finish a Short Rest, you can choose expended spell slots to recover. The spell slots can
    have a combined level that is equal to or less than half your Druid level (round up), and none of them can be
    level 6+. Once you recover spell slots with this feature, you can't do so again until you finish a Long Rest."""


# EOF
