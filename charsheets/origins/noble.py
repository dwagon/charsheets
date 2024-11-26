from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginNoble(BaseOrigin):
    tag = Origin.NOBLE
    proficiencies = {Skill.HISTORY, Skill.PERSUASION}
    origin_feat = Feat.SKILLED
    tool_proficiency = "Gaming Set"


# EOF
