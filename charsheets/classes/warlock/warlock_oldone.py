from charsheets.features.base_feature import BaseFeature
from charsheets.classes.warlock import Warlock
from charsheets.constants import Feature
from charsheets.spell import Spell


#################################################################################
class WarlockOldOne(Warlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Warlock (Great Old One Patron)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {PsychicSpells()}
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
        return abilities


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
    _desc = """When you form a telepathic bond with a creature using your Awakened Mind, you can force that creature 
    to make a Wisdom saving throw against your spell save DC. On a failed save, the creature has Disadvantage on 
    attack rolls against you, and you have Advantage on attack rolls against that creature for the duration of the bond.

    Once you use this feature, you can't use it again until you finish a Short or Long Rest unless you expend a Pact 
    Magic spell slot (no action required) to restore your use of it."""


# EOF
