from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class Criminal(BaseOrigin):
    tag = Origin.CRIMINAL
    proficiencies = {Skill.SLEIGHT_OF_HAND, Skill.STEALTH}
    origin_feat = Feat.ALERT
    tool_proficiency = "Thieves' Tools"


# EOF
