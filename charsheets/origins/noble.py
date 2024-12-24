from charsheets.constants import Origin, Skill, Tool
from charsheets.feats import Skilled
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Noble(BaseOrigin):
    tag = Origin.NOBLE
    proficiencies = {Skill.HISTORY, Skill.PERSUASION}
    origin_feat = Skilled
    tool_proficiency = Tool.GAMING_SET


# EOF
