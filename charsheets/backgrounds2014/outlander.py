from typing import cast

from charsheets.backgrounds2014.base_background import BaseBackground
from charsheets.constants import Background, Skill, Tool


#################################################################################
class Outlander(BaseBackground):
    tag = Background.OUTLANDER
    proficiencies = {Skill.ATHLETICS, Skill.SURVIVAL}
    tool_proficiencies = {cast(Tool, Tool.MUSICAL_INSTRUMENT)}


# EOF
