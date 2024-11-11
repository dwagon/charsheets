from charsheets.ability import BaseAbility
from charsheets.constants import Ability


#############################################################################
class AbilityFavoredEnemy(BaseAbility):
    tag = Ability.FAVOURED_ENEMY
    desc = """You always have the Hunter's Mark spell prepared. You can cast it twice without expending a spell slot
    and you regain all expended uses of this ability when you finish a Long Rest.
    """


#############################################################################
class AbilityDeftExplorer(BaseAbility):
    tag = Ability.DEFT_EXPLORER
    desc = """Thanks to your travels, you gain the following benefits.

    Expertise. Choose one of your skill proficiencies with which you lack Expertise. You gain Expertise in that skill.

    Languages. You know two languages of your choice"""


# EOF
