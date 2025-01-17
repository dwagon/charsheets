from charsheets.constants import Origin, Skill, Tool, Stat
from charsheets.abilities import Crafter
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Artisan(BaseOrigin):
    tag = Origin.ARTISAN
    proficiencies = {Skill.INVESTIGATION, Skill.PERSUASION}
    origin_feat = Crafter
    tool_proficiency = Tool.ARTISAN_TOOLS
    origin_stats = (Stat.STRENGTH, Stat.DEXTERITY, Stat.INTELLIGENCE)


# EOF
