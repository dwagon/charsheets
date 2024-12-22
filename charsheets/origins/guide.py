from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill, Tools


#################################################################################
class Guide(BaseOrigin):
    tag = Origin.GUIDE
    proficiencies = {Skill.STEALTH, Skill.SURVIVAL}
    origin_feat = Feat.MAGIC_INITIATE_DRUID
    tool_proficiency = Tools.CARTOGRAPHERS_TOOLS


# EOF
