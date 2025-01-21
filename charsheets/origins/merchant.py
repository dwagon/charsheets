from charsheets.constants import Origin, Skill, Tool, Stat
from charsheets.features import Lucky
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Merchant(BaseOrigin):
    tag = Origin.MERCHANT
    proficiencies = {Skill.ANIMAL_HANDLING, Skill.PERSUASION}
    origin_feat = Lucky
    tool_proficiency = Tool.NAVIGATORS_TOOLS
    origin_stats = (Stat.CONSTITUTION, Stat.INTELLIGENCE, Stat.CHARISMA)


# EOF
