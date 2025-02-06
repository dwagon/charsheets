from charsheets.constants import Origin, Skill, Tool, Stat
from charsheets.features import Healer
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Hermit(BaseOrigin):
    tag = Origin.HERMIT
    proficiencies = {Skill.MEDICINE, Skill.RELIGION}
    origin_feat = Healer
    tool_proficiency = Tool.HERBALISM_KIT
    origin_stats = (Stat.CONSTITUTION, Stat.WISDOM, Stat.CHARISMA)


# EOF
