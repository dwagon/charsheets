from charsheets.constants import Origin, Skill, Tools
from charsheets.feats import MagicInitiateWizard
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Sage(BaseOrigin):
    tag = Origin.SAGE
    proficiencies = {Skill.ARCANA, Skill.HISTORY}
    origin_feat = MagicInitiateWizard
    tool_proficiency = Tools.CALLIGRAPHERS_SUPPLIES


# EOF
