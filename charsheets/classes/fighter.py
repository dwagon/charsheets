from typing import Optional

from charsheets.character import Character
from charsheets.constants import Stat, Proficiencies, Ability, CharSubclassName, Feat
from charsheets.spells import Spells


#################################################################################
class Fighter(Character):
    #############################################################################
    @property
    def hit_dice(self) -> int:
        return 10

    #############################################################################
    def fighting_style(self, style: Feat):
        self.feats_list.add(style)

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return None

    #############################################################################
    def weapon_proficiency(self) -> set[Proficiencies]:
        return {Proficiencies.SIMPLE_WEAPONS, Proficiencies.MARTIAL_WEAPONS}

    #############################################################################
    def armour_proficiency(self) -> set[Proficiencies]:
        return {Proficiencies.LIGHT_ARMOUR, Proficiencies.MEDIUM_ARMOUR, Proficiencies.HEAVY_ARMOUR, Proficiencies.SHIELDS}

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        if stat in (Stat.STRENGTH, Stat.CONSTITUTION):
            return True

        return False

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities = {Ability.WEAPON_MASTERY, Ability.ACTION_SURGE, Ability.SECOND_WIND}

        if self.level >= 2:
            abilities.add(Ability.TACTICAL_MIND)
        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return 0

    #############################################################################
    def max_spell_level(self) -> int:
        return 0

    #############################################################################
    def spells(self, spell_level: int) -> list[Spells]:
        return []


#################################################################################
class Champion(Fighter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_sub_class(CharSubclassName.CHAMPION)

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {Ability.IMPROVED_CRITICAL, Ability.REMARKABLE_ATHLETE}
        return abilities


#################################################################################
class EldritchKnight(Fighter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_sub_class(CharSubclassName.ELDRITCH_KNIGHT)

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {Ability.WAR_BOND}
        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [0, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [0, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [1, 0, 0, 0, 0, 0, 0, 0, 0],
            4: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            5: [3, 0, 0, 0, 0, 0, 0, 0, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def max_spell_level(self) -> int:
        if self.level >= 19:
            return 4
        if self.level >= 13:
            return 3
        if self.level >= 7:
            return 2
        if self.level >= 3:
            return 1
        return 0


#################################################################################
class PsiWarrior(Fighter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_sub_class(CharSubclassName.PSI_WARRIOR)

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {Ability.PSIONIC_POWER}
        return abilities


# EOF
