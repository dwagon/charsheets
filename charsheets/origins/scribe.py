from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginScribe(BaseOrigin):
    tag = Origin.SCRIBE
    proficiencies = {Skill.INVESTIGATION, Skill.PERCEPTION}
    origin_feat = Feat.SKILLED


# EOF
