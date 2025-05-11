import math
from typing import Optional, Any, TYPE_CHECKING

from aenum import extend_enum
from charsheets.classes.base_class import BaseClass
from charsheets.constants import Stat, Skill, Feature, Recovery, CharacterClass, Weapon
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason

extend_enum(Feature, "ARCANE_RECOVERY14", "Arcane Recovery")

if TYPE_CHECKING:
    from charsheets.character import BaseCharacter


#################################################################################
class Wizard(BaseClass):
    _base_skill_proficiencies = {
        Skill.ARCANA,
        Skill.HISTORY,
        Skill.INSIGHT,
        Skill.INVESTIGATION,
        Skill.MEDICINE,
        Skill.RELIGION,
    }
    _base_class = CharacterClass.WIZARD
    _class_name = "Wizard"

    #############################################################################
    def mod_specific_weapon_proficiency(self, character: "BaseCharacter") -> Reason[Weapon]:
        return Reason("Wizard", Weapon.DAGGER, Weapon.DART, Weapon.SLING, Weapon.QUARTERSTAFF, Weapon.LIGHT_CROSSBOW)

    #############################################################################
    def level1init(self, **kwargs: Any):
        assert self.character is not None
        self.character.set_saving_throw_proficiency(Stat.INTELLIGENCE, Stat.WISDOM)

    #############################################################################
    def level1multi(self, **kwargs: Any):
        assert self.character is not None

    #############################################################################
    def level1(self, **kwargs: Any):
        self.add_feature(ArcaneRecovery())

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 6

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.INTELLIGENCE

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            4: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 3, 2, 0, 0, 0, 0, 0, 0],
            6: [4, 3, 3, 0, 0, 0, 0, 0, 0],
            7: [4, 3, 3, 1, 0, 0, 0, 0, 0],
            8: [4, 3, 3, 2, 0, 0, 0, 0, 0],
            9: [4, 3, 3, 3, 1, 0, 0, 0, 0],
            10: [4, 3, 3, 3, 2, 0, 0, 0, 0],
            11: [4, 3, 3, 3, 2, 1, 0, 0, 0],
            12: [4, 3, 3, 3, 2, 1, 0, 0, 0],
            13: [4, 3, 3, 3, 2, 1, 1, 0, 0],
            14: [4, 3, 3, 3, 2, 1, 1, 0, 0],
            15: [4, 3, 3, 3, 2, 1, 1, 1, 0],
            16: [4, 3, 3, 3, 2, 1, 1, 1, 0],
            17: [4, 3, 3, 3, 2, 1, 1, 1, 1],
            18: [4, 3, 3, 3, 3, 1, 1, 1, 1],
            19: [4, 3, 3, 3, 3, 2, 1, 1, 1],
            20: [4, 3, 3, 3, 3, 2, 2, 1, 1],
        }[self.level][spell_level - 1]


#############################################################################
class ArcaneRecovery(BaseFeature):
    tag = Feature.ARCANE_RECOVERY
    recovery = Recovery.SHORT_REST
    goes = 1

    @property
    def desc(self) -> str:
        slots = math.ceil(self.owner.level / 2)
        return f"""Once per day when you finish a short rest, you can choose expended spell slots to recover. The 
        spell slots can have a combined level that is equal to less than {slots}, and none of the slots can be level 
        6 or higher."""


# EOF
