""" Class based Stuff"""

from constants import CharClassName, Stat


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
    def __str__(self):
        return self.class_name.title()

    #############################################################################
    def stat_proficiency(self, stat: Stat) -> bool:
        match self.class_name:
            case CharClassName.RANGER:
                if stat in (Stat.STRENGTH, Stat.DEXTERITY):
                    return True
        return False
