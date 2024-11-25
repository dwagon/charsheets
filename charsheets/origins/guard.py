from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginGuard(BaseOrigin):
    tag = Origin.GUARD
    proficiencies = {Skill.ATHLETICS, Skill.PERCEPTION}
    origin_feat = Feat.ALERT
    tool_proficiency = "Gaming Set"


# EOF
