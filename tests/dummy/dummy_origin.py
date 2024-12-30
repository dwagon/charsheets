from charsheets.constants import Origin, Skill, Stat, Tool
from charsheets.origins.base_origin import BaseOrigin
from charsheets.reason import Reason
from tests.dummy.dummy_feat import DummyFeat


###############################################################################
class DummyOrigin(BaseOrigin):
    __test__ = False
    tag = Origin.NONE
    proficiencies = {Skill.ATHLETICS, Skill.PERCEPTION}
    origin_feat = DummyFeat
    tool_proficiency = Tool.NONE
    origin_stats = (Stat.STRENGTH, Stat.INTELLIGENCE, Stat.WISDOM)


# EOF
