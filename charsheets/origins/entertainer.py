from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill, Tools


#################################################################################
class Entertainer(BaseOrigin):
    tag = Origin.ENTERTAINER
    proficiencies = {Skill.ACROBATICS, Skill.PERFORMANCE}
    origin_feat = Feat.MUSICIAN
    tool_proficiency = Tools.MUSICAL_INSTRUMENT


# EOF
