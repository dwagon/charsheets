from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginFarmer(BaseOrigin):
    tag = Origin.FARMER
    proficiencies = {Skill.ANIMAL_HANDLING, Skill.NATURE}
    origin_feat = Feat.TOUGH
    tool_proficiency = "Carpenter's Tools"


# EOF
