from typing import cast

from charsheets.backgrounds2014.base_background import BaseBackground
from charsheets.constants import Background, Skill, Tool


#################################################################################
class Criminal(BaseBackground):
    tag = Background.CRIMINAL
    proficiencies = {Skill.DECEPTION, Skill.STEALTH}
    tool_proficiencies = {cast(Tool, Tool.GAMING_SET), cast(Tool, Tool.THIEVES_TOOLS)}


# EOF
