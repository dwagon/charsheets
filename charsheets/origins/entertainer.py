from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginEntertainer(BaseOrigin):
    tag = Origin.ENTERTAINER
    proficiencies = {Skill.ACROBATICS, Skill.PERFORMANCE}

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.MUSICIAN}


# EOF
