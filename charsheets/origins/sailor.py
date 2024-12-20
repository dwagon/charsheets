from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class Sailor(BaseOrigin):
    tag = Origin.SAILOR
    proficiencies = {Skill.ACROBATICS, Skill.PERCEPTION}
    origin_feat = Feat.TAVERN_BRAWLER
    tool_proficiency = "Navigator's Tools"


# EOF
