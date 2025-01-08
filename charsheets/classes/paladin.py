from typing import Optional

from charsheets.abilities import (
    LayOnHands,
    WeaponMastery,
    FightingStyle,
    PaladinsSmite,
    ChannelDivinity,
    ExtraAttack,
    FaithfulSteed,
)
from charsheets.abilities.base_ability import BaseAbility
from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill
from charsheets.reason import Reason
from charsheets.spells import Spells


#################################################################################
class Paladin(Character):
    _base_skill_proficiencies = {
        Skill.ATHLETICS,
        Skill.INSIGHT,
        Skill.MEDICINE,
        Skill.PERSUASION,
        Skill.RELIGION,
    }

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 10

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.CHARISMA

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason("Paladin", Proficiency.SIMPLE_WEAPONS, Proficiency.MARTIAL_WEAPONS)

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason("Paladin", Proficiency.SHIELDS, Proficiency.LIGHT_ARMOUR, Proficiency.MEDIUM_ARMOUR, Proficiency.HEAVY_ARMOUR)

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.WISDOM, Stat.CHARISMA)

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {LayOnHands(), WeaponMastery()}

        if self.level >= 2:
            abilities.add(FightingStyle())
            abilities.add(PaladinsSmite())
        if self.level >= 3:
            abilities.add(ChannelDivinity())
        if self.level >= 5:
            abilities.add(ExtraAttack())
            abilities.add(FaithfulSteed())

        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            4: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 2, 0, 0, 0, 0, 0, 0, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def mod_add_known_spells(self, character: "Character") -> Reason[Spells]:
        paladin_spells = {
            0: [
                # Cantrips are learnt
            ],
            1: [
                Spells.BLESS,
                Spells.COMMAND,
                Spells.COMPELLED_DUEL,
                Spells.CURE_WOUNDS,
                Spells.DETECT_EVIL_AND_GOOD,
                Spells.DETECT_MAGIC,
                Spells.DETECT_POISON_AND_DISEASE,
                Spells.DIVINE_FAVOR,
                Spells.DIVINE_SMITE,
                Spells.HEROISM,
                Spells.PROTECTION_FROM_EVIL_AND_GOOD,
                Spells.PURIFY_FOOD_AND_DRINK,
                Spells.SEARING_SMITE,
                Spells.SHIELD_OF_FAITH,
                Spells.THUNDEROUS_SMITE,
                Spells.WRATHFUL_SMITE,
            ],
            2: [
                Spells.AID,
                Spells.FIND_STEED,
                Spells.GENTLE_REPOSE,
                Spells.LESSER_RESTORATION,
                Spells.LOCATE_OBJECT,
                Spells.MAGIC_WEAPON,
                Spells.PRAYER_OF_HEALING,
                Spells.PROTECTION_FROM_POISON,
                Spells.SHINING_SMITE,
                Spells.WARDING_BOND,
                Spells.ZONE_OF_TRUTH,
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
        for spells in paladin_spells.values():
            for spell in spells:
                known_spells |= Reason("Paladin Spell", spell)
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


# EOF
