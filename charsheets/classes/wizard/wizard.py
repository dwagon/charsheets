from typing import Optional

from charsheets.features.base_feature import BaseFeature
from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill, Feature
from charsheets.reason import Reason


#################################################################################
class Wizard(Character):
    _base_skill_proficiencies = {
        Skill.ARCANA,
        Skill.HISTORY,
        Skill.INSIGHT,
        Skill.INVESTIGATION,
        Skill.MEDICINE,
        Skill.NATURE,
        Skill.RELIGION,
    }

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 6

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.INTELLIGENCE

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason("Class Proficiency", Proficiency.SIMPLE_WEAPONS)

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason()

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.INTELLIGENCE, Stat.WISDOM)

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {RitualAdept()}
        abilities.add(ArcaneRecovery())

        if self.level >= 2:
            abilities.add(Scholar())
        if self.level >= 5:
            abilities.add(MemorizeSpell())

        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            4: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 3, 2, 0, 0, 0, 0, 0, 0],
            6: [4, 3, 3, 0, 0, 0, 0, 0, 0],
            7: [4, 3, 3, 1, 0, 0, 0, 0, 0],
            8: [4, 3, 3, 2, 0, 0, 0, 0, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def max_spell_level(self) -> int:
        return min(9, ((self.level + 1) // 2))


#############################################################################
class RitualAdept(BaseFeature):
    tag = Feature.RITUAL_ADEPT
    _desc = """You can cast any spell as a Ritual if that spell has the Ritual tag and the spell is in your spellbook.
    You needn't have the spell prepared, but you must read from the book to cast a spell in this way."""


#############################################################################
class ArcaneRecovery(BaseFeature):
    tag = Feature.ARCANE_RECOVERY
    goes = 1

    @property
    def desc(self) -> str:
        slots = self.owner.level // 2
        return f"""You can regain some of your magical energy by studying your spellbook. When you finish a Short 
        Rest, you can choose expended spell slots to recover. The spell slots can have a combined level equal to no 
        more than {slots}, and none of the slots can be level 6 or higher.

        Once you use this feature, you can't do so again until you finish a Long Rest"""


#############################################################################
class Scholar(BaseFeature):
    tag = Feature.SCHOLAR
    _desc = """While studying magic, you also specialized in another field of study. Choose on of the following skills
    in which you have proficiency: Arcana, History, Investigation, Medicine, Nature, or Religion. You have Expertise
    in the chosen skill."""


#############################################################################
class MemorizeSpell(BaseFeature):
    tag = Feature.MEMORIZE_SPELL
    _desc = """Whenever you finish a Short Rest, you can study your spellbook and replace one of the level 1+ Wizard 
    spells you have prepared for your Spellcasting feature with another level 1+ spell from the book."""


# EOF
