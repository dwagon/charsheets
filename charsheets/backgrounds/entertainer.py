from typing import cast

from charsheets.backgrounds.base_background import BaseBackground
from charsheets.constants import Background, Skill, Tool


#################################################################################
class Entertainer(BaseBackground):
    tag = Background.ENTERTAINER
    proficiencies = {Skill.ACROBATICS, Skill.PERFORMANCE}
    tool_proficiencies = {cast(Tool, Tool.MUSICAL_INSTRUMENT)}


# EOF
