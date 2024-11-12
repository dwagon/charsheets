from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin


#################################################################################
class OriginSoldier(BaseOrigin):
    tag = Origin.SOLDIER

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.SAVAGE_ATTACKER}


# EOF
