from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill, Tools


#################################################################################
class Charlatan(BaseOrigin):
    tag = Origin.CHARLATAN
    proficiencies = {Skill.DECEPTION, Skill.SLEIGHT_OF_HAND}
    origin_feat = Feat.SKILLED
    tool_proficiency = Tools.FORGERY_KIT


# EOF
