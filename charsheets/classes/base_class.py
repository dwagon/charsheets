import sys
from typing import Optional, TYPE_CHECKING, Any

from charsheets.constants import Skill, CharacterClass
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
#############################################################################
#############################################################################
class BaseClass:
    _base_class = CharacterClass.NONE

    #########################################################################
    def __init__(self, **kwargs: Any):
        self._class_name = ""
        self.level: int = 0
        self.kwargs = kwargs
        self.character: Optional["Character"] = None

    #########################################################################
    def initialise_skills(self, skills: list[Skill]) -> None:
        assert self.character is not None
        for skill in skills:
            self.character.skills[skill].proficient = True
            self.character.skills[skill].origin = f"{self.class_name} Class Skill"

    #########################################################################
    def add_feature(self, new_feature: BaseFeature):
        assert self.character is not None
        self.character.add_feature(new_feature)

    #########################################################################
    def is_subclass(self, charclass: CharacterClass) -> bool:
        raise NotImplementedError

    #########################################################################
    @property
    def class_name(self) -> str:
        if self._class_name:
            return self._class_name
        return self.__class__.__name__

    #########################################################################
    @property
    def hit_dice(self) -> int:  # pragma: no coverage
        raise NotImplementedError

    #########################################################################
    def add_level(self, level: int):
        match level:
            case 1:
                self.level1(**self.kwargs)
            case 2:
                self.level2(**self.kwargs)
            case 3:
                self.level3(**self.kwargs)
            case 4:
                self.level4(**self.kwargs)
            case 5:
                self.level5(**self.kwargs)
            case 6:
                self.level6(**self.kwargs)
            case 7:
                self.level7(**self.kwargs)
            case 8:
                self.level8(**self.kwargs)
            case 9:
                self.level9(**self.kwargs)
            case 10:
                self.level10(**self.kwargs)
            case 11:
                self.level11(**self.kwargs)
            case 12:
                self.level12(**self.kwargs)
            case 13:
                self.level13(**self.kwargs)
            case _:
                raise NotImplementedError(f"NotImplemented: add_level({level=})")

    #########################################################################
    def _add_level(self, level: int, **kwargs: Any):
        assert self.character is not None
        self.level = level
        self.character._hp.append(Reason(f"level {level}", kwargs["hp"]))
        if "feat" in kwargs:
            self.add_feature(kwargs["feat"])
        if "feature" in kwargs:
            self.add_feature(kwargs["feature"])

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        if self.character.level == 1:
            # TODO: Split into multiclass lvl 1 and pure lvl 1
            self.initialise_skills(kwargs["skills"])
            self.character.set_saving_throw_proficiency(kwargs["stats"])
            for armor in kwargs.get("armor", []):
                self.character.add_armor_proficiency(Reason(self.class_name, armor))
            for weapon in kwargs.get("weapons", []):
                self.character.add_weapon_proficiency(Reason(self.class_name, weapon))
            kwargs["hp"] = self.hit_dice
        self._add_level(1, **kwargs)

    #############################################################################
    def level2(self, **kwargs: Any):
        self._add_level(2, **kwargs)

    #############################################################################
    def level3(self, **kwargs: Any):
        self._add_level(3, **kwargs)

    #############################################################################
    def level4(self, **kwargs: Any):
        if "feat" not in kwargs:
            raise InvalidOption("Level 4 should specify a feat")
        self._add_level(4, **kwargs)

    #############################################################################
    def level5(self, **kwargs: Any):
        self._add_level(5, **kwargs)

    #############################################################################
    def level6(self, **kwargs: Any):
        self._add_level(6, **kwargs)

    #############################################################################
    def level7(self, **kwargs: Any):
        self._add_level(7, **kwargs)

    #############################################################################
    def level8(self, **kwargs: Any):
        if "feat" not in kwargs:
            raise InvalidOption("Level 8 should specify a feat")
        self._add_level(8, **kwargs)

    #############################################################################
    def level9(self, **kwargs: Any):
        self._add_level(9, **kwargs)

    #############################################################################
    def level10(self, **kwargs: Any):
        self._add_level(10, **kwargs)

    #############################################################################
    def level11(self, **kwargs: Any):
        self._add_level(11, **kwargs)

    #############################################################################
    def level12(self, **kwargs: Any):
        if "feat" not in kwargs:
            raise InvalidOption("Level 12 should specify a feat")
        self._add_level(12, **kwargs)

    #############################################################################
    def level13(self, **kwargs: Any):
        self._add_level(13, **kwargs)


# EOF
