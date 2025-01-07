from charsheets.constants import Origin, Skill, Tool, Stat
from charsheets.feats import MagicInitiateDruid
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Guide(BaseOrigin):
    tag = Origin.GUIDE
    proficiencies = {Skill.STEALTH, Skill.SURVIVAL}
    origin_feat = MagicInitiateDruid
    tool_proficiency = Tool.CARTOGRAPHERS_TOOLS
    origin_stats = (Stat.DEXTERITY, Stat.CONSTITUTION, Stat.WISDOM)


# EOF
