from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginHermit(BaseOrigin):
    tag = Origin.HERMIT
    proficiencies = {Skill.MEDICINE, Skill.RELIGION}
    origin_feat = Feat.HEALER
    tool_proficiency = "Herbalism Kit"


# EOF
