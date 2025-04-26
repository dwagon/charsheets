from typing import cast

from charsheets.backgrounds2014.base_background import BaseBackground
from charsheets.constants import Background, Skill, Tool


#################################################################################
class Urchin(BaseBackground):
    tag = Background.URCHIN
    proficiencies = {Skill.SLEIGHT_OF_HAND, Skill.STEALTH}
    tool_proficiencies = {cast(Tool, Tool.DISGUISE_KIT), cast(Tool, Tool.THIEVES_TOOLS)}


# EOF
