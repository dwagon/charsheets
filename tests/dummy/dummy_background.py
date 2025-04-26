from charsheets.backgrounds2014.base_background import BaseBackground
from charsheets.constants import Skill, Tool, Background


###############################################################################
class DummyBackground(BaseBackground):
    __test__ = False
    tag = Background.NONE
    proficiencies = {Skill.DECEPTION, Skill.STEALTH}
    tool_proficiencies = {Tool.GAMING_SET}


# EOF
