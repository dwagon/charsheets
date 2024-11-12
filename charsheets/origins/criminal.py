from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin


#################################################################################
class OriginCriminal(BaseOrigin):
    tag = Origin.CRIMINAL

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.ALERT}


# EOF
