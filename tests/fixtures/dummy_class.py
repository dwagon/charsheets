from typing import Optional

from charsheets.character import Character
from charsheets.constants import Ability, Stat
from charsheets.reason import Reason
from charsheets.weapon import BaseWeapon


###############################################################################
class DummyCharClass(Character):
    __test__ = False

    @property
    def hit_dice(self) -> int:
        return 7

    ###########################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        if stat in (Stat.INTELLIGENCE, Stat.WISDOM):
            return True

        return False

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = {Ability.RAGE}

        return abilities

    #############################################################################
    def mod_ranged_atk_bonus(self, weapon: BaseWeapon) -> Reason:
        return Reason("test_char", 2)

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.STRENGTH


# EOF
