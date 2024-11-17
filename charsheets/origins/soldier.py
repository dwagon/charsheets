from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginSoldier(BaseOrigin):
    tag = Origin.SOLDIER
    proficiencies = {Skill.ATHLETICS, Skill.INTIMIDATION}

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.SAVAGE_ATTACKER}


# EOF
