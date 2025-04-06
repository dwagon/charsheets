from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.ranger import Ranger
from charsheets.constants import Feature, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "DREAD_AMBUSHER", "Dread Ambusher")
extend_enum(Feature, "GLOOM_STALKER_SPELLS", "Gloom Stalker Spells")
extend_enum(Feature, "IRON_MIND", "Iron Mind")
extend_enum(Feature, "STALKERS_FLURRY", "Stalkers Flurry")
extend_enum(Feature, "UMBRAL_SIGHT", "Umbral Sight")


#################################################################################
class RangerGloomStalker(Ranger):
    _class_name = "Ranger (Gloom Stalker)"

    #############################################################################
    def level3(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(DreadAmbusher())
        self.add_feature(UmbralSight())
        self.add_feature(GloomStalkerSpells())

    #############################################################################
    def level7(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(IronMind())

    #############################################################################
    def level11(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(StalkersFlurry())


#############################################################################
class GloomStalkerSpells(BaseFeature):
    tag = Feature.GLOOM_STALKER_SPELLS
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason("Gloom Stalker Spells", Spell.DISGUISE_SELF)
        if character.level >= 5:
            spells |= Reason("Gloom Stalker Spells", Spell.ROPE_TRICK)
        if character.level >= 9:
            spells |= Reason("Gloom Stalker Spells", Spell.FEAR)
        if character.level >= 13:
            spells |= Reason("Gloom Stalker Spells", Spell.GREATER_INVISIBILITY)
        if character.level >= 17:
            spells |= Reason("Gloom Stalker Spells", Spell.SEEMING)
        return spells


#############################################################################
class DreadAmbusher(BaseFeature):
    tag = Feature.DREAD_AMBUSHER
    recovery = Recovery.LONG_REST

    @property
    def goes(self) -> int:
        return max(1, self.owner.wisdom.modifier)

    @property
    def desc(self) -> str:
        return f"""Ambusher's Leap.  At the start of your first turn of each combat, your Speed increases by 10 feet
        until the end of that turn.

    Dreadful Strike. When you attack a creature and hit it with a weapon, you can deal an extra 2d6 Psychic damage. 
    You can use this benefit only once per turn, you can use it {self.goes} times."""

    def mod_initiative_bonus(self, character: "Character") -> Reason[int]:
        return Reason("Dread Ambusher", self.owner.wisdom.modifier)


#############################################################################
class UmbralSight(BaseFeature):
    tag = Feature.UMBRAL_SIGHT
    _desc = """You gain Darkvision with a range of 60 feet. If you already have Darkvision, its range increases by 60
    feet.

    You are also adept at evading creatures that rely on Darkvision. While entirely in Darkness, you have the
    Invisible condition to any creature that relies on Darkvision to see you in that Darkness."""

    # TODO - darkvision


#############################################################################
class IronMind(BaseFeature):
    tag = Feature.IRON_MIND
    _desc = """You gain proficiency in Wisdom saving 
    throws. If you already have this proficiency, you instead gain proficiency in Intelligence or Charisma saving 
    throws (your choice)."""


#############################################################################
class StalkersFlurry(BaseFeature):
    tag = Feature.STALKERS_FLURRY
    _desc = """The Psychic damage of your Dreadful Strike be- comes 2d8. In addition, when you use the Dreadful 
    Strike effect of your Dread Ambusher feature, you can cause one of the following additional effects.
    
    Sudden Strike. You can make another attack with the same weapon against a different creature that is within 5 
    feet of the original target and that is within the weapon's range.

    Mass Fear. The target and each creature within 10 feet of it must make a Wisdom saving throw against your spell 
    save DC. On a failed save, a creature has the Frightened condition until the start of your next turn."""


# EOF
