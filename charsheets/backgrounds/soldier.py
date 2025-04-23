from typing import cast

from charsheets.backgrounds.base_background import BaseBackground
from charsheets.constants import Background, Skill, Tool


#################################################################################
class Soldier(BaseBackground):
    tag = Background.SOLDIER
    proficiencies = {Skill.ATHLETICS, Skill.INTIMIDATION}
    tool_proficiencies = {cast(Tool, Tool.GAMING_SET)}


# EOF
