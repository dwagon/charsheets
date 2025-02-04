from charsheets.constants import Origin, Skill, Tool, Stat
from charsheets.features import MagicInitiateWizard
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Sage(BaseOrigin):
    tag = Origin.SAGE
    proficiencies = {Skill.ARCANA, Skill.HISTORY}
    tool_proficiency = Tool.CALLIGRAPHERS_SUPPLIES
    origin_stats = (Stat.CONSTITUTION, Stat.INTELLIGENCE, Stat.WISDOM)

    def __init__(self, stat1: Stat, stat2: Stat, stat3: Stat, initiate: MagicInitiateWizard):
        super().__init__(stat1, stat2, stat3)
        self.origin_feat = initiate


# EOF
