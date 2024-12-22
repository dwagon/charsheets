from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill, Tools


#################################################################################
class Wayfairer(BaseOrigin):
    tag = Origin.WAYFARER
    proficiencies = {Skill.INSIGHT, Skill.STEALTH}
    origin_feat = Feat.LUCKY
    tool_proficiency = Tools.THIEVES_TOOLS


# EOF
