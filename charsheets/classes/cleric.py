from typing import Optional

from charsheets.abilities import ChannelDivinity, SearUndead
from charsheets.abilities.base_ability import BaseAbility
from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill
from charsheets.reason import Reason
from charsheets.spells import Spells


#################################################################################
class Cleric(Character):
    _base_skill_proficiencies = {Skill.HISTORY, Skill.INSIGHT, Skill.MEDICINE, Skill.PERSUASION, Skill.RELIGION}

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 8

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.WISDOM

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason("Cleric", Proficiency.SIMPLE_WEAPONS)

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason("Cleric", Proficiency.SHIELDS, Proficiency.LIGHT_ARMOUR, Proficiency.MEDIUM_ARMOUR)

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.WISDOM, Stat.CHARISMA)

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()

        if self.level >= 2:
            abilities.add(ChannelDivinity())
        if self.level >= 3:
            abilities.add(SearUndead())
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
        }[self.level][spell_level - 1]

    #############################################################################
    def mod_add_known_spells(self, character: "Character") -> Reason[Spells]:
        cleric_spells = {
            0: [
                # Cantrips are learnt
            ],
            1: [
                Spells.BANE,
                Spells.BLESS,
                Spells.COMMAND,
                Spells.CREATE_OR_DESTROY_WATER,
                Spells.CURE_WOUNDS,
                Spells.DETECT_EVIL_AND_GOOD,
                Spells.DETECT_MAGIC,
                Spells.DETECT_POISON_AND_DISEASE,
                Spells.GUIDING_BOLT,
                Spells.HEALING_WORD,
                Spells.INFLICT_WOUNDS,
                Spells.PROTECTION_FROM_EVIL_AND_GOOD,
                Spells.PURIFY_FOOD_AND_DRINK,
                Spells.SANCTUARY,
                Spells.SHIELD_OF_FAITH,
            ],
            2: [
                Spells.AID,
                Spells.AUGURY,
                Spells.BLINDNESS_DEAFNESS,
                Spells.CALM_EMOTIONS,
                Spells.CONTINUAL_FLAME,
                Spells.ENHANCE_ABILITY,
                Spells.FIND_TRAPS,
                Spells.GENTLE_REPOSE,
                Spells.HOLD_PERSON,
                Spells.LESSER_RESTORATION,
                Spells.LOCATE_OBJECT,
                Spells.PRAYER_OF_HEALING,
                Spells.PROTECTION_FROM_POISON,
                Spells.SILENCE,
                Spells.SPIRITUAL_WEAPON,
                Spells.WARDING_BOND,
                Spells.ZONE_OF_TRUTH,
            ],
            3: [
                Spells.ANIMATE_DEAD,
                Spells.AURA_OF_VITALITY,
                Spells.BEACON_OF_HOPE,
                Spells.BESTOW_CURSE,
                Spells.CLAIRVOYANCE,
                Spells.CREATE_FOOD_AND_WATER,
                Spells.DAYLIGHT,
                Spells.DISPEL_MAGIC,
                Spells.FEIGN_DEATH,
                Spells.GLYPH_OF_WARDING,
                Spells.MAGIC_CIRCLE,
                Spells.MASS_HEALING_WORD,
                Spells.MELD_INTO_STONE,
                Spells.PROTECTION_FROM_ENERGY,
                Spells.REMOVE_CURSE,
                Spells.REVIVIFY,
                Spells.SENDING,
                Spells.SPEAK_WITH_DEAD,
                Spells.SPIRIT_GUARDIANS,
                Spells.TONGUES,
                Spells.WATER_WALK,
            ],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
        }

        known_spells: Reason[Spells] = Reason()
        for spells in cleric_spells.values():
            for spell in spells:
                known_spells |= Reason("Cleric Spell", spell)
        return known_spells

    #############################################################################
    def max_spell_level(self) -> int:
        return min(9, ((self.level + 1) // 2))


# EOF
