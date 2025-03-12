from typing import TYPE_CHECKING

from aenum import extend_enum

from charsheets.classes.warlock import Warlock
from charsheets.constants import Feature, DamageType, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


extend_enum(Feature, "CELESTIAL_RESILIENCE", "Celestial Resilience")
extend_enum(Feature, "CELESTIAL_SPELLS", "Celestial Spells")
extend_enum(Feature, "HEALING_LIGHT", "Healing Light")
extend_enum(Feature, "RADIANT_SOUL", "Radiant Soul")


#################################################################################
class WarlockCelestial(Warlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Celestial Warlock"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {HealingLight(), CelestialSpells()}
        abilities |= super().class_features()

        if self.level >= 6:
            abilities |= {RadiantSoul()}
        if self.level >= 10:
            abilities |= {CelestialResilience()}
        return abilities


#############################################################################
class CelestialSpells(BaseFeature):
    tag = Feature.CELESTIAL_SPELLS
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason(
            "Celestial Spells",
            Spell.AID,
            Spell.CURE_WOUNDS,
            Spell.GUIDING_BOLT,
            Spell.LESSER_RESTORATION,
            Spell.LIGHT,
            Spell.SACRED_FLAME,
        )
        if character.level >= 5:
            spells |= Reason("Celestial Spells", Spell.DAYLIGHT, Spell.REVIVIFY)
        if character.level >= 7:
            spells |= Reason("Celestial Spells", Spell.GUARDIAN_OF_FAITH, Spell.WALL_OF_FIRE)
        if character.level >= 9:
            spells |= Reason("Celestial Spells", Spell.GREATER_RESTORATION, Spell.SUMMON_CELESTIAL)
        return spells


#############################################################################
class HealingLight(BaseFeature):
    tag = Feature.HEALING_LIGHT
    recovery = Recovery.LONG_REST

    @property
    def goes(self) -> int:
        return self.owner.level + 1

    @property
    def desc(self) -> str:
        max_dice = max(1, self.owner.charisma.modifier)
        return f"""You gain the ability to channel celestial energy to heal wounds. You have a pool of {self.goes} d6s
        to fuel this healing.

        As a Bonus Action, you can heal yourself or one creature you can see within 60 feet of yourself, expending 
        dice from the pool. The maximum number of dice you can expend at once is {max_dice}. Roll the dice you 
        expend, and restore a number of Hit Points equal to the roll's total."""


#############################################################################
class RadiantSoul(BaseFeature):
    tag = Feature.RADIANT_SOUL
    _desc = """Once per turn, when a spell you cast deals Radiant or Fire damage, you can add your Charisma 
    modifier to that spell's damage against one of the spell's targets."""

    def mod_add_damage_resistances(self, character: "Character") -> Reason[DamageType]:
        return Reason("Radiant Soul", DamageType.RADIANT)


#############################################################################
class CelestialResilience(BaseFeature):
    tag = Feature.CELESTIAL_RESILIENCE
    _desc = """You gain Temporary Hit Points whenever you use your Magical Cunning feature or finish a Short or Long 
    Rest. These Temporary Hit Points equal your Warlock level plus your Charisma modifier. Additionally, choose up to 
    five creatures you can see when you gain the points. Those creatures each gain Temporary Hit Points equal to half 
    your Warlock level plus your Charisma modifier."""


# EOF
