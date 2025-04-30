from typing import Optional, TYPE_CHECKING, Any

from charsheets.constants import Skill, CharacterClass, Stat
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
#############################################################################
#############################################################################
class BaseClass:
    _base_class = CharacterClass.NONE
    _base_skill_proficiencies: set[Skill] = set()
    _class_name = "Undefined"

    #########################################################################
    def __init__(self, **kwargs: Any):
        self.level: int = 0
        self.kwargs = kwargs
        self.character: Optional["Character"] = None

    #########################################################################
    def __repr__(self) -> str:
        return f"<{self.class_name}:{self.level}>"

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
        return self._class_name or self.__class__.__name__

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
                assert "skills" in self.kwargs
                self.kwargs["hp"] = self.hit_dice
                self.level1init(**self.kwargs)
            else:
                self.level1multi(**self.kwargs)
            self.initialise_skills(self.kwargs.get("skills", []))
        elif level in {4, 8, 12, 16}:
            if "feat" not in self.kwargs:
                raise InvalidOption(f"Level {level} should specify a feat")
        elif level == 19:
            if "boon" not in self.kwargs:
                raise InvalidOption("Level 19 should specify an epic boon with 'boon=...")
            self.add_feature(self.kwargs["boon"])
        if hasattr(self, level_name):
            getattr(self, level_name)(**self.kwargs)
        self.every_level(**self.kwargs)
        self.level = level
        self.character.hp_track.append(Reason(f"level {level}", self.kwargs["hp"]))
        if "feat" in self.kwargs:
            self.add_feature(self.kwargs["feat"])

    #########################################################################
    @property
    def class_special(self) -> str:
        return ""

    #########################################################################
    def check_modifiers(self, modifier: str) -> Reason:
        assert self.character is not None
        result = Reason[Any]()
        if self.character.has_modifier(self, modifier):
            value = getattr(self, modifier)(character=self)
            result.extend(self.character._handle_modifier_result(value, f"Class {self.class_name}"))
        return result

    #############################################################################
    def level1multi(self, **kwargs: Any):
        """Multiclass into new class"""
        raise NotImplementedError  # pragma: no coverage

    #############################################################################
    def level1init(self, **kwargs: Any):
        """Start a new class (not multiclass)"""
        raise NotImplementedError  # pragma: no coverage

    #############################################################################
    def every_level(self, **kwargs: Any):
        """Potentially invoked by subclass every level"""
        pass  # pragma: no coverage

    #############################################################################
    def spell_damage_bonus(self, spell: Spell) -> int:
        return 0

    #############################################################################
    def spell_notes(self, spell: Spell) -> str:
        return ""


# EOF
