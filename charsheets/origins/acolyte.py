from typing import cast

from charsheets.constants import Origin, Skill, Tool, Stat
from charsheets.features import MagicInitiateCleric
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Acolyte(BaseOrigin):
    tag = Origin.ACOLYTE
    proficiencies = {Skill.INSIGHT, Skill.RELIGION}
    tool_proficiency = cast(Tool, Tool.CALLIGRAPHERS_SUPPLIES)
    origin_stats = (Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA)

    def __init__(self, stat1: Stat, stat2: Stat, stat3: Stat, initiate: MagicInitiateCleric):
        super().__init__(stat1, stat2, stat3)
        self.origin_feat = initiate


# EOF
