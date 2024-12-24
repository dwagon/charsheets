from charsheets.constants import Origin, Skill, Tools
from charsheets.feats import MagicInitiateDruid
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Guide(BaseOrigin):
    tag = Origin.GUIDE
    proficiencies = {Skill.STEALTH, Skill.SURVIVAL}
    origin_feat = MagicInitiateDruid
    tool_proficiency = Tools.CARTOGRAPHERS_TOOLS


# EOF
