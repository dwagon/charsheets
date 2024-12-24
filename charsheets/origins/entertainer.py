from charsheets.origins.base_origin import BaseOrigin
from charsheets.constants import Origin, Skill, Tools
from charsheets.feats import Musician


#################################################################################
class Entertainer(BaseOrigin):
    tag = Origin.ENTERTAINER
    proficiencies = {Skill.ACROBATICS, Skill.PERFORMANCE}
    origin_feat = Musician
    tool_proficiency = Tools.MUSICAL_INSTRUMENT


# EOF
