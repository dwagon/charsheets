from charsheets.constants import Origin, Skill, Tool
from charsheets.feats import Skilled
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Scribe(BaseOrigin):
    tag = Origin.SCRIBE
    proficiencies = {Skill.INVESTIGATION, Skill.PERCEPTION}
    origin_feat = Skilled
    tool_proficiency = Tool.CALLIGRAPHERS_SUPPLIES


# EOF
