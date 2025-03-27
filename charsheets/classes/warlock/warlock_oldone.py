from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.warlock import Warlock
from charsheets.constants import Feature, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "AWAKENED_MIND", "Awakened Mind")
extend_enum(Feature, "CLAIRVOYANT_COMBATANT", "Clairvoyant Combatant")
extend_enum(Feature, "ELDRITCH_HEX", "Eldritch Hex")
extend_enum(Feature, "GREAT_OLD_ONE_SPELLS", "Great Old One Spells")
extend_enum(Feature, "PSYCHIC_SPELLS", "Psychic Spells")


#################################################################################
class WarlockOldOne(Warlock):
    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(AwakenedMind())
        self.add_feature(PsychicSpells())
        self.add_feature(GreatOldOneSpells())

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(ClairvoyantCombatant())

    #############################################################################
    def level10(self, **kwargs: Any):
        self.add_feature(EldritchHex())


#############################################################################
class GreatOldOneSpells(BaseFeature):
    tag = Feature.GREAT_OLD_ONE_SPELLS
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason(
            "Great Old One Spells",
            Spell.DETECT_THOUGHTS,
            Spell.DISSONANT_WHISPERS,
            Spell.PHANTASMAL_FORCE,
            Spell.TASHAS_HIDEOUS_LAUGHTER,
        )
        if character.level >= 5:
            spells |= Reason("Great Old One Spells", Spell.CLAIRVOYANCE, Spell.HUNGER_OF_HADAR)
        if character.level >= 7:
            spells |= Reason("Great Old One Spells", Spell.CONFUSION, Spell.SUMMON_ABERRATION)
        if character.level >= 9:
            spells |= Reason("Great Old One Spells", Spell.MODIFY_MEMORY, Spell.TELEKINESIS)
        return spells


#############################################################################
class AwakenedMind(BaseFeature):
    tag = Feature.AWAKENED_MIND

    @property
    def desc(self) -> str:
        rng = max(1, self.owner.charisma.modifier)
        return f"""You can form a telepathic connection between your mind and the mind of another. As a Bonus Action, 
        choose one creature you can see within 30 feet of yourself. You and the chosen creature can communicate 
        telepathically with each other while the two of you are within {rng} miles. To understand each other, 
        you each must mentally use a language the other knows.
        
        The telepathic connection lasts for {self.owner.level} minutes. It ends early if you use 
        this feature to connect with a different creature."""


#############################################################################
class PsychicSpells(BaseFeature):
    tag = Feature.PSYCHIC_SPELLS
    _desc = """When you cast a Warlock spell that deals damage, you can change its damage type to Psychic. In addition,
    when you cast a Warlock spell that is an Enchantment or Illusion, you can do so without Verbal or Somatic
    components."""


#############################################################################
class ClairvoyantCombatant(BaseFeature):
    tag = Feature.CLAIRVOYANT_COMBATANT
    goes = 1
    recovery = Recovery.SHORT_REST
    _desc = """When you form a telepathic bond with a creature using your Awakened Mind, you can force that creature 
    to make a Wisdom saving throw against your spell save DC. On a failed save, the creature has Disadvantage on 
    attack rolls against you, and you have Advantage on attack rolls against that creature for the duration of the bond.

    Once you use this feature, you can't use it again until you finish a Short or Long Rest unless you expend a Pact 
    Magic spell slot (no action required) to restore your use of it."""


#############################################################################
class EldritchHex(BaseFeature):
    tag = Feature.ELDRITCH_HEX
    _desc = """Your alien patron grants you a powerful curse. You always have the 'Hex' spell prepared. When you cast 
    'Hex' and choose an ability, the target also has Disadvantage on saving throws of the chosen ability for the 
    duration of the spell."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Eldritch Hex", Spell.HEX)


# EOF
