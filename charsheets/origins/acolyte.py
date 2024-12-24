from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Origin, Skill, Tools
from charsheets.feats import MagicInitiateCleric


#################################################################################
class Acolyte(BaseOrigin):
    tag = Origin.ACOLYTE
    proficiencies = {Skill.INSIGHT, Skill.RELIGION}
    origin_feat = MagicInitiateCleric
    tool_proficiency = Tools.CALLIGRAPHERS_SUPPLIES


# EOF
