from enum import StrEnum, auto
from typing import TYPE_CHECKING

from charsheets.constants import Recovery
from charsheets.reason import Reason
from charsheets.spell import Spell, spell_name

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class EldritchInvocationNames(StrEnum):
    AGONIZING_BLAST = auto()
    ARMOR_OF_SHADOWS = auto()
    ASCENDANT_STEP = auto()
    DEVILS_SIGHT = auto()
    DEVOURING_BLADE = auto()
    ELDRITCH_MIND = auto()
    ELDRITCH_SMITE = auto()
    ELDRITCH_SPEAR = auto()
    FIENDISH_VIGOR = auto()
    GAZE_OF_TWO_MINDS = auto()
    GIFT_OF_THE_DEPTHS = auto()
    GIFT_OF_THE_PROTECTORS = auto()
    INVESTMENT_OF_THE_CHAIN_MASTER = auto()
    LESSONS_OF_THE_FIRST_ONES = auto()
    LIFEDRINKER = auto()
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
    VISIONS_OF_DISTANT_REALMS = auto()
    WHISPERS_OF_THE_GRAVE = auto()
    WITCH_SIGHT = auto()


#############################################################################
class BaseInvocation:
    _desc = "Unspecified"
    tag: EldritchInvocationNames = EldritchInvocationNames.NONE
    owner: "Character"
    recovery: Recovery = Recovery.NONE

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
        return f"""You can add {self.owner.charisma.modifier} to '{spell_name(self._spell)}' damage rolls."""


#############################################################################
class ArmorOfShadows(BaseInvocation):
    tag = EldritchInvocationNames.ARMOR_OF_SHADOWS

    @property
    def desc(self) -> str:
        ac = 13 + self.owner.dexterity.modifier
        return f"""You can cast 'Mage Armor' (AC {ac}) on yourself without expending a spell slot."""

    def mod_add_prepared_spell(self, character: "Character") -> Reason[Spell]:
        return Reason("Armour of Shadows", Spell.MAGE_ARMOR)


#############################################################################
class AscendantsStep(BaseInvocation):
    tag = EldritchInvocationNames.ASCENDANT_STEP
    _desc = """You can cast 'Levitate' on yourself without expending a spell slot."""

    def mod_add_prepared_spell(self, character: "Character") -> Reason[Spell]:
        return Reason("Ascendant Leap", Spell.LEVITATE)


#############################################################################
class DevilsSight(BaseInvocation):
    tag = EldritchInvocationNames.DEVILS_SIGHT
    _desc = """You can see normally in Dim Light and Darkness - both magical and non-magical
     - within 120 feet of yourself"""


#############################################################################
class DevouringBlade(BaseInvocation):
    tag = EldritchInvocationNames.DEVOURING_BLADE
    _desc = """The Extra Attack of your Thirsting Blade invocation confers two extra attacks rather than one."""


#############################################################################
class EldritchMind(BaseInvocation):
    tag = EldritchInvocationNames.ELDRITCH_MIND
    _desc = """You have Advantage on Constitution saving throws that you make to maintain Concentration"""


#############################################################################
class EldritchSmite(BaseInvocation):
    tag = EldritchInvocationNames.ELDRITCH_SMITE

    @property
    def desc(self):
        dmg = self.owner.max_spell_slot() + 1
        return f"""Once per turn when you hit a creature with your pact weapon, you can expend a Pact Magic spell slot
    to deal an extra {dmg}d8 Force damage to the target, and you can
    give the target the Prone condition if it is Huge or smaller."""


#############################################################################
class EldritchSpear(BaseInvocation):
    tag = EldritchInvocationNames.ELDRITCH_SPEAR

    def __init__(self, spell: Spell):
        self._spell = spell

    @property
    def desc(self) -> str:
        return f"""The range of '{spell_name(self._spell)}' increases by {30 * self.owner.level} feet."""


#############################################################################
class FiendishVigour(BaseInvocation):
    tag = EldritchInvocationNames.FIENDISH_VIGOR

    @property
    def desc(self):
        hp = 12 + 5 * (self.owner.max_spell_level() - 1)  # 2d4+4
        return f"""You can cast 'False Life' on yourself without expending a spell slot to gain {hp} Temporary Hit Points."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Fiendish Vigour", Spell.FALSE_LIFE)


#############################################################################
class GazeOfTwoMinds(BaseInvocation):
    tag = EldritchInvocationNames.GAZE_OF_TWO_MINDS
    _desc = """You can use a Bonus Action to touch a willing creature and perceive through its senses until the
    end of your next turn. As long as the creature is on the same plane of existence as you, you can take a Bonus
    Action of subsequent turns to maintain this connection, extending the duration until the end of your next turn. 
    The connection ends if you dont maintain it in this way.

    While perceiving through the other creature's senses, you benefit from any special sense possessed by that creature,
    and you can cast spells as if you were in your space or the other creature's space if the two of you are within
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
class GiftOfTheProtectors(BaseInvocation):
    tag = EldritchInvocationNames.GIFT_OF_THE_PROTECTORS
    goes = 1
    recovery = Recovery.LONG_REST
    _desc = """A new page appears in your Book of Shadows when you conjure it. With your permission, a creature can
    take an action to write its name on that page, which can contain {max(1, self.owner.charisma.modifier)} names.
    
    When any creature whose name is on the page is reduce to 0 Hit Points but not killed outright, the creature
    magically drops to 1 Hit Point instead. Once this magic is triggered, no creature can benefit from it until you
    finish a Long Rest.
    
    As a Magic action, you can erase a name on the page by touching it."""


#############################################################################
class InvestmentOfTheChainMaster(BaseInvocation):
    tag = EldritchInvocationNames.INVESTMENT_OF_THE_CHAIN_MASTER
    _desc = """When you cast 'Find Familiar', you infuse the summoned familiar with a measure of your eldritch power, 
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
class Lifedrinker(BaseInvocation):
    tag = EldritchInvocationNames.LIFEDRINKER
    _desc = """Once per turn when you hit a creature with your pact weapon, you can deal an extra 1d6 Necrotic,
    Psychic, or Radiant damage (your choice) to the creature, and you can expend one of your Hit Point dice to roll it
     and regain a number of Hit Points equal to the roll plus your Constitution modifier (minimum of 1 Hit Point)."""


#############################################################################
class MaskOfManyFaces(BaseInvocation):
    tag = EldritchInvocationNames.MASK_OF_MANY_FACES
    _desc = """You can cast 'Disguise Self' without expending a spell slot."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Mask of Many Faces", Spell.DISGUISE_SELF)


#############################################################################
class MasterOfMyriadForms(BaseInvocation):
    tag = EldritchInvocationNames.MASTER_OF_MYRIAD_FORMS
    _desc = """You can cast 'Alter Self' without expending a spell slot."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Master of Myriad Forms", Spell.ALTER_SELF)


#############################################################################
class MistyVisions(BaseInvocation):
    tag = EldritchInvocationNames.MISTY_VISIONS
    _desc = """You can cast Silent Image without expending a spell slot."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Misty Visions", Spell.SILENT_IMAGE)


#############################################################################
class OneWithShadows(BaseInvocation):
    tag = EldritchInvocationNames.ONE_WITH_SHADOWS
    _desc = """While you're in an area of Dim Light or Darkness, you can cast 'Invisibility' on yourself without 
            expending a spell slot."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("One with Shadows", Spell.INVISIBILITY)


#############################################################################
class OtherworldlyLeap(BaseInvocation):
    tag = EldritchInvocationNames.OTHERWORLDLY_LEAP
    _desc = """You can cast Jump on yourself without expending a spell slot."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Otherworldly Leap", Spell.JUMP)


#############################################################################
class PactOfTheBlade(BaseInvocation):
    tag = EldritchInvocationNames.PACT_OF_THE_BLADE
    _desc = """As a Bonus Action, you can conjure a pact weapon in your hand - a Simple or Martial Melee weapon of
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
    _desc = """You learn the 'Find Familiar' spell and can cast it as a Magic action without expending a spell slot.

    When you cast the spell, you choose one of the normal forms for you familiar or one of the following special
    forms: Imp, Pseudodragon, Quasit, Skeleton, Slaad Tadpole, Sphinx of Wonder, Sprite, or Venomous Snake.

    Additionally, when you take the Attack action, you can forgo one of your own attacks to allow your familiar to
    make one attack of its own with its Reaction."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Pact of the Chain", Spell.FIND_FAMILIAR)


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
        spells = [f"'{spell_name(_)}'" for _ in self._tome_spells]
        return f"""You can cast {', '.join(spells)} as Warlock spells"""


#############################################################################
class RepellingBlast(BaseInvocation):
    tag = EldritchInvocationNames.REPELLING_BLAST
    _desc = """"""

    def __init__(self, spell: Spell):
        self._spell = spell

    @property
    def desc(self) -> str:
        return f"""When you hit a Large or smaller creature wth {spell_name(self._spell)}, you can push the
            creature up to 10 feet straight away from you."""


#############################################################################
class ThirstingBlade(BaseInvocation):
    tag = EldritchInvocationNames.THIRSTING_BLADE
    _desc = """You gain the Extra Attack feature for your pact weapon only. With that feature, you can attack twice 
            with the weapon instead of once when you take the Attack action on your turn."""


#############################################################################
class VisionsOfDistantRealms(BaseInvocation):
    tag = EldritchInvocationNames.VISIONS_OF_DISTANT_REALMS
    _desc = """You can cast 'Arcane Eye' without expending a spell slot."""


#############################################################################
class WhispersOfTheGrave(BaseInvocation):
    tag = EldritchInvocationNames.WHISPERS_OF_THE_GRAVE
    _desc = """You can cast 'Speak with the Dead' without expending a spell slot."""


#############################################################################
class WitchSight(BaseInvocation):
    tag = EldritchInvocationNames.WITCH_SIGHT
    _desc = """You have TrueSight with a range of 30 feet."""


# EOF
