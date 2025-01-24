from enum import StrEnum, auto
from typing import TYPE_CHECKING

from charsheets.reason import Reason
from charsheets.spell import Spell
from charsheets.util import safe

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class EldritchInvocationNames(StrEnum):
    AGONIZING_BLAST = auto()
    ARMOR_OF_SHADOWS = auto()
    ASCENDANT_STEP = auto()
    DEVILS_SIGHT = auto()
    ELDRITCH_MIND = auto()
    ELDRITCH_SMITE = auto()
    ELDRITCH_SPEAR = auto()
    FIENDISH_VIGOR = auto()
    GAZE_OF_TWO_MINDS = auto()
    GIFT_OF_THE_DEPTHS = auto()
    INVESTMENT_OF_THE_CHAIN_MASTER = auto()
    LESSONS_OF_THE_FIRST_ONES = auto()
    MASK_OF_MANY_FACES = auto()
    MASTER_OF_MYRIAD_FORMS = auto()
    MISTY_VISIONS = auto()
    NONE = auto()
    ONE_WITH_SHADOWS = auto()
    OTHERWORLDLY_LEAP = auto()
    PACT_OF_THE_BLADE = auto()
    PACT_OF_THE_CHAIN = auto()
    PACT_OF_THE_TOME = auto()
    REPELLING_BLAST = auto()
    THIRSTING_BLADE = auto()


#############################################################################
class BaseInvocation:
    _desc = "Unspecified"
    tag: EldritchInvocationNames = EldritchInvocationNames.NONE

    @property
    def desc(self):
        return self._desc


#############################################################################
class AgonizingBlast(BaseInvocation):
    tag = EldritchInvocationNames.AGONIZING_BLAST

    def __init__(self, spell: Spell):
        self._spell = spell

    @property
    def desc(self) -> str:
        return f"""You can add your Charisma modifier to {safe(self._spell.name).title()} damage rolls."""


#############################################################################
class ArmorOfShadows(BaseInvocation):
    tag = EldritchInvocationNames.ARMOR_OF_SHADOWS
    _desc = """You can cast Mage Armor on yourself without expending a spell slot."""

    def mod_add_prepared_spell(self, character: "Character") -> Reason[Spell]:
        return Reason("Armour of Shadows", Spell.MAGE_ARMOR)


#############################################################################
class AscendantsStep(BaseInvocation):
    tag = EldritchInvocationNames.ASCENDANT_STEP
    _desc = """You can cast Levitate on yourself without expending a spell slot."""

    def mod_add_prepared_spell(self, character: "Character") -> Reason[Spell]:
        return Reason("Ascendant Leap", Spell.LEVITATE)


#############################################################################
class DevilsSight(BaseInvocation):
    tag = EldritchInvocationNames.DEVILS_SIGHT
    _desc = """You can see normally in Dim Light and Darkness - both magical and non-magical
     - within 120 feet of yourself"""


#############################################################################
class EldritchMind(BaseInvocation):
    tag = EldritchInvocationNames.ELDRITCH_MIND
    _desc = """You have Advantage on Constitution saving throws that you make to maintain Concentration"""


#############################################################################
class EldritchSmite(BaseInvocation):
    tag = EldritchInvocationNames.ELDRITCH_SMITE
    _desc = """Once per turn whn you hit a creature with your pact weapon, you can expend a Pact Magic spell slot
    to deal an extra 1d8 Force damage to the target, plus another 1d8 per level of the spell slot, and you can
    give the target the Prone condition if it is Huge or smaller."""


#############################################################################
class EldritchSpear(BaseInvocation):
    tag = EldritchInvocationNames.ELDRITCH_SPEAR

    def __init__(self, spell: Spell):
        self._spell = spell

    @property
    def desc(self) -> str:
        return f"""The range of {safe(self._spell.name).title()} increases by a number of feet equal to 30 times your
        Warlock level."""


#############################################################################
class FiendishVigour(BaseInvocation):
    tag = EldritchInvocationNames.FIENDISH_VIGOR
    _desc = """You can cast False Life on yourself without expending a spell slot. When you cast the spell with
    this feature, you don't roll the die for the Temporary Hit Points; you automatically get the highest number on
    the die."""

    def mod_add_prepared_spells(self, character: "Character"):
        return {Spell.FALSE_LIFE}


#############################################################################
class GazeOfTwoMinds(BaseInvocation):
    tag = EldritchInvocationNames.GAZE_OF_TWO_MINDS
    _desc = """You can use a Bonus Action to touch a willing creature and perceve through its senses until the
    end of your next turn. As long as the creature is on the same plane of existence as you, you can take a Bonus
    Action of subsequent turns to maintain this connection, extending the duration until the end of your next turn. 
    The connection ends if you dont maintain it in this way.

    While perceiving through the other creature's senses, you benefit from any special sense posses by that creature,
    amd you can cast spells as if you were in your space or the other creature's space if the two of you are within
    60 feet of each other."""


#############################################################################
class GiftOfTheDepths(BaseInvocation):
    tag = EldritchInvocationNames.GIFT_OF_THE_DEPTHS
    _desc = """You can breathe underwater, and you gain a Swim Speed equal to your Speed.

    You can also cast Water Breathing once without expending a spell slot. You regain the ability to cast it in this
    way again when you finish a Long Rest."""

    def mod_swim_movement(self, character: "Character") -> int:
        return 30


#############################################################################
class InvestmentOfTheChainMaster(BaseInvocation):
    tag = EldritchInvocationNames.INVESTMENT_OF_THE_CHAIN_MASTER
    _desc = """When you cast Find Familiar, you infuse the summoned familiar with a measure of your eldritch power, 
    granting the creature the following benefits:
    
    Aerial or Aquatic. The familiar gains either a Fly Speed or a Swim Speed (your choice) of 40 feet.
    
    Quick Attack. As a Bonus Action, you can command the familiar to take the Attack action.
    
    Necrotic or Radiant Damage. Whenever the familiar deals Bludgeoning, Piercing or Slashing damage, you can make it 
    deal Necrotic or Radiant damage instead.
    
    Your Save DC. If the familiar forces a creature to make a saving throw, it uses your spell save DC.
    
    Resistance. When the familiar takes damage, you can take a Reaction to grait it Resistance against that damage."""


#############################################################################
class LessonsOfTheFirstOnes(BaseInvocation):
    tag = EldritchInvocationNames.LESSONS_OF_THE_FIRST_ONES
    _desc = """You have received knowledge from an elder entity of the multiverse, allowing you to gain one
     Origin feat of your choice"""


#############################################################################
class MaskOfManyFaces(BaseInvocation):
    tag = EldritchInvocationNames.MASK_OF_MANY_FACES
    _desc = """You can cast Disguise Self without expending a spell slot."""

    def mod_add_prepared_spells(self, character: "Character"):
        return {Spell.DISGUISE_SELF}


#############################################################################
class MasterOfMyriadForms(BaseInvocation):
    tag = EldritchInvocationNames.MASTER_OF_MYRIAD_FORMS
    _desc = """You can cast Alter Sekf without expending a spell slot."""

    def mod_add_prepared_spells(self, character: "Character"):
        return {Spell.ALTER_SELF}


#############################################################################
class MistyVisions(BaseInvocation):
    tag = EldritchInvocationNames.MISTY_VISIONS
    _desc = """You can cast Silent Image without expending a spell slot."""

    def mod_add_prepared_spells(self, character: "Character"):
        return {Spell.SILENT_IMAGE}


#############################################################################
class OneWithShadows(BaseInvocation):
    tag = EldritchInvocationNames.ONE_WITH_SHADOWS
    _desc = """While you're in an area of Dim Light or Darkness, you can cast Invisibility on yourself without 
            expending a spell slot."""

    def mod_add_prepared_spells(self, character: "Character"):
        return {Spell.INVISIBILITY}


#############################################################################
class OtherworldlyLeap(BaseInvocation):
    tag = EldritchInvocationNames.OTHERWORLDLY_LEAP
    _desc = """You can cast Jump on yourself without expending a spell slot."""

    def mod_add_prepared_spells(self, character: "Character"):
        return {Spell.JUMP}


#############################################################################
class PactOfTheBlade(BaseInvocation):
    tag = EldritchInvocationNames.PACT_OF_THE_BLADE
    _desc = """As a Bonus Action, you cn conjure a pact weapon in your hand - a Simple or Martial Melee weapon of
    your choice with which you bond - or create a bond with a magic weapon you touch; you can't bond with a magic
    weapon if someone else is attuned to it or another Warlock is bonded with it. Until the bond ends, you have
    proficiency with the weapon and you can use it as a Spellcasting Focus.

    Whenever you attack with the bonded weapon, you can use your Charisma modifier for the attack and damage rolls
    instead of using Strength or Dexterity; and you can cause the weapon to deal Necrotic, Psychic, or Radiant
    damage or its normal damage type.
    """


#############################################################################
class PactOfTheChain(BaseInvocation):
    tag = EldritchInvocationNames.PACT_OF_THE_CHAIN
    _desc = """You learn the Find Familiar spell and can cast it as a Magic action without expending a spell slot.

    When you cast the spell, you choose one of the normal forms for you familiar or one of the following special
    forms: Imp, Pseudodragon, Quasit, Skeleton, Slaad Tadpole, Sphinx of Wonder, Sprite, or Venomous Snake.

    Additionally, when you take the Attack action, you can forgo one of your own attacks to allow your familiar to
    make one attack of its own with its Reaction."""

    def mod_add_prepared_spells(self, character: "Character"):
        return {Spell.FIND_FAMILIAR}


#############################################################################
class PactOfTheTome(BaseInvocation):
    tag = EldritchInvocationNames.PACT_OF_THE_TOME
    _desc = """Stitching together strands of shadow, you conjure forth a book in your hand at the end of a Short
    or Long Rest. This Book of Shadows contains eldritch magic that only you can access, granting you the benefits
    below.

    Cantrips and Rituals. While the
    book is on your person, you have the spells prepared, and they function as Warlock spells for you.

    Spellcasting Focus. You can use the book as a Spellcasting Focus."""

    def __init__(self, cantrip1: Spell, cantrip2: Spell, cantrip3: Spell, spell1: Spell, spell2: Spell):
        self._tome_spells = {cantrip1, cantrip2, cantrip3, spell1, spell2}

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        prepared = Reason[Spell]()
        for spell in self._tome_spells:
            prepared |= Reason("Pact of the Tome", spell)
        return prepared

    @property
    def desc(self) -> str:
        spells = [safe(_.name).title() for _ in self._tome_spells]
        return f"""You can cast {', '.join(spells)} as Warlock spells"""


#############################################################################
class RepellingBlast(BaseInvocation):
    tag = EldritchInvocationNames.REPELLING_BLAST
    _desc = """"""

    def __init__(self, spell: Spell):
        self._spell = spell

    @property
    def desc(self) -> str:
        return f"""When you hit a Large or smaller creature wth {safe(self._spell.name).title()}, you can push the
            creature up to 10 feet straight away from you."""


#############################################################################
class ThirstingBlade(BaseInvocation):
    tag = EldritchInvocationNames.THIRSTING_BLADE
    _desc = """Yout gain the Extra Attack feature for your pact weapon only. With that feature, you can attack twice 
            with the weapon instead of once when you take the Attack action on your turn."""


# EOF
