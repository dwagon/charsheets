from charsheets.constants import Origin, Skill, Tool
from charsheets.feats import SavageAttacker
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Soldier(BaseOrigin):
    tag = Origin.SOLDIER
    proficiencies = {Skill.ATHLETICS, Skill.INTIMIDATION}
    origin_feat = SavageAttacker
    tool_proficiency = Tool.GAMING_SET


# EOF
