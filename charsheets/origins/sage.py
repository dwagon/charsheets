from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginSage(BaseOrigin):
    tag = Origin.SAGE
    proficiencies = {Skill.ARCANA, Skill.HISTORY}
    origin_feat = Feat.MAGIC_INITIATE_WIZARD


# EOF
