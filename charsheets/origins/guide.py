from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin


#################################################################################
class OriginGuide(BaseOrigin):
    tag = Origin.GUIDE

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.MAGIC_INITIATE_DRUID}


# EOF
