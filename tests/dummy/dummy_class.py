from typing import Optional
from charsheets.features import ExtraAttack
from charsheets.features.base_feature import BaseFeature
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
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {ExtraAttack()}
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
