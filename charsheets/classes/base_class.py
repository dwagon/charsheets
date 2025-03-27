from typing import Optional, TYPE_CHECKING, Any

from charsheets.constants import Skill, CharacterClass, Stat
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
        return charclass == self._base_class

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:  # pragma: no coverage
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
    def spell_slots(self, spell_level: int) -> int:
        # Should be overridden in spell casting classes
        return 0

    #########################################################################
    def add_level(self, level: int):
        assert self.character is not None
        level_name = f"level{level}"
        if level == 1:
            if self.character.level == 1:
                self.kwargs["hp"] = self.hit_dice
                self.level1init(**self.kwargs)
            else:
                self.level1multi(**self.kwargs)
            self.initialise_skills(self.kwargs["skills"])
        elif level in {4, 8, 12}:
            if "feat" not in self.kwargs:
                raise InvalidOption(f"Level {level} should specify a feat")
        if hasattr(self, level_name):
            getattr(self, level_name)(**self.kwargs)
        self._add_level(level, **self.kwargs)

    #########################################################################
    @property
    def class_special(self) -> str:
        return ""

    #########################################################################
    def _add_level(self, level: int, **kwargs: Any):
        assert self.character is not None
        self.level = level
        self.character.hp_track.append(Reason(f"level {level}", kwargs["hp"]))
        if "feat" in kwargs:
            self.add_feature(kwargs["feat"])
        if "feature" in kwargs:
            self.add_feature(kwargs["feature"])

    #############################################################################
    def level1multi(self, **kwargs: Any):
        """Multiclass into new class"""
        raise NotImplementedError

    #############################################################################
    def level1init(self, **kwargs: Any):
        """Start a new class (not multiclass)"""
        raise NotImplementedError


# EOF
