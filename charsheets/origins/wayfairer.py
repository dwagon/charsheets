from charsheets.constants import Origin, Skill, Tool
from charsheets.feats import Lucky
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Wayfairer(BaseOrigin):
    tag = Origin.WAYFARER
    proficiencies = {Skill.INSIGHT, Skill.STEALTH}
    origin_feat = Lucky
    tool_proficiency = Tool.THIEVES_TOOLS


# EOF
