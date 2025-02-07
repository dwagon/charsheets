from typing import Optional, cast

from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill, Feature, Armour, Recovery
from charsheets.features import ExtraAttack, Evasion
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason


#################################################################################
class Monk(Character):
    _base_skill_proficiencies = {
        Skill.ACROBATICS,
        Skill.ATHLETICS,
        Skill.HISTORY,
        Skill.INSIGHT,
        Skill.RELIGION,
        Skill.STEALTH,
    }

    #############################################################################
    @property
    def hit_dice(self) -> int:
        return 8

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return None

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason("Monk", cast(Proficiency, Proficiency.SIMPLE_WEAPONS), cast(Proficiency, Proficiency.MARTIAL_WEAPONS))

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason()

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.STRENGTH, Stat.DEXTERITY)

    #############################################################################
    @property
    def class_special(self) -> str:
        return f"""Focus Points: {self.focus_points}

        Martial Arts Die: 1{self.martial_arts_die}"""

    #############################################################################
    @property
    def focus_points(self) -> int:
        return self.level if self.level >= 2 else 0

    #############################################################################
    @property
    def martial_arts_die(self) -> str:
        if self.level >= 17:
            return "d12"
        elif self.level >= 11:
            return "d10"
        elif self.level >= 5:
            return "d8"
        return "d6"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {UnarmoredDefenseMonk(), MartialArts()}

        if self.level >= 2:
            abilities.add(MonksFocus())
            abilities.add(UnarmoredMovement())
            abilities.add(UncannyMetabolism())
        if self.level >= 3:
            abilities.add(DeflectAttacks())
        if self.level >= 4:
            abilities.add(SlowFall())
        if self.level >= 5:
            abilities.add(ExtraAttack())
            abilities.add(StunningStrike())
        if self.level >= 6:
            abilities.add(EmpoweredStrikes())
        if self.level >= 7:
            abilities.add(Evasion())
        if self.level >= 9:
            abilities.add(AcrobaticMovement())
        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return 0

    #############################################################################
    def max_spell_level(self) -> int:
        return 0

    #############################################################################
    @property
    def monk_dc(self) -> int:
        return 8 + self.wisdom.modifier + self.proficiency_bonus


#############################################################################
class MartialArts(BaseFeature):
    tag = Feature.MARTIAL_ARTS

    @property
    def desc(self) -> str:
        return f"""Your practice of martial arts gives you mastery of combat styles that use your Unarmed Strike and
        Monk weapons, which are the following: Simple Melee weapons and Martial Melee weapons that have the
        Light property.

        You gain the following benefits while you are unarmed or wielding only Monk weapons and you aren't wearing armor
        or wielding a Shield.

        Bonus Unarmed Strike. You can make an Unarmed Strike as a Bonus Action.

        Martial Arts Die. You can roll 1{self.owner.martial_arts_die} in place of the normal damage of your
        Unarmed Strike or Monk weapons.

        Dexterous Attacks. You can use your Dexterity modifier ({self.owner.dexterity.modifier}) instead of your
        Strength modifier ({self.owner.strength.modifier}) for the attack and damage rolls of your Unarmed Strike
        and Monk weapons. In addition, when you use the Grapple or Shove option of your Unarmed Strike, you can use
        your Dexterity modifier ({self.owner.dexterity.modifier}) instead of your Strength modifier
        ({self.owner.strength.modifier}) to determine the save DC"""


#############################################################################
class UnarmoredDefenseMonk(BaseFeature):
    tag = cast(Feature, Feature.UNARMORED_DEFENSE_MONK)
    hide = True

    @property
    def desc(self) -> str:
        ac = 10 + self.owner.dexterity.modifier + self.owner.wisdom.modifier
        return f"""While you aren't wearing Armor or wielding a Shield, your base Armor Class equals {ac}"""

    def mod_ac_bonus(self, character: "Character") -> Reason[int]:
        if self.owner.shield or self.owner.armour.tag != Armour.NONE:
            return Reason("", 0)
        ac = self.owner.wisdom.modifier
        return Reason("Unarmored Defense", ac)


#############################################################################
class MonksFocus(BaseFeature):
    tag = Feature.MONKS_FOCUS
    recovery = Recovery.SHORT_REST

    @property
    def desc(self) -> str:
        return """"Flurry of Blows. You can expend 1 Focus Point to make two Unarmed Strikes as a Bonus Action.

        Patient Defense. You can take the Disengage action as a Bonus Action. Alternatively, you can expend
        1 Focus Point to take both the Disengage and the Dodge actions as a Bonus Action.

        Step of the Wind. You can take the Dash action as a Bonus Action. Alternatively, you can expend 1 Focus Point to
        take both the Disengage and Dash actions as a Bonus Action, and your jump distance is doubled for the turn."""

    @property
    def goes(self) -> int:
        return self.owner.focus_points


#############################################################################
class UnarmoredMovement(BaseFeature):
    tag = Feature.UNARMORED_MOVEMENT
    hide = True

    @property
    def desc(self) -> str:
        return """Your speed increases while you aren't wearing armor or wielding a Shield. """

    def mod_add_movement_speed(self, character: "Character") -> Reason[int]:
        if self.owner.shield or self.owner.armour.tag != Armour.NONE:
            return Reason("", 0)
        if self.owner.level >= 18:
            speed = 30
        elif self.owner.level >= 14:
            speed = 25
        elif self.owner.level >= 10:
            speed = 20
        elif self.owner.level >= 6:
            speed = 15
        else:
            speed = 10
        return Reason("Unarmored Movement", speed)


#############################################################################
class UncannyMetabolism(BaseFeature):
    tag = Feature.UNCANNY_METABOLISM
    goes = 1
    recovery = Recovery.LONG_REST

    @property
    def desc(self) -> str:
        return f"""When you roll Initiative, you can regain all expended Focus Points.
        Regain 1{self.owner.martial_arts_die} + {self.owner.level} HP."""


#############################################################################
class DeflectAttacks(BaseFeature):
    tag = Feature.DEFLECT_ATTACKS

    @property
    def desc(self) -> str:
        return f"""When an attack roll hits you and its damage includes Bludgeoning, Piercing,or Slashing damage,
    you can take a Reaction to reduce the attack’s total damage against you. The reduction equals 1d10 plus
    {self.owner.dexterity.modifier + self.owner.level}.

    If you reduce the damage to 0, you can expend 1 Focus Point to redirect some of the attack’s force. If you do so,
    choose a creature you can see within 5 feet of yourself if the attack was a melee attack or a creature you can
    see within 60 feet of yourself that isn’t behind Total Cover if the attack was a ranged attack. That creature
    must succeed on a Dexterity saving throw or take damage equal to 2{self.owner.martial_arts_die} +
    {self.owner.dexterity.modifier}. The damage is the same type dealt by the attack."""


#############################################################################
class SlowFall(BaseFeature):
    tag = Feature.SLOW_FALL

    @property
    def desc(self) -> str:
        reduce = self.owner.level * 5
        return f"""You can take a Reaction when you fall to reduce any damage you take from the fall by {reduce} HP."""


#############################################################################
class StunningStrike(BaseFeature):
    tag = Feature.STUNNING_STRIKE

    @property
    def desc(self) -> str:
        return f"""Once per turn when you hit a creature with a Monk weapon or an Unarmed Strike, you can expend 1
        Focus Point to attempt a stunning strike. The target must make a Constitution saving throw (DC
        {self.owner.monk_dc}).
        On a failed save, the target has the Stunned condition until the start of your next turn. On a successful save,
        the target’s Speed
        is halved until the start of your next turn, and the next attack roll made against the target before then has
        Advantage."""


#############################################################################
class EmpoweredStrikes(BaseFeature):
    tag = Feature.EMPOWERED_STRIKES
    _desc = """Whenever you deal damage with your Unarmed Strike, it can deal your choice of Force damage or its
    normal damage type."""


#############################################################################
class AcrobaticMovement(BaseFeature):
    tag = Feature.ACROBATIC_MOVEMENT
    _desc = """While you aren’t wearing armor or wielding a Shield, you gain the ability to move along vertical
        surfaces and across liquids on your turn without falling during the movement."""


# EOF
