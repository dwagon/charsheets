from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class Guide(BaseOrigin):
    tag = Origin.GUIDE
    proficiencies = {Skill.STEALTH, Skill.SURVIVAL}
    origin_feat = Feat.MAGIC_INITIATE_DRUID
    tool_proficiency = "Cartographer's Tools"


# EOF
