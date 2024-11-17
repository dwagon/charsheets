from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginGuard(BaseOrigin):
    tag = Origin.GUARD
    proficiencies = {Skill.ATHLETICS, Skill.PERCEPTION}

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.ALERT}


# EOF
