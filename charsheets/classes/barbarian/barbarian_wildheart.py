from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.barbarian import Barbarian
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


extend_enum(Feature, "ANIMAL_SPEAKER", "Animal Speaker")
extend_enum(Feature, "RAGE_OF_THE_WILDS", "Rage of the Wilds")
extend_enum(Feature, "ASPECTS_OF_THE_WILDS", "Aspects of the Wilds")
extend_enum(Feature, "NATURE_SPEAKER", "Nature Speaker")
extend_enum(Feature, "POWER_OF_THE_WILDS", "Power of the Wilds")


#################################################################################
class BarbarianPathOfTheWildHeart(Barbarian):
    _class_name = "Path of the Wild Heart Barbarian"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(AnimalSpeaker())
        self.add_feature(RageOfTheWilds())

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(AspectsOfTheWilds())

    #############################################################################
    def level10(self, **kwargs: Any):
        self.add_feature(NatureSpeaker())

    #############################################################################
    def level14(self, **kwargs: Any):
        self.add_feature(PowerOfTheWilds())


#############################################################################
class AnimalSpeaker(BaseFeature):
    tag = Feature.ANIMAL_SPEAKER
    _desc = """You can cast the Beast Sense and Speak with Animals spells but only as Rituals. Wisdom is your
    spellcasting Ability for them."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Animal Speaker", Spell.BEAST_SENSE) | Reason("Animal Speaker", Spell.SPEAK_WITH_ANIMALS)


#############################################################################
class RageOfTheWilds(BaseFeature):
    tag = Feature.RAGE_OF_THE_WILDS
    _desc = """Your Rage taps into the primal power of animals. Whenever you activate your Rage, you gain one of the
    following options of your choice.

    Bear. While your Rage is active, you have Resistance to every damage type except Force, Necrotic, Psychic and
    Radiant.

    Eagle. When you activate your Rage, you can take the Disengage and Dash actions as part of that Bonus Action.
    While yourRage is active, you can take a Bonus Action to take both of those actions.

    Wolf. While your Rage is active, your allies have Advantage on attack rolls against any enemy of yours with 5 feet
    of you."""


#############################################################################
class AspectsOfTheWilds(BaseFeature):
    tag = Feature.ASPECTS_OF_THE_WILDS
    _desc = """You gain one of the following options of your choice. Whenever you finish a Long Rest, you can change 
    your choice.

    Owl. You have Darkvision with a range of 60 feet. If you already have Darkvision, its range increases by 60 feet.

    Panther. You have a Climb Speed equal to your Speed.

    Salmon. You have a Swim Speed equal to your Speed."""


#############################################################################
class NatureSpeaker(BaseFeature):
    tag = Feature.NATURE_SPEAKER
    _desc = """You can cast the 'Commune with Nature' spell but only as a Ritual. Wisdom is your spellcasting
            ability for it."""


#############################################################################
class PowerOfTheWilds(BaseFeature):
    tag = Feature.POWER_OF_THE_WILDS
    _desc = """Whenever you activate your Rage, you gain one of the following options of your choice. 
    
    Falcon. While your Rage is active, you have a Fly Speed equal to your Speed if you aren't wearing any armor.

    Lion. While your Rage is active, any of your ene- mies within 5 feet of you have Disadvantage on attack rolls 
    against targets other than you or another Barbarian who has this option active.

    Ram. While your Rage is active, you can cause a Large or smaller creature to have the Prone condition when you 
    hit it with a melee attack."""


# EOF
