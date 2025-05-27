from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes2014.sorcerer.sorcerer import Sorcerer
from charsheets.constants import Language, Feature, Stat
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.species.dragonborn import Ancestor

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

"""
Draconic Bloodline

Your innate magic comes from draconic magic that was mingled with your blood or that of your ancestors. Most often, 
sorcerers with this origin trace their descent back to a mighty sorcerer of ancient times who made a bargain with a 
dragon or who might even have claimed a dragon parent. Some of these bloodlines are well established in the world, 
but most are obscure. Any given sorcerer could be the first of a new bloodline, as a result of a pact or some other 
exceptional circumstance.

Elemental Affinity: Starting at 6th level, when you cast a spell that deals damage of the type associated with your 
draconic ancestry, you can add your Charisma modifier to one damage roll of that spell. At the same time, 
you can spend 1 sorcery point to gain resistance to that damage type for 1 hour. Dragon Wings

At 14th level, you gain the ability to sprout a pair of dragon wings from your back, gaining a flying speed equal to 
your current speed. You can create these wings as a bonus action on your turn. They last until you dismiss them as a 
bonus action on your turn.

You can’t manifest your wings while wearing armor unless the armor is made to accommodate them, and clothing not made 
to accommodate your wings might be destroyed when you manifest them. Draconic Presence

Beginning at 18th level, you can channel the dread presence of your dragon ancestor, causing those around you to 
become awestruck or frightened. As an action, you can spend 5 sorcery points to draw on this power and exude an aura 
of awe or fear (your choice) to a distance of 60 feet. For 1 minute or until you lose your concentration (as if you 
were casting a concentration spell), each hostile creature that starts its turn in this aura must succeed on a Wisdom 
saving throw or be charmed (if you chose awe) or frightened (if you chose fear) until the aura ends. A creature that 
succeeds on this saving throw is immune to your aura for 24 hours."""

extend_enum(Feature, "DRACONIC_BLOODLINE14", "Draconic Ancestry")
extend_enum(Feature, "DRACONIC_RESILIENCE14", "Draconic Resilience")


#################################################################################
class DraconicSorcerer(Sorcerer):

    def __init__(self, ancestry: Ancestor, **kwargs):
        self.ancestry = ancestry
        super().__init__(**kwargs)

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        self.character.add_feature(DraconicAncestry())
        self.character.add_feature(DraconicResilience())

        super().level1(**kwargs)

    #############################################################################
    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason("Draconic Sorcerer", Language.DRACONIC)

    #############################################################################
    def mod_hp_bonus(self, character: "BaseCharacter") -> Reason[int]:
        assert self.character is not None
        assert self.character.sorcerer is not None
        return Reason("Draconic Resilience", self.character.sorcerer.level)


#############################################################################
class DraconicAncestry(BaseFeature):
    tag = Feature.DRACONIC_BLOODLINE14
    _desc = """Whenever you make a Charisma check when interacting with dragons, your proficiency bonus is doubled if 
it applies to the check."""


#############################################################################
class DraconicResilience(BaseFeature):
    tag = Feature.DRACONIC_RESILIENCE14

    @property
    def desc(self) -> str:
        ac = 13 + self.owner.stats[Stat.DEXTERITY].modifier
        return f"""Parts of your skin are covered by a thin sheen of dragon-like scales. When you aren’t wearing armor,
    your AC is {ac}."""


# EOF
