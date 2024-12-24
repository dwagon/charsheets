from charsheets.constants import Origin, Skill, Tools
from charsheets.feats import Alert
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Criminal(BaseOrigin):
    tag = Origin.CRIMINAL
    proficiencies = {Skill.SLEIGHT_OF_HAND, Skill.STEALTH}
    origin_feat = Alert
    tool_proficiency = Tools.THIEVES_TOOLS


# EOF
