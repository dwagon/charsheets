from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginSage(BaseOrigin):
    tag = Origin.SAGE
    proficiencies = {Skill.ARCANA, Skill.HISTORY}

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.MAGIC_INITIATE_WIZARD}


# EOF
