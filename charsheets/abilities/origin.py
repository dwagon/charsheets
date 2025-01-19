from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Skill, Tool, ProficiencyType, Ability, Stat
from charsheets.exception import NotDefined
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Alert(BaseAbility):
    tag = Ability.ALERT
    _desc = """Initiative Swap. Immediately after you roll Initiative, you can swap your Initiative with the 
    Initiative of one willing ally in the same combat. You can’t make this swap if you or the ally has the 
    Incapacitated condition."""

    def mod_initiative_bonus(self, character: "Character") -> int:
        return character.proficiency_bonus


#############################################################################
class Crafter(BaseAbility):
    tag = Ability.CRAFTER

    #########################################################################
    @property
    def desc(self) -> str:
        s = ", ".join(sorted(list(self._tools)))
        return f"""You gain the following benefits.

        Tool Proficiency. You gained proficiency with {s}.

        Discount. Whenever you buy a non magical item, you receive a 20 percent discount on it.

        Fast Crafting. When you finish a Long Rest, you can craft one piece of gear from the Fast Crafting table, 
        provided you have the Artisan’s Tools associated with that item and have proficiency with those tools. The 
        item lasts until you finish another Long Rest, at which point the item falls apart."""

    #########################################################################
    def set_tools(self, tool1: Tool, tool2: Tool, tool3: Tool):
        self._tools = {tool1, tool2, tool3}

    #########################################################################
    def mod_add_tool_proficiency(self, character: "Character") -> Reason[Tool]:
        if not hasattr(self, "_tools") or not self._tools:
            raise NotDefined("Need to use set_tools() for Crafter feat")
        return Reason("Crafter", *list({_ for _ in self._tools if isinstance(_, Tool)}))


#############################################################################
class Healer(BaseAbility):
    tag = Ability.HEALER
    _desc = """You gain the following benefits.

        Battle Medic. If you have a Healer's Kit, you can expend one use of it and tend to a creature within 5 feet 
        of yourself as a Utilize action. That creature can expend on of its Hit Point Dice, and you then roll that 
        die. The creature regains a number of Hit Points equal to the roll plus your Proficiency Bonus.

        Healing Rerolls. Whenever you roll a die to determine the number of Hit Points you restore with a spell or 
        with this feat's Battle Medic benefit, you can reroll the die if it rolls a 1, and you must use the new roll."""


#############################################################################
class Lucky(BaseAbility):
    tag = Ability.LUCKY

    @property
    def goes(self) -> int:
        return self.owner.proficiency_bonus

    @property
    def desc(self) -> str:
        return f"""You gain the following benefits.
    
    Luck Points. You have a {self.goes} Luck Points and can spend the point on the
    benefits below. You regain your expended Luck Points when you finish a Long Rest.

    Advantage. When you roll a d20 for a D20 Test, you can spend 1 Luck Point to give yourself Advantage on the roll.

    Disadvantage. When a creature rolls a d20 for an attack roll against you, you can spend 1 Luck Point
    to impose Disadvantage on that roll."""


#############################################################################
class MagicInitiate(BaseAbility):
    goes = 1

    def __init__(self, spell_list: str, spellcasting_stat: Stat, cantrip1: Spell, cantrip2: Spell, level1: Spell):
        super().__init__()
        self.spell_list = spell_list
        self.spellcasting_stat = spellcasting_stat
        self.cantrip1 = cantrip1
        self.cantrip2 = cantrip2
        self.level1 = level1

    @property
    def desc(self) -> str:
        return f"""Spellcasting ability is {self.spellcasting_stat}.
        
        Two Cantrips: '{self.cantrip1}' and '{self.cantrip2}'.

        You can cast '{self.level1}' once without a spell slot, and you regain the ability to cast it in that way 
        when you finish a Long Rest. You can also cast the spell using any spell slots you have.

        Spell Change. Whenever you gain a new level, you can replace one of the spells you chose for this feat with a 
        different spell of the same level from the chosen spell list."""

    def mod_add_known_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Magic Initiate", self.cantrip1, self.cantrip2)

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Magic Initiate Cleric", self.level1)


#############################################################################
class MagicInitiateCleric(MagicInitiate):
    tag = Ability.MAGIC_INITIATE_CLERIC

    def __init__(self, spellcasting_stat: Stat, cantrip1: Spell, cantrip2: Spell, level1: Spell):
        super().__init__("Cleric", spellcasting_stat, cantrip1, cantrip2, level1)


#############################################################################
class MagicInitiateDruid(MagicInitiate):
    tag = Ability.MAGIC_INITIATE_DRUID

    def __init__(self, spellcasting_stat: Stat, cantrip1: Spell, cantrip2: Spell, level1: Spell):
        super().__init__("Druid", spellcasting_stat, cantrip1, cantrip2, level1)


#############################################################################
class MagicInitiateWizard(MagicInitiate):
    tag = Ability.MAGIC_INITIATE_WIZARD

    def __init__(self, spellcasting_stat: Stat, cantrip1: Spell, cantrip2: Spell, level1: Spell):
        super().__init__("Wizard", spellcasting_stat, cantrip1, cantrip2, level1)


#############################################################################
class Musician(BaseAbility):
    tag = Ability.MUSICIAN
    _desc = """You gain the following benefits.
    
    Instrument Training. You gain proficiency with three Musical Instruments of your choice.
    
    Encouraging Song. As you finish a Short or Long Rest, you can play a song on a Musical Instrument with which you
    have proficiency and give Heroic Inspiration to allies who hear the song. The number of allies you can affect in
    this way equals your Proficiency Bonus.
    """

    #########################################################################
    def mod_add_tool_proficiency(self, character: "Character") -> Reason[Tool]:
        return Reason("Musician", Tool.MUSICAL_INSTRUMENT)


#############################################################################
class SavageAttacker(BaseAbility):
    tag = Ability.SAVAGE_ATTACKER
    _desc = """You've trained to deal particularly damaging strikes. Once per turn when you hit a target with a weapon,
    you can roll the weapon's damage dice twice and use either roll against the target.
    """


#############################################################################
class Skilled(BaseAbility):
    tag = Ability.SKILLED
    hide = True

    #########################################################################
    def set_skills(self, skill1: ProficiencyType, skill2: ProficiencyType, skill3: ProficiencyType):
        self._skills = {skill1, skill2, skill3}

    #########################################################################
    @property
    def desc(self) -> str:
        s = ", ".join(sorted(list(self._skills)))
        return f"""You have proficiency in: {s}"""

    #########################################################################
    def mod_add_skill_proficiency(self, character: "Character") -> Reason[Skill]:
        if not hasattr(self, "_skills"):
            raise NotDefined("Need to use set_skills() for Skill feat")
        return Reason("Skilled", *list({_ for _ in self._skills if isinstance(_, Skill)}))

    #########################################################################
    def mod_add_tool_proficiency(self, character: "Character") -> Reason[Tool]:
        if not hasattr(self, "_skills"):
            raise NotDefined("Need to use set_skills() for Skill feat")
        return Reason("Skilled", *list({_ for _ in self._skills if isinstance(_, Tool)}))


#############################################################################
class TavernBrawler(BaseAbility):
    tag = Ability.TAVERN_BRAWLER
    _desc = """You gain the following benefits.

    Enhanced Unarmed Strike. When you hit with you Unarmed Strike and deal damage, you can deal Bludgeoning damage
    equal to 1d4 plus your Strength modifier instead of the normal damage of an Unarmed Strike.

    Damage Rerolls. Whenever you roll a damage die for your Unarmed Strike, you can reroll the die if it rolls a 1, 
    and you must use the new roll.

    Improvised Weaponry. You have proficiency with improvised weapons.

    Push. When you hit a creature with an Unarmed Strike as part of the Attack action on your turn, you can deal damage
    to the target and also push it 5 feet away from you. You can use this benefit only once per turn."""


#############################################################################
class Tough(BaseAbility):
    tag = Ability.TOUGH
    hide = True

    @property
    def desc(self) -> str:
        return f"Your Hit Point maximum increased by {self.mod_hp_bonus(self.owner)}"

    def mod_hp_bonus(self, character: "Character") -> Reason[int]:
        return Reason("Tough", self.owner.level * 2)


# EOF
