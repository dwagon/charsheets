from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Origin, Skill, Tool, Stat
from charsheets.abilities import MagicInitiateCleric


#################################################################################
class Acolyte(BaseOrigin):
    tag = Origin.ACOLYTE
    proficiencies = {Skill.INSIGHT, Skill.RELIGION}
    origin_feat = MagicInitiateCleric
    tool_proficiency = Tool.CALLIGRAPHERS_SUPPLIES
    origin_stats = (Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA)


# EOF
