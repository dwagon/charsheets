from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin


#################################################################################
class OriginSage(BaseOrigin):
    tag = Origin.SAGE

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.MAGIC_INITIATE_WIZARD}


# EOF
