import sys
from typing import Optional, Type, Any
from enum import StrEnum, auto
from charsheets.character import Character
from charsheets.constants import Stat, Proficiencies, Ability, CharSubclassName
from charsheets.exception import UnhandledException
from charsheets.reason import Reason
from charsheets.spells import Spells, SPELL_LEVELS
from charsheets.util import safe


#############################################################################
class EldritchInvocation(StrEnum):
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
    tag: EldritchInvocation = EldritchInvocation.NONE


#################################################################################
class Warlock(Character):
    #########################################################################
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.invocations: list[BaseInvocation] = []

    #########################################################################
    @property
    def class_special(self) -> str:
        ans = ["Eldritch Invocations"]
        for invocation in self.invocations:
            ans.append(safe(invocation.tag.title()))
            if hasattr(invocation, "desc"):
                ans.append(getattr(invocation, "desc"))
            else:
                ans.append(invocation._desc)
            ans.append("\n")
        return "\n".join(ans)

    #########################################################################
    def add_invocation(self, invocation: BaseInvocation):
        self.invocations.append(invocation)

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 8

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.CHARISMA

    #############################################################################
    def weapon_proficiency(self) -> set[Proficiencies]:
        return {
            Proficiencies.SIMPLE_WEAPONS,
        }

    #############################################################################
    def armour_proficiency(self) -> set[Proficiencies]:
        return {
            Proficiencies.LIGHT_ARMOUR,
        }

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        if stat in (Stat.WISDOM, Stat.CHARISMA):
            return True

        return False

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities = set()

        abilities.add(Ability.ELDRITCH_INVOCATIONS)
        abilities.add(Ability.PACT_MAGIC)
        if self.level >= 2:
            abilities.add(Ability.MAGICAL_CUNNING)
        if self.level >= 3:
            match self.sub_class_name:
                case CharSubclassName.ARCHFEY_PATRON:
                    if level >= 3:
                        pass
                case CharSubclassName.CELESTIAL_PATRON:
                    if level >= 3:
                        pass
                case CharSubclassName.FIEND_PATRON:
                    if level >= 3:
                        pass
                case CharSubclassName.GREAT_OLD_ONE_PATRON:
                    if self.level >= 3:
                        pass
                case _:
                    raise UnhandledException(f"{self.sub_class_name} doesn't have class_abilities() defined")

        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [1, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [2, 2, 0, 0, 0, 0, 0, 0, 0],
            4: [2, 2, 0, 0, 0, 0, 0, 0, 0],
            5: [2, 2, 2, 0, 0, 0, 0, 0, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def max_spell_level(self, char_level: int) -> int:
        return min(5, (char_level + 1) // 2)

    #############################################################################
    def spells(self, spell_level: int) -> list[Spells]:
        result = []
        for spell in self.known_spells:
            if SPELL_LEVELS[spell] == spell_level:
                result.append(spell)
        return result

    #############################################################################
    def check_set_modifiers(self, modifier: str) -> set[Any]:
        result = set()
        result |= super().check_set_modifiers(modifier)
        for invocation in self.invocations:
            if hasattr(invocation, modifier):
                result |= getattr(invocation, modifier)(character=self)
        return result

    #############################################################################
    def check_modifiers(self, modifier: str) -> Reason:
        result = Reason()
        result.extend(super().check_modifiers(modifier))
        for invocation in self.invocations:
            if hasattr(invocation, modifier):
                result.add(f"invocation {invocation}", getattr(invocation, modifier)(character=self))
        return result


#############################################################################
class AgonizingBlast(BaseInvocation):
    tag = EldritchInvocation.AGONIZING_BLAST

    def __init__(self, spell: Spells):
        self._spell = spell

    @property
    def desc(self) -> str:
        return f"""You can add your Charisma modifier to {safe(self._spell.name).title()} damage rolls."""


#############################################################################
class ArmorOfShadows(BaseInvocation):
    tag = EldritchInvocation.ARMOR_OF_SHADOWS
    _desc = """You can cast Mage Armor on yourself without expending a spell slot."""

    def mod_add_prepared_spell(self):
        return {Spells.MAGE_ARMOR}

    def mod_add_known_spells(self, character: "Character"):
        return {Spells.MAGE_ARMOR}


#############################################################################
class AscendantsStep(BaseInvocation):
    tag = EldritchInvocation.ASCENDANT_STEP
    _desc = """You can cast Levitate on yourself without expending a spell slot."""

    def mod_add_prepared_spell(self):
        return {Spells.LEVITATE}

    def mod_add_known_spells(self, character: "Character"):
        return {Spells.LEVITATE}


#############################################################################
class DevilsSight(BaseInvocation):
    tag = EldritchInvocation.DEVILS_SIGHT
    _desc = """You can see normally in Dim Light and Darkness - both magical and non-magical
     - within 120 feet of yourself"""


#############################################################################
class EldritchMind(BaseInvocation):
    tag = EldritchInvocation.ELDRITCH_MIND
    _desc = """You have Advantage on Constitution saving throws that you make to maintain Concentration"""


#############################################################################
class EldritchSmite(BaseInvocation):
    tag = EldritchInvocation.ELDRITCH_SMITE
    _desc = """Once per turn whn you hit a creature with your pact weapon, you can expend a Pact Magic spell slot
    to deal an extra 1d8 Force damage to the target, plus another 1d8 per level of the spell slot, and you can
    give the target the Prone condition if it is Huge or smaller."""


#############################################################################
class EldritchSpear(BaseInvocation):
    tag = EldritchInvocation.ELDRITCH_SPEAR

    def __init__(self, spell: Spells):
        self._spell = spell

    @property
    def desc(self) -> str:
        return f"""The range of {safe(self._spell.name).title()} increases by a number of feet equal to 30 times your
        Warlock level."""


#############################################################################
class FiendishVigour(BaseInvocation):
    tag = EldritchInvocation.FIENDISH_VIGOR
    _desc = """You can cast False Life on yourself without expending a spell slot. When you cast the spell with
    this feature, you don't roll the die for the Temporary Hit Points; you automatically get the highest number on
    the die."""

    def mod_add_prepared_spells(self, character: "Character"):
        return {Spells.FALSE_LIFE}

    def mod_add_known_spells(self, character: "Character"):
        return {Spells.FALSE_LIFE}


#############################################################################
class GazeOfTwoMinds(BaseInvocation):
    tag = EldritchInvocation.GAZE_OF_TWO_MINDS
    _desc = """You can use a Bonus Action to touch a willing creature and perceve through its senses until the
    end of your next turn. As long as the creature is on the same plane of existence as you, you can take a Bonus
    Action of subsequent turns to maintain this connection, extending the duration until the end of your next turn. 
    The connection ends if you dont maintain it in this way.
    
    While perceiving through the other creature's senses, you benefit from any special sense posses by that creature,
    amd you can cast spells as if you were in your space or the other creature's space if the two of you are within
    60 feet of each other."""


#############################################################################
class GiftOfTheDepths(BaseInvocation):
    tag = EldritchInvocation.GIFT_OF_THE_DEPTHS
    _desc = """You can breathe underwater, and you gain a Swim Speed equal to your Speed.
    
    You can also cast Water Breathing once without expending a spell slot. You regain the ability to cast it in this
    way again when you finish a Long Rest."""

    def mod_swim_movement(self, character: "Character") -> int:
        return 30


#############################################################################
class LessonsOfTheFirstOnes(BaseInvocation):
    tag = EldritchInvocation.LESSONS_OF_THE_FIRST_ONES
    _desc = """You have received knowledge from an elder entity of the multiverse, allowing you to gain one
     Origin feat of your choice"""


#############################################################################
class MaskOfManyFaces(BaseInvocation):
    tag = EldritchInvocation.MASK_OF_MANY_FACES
    _desc = """You can cast Disguise Self without expending a spell slot."""

    def mod_add_prepared_spells(self, character: "Character"):
        return {Spells.DISGUISE_SELF}

    def mod_add_known_spells(self, character: "Character"):
        return {Spells.DISGUISE_SELF}


#############################################################################
class MistyVisions(BaseInvocation):
    tag = EldritchInvocation.MISTY_VISIONS
    _desc = """You can cast Silent Image without expending a spell slot."""

    def mod_add_prepared_spells(self, character: "Character"):
        return {Spells.SILENT_IMAGE}

    def mod_add_known_spells(self, character: "Character"):
        return {Spells.SILENT_IMAGE}


#############################################################################
class OtherworldlyLeap(BaseInvocation):
    tag = EldritchInvocation.OTHERWORLDLY_LEAP
    _desc = """You can cast Jump on yourself without expending a spell slot."""

    def mod_add_prepared_spells(self, character: "Character"):
        return {Spells.JUMP}

    def mod_add_known_spells(self, character: "Character"):
        return {Spells.JUMP}


#############################################################################
class PactOfTheBlade(BaseInvocation):
    tag = EldritchInvocation.PACT_OF_THE_BLADE
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
    tag = EldritchInvocation.PACT_OF_THE_CHAIN
    _desc = """You learn the Find Familiar spell and can cast it as a Magic action without expending a spell slot.
    
    When you cast the spell, you choose one of the normal forms for you familiar or one of the following special
    forms: Imp, Pseudodragon, Quasit, Skeleton, Slaad Tadpole, Sphinx of Wonder, Sprite, or Venomous Snake.
    
    Additionally, when you take the Attack action, you can forgo one of your own attacks to allow your familiar to
    make one attack of its own with its Reaction."""

    def mod_add_prepared_spells(self, character: "Character"):
        return {Spells.FIND_FAMILIAR}

    def mod_add_known_spells(self, character: "Character"):
        return {Spells.FIND_FAMILIAR}


#############################################################################
class PactOfTheTome(BaseInvocation):
    tag = EldritchInvocation.PACT_OF_THE_TOME
    _desc = """Stitching together strands of shadow, you conjure forth a book in your hand at the end of a Short
    or Long Rest. This Book of Shadows contains eldritch magic that only you can access, granting you the benefits
    below.
    
    Cantrips and Rituals. While the
    book is on your person, you have the spells prepared, and they function as Warlock spells for you.
    
    Spellcasting Focus. You can use the book as a Spellcasting Focus."""

    def __init__(self, cantrip1: Spells, cantrip2: Spells, cantrip3: Spells, spell1: Spells, spell2: Spells):
        self._tome_spells = {cantrip1, cantrip2, cantrip3, spell1, spell2}

    def mod_add_prepared_spells(self, character: "Character"):
        return self._tome_spells

    def mod_add_known_spells(self, character: "Character"):
        return self._tome_spells

    @property
    def desc(self) -> str:
        spells = [safe(_.name).title() for _ in self._tome_spells]
        return f"""You can cast {', '.join(spells)} as Warlock spells"""


#############################################################################
class RepellingBlast(BaseInvocation):
    tag = EldritchInvocation.REPELLING_BLAST
    _desc = """"""

    def __init__(self, spell: Spells):
        self._spell = spell

    @property
    def desc(self) -> str:
        return f"""When you hit a Large or smaller creature wth {safe(self._spell.name).title()}, you can push the
creature up to 10 feet straight away from you."""


# EOF
