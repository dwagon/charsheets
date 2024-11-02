""" Class based Stuff"""

from charsheets.constants import CharClassName, Stat


#############################################################################
class CharClass:
    def __init__(self, name: CharClassName):
        self.class_name = name

    #########################################################################
    @property
    def hit_dice(self) -> int:
        match self.class_name:
            case CharClassName.RANGER:
                return 8
        return 0

    #############################################################################
    def spell_slots(self, level: int) -> list[int]:
        ranger_slots = {
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            4: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 2, 0, 0, 0, 0, 0, 0, 0],
        }
        match self.class_name:
            case CharClassName.RANGER:
                return ranger_slots[level]

        return [0, 0, 0, 0, 0, 0, 0, 0, 0]

    #############################################################################
    @property
    def spell_casting_ability(self) -> Stat:
        match self.class_name:
            case CharClassName.RANGER:
                return Stat.WISDOM

    #############################################################################
    def __str__(self):
        return self.class_name.title()

    #############################################################################
    def stat_proficiency(self, stat: Stat) -> bool:
        match self.class_name:
            case CharClassName.RANGER:
                if stat in (Stat.STRENGTH, Stat.DEXTERITY):
                    return True
        return False
