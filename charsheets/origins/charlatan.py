from charsheets.constants import Origin, Skill, Tool, Stat
from charsheets.feats import Skilled
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Charlatan(BaseOrigin):
    tag = Origin.CHARLATAN
    proficiencies = {Skill.DECEPTION, Skill.SLEIGHT_OF_HAND}
    origin_feat = Skilled
    tool_proficiency = Tool.FORGERY_KIT
    origin_stats = (Stat.DEXTERITY, Stat.CONSTITUTION, Stat.CHARISMA)


# EOF
