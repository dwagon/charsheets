from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill, Tool, Stat
from charsheets.feats import Healer


#################################################################################
class Hermit(BaseOrigin):
    tag = Origin.HERMIT
    proficiencies = {Skill.MEDICINE, Skill.RELIGION}
    origin_feat = Healer
    tool_proficiency = Tool.HERBALISM_KIT
    origin_stats = (Stat.CONSTITUTION, Stat.WISDOM, Stat.CHARISMA)


# EOF
