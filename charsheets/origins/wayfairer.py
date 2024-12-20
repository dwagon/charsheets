from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class Wayfairer(BaseOrigin):
    tag = Origin.WAYFARER
    proficiencies = {Skill.INSIGHT, Skill.STEALTH}
    origin_feat = Feat.LUCKY
    tool_proficiency = "Thieves' Tools"


# EOF
