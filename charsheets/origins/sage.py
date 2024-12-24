from charsheets.constants import Origin, Skill, Tool
from charsheets.feats import MagicInitiateWizard
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Sage(BaseOrigin):
    tag = Origin.SAGE
    proficiencies = {Skill.ARCANA, Skill.HISTORY}
    origin_feat = MagicInitiateWizard
    tool_proficiency = Tool.CALLIGRAPHERS_SUPPLIES


# EOF
