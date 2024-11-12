from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin


#################################################################################
class OriginSailor(BaseOrigin):
    tag = Origin.SAILOR

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.TAVERN_BRAWLER}


# EOF
