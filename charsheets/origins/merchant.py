from charsheets.constants import Origin, Skill, Tool
from charsheets.feats import Lucky
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Merchant(BaseOrigin):
    tag = Origin.MERCHANT
    proficiencies = {Skill.ANIMAL_HANDLING, Skill.PERSUASION}
    origin_feat = Lucky
    tool_proficiency = Tool.NAVIGATORS_TOOLS


# EOF
