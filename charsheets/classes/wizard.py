from typing import Optional

from charsheets.character import Character
from charsheets.constants import Stat, Proficiencies, Ability, CharSubclassName
from charsheets.spells import Spells, SPELL_LEVELS


#################################################################################
class Wizard(Character):
    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 6

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.INTELLIGENCE

    #############################################################################
    def weapon_proficiency(self) -> set[Proficiencies]:
        return {
            Proficiencies.SIMPLE_WEAPONS,
        }

    #############################################################################
    def armour_proficiency(self) -> set[Proficiencies]:
        return set()

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        if stat in (Stat.INTELLIGENCE, Stat.WISDOM):
            return True

        return False

    #############################################################################
    def class_abilities(self, level: int) -> set[Ability]:
        abilities = set()
        abilities.add(Ability.RITUAL_ADEPT)
        abilities.add(Ability.ARCANE_RECOVERY)

        if level >= 2:
            abilities.add(Ability.SCHOLAR)
        if level >= 3:
            match self.sub_class_name:
                case CharSubclassName.ABJURER:
                    pass
                case CharSubclassName.DIVINER:
                    pass
                case CharSubclassName.EVOKER:
                    pass
                case CharSubclassName.ILLUSIONIST:
                    pass

        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            4: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 3, 2, 0, 0, 0, 0, 0, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def spells(self, spell_level: int) -> list[Spells]:
        wizard_spells: dict[int, list[Spells]] = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
        }

        result = wizard_spells[spell_level]
        for spell in self.known_spells:
            if SPELL_LEVELS[spell] == spell_level:
                result.append(spell)
        return result

    #############################################################################
    def max_spell_level(self, char_level: int) -> int:
        return min(9, (self.level // 2) + 1)


# EOF
