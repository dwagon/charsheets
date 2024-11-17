from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginNoble(BaseOrigin):
    tag = Origin.NOBLE
    proficiencies = {Skill.HISTORY, Skill.PERSUASION}

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.SKILLED}


# EOF
