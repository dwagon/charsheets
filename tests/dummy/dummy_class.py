from typing import Optional

from charsheets.abilities import Rage
from charsheets.abilities.base_ability import BaseAbility
from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill
from charsheets.reason import Reason
from charsheets.weapons.base_weapon import BaseWeapon


###############################################################################
class DummyCharClass(Character):
    __test__ = False
    _base_skill_proficiencies = {
        Skill.ARCANA,
        Skill.HISTORY,
        Skill.INSIGHT,
        Skill.INVESTIGATION,
        Skill.MEDICINE,
        Skill.NATURE,
        Skill.RELIGION,
        Skill.DECEPTION,
        Skill.PERCEPTION,
    }

    @property
    def hit_dice(self) -> int:
        return 7

    ###########################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.INTELLIGENCE, Stat.WISDOM)

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {Rage()}
        return abilities

    #############################################################################
    def mod_ranged_atk_bonus(self, weapon: BaseWeapon) -> Reason:
        return Reason("test_char", 2)

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.STRENGTH

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason("DummyClass", Proficiency.SIMPLE_WEAPONS)

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason()


# EOF
