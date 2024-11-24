from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginAcolyte(BaseOrigin):
    tag = Origin.ACOLYTE
    proficiencies = {Skill.INSIGHT, Skill.RELIGION}
    origin_feat = Feat.MAGIC_INITIATE_CLERIC


# EOF
