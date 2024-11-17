from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginSailor(BaseOrigin):
    tag = Origin.SAILOR
    proficiencies = {Skill.ACROBATICS, Skill.PERCEPTION}

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.TAVERN_BRAWLER}


# EOF
