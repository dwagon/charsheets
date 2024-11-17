from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginHermit(BaseOrigin):
    tag = Origin.HERMIT
    proficiencies = {Skill.MEDICINE, Skill.RELIGION}

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.HEALER}


# EOF
