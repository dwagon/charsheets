from charsheets.ability import BaseAbility
from charsheets.constants import Ability


#############################################################################
class AbilityDruidic(BaseAbility):
    tag = Ability.DRUIDIC
    desc = """You know Druidic, the secret language of Druids."""


#############################################################################
class AbilityPrimalOrder(BaseAbility):
    tag = Ability.PRIMAL_KNOWLEDGE
    desc = """You have dedicated yourself to one of the following sacred roles: Magician, Warden."""


#############################################################################
class AbilityWildShape(BaseAbility):
    tag = Ability.WILD_SHAPE
    desc = """The power of nature allows you to assume the form of an animal.
    As a Bonus Action, you shape-shift into a Beast form that you have learned for this feature."""


#############################################################################
class AbilityWildCompanion(BaseAbility):
    tag = Ability.WILD_COMPANION
    desc = """You can summon a nature spirit that assumes an animal form to aid you. As a Magic action,
    you can expend a spell slot or a use of Wild Shape to cast the Find Familiar spell without Material components.
    When you cast the spell in this way, the familiar is Fey and disappears when you finish a long rest."""


# EOF
