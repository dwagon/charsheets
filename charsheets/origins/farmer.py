from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class Farmer(BaseOrigin):
    tag = Origin.FARMER
    proficiencies = {Skill.ANIMAL_HANDLING, Skill.NATURE}
    origin_feat = Feat.TOUGH
    tool_proficiency = "Carpenter's Tools"


# EOF
