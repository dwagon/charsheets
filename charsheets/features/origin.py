from typing import TYPE_CHECKING, cast
from aenum import extend_enum

from charsheets.constants import Skill, Tool, ProficiencyType, Feature, Stat, Recovery
from charsheets.exception import NotDefined, InvalidOption
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell, spell_name

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "ALERT", "Alert")
extend_enum(Feature, "CRAFTER", "Crafter")
extend_enum(Feature, "HEALER", "Healer")
extend_enum(Feature, "LUCKY", "Lucky")
extend_enum(Feature, "MAGIC_INITIATE_CLERIC", "Magic Initiate (Cleric)")
extend_enum(Feature, "MAGIC_INITIATE_DRUID", "Magic Initiate (Druid)")
extend_enum(Feature, "MAGIC_INITIATE_WIZARD", "Magic Initiate (Wizard)")
extend_enum(Feature, "MUSICIAN", "Musician")
extend_enum(Feature, "SAVAGE_ATTACKER", "Savage Attacker")
extend_enum(Feature, "SKILLED", "Skilled")
extend_enum(Feature, "TAVERN_BRAWLER", "Tavern Brawler")
extend_enum(Feature, "TOUGH", "Tough")


#############################################################################
class Alert(BaseFeature):
    tag = Feature.ALERT
    _desc = """Initiative Swap. Immediately after you roll Initiative, you can swap your Initiative with the
    Initiative of one willing ally in the same combat. You can’t make this swap if you or the ally has the
    Incapacitated condition."""

    def mod_initiative_bonus(self, character: "Character") -> Reason[int]:
        return Reason("Alert", character.proficiency_bonus)


#############################################################################
class Crafter(BaseFeature):
    tag = Feature.CRAFTER
    _desc = """Discount. Whenever you buy a non magical item, you receive a 20 percent discount on it.

        Fast Crafting. When you finish a Long Rest, you can craft one piece of gear from the Fast Crafting table,
        provided you have the Artisan’s Tools associated with that item and have proficiency with those tools. The
        item lasts until you finish another Long Rest, at which point the item falls apart."""

    #########################################################################
    def __init__(self, *tools: Tool):
        super().__init__()
        if len(tools) != 3:
            raise InvalidOption("Crafter needs three tools")
        self._tools = set(tools)

    #########################################################################
    def mod_add_tool_proficiency(self, character: "Character") -> Reason[Tool]:
        if not hasattr(self, "_tools") or not self._tools:
            raise NotDefined("Need to use set_tools() for Crafter feat")
        return Reason("Crafter", *list({_ for _ in self._tools if isinstance(_, Tool)}))


#############################################################################
class Healer(BaseFeature):
    tag = Feature.HEALER
    _desc = """Battle Medic. If you have a Healer's Kit, you can expend one use of it and tend to a creature within 5 
    feet of yourself as a Utilize action. That creature can expend on of its Hit Point Dice, and you then roll that 
    die. The creature regains a number of Hit Points equal to the roll plus your Proficiency Bonus.

    Healing Rerolls. Whenever you roll a die to determine the number of Hit Points you restore with a spell or
    with this feat's Battle Medic benefit, you can reroll the die if it rolls a 1, and you must use the new roll."""


#############################################################################
class Lucky(BaseFeature):
    tag = Feature.LUCKY
    recovery = Recovery.LONG_REST

    @property
    def goes(self) -> int:
        return self.owner.proficiency_bonus

    @property
    def desc(self) -> str:
        return f"""Luck Points. You have a {self.goes} Luck Points.

    Advantage. When you roll a d20 for a D20 Test, you can spend 1 Luck Point to give yourself Advantage on the roll.

    Disadvantage. When a creature rolls a d20 for an attack roll against you, you can spend 1 Luck Point
    to impose Disadvantage on that roll."""


#############################################################################
class MagicInitiate(BaseFeature):
    goes = 1
    recovery = Recovery.LONG_REST

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

        Two Cantrips: '{spell_name(self.cantrip1)}' and '{spell_name(self.cantrip2)}'.

        You can cast '{spell_name(self.level1)}' once without a spell slot.
        You can also cast the spell using any spell slots you have."""

    def mod_add_known_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Magic Initiate", self.cantrip1, self.cantrip2)

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Magic Initiate Cleric", self.level1)


#############################################################################
class MagicInitiateCleric(MagicInitiate):
    tag = cast(Feature, Feature.MAGIC_INITIATE_CLERIC)

    def __init__(self, spellcasting_stat: Stat, cantrip1: Spell, cantrip2: Spell, level1: Spell):
        super().__init__("Cleric", spellcasting_stat, cantrip1, cantrip2, level1)


#############################################################################
class MagicInitiateDruid(MagicInitiate):
    tag = cast(Feature, Feature.MAGIC_INITIATE_DRUID)

    def __init__(self, spellcasting_stat: Stat, cantrip1: Spell, cantrip2: Spell, level1: Spell):
        super().__init__("Druid", spellcasting_stat, cantrip1, cantrip2, level1)


#############################################################################
class MagicInitiateWizard(MagicInitiate):
    tag = cast(Feature, Feature.MAGIC_INITIATE_WIZARD)

    def __init__(self, spellcasting_stat: Stat, cantrip1: Spell, cantrip2: Spell, level1: Spell):
        super().__init__("Wizard", spellcasting_stat, cantrip1, cantrip2, level1)


#############################################################################
class Musician(BaseFeature):
    tag = Feature.MUSICIAN

    @property
    def desc(self) -> str:
        return f"""Encouraging Song. As you finish a Short or Long Rest, you can play a song on a Musical Instrument
        and give Heroic Inspiration to {self.owner.proficiency_bonus} allies who hear the song."""

    #########################################################################
    def mod_add_tool_proficiency(self, character: "Character") -> Reason[Tool]:
        return Reason("Musician", cast(Tool, Tool.MUSICAL_INSTRUMENT))


#############################################################################
class SavageAttacker(BaseFeature):
    tag = Feature.SAVAGE_ATTACKER
    _desc = """You've trained to deal particularly damaging strikes. Once per turn when you hit a target with a weapon,
    you can roll the weapon's damage dice twice and use either roll against the target.
    """


#############################################################################
class Skilled(BaseFeature):
    tag = Feature.SKILLED
    hide = True

    #########################################################################
    def __init__(self, skill1: ProficiencyType, skill2: ProficiencyType, skill3: ProficiencyType):
        self._skills = {skill1, skill2, skill3}

    #########################################################################
    def mod_add_skill_proficiency(self, character: "Character") -> Reason[Skill]:
        return Reason("Skilled", *list({_ for _ in self._skills if isinstance(_, Skill)}))

    #########################################################################
    def mod_add_tool_proficiency(self, character: "Character") -> Reason[Tool]:
        return Reason("Skilled", *list({_ for _ in self._skills if isinstance(_, Tool)}))


#############################################################################
class TavernBrawler(BaseFeature):
    tag = Feature.TAVERN_BRAWLER
    _desc = """Enhanced Unarmed Strike. When you hit with you Unarmed Strike and deal damage, you can deal Bludgeoning damage
    equal to 1d4 plus your Strength modifier instead of the normal damage of an Unarmed Strike.

    Damage Rerolls. Whenever you roll a damage die for your Unarmed Strike, you can reroll the die if it rolls a 1
    and you must use the new roll.

    Improvised Weaponry. You have proficiency with improvised weapons.

    Push. When you hit a creature with an Unarmed Strike as part of the Attack action on your turn, you can deal damage
    to the target and also push it 5 feet away from you. You can use this benefit only once per turn."""


#############################################################################
class Tough(BaseFeature):
    tag = Feature.TOUGH
    hide = True

    @property
    def desc(self) -> str:
        return f"Your Hit Point maximum increased by {self.mod_hp_bonus(self.owner)}"

    def mod_hp_bonus(self, character: "Character") -> Reason[int]:
        return Reason("Tough", self.owner.level * 2)


# EOF
