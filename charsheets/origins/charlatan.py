from typing import cast

from charsheets.constants import Origin, Skill, Tool, Stat
from charsheets.features import Skilled
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Charlatan(BaseOrigin):
    tag = Origin.CHARLATAN
    proficiencies = {Skill.DECEPTION, Skill.SLEIGHT_OF_HAND}
    tool_proficiency = cast(Tool, Tool.FORGERY_KIT)
    origin_stats = (Stat.DEXTERITY, Stat.CONSTITUTION, Stat.CHARISMA)

    def __init__(self, stat1: Stat, stat2: Stat, stat3: Stat, skilled: Skilled):
        super().__init__(stat1, stat2, stat3)
        self.origin_feat = skilled


# EOF
