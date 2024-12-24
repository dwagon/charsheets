from charsheets.constants import Origin, Skill, Tools
from charsheets.feats import SavageAttacker
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Soldier(BaseOrigin):
    tag = Origin.SOLDIER
    proficiencies = {Skill.ATHLETICS, Skill.INTIMIDATION}
    origin_feat = SavageAttacker
    tool_proficiency = Tools.GAMING_SET


# EOF
