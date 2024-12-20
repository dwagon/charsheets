from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class Scribe(BaseOrigin):
    tag = Origin.SCRIBE
    proficiencies = {Skill.INVESTIGATION, Skill.PERCEPTION}
    origin_feat = Feat.SKILLED
    tool_proficiency = "Calligrapher's Supplies"


# EOF
