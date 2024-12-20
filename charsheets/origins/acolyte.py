from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class Acolyte(BaseOrigin):
    tag = Origin.ACOLYTE
    proficiencies = {Skill.INSIGHT, Skill.RELIGION}
    origin_feat = Feat.MAGIC_INITIATE_CLERIC
    tool_proficiency = "Calligrapher's Supplies"


# EOF
