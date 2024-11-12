from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin


#################################################################################
class OriginEntertainer(BaseOrigin):
    tag = Origin.ENTERTAINER

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.MUSICIAN}


# EOF
