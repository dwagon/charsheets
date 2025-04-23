from typing import cast

from aenum import extend_enum

from charsheets.backgrounds2014.base_background import BaseBackground
from charsheets.constants import Background, Skill, Tool, Feature

extend_enum(Feature, "ARCANE_RECOVERY14", "Arcane Recovery")


#################################################################################
class Criminal(BaseBackground):
    tag = Background.CRIMINAL
    proficiencies = {Skill.DECEPTION, Skill.STEALTH}
    tool_proficiencies = {cast(Tool, Tool.GAMING_SET)}

    def __init__(self):
        super().__init__()


# EOF
