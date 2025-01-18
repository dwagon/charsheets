from charsheets.constants import Origin, Skill, Tool, Stat
from charsheets.abilities import MagicInitiateDruid
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Guide(BaseOrigin):
    tag = Origin.GUIDE
    proficiencies = {Skill.STEALTH, Skill.SURVIVAL}
    tool_proficiency = Tool.CARTOGRAPHERS_TOOLS
    origin_stats = (Stat.DEXTERITY, Stat.CONSTITUTION, Stat.WISDOM)

    def __init__(self, stat1: Stat, stat2: Stat, stat3: Stat, initiate: MagicInitiateDruid):
        super().__init__(stat1, stat2, stat3)
        self.origin_feat = initiate


# EOF
