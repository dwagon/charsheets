from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin


#################################################################################
class OriginMerchant(BaseOrigin):
    tag = Origin.MERCHANT

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.LUCKY}


# EOF
