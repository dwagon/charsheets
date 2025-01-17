from charsheets.abilities import MagicInitiateWizard
from charsheets.constants import Origin, Skill, Tool, Stat
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Sage(BaseOrigin):
    tag = Origin.SAGE
    proficiencies = {Skill.ARCANA, Skill.HISTORY}
    origin_feat = MagicInitiateWizard
    tool_proficiency = Tool.CALLIGRAPHERS_SUPPLIES
    origin_stats = (Stat.CONSTITUTION, Stat.INTELLIGENCE, Stat.WISDOM)


# EOF
