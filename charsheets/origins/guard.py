from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill, Stat, Tools


#################################################################################
class Guard(BaseOrigin):
    tag = Origin.GUARD
    proficiencies = {Skill.ATHLETICS, Skill.PERCEPTION}
    origin_feat = Feat.ALERT
    tool_proficiency = Tools.GAMING_SET
    origin_stats = (Stat.STRENGTH, Stat.INTELLIGENCE, Stat.WISDOM)


# EOF
