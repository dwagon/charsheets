from typing import cast

from charsheets.backgrounds2014.base_background import BaseBackground
from charsheets.constants import Skill, Tool, Background


#################################################################################
class Charlatan(BaseBackground):
    tag = Background.CHARLATAN
    proficiencies = {Skill.DECEPTION, Skill.SLEIGHT_OF_HAND}
    tool_proficiency = {cast(Tool, Tool.FORGERY_KIT), cast(Tool, Tool.DISGUISE_KIT)}


# EOF
