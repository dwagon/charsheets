from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginGuide(BaseOrigin):
    tag = Origin.GUIDE
    proficiencies = {Skill.STEALTH, Skill.SURVIVAL}
    origin_feat = Feat.MAGIC_INITIATE_DRUID


# EOF
