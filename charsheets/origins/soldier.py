from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill, Tools


#################################################################################
class Soldier(BaseOrigin):
    tag = Origin.SOLDIER
    proficiencies = {Skill.ATHLETICS, Skill.INTIMIDATION}
    origin_feat = Feat.SAVAGE_ATTACKER
    tool_proficiency = Tools.GAMING_SET


# EOF
