from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin


#################################################################################
class OriginWayfairer(BaseOrigin):
    tag = Origin.WAYFARER

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.LUCKY}


# EOF
