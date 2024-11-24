from charsheets.origin import BaseOrigin
from charsheets.constants import Feat, Origin, Skill


#################################################################################
class OriginArtisan(BaseOrigin):
    tag = Origin.ARTISAN
    proficiencies = {Skill.INVESTIGATION, Skill.PERSUASION}
    origin_feat = Feat.CRAFTER


# EOF
