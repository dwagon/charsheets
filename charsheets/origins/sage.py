from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill, Tools


#################################################################################
class Sage(BaseOrigin):
    tag = Origin.SAGE
    proficiencies = {Skill.ARCANA, Skill.HISTORY}
    origin_feat = Feat.MAGIC_INITIATE_WIZARD
    tool_proficiency = Tools.CALLIGRAPHERS_SUPPLIES


# EOF
