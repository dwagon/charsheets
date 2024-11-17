from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginWayfairer(BaseOrigin):
    tag = Origin.WAYFARER
    proficiencies = {Skill.INSIGHT, Skill.STEALTH}

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.LUCKY}


# EOF
