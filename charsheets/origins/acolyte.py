from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginAcolyte(BaseOrigin):
    tag = Origin.ACOLYTE
    proficiencies = {Skill.INSIGHT, Skill.RELIGION}

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.MAGIC_INITIATE_CLERIC}


# EOF
