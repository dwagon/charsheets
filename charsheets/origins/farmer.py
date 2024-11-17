from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginFarmer(BaseOrigin):
    tag = Origin.FARMER
    proficiencies = {Skill.ANIMAL_HANDLING, Skill.NATURE}

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.TOUGH}


# EOF
