from charsheets.constants import Origin, Skill, Tool, Stat
from charsheets.feats import Alert
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Criminal(BaseOrigin):
    tag = Origin.CRIMINAL
    proficiencies = {Skill.SLEIGHT_OF_HAND, Skill.STEALTH}
    origin_feat = Alert
    tool_proficiency = Tool.THIEVES_TOOLS
    origin_stats = (Stat.DEXTERITY, Stat.CONSTITUTION, Stat.INTELLIGENCE)


# EOF
