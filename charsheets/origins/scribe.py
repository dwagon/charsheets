from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill, Tools


#################################################################################
class Scribe(BaseOrigin):
    tag = Origin.SCRIBE
    proficiencies = {Skill.INVESTIGATION, Skill.PERCEPTION}
    origin_feat = Feat.SKILLED
    tool_proficiency = Tools.CALLIGRAPHERS_SUPPLIES


# EOF
