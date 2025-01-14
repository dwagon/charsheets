from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability
from charsheets.reason import Reason
from charsheets.spells import Spells

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class FavoredEnemy(BaseAbility):
    tag = Ability.FAVOURED_ENEMY
    _desc = """You always have the Hunter's Mark spell prepared. You can cast it twice without expending a spell slot
    and you regain all expended uses of this ability when you finish a Long Rest.
    """

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        return Reason("Favoured Enemy", Spells.HUNTERS_MARK)


#############################################################################
class DeftExplorer(BaseAbility):
    tag = Ability.DEFT_EXPLORER
    _desc = """Thanks to your travels, you gain the following benefits.

    Expertise. Choose one of your skill proficiencies with which you lack Expertise. You gain Expertise in that skill.

    Languages. You know two languages of your choice"""
    # TODO - select languages
    # TODO - select skill


#############################################################################
class PrimalCompanion(BaseAbility):
    tag = Ability.PRIMAL_COMPANION
    _desc = """You magically summon a primal beast, which draws strength from your bond with nature."""


#############################################################################
class DreadfulStrikes(BaseAbility):
    tag = Ability.DREADFUL_STRIKES
    _desc = """You can augment your weapon strikes with mind-scarring magic drawn from the murky hollows of the
    Fey wild. When you hit a creature with a weapon, you can deal an extra 1d4 Psychic damage to the target,
    which can take this extra damage only once per turn."""


#############################################################################
class OtherworldlyGlamour(BaseAbility):
    tag = Ability.OTHERWORLDLY_GLAMOUR
    _desc = """Whenever you make a Charisma check, you gain a bonus to the check equal to your Wisdom modifier (min +1).
    You also gain proficiency in one of these skills of your choice: Deception, Performance or Persuasion"""
    # TODO - select skill


#############################################################################
class FeywildGifts(BaseAbility):
    tag = Ability.FEYWILD_GIFTS
    _desc = """You possess a fey blessing."""


#############################################################################
class FeyWandererSpells(BaseAbility):
    tag = Ability.FEY_WANDERER_SPELLS
    _desc = """Feywild Gifts
    
    1 Illusory butterflies flutter around you while you take aShort or Long Rest.
    
    2 Flowers bloom from your hair each dawn.
    
    3 You faintly smell of cinnamon, lavender, nutmeg, or another comforting herb or spice.
    
    4 Your shadow dances while noone is looking directly at it.
    
    5 Horns or antlers sprout from your head.
    
    6 Your skin and hair change color each dawn."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        spells = Reason("Fey Wanderer", Spells.CHARM_PERSON)
        if character.level >= 5:
            spells = Reason("Fey Wanderer", Spells.MISTY_STEP)
        return spells


#############################################################################
class DreadAmbusher(BaseAbility):
    tag = Ability.DREAD_AMBUSHER
    _desc = """You have mastered the art of creating fearsome ambushes, granting you the following benefits.
    
    Ambusher's Leap.  At the start of your first turn of each combat, your Speed increases by 10 feet until the end 
    of that turn.
    
    Dreadful Strike. When you attack a creature and hit it with a weapon, you can deal an extra 2d6 Psychic damage. 
    You can use this benefit only once per turn, you can use it a number of times equal to your Wisdom modifier (
    minimum of once), and you regain all expended uses when you finish a Long Rest.
    
    Initiative Bonus. When you roll Initiative, you can add your Wisdom modifier to the roll."""


#############################################################################
class UmbralSight(BaseAbility):
    tag = Ability.UMBRAL_SIGHT
    _desc = """You gain Darkvision with a range of 60 feet. If you already have Darkvision, its range increases by 60
    feet.
    
    You are also adept at evading creatures that rely on Darkvision. While entirely in Darkness, you have the
    Invisible condition to any creature that relies on Darkvision to see you in that Darkness."""

    # TODO - darkvision


#############################################################################
class HuntersPrey(BaseAbility):
    tag = Ability.HUNTERS_PREY
    _desc = """You gain one of the following. Whenever you finish a Long Rest you can replace the option.

    Colossus Slayer. Your tenacity can wear down even the most resilient foes. When you hit a creature with a weapon,
    the weapon deals an extra 1d8 damage to the target if its missing any of its Hit Points. You can deal this extra 
    damage only once per turn.

    Horde Breaker. Once on each of your turns when you make an attack with a weapon, you can make another attack with 
    the same weapon against a different creature that is within 5 feet of the original target, that is within the 
    weapon's range, and you haven't attacked this turn.
    """


#############################################################################
class HuntersLore(BaseAbility):
    tag = Ability.HUNTERS_LORE
    _desc = """You can call on the forces of nature to reveal certain strengths and weaknesses of your prey.
    While a creature is marked by your Hunter’s Mark, you know whether that creature has any
    Immunities, Resistances, or Vulnerabilities, and if the creature has any, you know what they are."""


#############################################################################
class Roving(BaseAbility):
    tag = Ability.ROVING
    _desc = """Your speed increases by 10 feet if you aren't wearing Heavy armor. You also have a Climb Speed
    and Swim Speed equal to your Speed."""


# EOF
