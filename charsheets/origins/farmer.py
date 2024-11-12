from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin


#################################################################################
class OriginFarmer(BaseOrigin):
    tag = Origin.FARMER

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.TOUGH}


# EOF
