from typing import cast

from charsheets.constants import Origin, Skill, Tool, Stat
from charsheets.features import Skilled
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Noble(BaseOrigin):
    tag = Origin.NOBLE
    proficiencies = {Skill.HISTORY, Skill.PERSUASION}
    tool_proficiency = cast(Tool, Tool.GAMING_SET)
    origin_stats = (Stat.STRENGTH, Stat.INTELLIGENCE, Stat.CHARISMA)

    def __init__(self, stat1: Stat, stat2: Stat, stat3: Stat, skilled: Skilled):
        super().__init__(stat1, stat2, stat3)
        self.origin_feat = skilled


# EOF
