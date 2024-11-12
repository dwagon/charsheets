from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin


#################################################################################
class OriginArtisan(BaseOrigin):
    tag = Origin.ARTISAN

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.CRAFTER}


# EOF
