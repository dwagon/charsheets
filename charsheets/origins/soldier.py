from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class Soldier(BaseOrigin):
    tag = Origin.SOLDIER
    proficiencies = {Skill.ATHLETICS, Skill.INTIMIDATION}
    origin_feat = Feat.SAVAGE_ATTACKER
    tool_proficiency = "Gaming Set"


# EOF
