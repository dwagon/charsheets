""" Class based Stuff"""

from types import ModuleType
from typing import Optional, Type

from charsheets.constants import CharClassName, Stat, Proficiencies, Ability, CharSubclassName
from charsheets.exception import UnhandledException
from charsheets.spells import Spells

# from charsheets.util import import_generic


#############################################################################
class BaseCharClass:
    tag = "Unknown"

    def __init__(self, class_name: CharClassName, sub_class: CharSubclassName, pcm: ModuleType):
        self.class_name = class_name
        self.sub_class_name = sub_class
        self.pcm = pcm

    #########################################################################
    @property
    def hit_dice(self) -> int:
        raise NotImplemented

    #############################################################################
    def spell_slots(self, level: int) -> list[int]:
        raise NotImplemented

    #############################################################################
    def spells(self, spell_level: int) -> list[Spells]:
        raise NotImplemented

    #############################################################################
    def max_spell_level(self, char_level: int) -> int:
        raise NotImplemented

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        raise NotImplemented

    #############################################################################
    def name(self):
        if self.sub_class_name == CharSubclassName.NONE:
            return f"{self.class_name.title()}"
        return f"{self.class_name.title()} ({self.sub_class_name.title()})"

    #############################################################################
    def weapon_proficiency(self) -> set[Proficiencies]:
        raise NotImplemented

    #############################################################################
    def armour_proficiency(self) -> set[Proficiencies]:
        raise NotImplemented

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        raise NotImplemented

    #############################################################################
    def class_abilities(self, level: int) -> set[Ability]:
        raise NotImplemented


# EOF
