from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin


#################################################################################
class OriginGuard(BaseOrigin):
    tag = Origin.GUARD

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.ALERT}


# EOF
