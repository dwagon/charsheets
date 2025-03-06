from typing import TYPE_CHECKING
from aenum import extend_enum

from charsheets.classes.warlock import Warlock
from charsheets.constants import Feature, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:
    from charsheets.character import Character


#################################################################################
class WarlockOldOne(Warlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Great Old One Warlock"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {AwakenedMind(), PsychicSpells()}
        abilities |= super().class_features()

        self.prepare_spells(
            Spell.DETECT_THOUGHTS,
            Spell.DISSONANT_WHISPERS,
            Spell.PHANTASMAL_FORCE,
            Spell.TASHAS_HIDEOUS_LAUGHTER,
        )
        if self.level >= 5:
            self.prepare_spells(Spell.CLAIRVOYANCE, Spell.HUNGER_OF_HADAR)
        if self.level >= 6:
            abilities |= {ClairvoyantCombatant()}
        if self.level >= 5:
            self.prepare_spells(Spell.CONFUSION, Spell.SUMMON_ABERRATION)
        if self.level >= 9:
            self.prepare_spells(Spell.MODIFY_MEMORY, Spell.TELEKINESIS)
        if self.level >= 10:
            abilities |= {EldritchHex()}
        return abilities


extend_enum(Feature, "AWAKENED_MIND", "Awakened Mind")
extend_enum(Feature, "PSYCHIC_SPELLS", "Psychic Spells")
extend_enum(Feature, "CLAIRVOYANT_COMBATANT", "Clairvoyant Combatant")
extend_enum(Feature, "ELDRITCH_HEX", "Eldritch Hex")


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
