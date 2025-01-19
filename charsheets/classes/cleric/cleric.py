from typing import Optional

from charsheets.abilities.base_ability import BaseAbility
from charsheets.abilities import ChannelDivinity
from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill, Ability
from charsheets.reason import Reason
from charsheets.spell import Spell


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
    def mod_add_known_spells(self, character: "Character") -> Reason[Spell]:
        cleric_spells = {
            0: [
                # Cantrips are learnt
            ],
            1: [
                Spell.BANE,
                Spell.BLESS,
                Spell.COMMAND,
                Spell.CREATE_OR_DESTROY_WATER,
                Spell.CURE_WOUNDS,
                Spell.DETECT_EVIL_AND_GOOD,
                Spell.DETECT_MAGIC,
                Spell.DETECT_POISON_AND_DISEASE,
                Spell.GUIDING_BOLT,
                Spell.HEALING_WORD,
                Spell.INFLICT_WOUNDS,
                Spell.PROTECTION_FROM_EVIL_AND_GOOD,
                Spell.PURIFY_FOOD_AND_DRINK,
                Spell.SANCTUARY,
                Spell.SHIELD_OF_FAITH,
            ],
            2: [
                Spell.AID,
                Spell.AUGURY,
                Spell.BLINDNESS_DEAFNESS,
                Spell.CALM_EMOTIONS,
                Spell.CONTINUAL_FLAME,
                Spell.ENHANCE_ABILITY,
                Spell.FIND_TRAPS,
                Spell.GENTLE_REPOSE,
                Spell.HOLD_PERSON,
                Spell.LESSER_RESTORATION,
                Spell.LOCATE_OBJECT,
                Spell.PRAYER_OF_HEALING,
                Spell.PROTECTION_FROM_POISON,
                Spell.SILENCE,
                Spell.SPIRITUAL_WEAPON,
                Spell.WARDING_BOND,
                Spell.ZONE_OF_TRUTH,
            ],
            3: [
                Spell.ANIMATE_DEAD,
                Spell.AURA_OF_VITALITY,
                Spell.BEACON_OF_HOPE,
                Spell.BESTOW_CURSE,
                Spell.CLAIRVOYANCE,
                Spell.CREATE_FOOD_AND_WATER,
                Spell.DAYLIGHT,
                Spell.DISPEL_MAGIC,
                Spell.FEIGN_DEATH,
                Spell.GLYPH_OF_WARDING,
                Spell.MAGIC_CIRCLE,
                Spell.MASS_HEALING_WORD,
                Spell.MELD_INTO_STONE,
                Spell.PROTECTION_FROM_ENERGY,
                Spell.REMOVE_CURSE,
                Spell.REVIVIFY,
                Spell.SENDING,
                Spell.SPEAK_WITH_DEAD,
                Spell.SPIRIT_GUARDIANS,
                Spell.TONGUES,
                Spell.WATER_WALK,
            ],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
        }

        known_spells: Reason[Spell] = Reason()
        for spells in cleric_spells.values():
            for spell in spells:
                known_spells |= Reason("Cleric Spell", spell)
        return known_spells

    #############################################################################
    def max_spell_level(self) -> int:
        return min(9, ((self.level + 1) // 2))


#############################################################################
class SearUndead(BaseAbility):
    tag = Ability.SEAR_UNDEAD
    _desc = ""

    @property
    def desc(self) -> str:
        bonus = max(1, self.owner.wisdom.modifier)
        return f"""Whenever you use Turn Undead, you can roll {bonus}d8's 
    and add the rolls together. Each Undead that fails its saving throw against that use of Turn Undead takes Radiant
    damage equal to the roll's total. This damage doesn't end the turn effect."""


#################################################################################
class DivineProtector(BaseAbility):
    tag = Ability.DIVINE_ORDER_PROTECTOR
    _desc = """Trained for battle, you gain proficiency with Martial weapons and training with Heavy armor."""
    hide = True

    #############################################################################
    def mod_weapon_proficiency(self, character: "Character") -> Reason[Proficiency]:
        return Reason[Proficiency]("Protector", Proficiency.MARTIAL_WEAPONS)

    #############################################################################
    def mod_armour_proficiency(self, character: "Character") -> Reason[Proficiency]:
        return Reason("Protector", Proficiency.HEAVY_ARMOUR)


#################################################################################
class Thaumaturge(BaseAbility):
    tag = Ability.DIVINE_ORDER_THAUMATURGE
    _desc = """Thaumaturge. You know one extra cantrip from the Cleric spell list."""

    # Users will have to add their own cantrip to the learnt spells.

    def mod_skill_arcana(self, character: "Character") -> Reason[int]:
        return Reason[int]("thaumaturge", max(1, character.wisdom.modifier))

    def mod_skill_religion(self, character: "Character") -> Reason[int]:
        return Reason[int]("thaumaturge", max(1, character.wisdom.modifier))


# EOF
