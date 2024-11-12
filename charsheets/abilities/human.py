from charsheets.ability import BaseAbility
from charsheets.constants import Ability


#############################################################################
class AbilityResourceful(BaseAbility):
    tag = Ability.RESOURCEFUL
    desc = """You gain Heroic Inspiration whenever you finish a Long Rest."""


#############################################################################
class AbilitySkillful(BaseAbility):
    tag = Ability.SKILLFUL
    desc = """You gain proficiency in one skill of your choice."""


# EOF
