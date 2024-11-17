from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginGuide(BaseOrigin):
    tag = Origin.GUIDE
    proficiencies = {Skill.STEALTH, Skill.SURVIVAL}

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.MAGIC_INITIATE_DRUID}


# EOF
