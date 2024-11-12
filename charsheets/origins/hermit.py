from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin


#################################################################################
class OriginHermit(BaseOrigin):
    tag = Origin.HERMIT

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.HEALER}


# EOF
