from typing import cast, TYPE_CHECKING

from charsheets.backgrounds.base_background import BaseBackground
from charsheets.constants import Background, Skill, Tool, Language
from charsheets.reason import Reason

if TYPE_CHECKING:
    from charsheets.character import BaseCharacter


#################################################################################
class Noble(BaseBackground):
    tag = Background.NOBLE
    proficiencies = {Skill.HISTORY, Skill.PERSUASION}
    tool_proficiencies = {cast(Tool, Tool.GAMING_SET)}

    def __init__(self, language: Language):
        self._language = language
        super().__init__()

    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason("Noble", *self._language)


# EOF
