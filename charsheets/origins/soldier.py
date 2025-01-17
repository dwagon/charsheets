from charsheets.constants import Origin, Skill, Tool, Stat
from charsheets.abilities import SavageAttacker
from charsheets.origins.base_origin import BaseOrigin


#################################################################################
class Soldier(BaseOrigin):
    tag = Origin.SOLDIER
    proficiencies = {Skill.ATHLETICS, Skill.INTIMIDATION}
    origin_feat = SavageAttacker
    tool_proficiency = Tool.GAMING_SET
    origin_stats = (Stat.STRENGTH, Stat.DEXTERITY, Stat.CONSTITUTION)


# EOF
