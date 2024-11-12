from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin


#################################################################################
class OriginScribe(BaseOrigin):
    tag = Origin.SCRIBE

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.SKILLED}


# EOF
