from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginArtisan(BaseOrigin):
    tag = Origin.ARTISAN
    proficiencies = {Skill.INVESTIGATION, Skill.PERSUASION}

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.CRAFTER}


# EOF
