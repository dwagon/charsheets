from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill, Tools


#################################################################################
class Merchant(BaseOrigin):
    tag = Origin.MERCHANT
    proficiencies = {Skill.ANIMAL_HANDLING, Skill.PERSUASION}
    origin_feat = Feat.LUCKY
    tool_proficiency = Tools.NAVIGATORS_TOOLS


# EOF
