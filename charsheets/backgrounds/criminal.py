from typing import cast

from charsheets.backgrounds.base_background import BaseBackground
from charsheets.constants import Background, Skill, Tool


#################################################################################
class Criminal(BaseBackground):
    tag = Background.CRIMINAL
    proficiencies = {Skill.DECEPTION, Skill.STEALTH}
    tool_proficiencies = {cast(Tool, Tool.GAMING_SET)}


# EOF
