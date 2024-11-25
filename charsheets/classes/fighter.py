from typing import Optional

from charsheets.character import Character
from charsheets.constants import Stat, Proficiencies, Ability, CharSubclassName, Feat
from charsheets.exception import UnhandledException


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
    def class_abilities(self, level: int) -> set[Ability]:
        abilities = set()

        abilities.add(Ability.WEAPON_MASTERY)
        abilities.add(Ability.ACTION_SURGE)
        abilities.add(Ability.SECOND_WIND)

        if level >= 2:
            abilities.add(Ability.TACTICAL_MIND)
        if level >= 3:
            match self.sub_class_name:
                case CharSubclassName.CHAMPION:
                    abilities.add(Ability.IMPROVED_CRITICAL)
                    abilities.add(Ability.REMARKABLE_ATHLETE)
                case _:
                    raise UnhandledException(f"{self.sub_class_name} doesn't have class_abilities() defined")

        return abilities

    #############################################################################
    def spell_slots(self, level: int) -> list[int]:
        return [0, 0, 0, 0, 0, 0, 0, 0, 0]

    #############################################################################
    def max_spell_level(self, char_level: int) -> int:
        return 0

    #############################################################################
    def spells(self, spell_level: int) -> list[tuple[str, str]]:
        return []


# EOF
