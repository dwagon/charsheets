from typing import TYPE_CHECKING, cast
from aenum import extend_enum

from charsheets.constants import Feature, Sense, Stat, Skill, Proficiency, Tool, DamageType, Recovery
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature, StatIncreaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell, spell_name, SPELL_DETAILS, SpellFlag, SpellSchool

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "ABILITY_SCORE_IMPROVEMENT", "Ability Score Improvement")
extend_enum(Feature, "ACTOR", "Actor")
extend_enum(Feature, "ATHLETE", "Athlete")
extend_enum(Feature, "CHARGER", "Charger")
extend_enum(Feature, "CHEF", "Chef")
extend_enum(Feature, "CROSSBOW_EXPERT", "Crossbow Expert")
extend_enum(Feature, "CRUSHER", "Crusher")
extend_enum(Feature, "DEFENSIVE_DUELIST", "Defensive Duelist")
extend_enum(Feature, "DUAL_WIELDER", "Dual Wielder")
extend_enum(Feature, "DURABLE", "DURABLE")
extend_enum(Feature, "ELEMENTAL_ADEPT", "Elemental Adept")
extend_enum(Feature, "FEY_TOUCHED", "Fey Touched")
extend_enum(Feature, "GRAPPLER", "Grappler")
extend_enum(Feature, "GREAT_WEAPON_MASTER", "Great Weapon Master")
extend_enum(Feature, "HEAVILY_ARMORED", "Heavily Armored")
extend_enum(Feature, "HEAVY_ARMOR_MASTER", "Heavy Armor Master")
extend_enum(Feature, "INSPIRING_LEADER", "Inspiring Leader")
extend_enum(Feature, "KEEN_MIND", "Keen Mind")
extend_enum(Feature, "LIGHTLY_ARMORED", "Lightly Armored")
extend_enum(Feature, "MAGE_SLAYER", "Mage Slayer")
extend_enum(Feature, "MARTIAL_WEAPON_TRAINING", "Martial Weapon Training")
extend_enum(Feature, "MEDIUM_ARMOR_MASTER", "Medium Armor Master")
extend_enum(Feature, "MODERATELY_ARMORED", "Moderately Armored")
extend_enum(Feature, "MOUNTED_COMBATANT", "Mounted Combatant")
extend_enum(Feature, "OBSERVANT", "Observant")
extend_enum(Feature, "PIERCER", "Piercer")
extend_enum(Feature, "POISONER", "Poisoner")
extend_enum(Feature, "POLEARM_MASTER", "Polearm Master")
extend_enum(Feature, "RESILIENT", "Resilient")
extend_enum(Feature, "RITUAL_CASTER", "Ritual Caster")
extend_enum(Feature, "SENTINEL", "Sentinel")
extend_enum(Feature, "SHADOW_TOUCHED", "Shadow Touched")
extend_enum(Feature, "SHARPSHOOTER", "Sharpshooter")
extend_enum(Feature, "SHIELD_MASTER", "Shield Master")
extend_enum(Feature, "SKILL_EXPERT", "Skill Expert")
extend_enum(Feature, "SKULKER", "Skulker")
extend_enum(Feature, "SLASHER", "Slasher")
extend_enum(Feature, "SPEEDY", "Speedy")
extend_enum(Feature, "SPELL_SNIPER", "Spell Sniper")
extend_enum(Feature, "TELEKINETIC", "Telekinetic")
extend_enum(Feature, "TELEPATHIC", "Telepathic")
extend_enum(Feature, "WAR_CASTER", "War Caster")
extend_enum(Feature, "WEAPON_MASTER", "Weapon Master")


#############################################################################
class AbilityScoreImprovement(StatIncreaseFeature):
    tag = Feature.ABILITY_SCORE_IMPROVEMENT
    _desc = """Increase a stat twice"""
    hide = True
    _num_stats = 2
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY, Stat.CONSTITUTION, Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]

    def __init__(self, stat1: Stat, stat2: Stat):
        super().__init__(*[stat1, stat2])


#############################################################################
class Actor(BaseFeature):
    tag = Feature.ACTOR

    #############################################################################
    @property
    def desc(self) -> str:
        bonus = self.owner.charisma.modifier + 8 + self.owner.proficiency_bonus
        return f"""Impersonation. While you're disguised as a real or fictional person, you have Advantage on
        Charisma (Deception or Performance) checks to convince others that you are that person.

        Mimicry. You can mimic the sounds of other creatures, including speech. A creature that hears the mimicry 
        must succeed on a Wisdom (Insight) check to determine the effect is faked (DC {bonus})."""

    #############################################################################
    def mod_stat_cha(self, character: "Character") -> int:
        return 1


#############################################################################
class Athlete(StatIncreaseFeature):
    tag = Feature.ATHLETE
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY]
    _desc = """Climb Speed. You gain a Climb Speed equal to your Speed.

    Hop Up. When you have the Prone condition, you can right yourself with only 5 feet of movement. 

    Jumping. You can make a running Long or High Jump after moving only 5 feet."""


#############################################################################
class Charger(StatIncreaseFeature):
    tag = Feature.CHARGER
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY]
    _desc = """Improved Dash. When you take the Dash action, your Speed increases by 10 feet for that action.

    Charge Attack. If you move at least 10 feet in a straight line toward a target immediately before hitting it 
    with a melee attack roll as part of the Attack action, choose one of the following effects: gain a 1d8 bonus to 
    the attack's damage roll, or push the target up to 10 feet away if it is no more than one size larger than you. 
    You can use this benefit only once on each of your turns."""


#############################################################################
class Chef(StatIncreaseFeature):
    tag = Feature.CHEF
    _valid_stats = [Stat.CONSTITUTION, Stat.WISDOM]

    @property
    def desc(self) -> str:
        return f"""Replenishing Meal. As part of a Short Rest, you can cook special food if you have ingredients and 
        Cook's Utensils on hand. You can prepare enough of this food for {4 + self.owner.proficiency_bonus} creatures. 
        At the end of the Short Rest, any creature who eats the food and spends one or more Hit Dice
        to regain Hit Points regains an extra 1d8 Hit Points.

        Bolstering Treats. With 1 hour of work or when you finish a Long Rest, you can cook
        {self.owner.proficiency_bonus} treats if you have ingredients and Cook's Utensils on hand. These special 
        treats last 8 hours after being made. A creature can use a Bonus Action to eat one of those treats to
        gain {self.owner.proficiency_bonus} Temporary Hit Points."""

    def mod_add_tool_proficiency(self, character: "Character") -> Reason[Tool]:
        return Reason("Chef", cast(Tool, Tool.COOKS_UTENSILS))


#############################################################################
class CrossbowExpert(StatIncreaseFeature):
    tag = Feature.CROSSBOW_EXPERT
    _valid_stats = [Stat.DEXTERITY]

    _desc = """Ignore Loading. You ignore the Loading property of crossbows. If you're holding one of them, you can
    load a piece of ammunition into it even if you lack a free hand.

    Firing in Melee. Being within 5 feet of an enemy doesn't impose Disadvantage on your attack rolls with crossbows.

    Dual Wielding. When you make the extra attack of the Light property, you can add your ability modifier to the 
    damage of the extra attack if that attack is with a crossbow that has the Light property and you aren't already 
    adding that modifier to the damage."""


#############################################################################
class Crusher(StatIncreaseFeature):
    tag = Feature.CRUSHER
    _valid_stats = [Stat.STRENGTH, Stat.CONSTITUTION]

    _desc = """Push. Once per turn, when you hit a creature with an attack that deals Bludgeoning damage, 
    you can move it 5 feet to an unoccupied space if the target is no more than one size larger than you.

    Enhanced Critical. When you score a Critical Hit that deals Bludgeoning damage to a creature, attack rolls 
    against that creature have Advantage until the start of your next turn."""


#############################################################################
class DefensiveDuelist(StatIncreaseFeature):
    tag = Feature.DEFENSIVE_DUELIST
    _valid_stats = [Stat.DEXTERITY]

    @property
    def desc(self) -> str:
        return f"""Parry. If you're holding a Finesse weapon and another creature hits you with a melee attack, 
    you can take a Reaction to add {self.owner.proficiency_bonus} to your Armor Class, potentially causing the 
    attack to miss you. You gain this bonus to your AC against melee attacks until the start of your next turn."""


#############################################################################
class DualWielder(StatIncreaseFeature):
    tag = Feature.DUAL_WIELDER
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY]

    _desc = """Enhanced Dual Wielding. When you take the Attack action on your turn and attack with a weapon that has 
    the Light property, you can make one extra attack as a Bonus Action later on the same turn with a different 
    weapon, which must be a Melee weapon that lacks the Two-Handed property. You don't add your ability modifier to 
    the extra attack's damage unless that modifier is negative.

    Quick Draw. You can draw or stow two weapons that lack the Two-Handed property when you would normally be able to 
    draw or stow only one."""


#############################################################################
class Durable(StatIncreaseFeature):
    tag = Feature.DURABLE
    _valid_stats = [Stat.CONSTITUTION]

    _desc = """Defy Death. You have Advantage on Death Saving Throws.

    Speedy Recovery. As a Bonus Action, you can expend one of your Hit Point Dice, roll the die, and regain a 
    number of Hit Points equal to the roll."""


#############################################################################
class ElementalAdept(StatIncreaseFeature):
    tag = Feature.ELEMENTAL_ADEPT
    _valid_stats = [Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]

    def __init__(self, dmg_type: DamageType, *stats: Stat):
        super().__init__(*stats)
        self._dmg_type = dmg_type
        if dmg_type not in (DamageType.ACID, DamageType.COLD, DamageType.FIRE, DamageType.LIGHTNING, DamageType.THUNDER):
            raise InvalidOption("Elemental Adept - invalid damage type")

    @property
    def desc(self) -> str:
        return f"""Energy Mastery. Spells you cast ignore Resistance to {self._dmg_type.title()} damage. In addition, 
        when you roll damage for a spell you cast that deals {self._dmg_type.title()} damage, you can treat any 1 on a
        damage die as a 2."""


#############################################################################
class FeyTouched(StatIncreaseFeature):
    tag = Feature.FEY_TOUCHED
    _valid_stats = [Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]
    _goes = 1
    recovery = Recovery.LONG_REST

    def __init__(self, spell: Spell, *stats: Stat):
        super().__init__(*stats)
        if not isinstance(spell, Spell):
            raise InvalidOption("FeyTouched needs to specify a spell")
        self._spell = spell

    @property
    def desc(self) -> str:
        return f"""Fey Magic. You can cast 'Misty Step' or '{spell_name(self._spell)}' of these spells without
        expending a spell slot. You can also cast these spells using spell slots you have of the appropriate level.
        The spells' spellcasting ability is {self.stats[0].title()}."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Fey Touched", Spell.MISTY_STEP, self._spell)


#############################################################################
class Grappler(StatIncreaseFeature):
    tag = Feature.GRAPPLER
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY]

    _desc = """Punch and Grab. When you hit a creature with an Unarmed Strike as part of the Attack action on your turn, 
    you can use both the Damage and the Grapple option. You can use this benefit only once per turn.

    Attack Advantage. You have Advantage on attack rolls against a creature Grappled by you.

    Fast Wrestler. Your Speed isn't halved when you move a creature Grappled by you if the creature is your size or 
    smaller."""


#############################################################################
class GreatWeaponMaster(StatIncreaseFeature):
    tag = Feature.GREAT_WEAPON_MASTER
    _valid_stats = [Stat.STRENGTH]

    _desc = """Heavy Weapon Mastery. When you hit a creature with a weapon that has the Heavy property as part of the 
    Attack action on your turn, you can cause the weapon to deal extra damage to the target. The extra damage equals 
    your Proficiency Bonus.

    Hew. Immediately after you score a Critical Hit with a Melee weapon or reduce a creature to O Hit Points with 
    one, you can make one attack with the same weapon as a Bonus Action."""


#############################################################################
class HeavilyArmored(StatIncreaseFeature):
    tag = Feature.HEAVILY_ARMORED
    _valid_stats = [Stat.STRENGTH, Stat.CONSTITUTION]
    hide = True

    _desc = """Armor Training. You gain training with Heavy armor."""

    def mod_armour_proficiency(self, character: "Character") -> Reason[Proficiency]:
        return Reason("Heavily Armored", cast(Proficiency, Proficiency.HEAVY_ARMOUR))


#############################################################################
class HeavyArmorMaster(StatIncreaseFeature):
    tag = Feature.HEAVY_ARMOR_MASTER
    _valid_stats = [Stat.STRENGTH, Stat.CONSTITUTION]

    @property
    def desc(self) -> str:
        return f"""Damage Reduction. When you're hit by an attack while you're wearing Heavy armor, any Bludgeoning,
    Piercing, and Slashing damage dealt to you by that attack is reduced by {self.owner.proficiency_bonus}."""


#############################################################################
class InspiringLeader(StatIncreaseFeature):
    tag = Feature.INSPIRING_LEADER
    _valid_stats = [Stat.WISDOM, Stat.CHARISMA]

    @property
    def desc(self) -> str:
        thp = self.owner.level + self.owner.stats[self.stats[0]].modifier
        return f"""Bolstering Performance. When you finish a Short or Long Rest, you can give an inspiring 
        performance: a speech, song, or dance. When you do so, choose up to six allies (which can include yourself) 
        within 30 feet of yourself who witness the performance. The chosen creatures each gain {thp} Temporary Hit 
        Points."""


#############################################################################
class KeenMind(StatIncreaseFeature):
    tag = Feature.KEEN_MIND
    _valid_stats = [Stat.INTELLIGENCE]

    def __init__(self, skill: Skill, *stats: Stat):
        super().__init__(*stats)
        if skill not in (Skill.ARCANA, Skill.HISTORY, Skill.INVESTIGATION, Skill.NATURE, Skill.RELIGION):
            raise InvalidOption("Keen mind skill not supported")
        self._skill = skill

    _desc = """Quick Study. You can take the Study action as a Bonus Action."""

    # TODO: if you already have proficiency in it, you gain Expertise in it.

    def mod_add_skill_proficiency(self, character: "Character") -> Reason[Skill]:
        return Reason("Keen Mind", self._skill)


#############################################################################
class LightlyArmored(StatIncreaseFeature):
    tag = Feature.LIGHTLY_ARMORED
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY]
    hide = True

    _desc = """Armor Training. You gain training with Light armor and Shields."""

    def mod_armour_proficiency(self, character: "Character") -> Reason[Proficiency]:
        return Reason("Lightly Armored", cast(Proficiency, Proficiency.SHIELDS), cast(Proficiency, Proficiency.LIGHT_ARMOUR))


#############################################################################
class MageSlayer(StatIncreaseFeature):
    tag = Feature.MAGE_SLAYER
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY]
    recovery = Recovery.SHORT_REST
    _goes = 1

    _desc = """Concentration Breaker. When you damage a creature that is concentrating, it has Disadvantage on the 
    saving throw it makes to maintain Concentration.

    Guarded Mind. If you fail an Intelligence, a Wisdom, or a Charisma saving throw, you can cause yourself to 
    succeed instead."""


#############################################################################
class MartialWeaponTraining(StatIncreaseFeature):
    tag = Feature.MARTIAL_WEAPON_TRAINING
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY]
    hide = True

    _desc = """Weapon Proficiency. You gain proficiency with Martial weapons."""

    def mod_weapon_proficiency(self, character: "Character") -> Reason[Proficiency]:
        return Reason("Martial Weapon Training", cast(Proficiency, Proficiency.MARTIAL_WEAPONS))


#############################################################################
class MediumArmorMaster(StatIncreaseFeature):
    tag = Feature.MEDIUM_ARMOR_MASTER
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY]

    _desc = """Dexterous Wearer. While you're wearing Medium armor, you can add 3, rather than 2, to your AC if you 
    have a Dexterity score of 16 or higher."""


#############################################################################
class ModeratelyArmored(StatIncreaseFeature):
    tag = Feature.MODERATELY_ARMORED
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY]
    _desc = """Armor Training. You gain training with Medium armor."""
    hide = True

    def mod_armour_proficiency(self, character: "Character") -> Reason[Proficiency]:
        return Reason("Moderately Armored", cast(Proficiency, Proficiency.MEDIUM_ARMOUR))


#############################################################################
class MountedCombatant(StatIncreaseFeature):
    tag = Feature.MOUNTED_COMBATANT
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY, Stat.WISDOM]

    _desc = """Mounted Strike. While mounted, you have Advantage on attack rolls against any unmounted creature 
    within 5 feet of your mount that is at least one size smaller than the mount.

    Leap Aside. If your mount is subjected to an effect that allows it to make a Dexterity saving throw to take only 
    half damage, it instead takes no damage if it succeeds on the saving throw and only half damage if it fails. 
    For your mount to gain this benefit, you must be riding it, and neither of you can have the Incapacitated condition.

    Veer. While mounted, you can force an attack that hits your mount to hit you instead if you don't have the 
    Incapacitated condition."""


#############################################################################
class Observant(StatIncreaseFeature):
    tag = Feature.OBSERVANT
    _valid_stats = [Stat.INTELLIGENCE, Stat.WISDOM]

    def __init__(self, skill: Skill, *stats: Stat):
        super().__init__(*stats)
        if skill not in (Skill.INSIGHT, Skill.INVESTIGATION, Skill.PERCEPTION):
            raise InvalidOption("Observant skill not supported")
        self._skill = skill

    _desc = """Quick Search. You can take the Search action as a Bonus Action."""

    # TODO if you already have proficiency in it, you gain Expertise in it.

    def mod_add_skill_proficiency(self, character: "Character") -> Reason[Skill]:
        return Reason("Observant", self._skill)


#############################################################################
class Piercer(StatIncreaseFeature):
    tag = Feature.PIERCER
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY]

    _desc = """Puncture. Once per turn, when you hit a creature with an attack that deals Piercing damage, 
    you can reroll one of the attack's damage dice, and you must use the new roll.

    Enhanced Critical. When you score a Critical Hit that deals Piercing damage to a creature, you can roll one 
    additional damage die when determining the extra Piercing damage the target takes."""


#############################################################################
class Poisoner(StatIncreaseFeature):
    tag = Feature.POISONER
    _valid_stats = [Stat.INTELLIGENCE, Stat.DEXTERITY]

    @property
    def desc(self) -> str:
        dc = 8 + self.owner.stats[self.stats[0]].modifier + self.owner.proficiency_bonus
        pb = self.owner.proficiency_bonus
        return f"""Potent Poison. When you make a damage roll that deals Poison damage, it ignores Resistance to 
        Poison damage.

        Brew Poison. With 1 hour of work using a Poisoner's Kit and expending 50 GP worth of materials, 
        you can create {pb} poison doses. As a Bonus Action, you can apply a poison dose to a
        weapon or piece of ammunition. Once applied, the poison retains its potency for 1 minute or until you hit with 
        the poisoned item, whichever is shorter. When a creature takes damage from the poisoned item, that creature must 
        succeed on a Constitution saving throw (DC {dc}) or take 2d8 Poison damage and have the Poisoned
        condition until the end of your next turn."""

    def mod_add_tool_proficiency(self, character: "Character") -> Reason[Tool]:
        return Reason("Poisoner", cast(Tool, Tool.POISONERS_KIT))


#############################################################################
class PolearmMaster(StatIncreaseFeature):
    tag = Feature.POLEARM_MASTER
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY]

    _desc = """Pole Strike. Immediately after you take the Attack action and attack with a Quarterstaff, a Spear, 
    or a weapon that has the Heavy and Reach properties, you can use a Bonus Action to make a melee attack with the 
    opposite end of the weapon. The weapon deals Bludgeoning damage, and the weapon's damage die for this attack is a 
    d4.

    Reactive Strike. While you're holding a Quarterstaff, a Spear, or a weapon that has the Heavy and Reach 
    properties, you can take a Reaction to make one melee attack against a creature that enters the reach you have 
    with that weapon."""


#############################################################################
class Resilient(StatIncreaseFeature):
    tag = Feature.RESILIENT
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY, Stat.CONSTITUTION, Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]

    @property
    def desc(self) -> str:
        return f"""Saving Throw Proficiency. You gain saving throw proficiency with {self.stats[0].title()}."""

    # TODO - add saving throw proficiency


#############################################################################
class RitualCaster(StatIncreaseFeature):
    tag = Feature.RITUAL_CASTER
    _valid_stats = [Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]
    recovery = Recovery.LONG_REST
    _goes = 1

    def __init__(self, *stats: Stat, spells: list[Spell]):
        super().__init__(*stats)
        for spell in spells:
            if SPELL_DETAILS[spell].level != 1:
                raise InvalidOption(f"Ritual Caster: {spell_name(spell)} must be level 1")
            if not SPELL_DETAILS[spell].flags & SpellFlag.RITUAL:
                raise InvalidOption(f"Ritual Caster: {spell_name(spell)}  must be a ritual")
        self._spells = spells

    @property
    def desc(self) -> str:
        spells = ", ".join(f"'{spell_name(_)}'" for _ in self._spells)
        return f"""Ritual Spells. You can cast {spells} with any spell slots you have. The spells' 
    spellcasting ability is {self.stats[0].title()}.

    Quick Ritual. With this benefit, you can cast a Ritual spell that you have prepared using its regular casting 
    time rather than the extended time for a Ritual. Doing so doesn't require a spell slot."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        ans = Reason[Spell]()
        for spell in self._spells:
            ans |= Reason("Ritual Caster", spell)
        return ans


#############################################################################
class Sentinel(StatIncreaseFeature):
    tag = Feature.SENTINEL
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY]
    _desc = """Guardian. Immediately after a creature within 5 feet of you takes the Disengage action or hits a 
    target other than you with an attack, you can make an Opportunity Attack against that creature.

    Halt. When you hit a creature with an Opportunity Attack, the creature's Speed becomes O for the rest of the 
    current turn."""


#############################################################################
class ShadowTouched(StatIncreaseFeature):
    tag = Feature.SHADOW_TOUCHED
    _valid_stats = [Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]
    recovery = Recovery.LONG_REST
    _goes = 1

    def __init__(self, spell: Spell, *stats: Stat):
        super().__init__(*stats)
        self._spell = spell
        if SPELL_DETAILS[spell].school not in (SpellSchool.NECROMANCY, SpellSchool.ILLUSION):
            raise InvalidOption(f"Spell '{spell_name(spell)} must be Necromancy or Illusion, not {SPELL_DETAILS[spell].school}")
        if SPELL_DETAILS[spell].level != 1:
            raise InvalidOption(f"Spell '{spell_name(spell)} must be level 1, not {SPELL_DETAILS[spell].level}")

    @property
    def desc(self) -> str:
        return f"""Shadow Magic. You always have '{spell_name(self._spell)}' and the 'Invisibility' spell prepared. 
        You can cast each of these spells without expending a spell slot. You can also cast these spells using spell 
        slots you have of the appropriate level. The spells' spellcasting ability is {self.stats[0].title()}."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Shadow Touched", Spell.INVISIBILITY, self._spell)


#############################################################################
class Sharpshooter(StatIncreaseFeature):
    tag = Feature.SHARPSHOOTER
    _valid_stats = [Stat.DEXTERITY]
    _desc = """Bypass Cover: Your ranged attacks with weapons ignore Half Cover and Three-Quarters Cover.

    Firing in Melee. Being within S feet of an enemy doesn't impose Disadvantage on your attack rolls with Ranged 
    weapons.

    Long Shots. Attacking at long range doesn't impose Disadvantage on your attack rolls with Ranged weapons."""


#############################################################################
class ShieldMaster(StatIncreaseFeature):
    tag = Feature.SHIELD_MASTER
    _valid_stats = [Stat.STRENGTH]

    _desc = """Shield Bash. If you attack a creature within 5 feet of you as part of the Attack action and hit with a 
    Melee weapon, you can immediately bash the target with your Shield if it's equipped, forcing the target to make a 
    Strength saving throw (DC 8 plus your Strength modifier and Proficiency Bonus). On a failed save, you either push 
    the target 5 feet from you or cause it to have the Prone condition (your choice). You can use this benefit only 
    once on each of your turns.

    Interpose Shield. If you're subjected to an effect that allows you to make a Dexterity saving throw to take only 
    half damage, you can take a Reaction to take no damage if you succeed on the saving throw and are holding a 
    Shield."""


#############################################################################
class SkillExpert(StatIncreaseFeature):
    tag = Feature.SKILL_EXPERT
    hide = True
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY, Stat.CONSTITUTION, Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]
    _desc = """Skill Proficiency. You gain proficiency in one skill of your choice.

    Expertise. Choose one skill in which you have proficiency but lack Expertise. You gain Expertise with that skill."""

    #############################################################################
    def __init__(self, proficient: Skill, expert: Skill, *stats: Stat):
        super().__init__(*stats)
        self.proficient = proficient
        self.expert = expert

    #############################################################################
    def mod_add_skill_expertise(self, character: "Character") -> Reason[Skill]:
        return Reason("Skill Expert", self.expert)

    #############################################################################
    def mod_add_skill_proficiency(self, character: "Character") -> Reason[Skill]:
        return Reason("Skill Expert", self.proficient)


#############################################################################
class Skulker(StatIncreaseFeature):
    tag = Feature.SKULKER
    _valid_stats = [Stat.DEXTERITY]

    _desc = """Fog of War. You exploit the distractions of battle, gaining Advantage on any Dexterity (Stealth) check 
    you make as part of the Hide action during combat. 

    Sniper. If you make an attack roll while hidden and the roll misses, making the attack roll doesn't reveal your 
    location."""

    def mod_add_sense(self, character: "Character") -> Reason[Sense]:
        return Reason("Skulker", cast(Sense, Sense.BLINDSIGHT10))


#############################################################################
class Slasher(StatIncreaseFeature):
    tag = Feature.SLASHER
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY]

    _desc = """Hamstring. Once per turn when you hit a creature with an attack that deals Slashing damage, 
    you can reduce the Speed of that creature by 10 feet until the start of your next turn.

    Enhanced Critical. When you score a Critical Hit that deals Slashing damage to a creature, it has Disadvantage on 
    attack rolls until the start of your next turn."""


#############################################################################
class Speedy(StatIncreaseFeature):
    tag = Feature.SPEEDY
    _valid_stats = [Stat.CONSTITUTION, Stat.DEXTERITY]

    _desc = """Dash over Difficult Terrain. When you take the Dash action on your turn, Difficult Terrain doesn't 
    cost you extra movement for the rest of that turn.

    Agile Movement. Opportunity Attacks have Disadvantage against you."""

    def mod_add_movement_speed(self, character: "Character") -> Reason[int]:
        return Reason("Speedy", 10)


#############################################################################
class SpellSniper(StatIncreaseFeature):
    tag = Feature.SPELL_SNIPER
    _valid_stats = [Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]

    _desc = """Bypass Cover. Your attack rolls for spells ignore Half Cover and Three-Quarters Cover.

    Casting in Melee. Being within 5 feet of an enemy doesn't impose Disadvantage on your attack rolls with spells.

    Increased Range. When you cast a spell that has a range of at least 10 feet and requires you to make an attack 
    roll, you can increase the spell's range by 60 feet."""


#############################################################################
class Telekinetic(StatIncreaseFeature):
    tag = Feature.TELEKINETIC
    _valid_stats = [Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]

    @property
    def desc(self) -> str:
        dc = 8 + self.owner.stats[self.stats[0]].modifier + self.owner.proficiency_bonus
        return f"""Minor Telekinesis. You learn the 'Mage Hand' spell. You can cast it without Verbal or Somatic 
        components, you can make the spectral hand Invisible, and its range increases by 30 feet when you cast it. 
        The spell's spellcasting ability is {self.stats[0].title()}.

        Telekinetic Shove. As a Bonus Action, you can telekinetically shove one creature you can see within 30 feet 
        of yourself. When you do so, the target must succeed on a Strength saving throw (DC {dc}) or be moved 5 feet 
        toward or away from you."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Telekinetic", Spell.MAGE_HAND)


#############################################################################
class Telepathic(StatIncreaseFeature):
    tag = Feature.TELEPATHIC
    _valid_stats = [Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]
    recovery = Recovery.LONG_REST
    _goes = 1

    @property
    def desc(self) -> str:
        return f"""Telepathic Utterance. You can speak telepathically to any creature you can see within 60 feet of 
    yourself. Your telepathic utterances are in a language you know, and the creature understands you only if it 
    knows that language. Your communication doesn't give the creature the ability to respond to you telepathically.

    Detect Thoughts. You can cast it without a spell slot or spell components. You can also cast it using spell slots 
    you have of the appropriate level. Your spellcasting ability for the spell is {self.stats[0].title()}"""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Telepathic", Spell.DETECT_THOUGHTS)


#############################################################################
class WarCaster(StatIncreaseFeature):
    tag = Feature.WAR_CASTER
    _valid_stats = [Stat.INTELLIGENCE, Stat.WISDOM, Stat.CHARISMA]

    _desc = """Concentration. You have Advantage on Constitution saving throws that you make to maintain Concentration.

    Reactive Spell. When a creature provokes an Opportunity Attack from you by leaving your reach, you can take a 
    Reaction to cast a spell at the creature rather than making an Opportunity Attack. The spell must have a casting 
    time of one action and must target only that creature.

    Somatic Components. You can perform the Somatic components of spells even when you have weapons or a Shield in 
    one or both hands."""


#############################################################################
class WeaponMaster(StatIncreaseFeature):
    tag = Feature.WEAPON_MASTER
    _valid_stats = [Stat.STRENGTH, Stat.DEXTERITY]

    _desc = """Mastery Property. Your training with weapons allows you to use the mastery property of one kind of 
    Simple or Martial weapon of your choice, provided you have proficiency with it. Whenever you finish a Long Rest, 
    you can change the kind of weapon to another eligible kind."""


# EOF
