from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin


#################################################################################
class OriginAcolyte(BaseOrigin):
    tag = Origin.ACOLYTE

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.MAGIC_INITIATE_CLERIC}


# EOF
