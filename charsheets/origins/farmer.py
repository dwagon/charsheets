from charsheets.constants import Origin, Skill, Tools
from charsheets.feats import Tough
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Farmer(BaseOrigin):
    tag = Origin.FARMER
    proficiencies = {Skill.ANIMAL_HANDLING, Skill.NATURE}
    origin_feat = Tough
    tool_proficiency = Tools.CARPENTERS_TOOLS


# EOF
