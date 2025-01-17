from charsheets.constants import Origin, Skill, Tool, Stat
from charsheets.abilities import TavernBrawler
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Sailor(BaseOrigin):
    tag = Origin.SAILOR
    proficiencies = {Skill.ACROBATICS, Skill.PERCEPTION}
    origin_feat = TavernBrawler
    tool_proficiency = Tool.NAVIGATORS_TOOLS
    origin_stats = (Stat.STRENGTH, Stat.DEXTERITY, Stat.WISDOM)


# EOF
