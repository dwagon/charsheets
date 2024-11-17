from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginMerchant(BaseOrigin):
    tag = Origin.MERCHANT
    proficiencies = {Skill.ANIMAL_HANDLING, Skill.PERSUASION}

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.LUCKY}


# EOF
