from typing import Optional, Any

from charsheets.character import Character
from charsheets.classes.base_class import BaseClass
from charsheets.constants import Stat, Skill
from charsheets.features import ExtraAttack
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.weapons.base_weapon import BaseWeapon


###############################################################################
class DummyCharClass(BaseClass):
    __test__ = False
    _base_skill_proficiencies = {
        Skill.ARCANA,
        Skill.HISTORY,
        Skill.INSIGHT,
        Skill.MEDICINE,
        Skill.NATURE,
        Skill.DECEPTION,
        Skill.PERCEPTION,
    }

    #############################################################################
    def level1init(self, **kwargs: Any):
        assert self.character is not None
        self.character.set_saving_throw_proficiency(Stat.INTELLIGENCE, Stat.WISDOM)

    #############################################################################
    def level1multi(self, **kwargs: Any):
        assert self.character is not None

    #############################################################################
    def level1(self, **kwargs: Any):
        self.add_feature(ExtraAttack())

    ###########################################################################
    @property
    def hit_dice(self) -> int:
        return 7

    ###########################################################################
    def mod_extra_attack(self, character: "Character") -> Reason[str]:
        return Reason("Extra Attack", "Bunny Rabbit")

    ###########################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.INTELLIGENCE, Stat.WISDOM)

    #############################################################################
    def mod_ranged_atk_bonus(self, weapon: BaseWeapon) -> Reason:
        return Reason("test_char", 2)

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.STRENGTH


# EOF
