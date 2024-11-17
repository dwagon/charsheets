from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginCharlatan(BaseOrigin):
    tag = Origin.CHARLATAN
    proficiencies = {Skill.DECEPTION, Skill.SLEIGHT_OF_HAND}

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.SKILLED}


# EOF
