from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginMerchant(BaseOrigin):
    tag = Origin.MERCHANT
    proficiencies = {Skill.ANIMAL_HANDLING, Skill.PERSUASION}
    origin_feat = Feat.LUCKY
    tool_proficiency = "Navigator's Tools"


# EOF
