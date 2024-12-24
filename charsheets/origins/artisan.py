from charsheets.constants import Origin, Skill, Tool
from charsheets.feats import Crafter
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Artisan(BaseOrigin):
    tag = Origin.ARTISAN
    proficiencies = {Skill.INVESTIGATION, Skill.PERSUASION}
    origin_feat = Crafter
    tool_proficiency = Tool.ARTISAN_TOOLS


# EOF
