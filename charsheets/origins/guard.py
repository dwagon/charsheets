from charsheets.constants import Origin, Skill, Stat, Tools
from charsheets.feats import Alert
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Guard(BaseOrigin):
    tag = Origin.GUARD
    proficiencies = {Skill.ATHLETICS, Skill.PERCEPTION}
    origin_feat = Alert
    tool_proficiency = Tools.GAMING_SET
    origin_stats = (Stat.STRENGTH, Stat.INTELLIGENCE, Stat.WISDOM)


# EOF
