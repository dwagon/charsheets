from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin


#################################################################################
class OriginNoble(BaseOrigin):
    tag = Origin.NOBLE

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.SKILLED}


# EOF
