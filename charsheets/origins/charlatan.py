from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginCharlatan(BaseOrigin):
    tag = Origin.CHARLATAN
    proficiencies = {Skill.DECEPTION, Skill.SLEIGHT_OF_HAND}
    origin_feat = Feat.SKILLED
    tool_proficiency = "Forgery Kit"


# EOF
