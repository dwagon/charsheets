from typing import TYPE_CHECKING

from charsheets.constants import Feat
from charsheets.feats.base_feat import BaseFeat

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Alert(BaseFeat):
    tag = Feat.ALERT
    desc = """You gain the following benefits.

Initiative Proficiency. When you roll Initiative, you can add your Proficiency Bonus to the roll.

Initiative Swap. Immediately after you roll Initiative, you can swap your Initiative with the Initiative of one willing
ally in the same combat. You can’t make this swap if you or the ally has the Incapacitated condition."""

    @classmethod
    def mod_initiative_bonus(cls, character: "Character"):
        return character.proficiency_bonus


#############################################################################
class Crafter(BaseFeat):
    tag = Feat.CRAFTER
    desc = """You gain the following benefits.

Tool Proficiency.

Discount. Whenever you buy a non-magical item, you receive a 20 percent discount on it.

Fast Crafting. When you finish a Long Rest, you can craft one piece of gear."""


#############################################################################
class Healer(BaseFeat):
    tag = Feat.HEALER
    desc = """You gain the following benefits.

Battle Medic. If you have a Healer's Kit, you can expend one use of it and tend to a creature within 5 feet of
yourself as a Utilize action. That creature can expend on of its Hit Point Dice, and you then roll that die.
The creature regains a number of Hit Points equal to the roll plus your Proficiency Bonus.

Healing Rerolls. Whenever you roll a die to determine the number of Hit Points you restore with a spell or with this
feat's Battle Medic benefit, you can reroll the die if it rolls a 1, and you must use the new roll."""


#############################################################################
class Lucky(BaseFeat):
    tag = Feat.LUCKY
    desc = """You gain the following benefits.

    Luck Points. 

    Advantage.

    Disadvantage."""


#############################################################################
class MagicInitiateCleric(BaseFeat):
    tag = Feat.MAGIC_INITIATE_CLERIC
    desc = """You gain the following benefits.

Two Cantrips. You learn two cantrips of your choice from the Cleric spell list. Intelligence, Wisdom, or Charisma is
your spellcasting ability for this feat’s spells (choose when you select this feat).

Level 1 Spell. Choose a level 1 spell from the same list you selected for this feat’s cantrips. 
You always have that spell prepared. You can cast it once without a spell slot, and you regain the ability to cast it 
in that way when you finish a Long Rest. You can also cast the spell using any spell slots you have.

Spell Change. Whenever you gain a new level, you can replace one of the spells you chose for this feat with a 
different spell of the same level from the chosen spell list."""


#############################################################################
class MagicInitiateDruid(BaseFeat):
    tag = Feat.MAGIC_INITIATE_DRUID
    desc = """You gain the following benefits.

Two Cantrips. You learn two cantrips of your choice from the Druid spell list. Intelligence, Wisdom, or Charisma is 
your spellcasting ability for this feat’s spells (choose when you select this feat).

Level 1 Spell. Choose a level 1 spell from the same list you selected for this feat’s cantrips.
You always have that spell prepared. You can cast it once without a spell slot, and you regain the ability to cast it
in that way when you finish a Long Rest. You can also cast the spell using any spell slots you have.

Spell Change. Whenever you gain a new level, you can replace one of the spells you chose for this feat with a
different spell of the same level from the chosen spell list."""


#############################################################################
class MagicInitiateWizard(BaseFeat):
    tag = Feat.MAGIC_INITIATE_WIZARD
    desc = """You gain the following benefits.

Two Cantrips. You learn two cantrips of your choice from the Wizard spell list. Intelligence, Wisdom, or Charisma is
your spellcasting ability for this feat’s spells (choose when you select this feat).

Level 1 Spell. Choose a level 1 spell from the same list you selected for this feat’s cantrips.
You always have that spell prepared. You can cast it once without a spell slot, and you regain the ability to cast it
in that way when you finish a Long Rest. You can also cast the spell using any spell slots you have.

Spell Change. Whenever you gain a new level, you can replace one of the spells you chose for this feat with a
different spell of the same level from the chosen spell list."""


#############################################################################
class Musician(BaseFeat):
    tag = Feat.MUSICIAN
    desc = """You gain the following benefits.
    
    Instrument Training. You gain proficiency with three Musical Instruments of your choice.
    
    Encouraging Song. As you finish a Short or Long Rest, you can play a song on a Musical Instrument with which you
    have proficiency and give Heroic Inspiration to allies who hear the song. The number of allies you can affect in
    this way equals your Proficiency Bonus.
    """


#############################################################################
class SavageAttacker(BaseFeat):
    tag = Feat.SAVAGE_ATTACKER
    desc = """You've trained to deal particularly damaging strikes. Once per turn when you hit a target with a weapon,
    you can roll the weapon's damage dice twice and use either roll against the target.
    """


#############################################################################
class Skilled(BaseFeat):
    tag = Feat.SKILLED
    desc = """You gain proficiency in any combination of three skills or tools of your choice."""


#############################################################################
class TavernBrawler(BaseFeat):
    tag = Feat.TAVERN_BRAWLER
    desc = """You gain the following benefits.

    Enhanced Unarmed Strike. When you hit with you Unarmed Strike and deal damage, you can deal Bludgeoning damage
    equal to 1d4 plus your Strength modifier instead of the normal damage of an Unarmed Strike.

    Damage Rerolls. Whenever you roll a damage die for your Unarmed Strike, you can reroll the die if it rolls a 1, 
    and you must use the new roll.

    Improvised Weaponry. You have proficiency with improvised weapons.

    Push. When you hit a creature with an Unarmed Strike as part of the Attack action on your turn, you can deal damage
    to the target and also push it 5 feet away from you. You can use this benefit only once per turn."""


#############################################################################
class Tough(BaseFeat):
    tag = Feat.TOUGH
    desc = """Your Hit Point maximum increases by an amount equal to twice your character level when you gain this feat.
     Whenever you gain a character level thereafter, your Hit Point maximum increases by an additional 2 Hit Points"""


# EOF
