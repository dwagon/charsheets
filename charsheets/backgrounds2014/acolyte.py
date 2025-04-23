from typing import TYPE_CHECKING
from charsheets.backgrounds2014.base_background import BaseBackground
from charsheets.constants import Skill, Background, Language
from charsheets.reason import Reason

if TYPE_CHECKING:
    from charsheets.character import BaseCharacter


#################################################################################
class Acolyte(BaseBackground):
    tag = Background.ACOLYTE
    proficiencies = {Skill.INSIGHT, Skill.RELIGION}

    def __init__(self, language1: Language, language2: Language):
        self._languages = [language1, language2]
        super().__init__()

    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason("Acolyte", *self._languages)


# EOF
