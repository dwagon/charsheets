from typing import Optional

from charsheets.abilities import WeaponMastery, FightingStyle, ExtraAttack
from charsheets.abilities.base_ability import BaseAbility
from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill, Ability
from charsheets.reason import Reason
from charsheets.spells import Spells


#################################################################################
class Ranger(Character):
    _base_skill_proficiencies = {
        Skill.ANIMAL_HANDLING,
        Skill.ATHLETICS,
        Skill.INSIGHT,
        Skill.INVESTIGATION,
        Skill.NATURE,
        Skill.PERCEPTION,
        Skill.STEALTH,
        Skill.SURVIVAL,
    }

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 10

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.WISDOM

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason("Ranger", Proficiency.SIMPLE_WEAPONS, Proficiency.MARTIAL_WEAPONS)

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason("Ranger", Proficiency.SHIELDS, Proficiency.LIGHT_ARMOUR, Proficiency.MEDIUM_ARMOUR)
        # type: ignore

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.STRENGTH, Stat.DEXTERITY)

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {FavoredEnemy(), WeaponMastery()}
        if self.level >= 2:
            abilities.add(DeftExplorer())
            abilities.add(FightingStyle())
        if self.level >= 5:
            abilities.add(ExtraAttack())
        if self.level >= 5:
            abilities.add(Roving())
        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            4: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            6: [4, 2, 0, 0, 0, 0, 0, 0, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def mod_add_known_spells(self, character: "Character") -> Reason[Spells]:
        ranger_spells = {
            0: [],
            1: [
                Spells.ALARM,
                Spells.ANIMAL_FRIENDSHIP,
                Spells.CURE_WOUNDS,
                Spells.DETECT_MAGIC,
                Spells.DETECT_POISON_AND_DISEASE,
                Spells.ENSNARING_STRIKE,
                Spells.ENTANGLE,
                Spells.FOG_CLOUD,
                Spells.GOODBERRY,
                Spells.HAIL_OF_THORNS,
                Spells.HUNTERS_MARK,
                Spells.JUMP,
                Spells.LONGSTRIDER,
                Spells.SPEAK_WITH_ANIMALS,
            ],
            2: [
                Spells.AID,
                Spells.ANIMAL_MESSENGER,
                Spells.BARKSKIN,
                Spells.BEAST_SENSE,
                Spells.CORDON_OF_ARROWS,
                Spells.DARKVISION,
                Spells.ENHANCE_ABILITY,
                Spells.FIND_TRAPS,
                Spells.GUST_OF_WIND,
                Spells.LESSER_RESTORATION,
                Spells.LOCATE_ANIMALS_OR_PLANTS,
                Spells.MAGIC_WEAPON,
                Spells.PASS_WITHOUT_TRACE,
                Spells.PROTECTION_FROM_POISON,
                Spells.SILENCE,
                Spells.SPIKE_GROWTH,
                Spells.SUMMON_BEAST,
            ],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
        }

        known_spells: Reason[Spells] = Reason()
        for spells in ranger_spells.values():
            for spell in spells:
                known_spells |= Reason("Ranger Spell", spell)
        return known_spells

    #############################################################################
    def max_spell_level(self) -> int:
        if self.level >= 17:
            return 5
        elif self.level >= 13:
            return 4
        elif self.level >= 9:
            return 3
        elif self.level >= 5:
            return 2
        return 1


#############################################################################
class FavoredEnemy(BaseAbility):
    tag = Ability.FAVOURED_ENEMY
    _desc = """You always have the Hunter's Mark spell prepared. You can cast it twice without expending a spell slot
    and you regain all expended uses of this ability when you finish a Long Rest.
    """

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        return Reason("Favoured Enemy", Spells.HUNTERS_MARK)


#############################################################################
class DeftExplorer(BaseAbility):
    tag = Ability.DEFT_EXPLORER
    _desc = """Thanks to your travels, you gain the following benefits.

    Expertise. Choose one of your skill proficiencies with which you lack Expertise. You gain Expertise in that skill.

    Languages. You know two languages of your choice"""
    # TODO - select languages
    # TODO - select skill


#############################################################################
class FeywildGifts(BaseAbility):
    tag = Ability.FEYWILD_GIFTS
    _desc = """You possess a fey blessing."""


#############################################################################
class Roving(BaseAbility):
    tag = Ability.ROVING
    _desc = """Your speed increases by 10 feet if you aren't wearing Heavy armor. You also have a Climb Speed
    and Swim Speed equal to your Speed."""


# EOF
