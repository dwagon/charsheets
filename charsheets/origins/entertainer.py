from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginEntertainer(BaseOrigin):
    tag = Origin.ENTERTAINER
    proficiencies = {Skill.ACROBATICS, Skill.PERFORMANCE}
    origin_feat = Feat.MUSICIAN
    tool_proficiency = "Musical Instrument"


# EOF
