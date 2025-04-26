from typing import cast

from charsheets.backgrounds2014.base_background import BaseBackground
from charsheets.constants import Background, Skill, Tool


#################################################################################
class Sailor(BaseBackground):
    tag = Background.SAILOR
    proficiencies = {Skill.ATHLETICS, Skill.PERCEPTION}
    tool_proficiencies = {cast(Tool, Tool.NAVIGATORS_TOOLS), cast(Tool, Tool.VEHICLES_SEA)}


# EOF
