from typing import TYPE_CHECKING

from charsheets.classes.warlock import Warlock
from charsheets.constants import Feature, DamageType
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class WarlockCelestial(Warlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Warlock (Celestial Patron)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {HealingLight()}
        abilities |= super().class_features()
        self.prepare_spells(
            Spell.AID,
            Spell.CURE_WOUNDS,
            Spell.GUIDING_BOLT,
            Spell.LESSER_RESTORATION,
            Spell.LIGHT,
            Spell.SACRED_FLAME,
        )
        if self.level >= 5:
            self.prepare_spells(Spell.DAYLIGHT, Spell.REVIVIFY)
        if self.level >= 6:
            abilities |= {RadiantSoul()}
        if self.level >= 5:
            self.prepare_spells(Spell.GUARDIAN_OF_FAITH, Spell.WALL_OF_FIRE)
        if self.level >= 9:
            self.prepare_spells(Spell.GREATER_RESTORATION, Spell.SUMMON_CELESTIAL)
        return abilities


#############################################################################
class HealingLight(BaseFeature):
    tag = Feature.HEALING_LIGHT
    _desc = """You gain the ability to channel celestial energy to heal wounds. You have a pool of d6s to fuel this
    healing. The number of dice in the pool equals 1 plus your Warlock level.

    As a Bonus Action, you can heal yourself or one creature you can see within 60 feet of yourself, expending dice
    from the pool. The maximum number of dice you can expend at once equals your Charisma modifier (minimum of one die).
    Roll the dice you expend, and restore a number of Hit Points equal to the roll's total. Your pool regains all
    expended dice when you finish a Long Rest.
    """


#############################################################################
class RadiantSoul(BaseFeature):
    tag = Feature.RADIANT_SOUL
    _desc = """Your link to your patron allows you to serve as a conduit for radiant energy. You have Resistance to 
    Radiant damage. Once per turn, when a spell you cast deals Radiant or Fire damage, you can add your Charisma 
    modifier to that spell's damage against one of the spell's targets."""

    def mod_add_damage_resistances(self, character: "Character") -> Reason[DamageType]:
        return Reason("Radiant Soul", DamageType.RADIANT)


# EOF
