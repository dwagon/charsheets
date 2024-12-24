from charsheets.constants import Origin, Skill, Tools
from charsheets.feats import TavernBrawler
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Sailor(BaseOrigin):
    tag = Origin.SAILOR
    proficiencies = {Skill.ACROBATICS, Skill.PERCEPTION}
    origin_feat = TavernBrawler
    tool_proficiency = Tools.NAVIGATORS_TOOLS


# EOF
