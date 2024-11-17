from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginCriminal(BaseOrigin):
    tag = Origin.CRIMINAL
    proficiencies = {Skill.SLEIGHT_OF_HAND, Skill.STEALTH}

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.ALERT}


# EOF
