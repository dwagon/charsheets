from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill, Stat, Tools


###############################################################################
class DummyOrigin(BaseOrigin):
    __test__ = False
    tag = Origin.NONE
    proficiencies = {Skill.ATHLETICS, Skill.PERCEPTION}
    origin_feat = Feat.ALERT
    tool_proficiency = Tools.NONE
    origin_stats = (Stat.STRENGTH, Stat.INTELLIGENCE, Stat.WISDOM)


# EOF
