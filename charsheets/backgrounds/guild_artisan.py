from typing import cast

from charsheets.backgrounds.base_background import BaseBackground
from charsheets.constants import Background, Skill, Tool


#################################################################################
class GuildArtisan(BaseBackground):
    tag = Background.GUILD_ARTISAN
    proficiencies = {Skill.INSIGHT, Skill.PERSUASION}
    tool_proficiencies = {cast(Tool, Tool.ARTISAN_TOOLS)}


# EOF
