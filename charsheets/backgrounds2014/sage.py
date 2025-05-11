from typing import TYPE_CHECKING

from charsheets.backgrounds2014.base_background import BaseBackground
from charsheets.constants import Background, Skill, Language
from charsheets.reason import Reason

if TYPE_CHECKING:
    from charsheets.character import BaseCharacter


#################################################################################
class Sage(BaseBackground):
    tag = Background.SAGE
    proficiencies = {Skill.ARCANA, Skill.HISTORY}
    tool_proficiencies = set()

    def __init__(self, language1: Language, language2: Language):
        self._languages = [language1, language2]
        super().__init__()

    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason("Outlander", *self._languages)


# EOF
