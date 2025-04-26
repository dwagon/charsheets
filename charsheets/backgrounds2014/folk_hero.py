from typing import cast

from charsheets.backgrounds2014.base_background import BaseBackground
from charsheets.constants import Background, Skill, Tool


#################################################################################
class FolkHero(BaseBackground):
    tag = Background.FOLK_HERO
    proficiencies = {Skill.ANIMAL_HANDLING, Skill.SURVIVAL}
    tool_proficiencies = {cast(Tool, Tool.ARTISAN_TOOLS), cast(Tool, Tool.VEHICLES_LAND)}


# EOF
