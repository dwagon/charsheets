from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.sorcerer import Sorcerer
from charsheets.constants import Feature, DamageType
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "ABERRANT_SORCERY", "Aberrant Sorcery")
extend_enum(Feature, "PSIONIC_SORCERY", "Psionic Sorcery")
extend_enum(Feature, "PSIONIC_SPELLS", "Psionic Spells")
extend_enum(Feature, "PSYCHIC_DEFENSES", "Psychic Defenses")
extend_enum(Feature, "TELEPATHIC_SPEECH", "Telepathic Speech")


#################################################################################
class SorcererAberrant(Sorcerer):

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(AberrantSorcery())
        self.add_feature(PsionicSpells())
        self.add_feature(TelepathicSpeech())

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(PsionicSorcery())
        self.add_feature(PsychicDefenses())


#############################################################################
class PsionicSpells(BaseFeature):
    tag = Feature.PSIONIC_SPELLS
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason(
            "Psionic Spells",
            Spell.ARMS_OF_HADAR,
            Spell.CALM_EMOTIONS,
            Spell.DETECT_THOUGHTS,
            Spell.DISSONANT_WHISPERS,
            Spell.MIND_SLIVER,
        )
        if character.level >= 5:
            spells |= Reason("Psionic Spells", Spell.HUNGER_OF_HADAR, Spell.SENDING)
        if character.level >= 7:
            spells |= Reason("Psionic Spells", Spell.EVARDS_BLACK_TENTACLES, Spell.SUMMON_ABERRATION)
        if character.level >= 9:
            spells |= Reason("Psionic Spells", Spell.RARYS_TELEPATHIC_BOND, Spell.TELEKINESIS)
        return spells


#############################################################################
class AberrantSorcery(BaseFeature):
    tag = Feature.ABERRANT_SORCERY
    hide = True
    _desc = """An alien influence has wrapped its tendrils around your mind, giving you psionic power. You can now 
    touch other minds with that power and alter the world around you. Will this power shine from you as a hopeful 
    beacon to others? Or will you be a terror to those who feel the stab of your mind? Perhaps a psychic wind 
    from the Astral Plane carried psionic energy to you, or you were exposed to the Far Realm’s warping 
    influence. Alternatively, you were implanted with a mind flayer tadpole, but your transformation into a mind 
    flayer never occurred; now the tadpole’s psionic power is yours. However you acquired this power, your mind is 
    aflame with it"""


#############################################################################
class TelepathicSpeech(BaseFeature):
    tag = Feature.TELEPATHIC_SPEECH
    _desc = """You can form a telepathic connection between your mind and the mind of another. As a Bonus Action, 
    choose one creature you can see within 30 feet of yourself. You and the chosen creature can communicate 
    telepathic with each other while the two of you are within a number of miles of each other equal to your Charisma 
    modifier (minimum of 1 mile). To understand each other, you each must mentally use a language the other knows. 

    The telepathic connection lasts for a number of minutes equal to your Sorcerer level. It ends early if you use 
    this ability to form a connection with a different creature."""


#############################################################################
class PsionicSorcery(BaseFeature):
    tag = Feature.PSIONIC_SORCERY
    _desc = """When you cast any level 1+ spell from your Psionic Spells feature, you can cast it by expending a 
    spell slot as normal or by spending a number of Sorcery Points equal to the spell's level. If you cast the spell 
    using Sorcery Points, it requires no Verbal or Somatic components, and it requires no Material components unless 
    they are consumed by the spell or have a cost specified in it."""


#############################################################################
class PsychicDefenses(BaseFeature):
    tag = Feature.PSYCHIC_DEFENSES
    _desc = """You have Advantage on saving throws to avoid or end the Charmed or Frightened condition."""

    def mod_add_damage_resistances(self, character: "Character") -> Reason[DamageType]:
        return Reason("Psychic Defenses", DamageType.PSYCHIC)


# EOF
