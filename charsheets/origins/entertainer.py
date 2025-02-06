from charsheets.constants import Origin, Skill, Tool, Stat
from charsheets.features import Musician
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Entertainer(BaseOrigin):
    tag = Origin.ENTERTAINER
    proficiencies = {Skill.ACROBATICS, Skill.PERFORMANCE}
    origin_feat = Musician
    tool_proficiency = Tool.MUSICAL_INSTRUMENT
    origin_stats = (Stat.STRENGTH, Stat.DEXTERITY, Stat.CHARISMA)


# EOF
