from typing import cast

from charsheets.constants import Origin, Skill, Tool, Stat
from charsheets.features import Crafter
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Artisan(BaseOrigin):
    tag = Origin.ARTISAN
    proficiencies = {Skill.INVESTIGATION, Skill.PERSUASION}
    tool_proficiency = cast(Tool, Tool.ARTISAN_TOOLS)
    origin_stats = (Stat.STRENGTH, Stat.DEXTERITY, Stat.INTELLIGENCE)

    def __init__(self, stat1: Stat, stat2: Stat, stat3: Stat, crafter: Crafter):
        super().__init__(stat1, stat2, stat3)
        self.origin_feat = crafter


# EOF
