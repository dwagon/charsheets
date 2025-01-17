from charsheets.constants import Origin, Skill, Tool, Stat
from charsheets.abilities import Tough
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Farmer(BaseOrigin):
    tag = Origin.FARMER
    proficiencies = {Skill.ANIMAL_HANDLING, Skill.NATURE}
    origin_feat = Tough
    tool_proficiency = Tool.CARPENTERS_TOOLS
    origin_stats = (Stat.STRENGTH, Stat.CONSTITUTION, Stat.WISDOM)


# EOF
