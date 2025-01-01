from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability, Proficiency
from charsheets.reason import Reason
from charsheets.spells import Spells

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class ChannelDivinity(BaseAbility):
    tag = Ability.CHANNEL_DIVINITY
    _desc = """You can channel divine energy.
    
    Divine Spark. As a Magic action, you point your Holy Symbol at another creature you can see within 30 feet of
    yourself and focus divine energy at it. Roll 1d8 and add your Wisdom modifier. You either restore Hot Points to
    the creature equal to that total or force the creature to Make a Constitution saving throw. On a failed save, the
    creature takes Necrotic or Radiant damage (your choice) equal to that total. On a successful save, the creature
    takes half as much damage.
    
    Turn Undead. As a Magic action, you present your Hold Symbol and censure Undead creatures. Each Undead of your
    choice within 30 feet of you must make a Wisdom saving throw. If the creature fails its save, it has the Frightened
    and Incapacitated condition for 1 minute. For that duration, it tries to mave as far from you as it can on its
    turns. This effect ends early on the creature if it takes any damage, if you have the Incapacitated condition,
    or if you die
    """


#############################################################################
class DiscipleOfLife(BaseAbility):
    tag = Ability.DISCIPLE_OF_LIFE
    _desc = """When a spell you cast with a spell slot restores Hit Points to a creature, that creature regains
    additional Hit Points on the turn you cast the spell. The additional Hit Points equal 2 plus the spell
    slot’s level."""


#############################################################################
class LifeDomainSpells(BaseAbility):
    tag = Ability.LIFE_DOMAIN_SPELLS
    _desc = """Your connection to this divine domain ensures you always have certain spells ready. When you reach a
    Cleric level specified in the Life Domain Spells table, you thereafter always have the listed spells prepared."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        return Reason("Life Domain Spells", Spells.BLESS, Spells.CURE_WOUNDS, Spells.AID, Spells.LESSER_RESTORATION)


#############################################################################
class PreserveLife(BaseAbility):
    tag = Ability.PRESERVE_LIFE
    _desc = """As a Magic action, you present your Holy Symbol and expend a use of your Channel Divinity to evoke healing
    energy that can restore a number of Hit Points equal to five times your Cleric level. Choose Bloodied creatures
    within 30 feet of yourself (which can include you), and divide those Hit Points among them. This feature can
    restore a creature to no more than half its Hit Point maximum."""


#################################################################################
class DivineProtector(BaseAbility):
    tag = Ability.DIVINE_ORDER_PROTECTOR
    _desc = """Trained for battle, you gain proficiency with Martial weapons and training with Heavy armor."""

    #############################################################################
    def mod_weapon_proficiency(self, character: "Character") -> Reason[Proficiency]:
        return Reason[Proficiency]("Protector", Proficiency.MARTIAL_WEAPONS)

    #############################################################################
    def mod_armour_proficiency(self, character: "Character") -> Reason[Proficiency]:
        return Reason("Protector", Proficiency.HEAVY_ARMOUR)


#################################################################################
class Thaumaturge(BaseAbility):
    tag = Ability.DIVINE_ORDER_THAUMATURGE
    _desc = """Thaumaturge. You know one extra cantrip from the Cleric spell list. In addition, your mystical connection 
    to the divine gives you a bonus to your Intelligence (Arcana or Religion) checks.
    The bonus equals your Wisdom modifier (minimum of +1).
    """

    # Users will have to add their own cantrip to the learnt spells.

    def mod_skill_arcana(self, character: "Character") -> Reason[int]:
        modifier = Reason[int]("thaumaturge", max(1, character.wisdom.modifier))
        return modifier

    def mod_skill_religion(self, character: "Character") -> Reason[int]:
        modifier = Reason[int]("thaumaturge", max(1, character.wisdom.modifier))
        return modifier


#################################################################################
class WardingFlare(BaseAbility):
    tag = Ability.WARDING_FLARE
    _desc = """When a creature that you can see within 30 feet of yourself makes an attack roll, you can take
    a Reaction to impose Disadvantage on the attack roll, causing light to flare before it hits or misses.
    
    You can use this feature a number of times equal to your Wisdom modifier (minimum of once). You regain all expended
    uses when you finish a Long Rest."""


#############################################################################
class LightDomainSpells(BaseAbility):
    tag = Ability.LIGHT_DOMAIN_SPELLS
    _desc = """Your connection to this divine domain ensures you always have certain spells ready. When you reach a
    Cleric level specified in the Light Domain Spells table, you thereafter always have the listed spells prepared."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        return Reason(
            "Light Domain Spells", Spells.BURNING_HANDS, Spells.FAERIE_FIRE, Spells.SCORCHING_RAY, Spells.SEE_INVISIBILITY
        )


#################################################################################
class RadianceOfTheDawn(BaseAbility):
    tag = Ability.RADIANCE_OF_THE_DAWN
    _desc = """As a Magic action, you present your Holy Symbol and expend a use of your Channel Divinity to emit a 
    flash of light in a 30-foot Emanation originating from yourself. Any magical Darkness - such as that created by
    the Darkness spell - in that area is dispelled. Additionally, each creature of your choice in that area must
    make a Constitution saving throw, taking Radiant damage equal to 2d10 plus your Cleric level on a failed save or
    half as much damage on a successful one."""


#############################################################################
class WarDomainSpells(BaseAbility):
    tag = Ability.WAR_DOMAIN_SPELLS
    _desc = """Your connection to this divine domain ensures you always have certain spells ready. When you reach a
    Cleric level specified in the War Domain Spells table, you thereafter always have the listed spells prepared."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        return Reason(
            "War Domain Spells", Spells.GUIDING_BOLT, Spells.MAGIC_WEAPON, Spells.SHIELD_OF_FAITH, Spells.SPIRITUAL_WEAPON
        )


#################################################################################
class GuidedStrike(BaseAbility):
    tag = Ability.GUIDED_STRIKE
    _desc = """When you or a creature within 30 feet of you misses with an attack roll, you can expend one use of
    your Channel Divinity and give that roll a +10 bonus, potentially causing it to hit. When you use this feature to
    benefit another creature's attack roll, you must take a Reaction to do so"""


#################################################################################
class InvokeDuplicity(BaseAbility):
    tag = Ability.INVOKE_DUPLICITY
    _desc = """As a Bonus Actoin, you can expend one use of your Channel Divinity to create a pefect visual illusion
    of yourself in an unoccupied space you can see within 30 feet of yourself. The illusion is intangible and
    doesn't occupy its space. It lasts for 1 minute, but it ends early if you dismiss it (no action required) or have
    the Incapacitated condition. The illusion is animated and mimics your expressions and gestures. While it persists,
    you gain the following benefits.
    
    Cast Spells. You can cast spells as though were in the illusion's space, but you must use your own senses.
    
    Distract. When both you and your illusion are with 5 feet of a creature that can see the illusion, you have
    Advantage on attack rolls against that creature, given how distracting the illusion is to the target.
    
    Move. As a Bonus Action, you can move the illusion up to 30 feet to an unoccupied space you can see that is within
    120 feet of yourself."""


#################################################################################
class WarPriest(BaseAbility):
    tag = Ability.WAR_PRIEST
    _desc = """As a Bonus Action, you can make one attack with a weapon or an Unarmed Strike. You can use this Bonus
    Action a number of times equal to your Wisdom modifier (minimum of once). You regain all expended uses when you
    finish a Short or Long Rest."""


#################################################################################
class BlessingOfTheTrickster(BaseAbility):
    tag = Ability.BLESSING_OF_THE_TRICKSTER
    _desc = """As a Magic action, you can choose yourself or a willing creature within 30 feet of yourself to have
    Advantage on Dexterity (Stealth) checks. This blessing lasts until you finish a Long Rest or you use this
    feature again."""


#############################################################################
class TrickeryDomainSpells(BaseAbility):
    tag = Ability.TRICKERY_DOMAIN_SPELLS
    _desc = """Your connection to this divine domain ensures you always have certain spells ready. When you reach a
    Cleric level specified in the Trickery Domain Spells table, you thereafter always have the listed spells prepared."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        return Reason(
            "Trickery Domain Spells", Spells.CHARM_PERSON, Spells.DISGUISE_SELF, Spells.INVISIBILITY, Spells.PASS_WITHOUT_TRACE
        )


# EOF
