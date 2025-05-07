from typing import cast, TYPE_CHECKING

from charsheets.backgrounds2014.base_background import BaseBackground
from charsheets.constants import Background, Skill, Tool, Language
from charsheets.reason import Reason

if TYPE_CHECKING:
    from charsheets.character import BaseCharacter


#################################################################################
class Outlander(BaseBackground):
    tag = Background.OUTLANDER
    proficiencies = {Skill.ATHLETICS, Skill.SURVIVAL}
    tool_proficiencies = {cast(Tool, Tool.MUSICAL_INSTRUMENT)}

    def __init__(self, language: Language):
        self._language = language
        super().__init__()

    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason("Outlander", self._language)


# EOF
