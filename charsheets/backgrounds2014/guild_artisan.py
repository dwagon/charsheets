from typing import cast, TYPE_CHECKING

from charsheets.backgrounds2014.base_background import BaseBackground
from charsheets.constants import Background, Skill, Tool, Language
from charsheets.reason import Reason

if TYPE_CHECKING:
    from charsheets.character import BaseCharacter


#################################################################################
class GuildArtisan(BaseBackground):
    tag = Background.GUILD_ARTISAN
    proficiencies = {Skill.INSIGHT, Skill.PERSUASION}
    tool_proficiencies = {cast(Tool, Tool.ARTISAN_TOOLS)}

    def __init__(self, language: Language):
        self._language = language
        super().__init__()

    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason("Guild Artisan", self._language)


# EOF
