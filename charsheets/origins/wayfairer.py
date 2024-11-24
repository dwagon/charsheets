from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginWayfairer(BaseOrigin):
    tag = Origin.WAYFARER
    proficiencies = {Skill.INSIGHT, Skill.STEALTH}
    origin_feat = Feat.LUCKY


# EOF
