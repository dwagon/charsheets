from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability
from charsheets.reason import Reason
from charsheets.spells import Spells

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class MartialArts(BaseAbility):
    tag = Ability.MARTIAL_ARTS
    _desc = """Your practice of martial arts gives you mastery of combat styles that use your Unarmed Strike and Monk 
    weapons, which are the following: Simple Melee weapons and Martial Melee weapons that have the Light property

    You gain the following benefits while you are unarmed or wielding only Monk weapons and you aren't wearing armor 
    or wielding a Shield.

    Bonus Unarmed Strike. You can make an Unarmed Strike as a Bonus Action. 
    
    Martial Arts Die.You can roll 1d6 in place of the normal damage of your Unarmed Strike or Monk weapons. This die 
    changes as you gain Monk levels, as shown in the Martial Arts column of the Monk Features table.

    Dexterous Attacks. You can use your Dexterity modifier instead of your Strength modifier for the attack and 
    damage rolls of your Unarmed Strikes and Monk weapons. In addition,when you use the Grapple or Shove option of 
    your Unarmed Strike, you can use your Dexterity modifier instead of your Strength modifier to determine the save 
    DC"""


#############################################################################
class UnarmoredDefenseMonk(BaseAbility):
    tag = Ability.UNARMORED_DEFENSE_MONK
    _desc = """While you aren't wearing Armor or wielding a Shield, your base Armor Class equals 10 plus your 
    Dexterity and Wisdom modifiers."""


#############################################################################
class MonksFocus(BaseAbility):
    tag = Ability.MONKS_FOCUS
    _desc = """Your focus and martial training allow you to harness a well of extraordinary energy within yourself. 
    This energy is represented by Focus Points. Your Monk level determines the number of points you have, as shown in 
    the Focus Points column of the Monk Features table.
    
    You can expend these points to enhance or fuel certain Monk features. You start knowing three such features: 
    Flurry of Blows,Patient Defense, and Step of the Wind, each of which is detailed below.
    
    When you expend a Focus Point, it is unavailable until you finish a Short or Long Rest, at the end of which you 
    regain all your expended points.
    
    Some features that use Focus Points require your target to make a saving throw. The save DC equals 8 plus your 
    Wisdom modifier and Proficiency Bonus.
    
    Flurry of Blows. You can expend 1 Focus Point to make two Unarmed Strikes as a Bonus Action.
    
    PatientDefense. You can take the Disengage action as a Bonus Action. Alternatively, you can expend 1Focus Point 
    to take both the Disengage and the Dodge actions as a Bonus Action.
    
    Step of the Wind. You can take the Dash action as a Bonus Action. Alternatively, you can expend 1 Focus Point to 
    take both the Disengage and Dash actions asa Bonus Action, and your jump distance"""


#############################################################################
class UnarmoredMovement(BaseAbility):
    tag = Ability.UNARMORED_MOVEMENT
    _desc = """Your speed increases by 10 feet while you aren't wearing armor or wielding a Shield. This bonus 
    increases when you reach certain Monk levels, as shown on the Monk Features table."""


#############################################################################
class UncannyMetabolism(BaseAbility):
    tag = Ability.UNCANNY_METABOLISM
    _desc = """When you roll Initiative, you can regain all expended Focus Points. When you do so, roll your 
    Martial Arts die, and regain a number of Hit Points equal to your Monk level plus the number rolled. Once you use 
    this feature, you can’t use it again until you finish a Long Rest."""


#############################################################################
class DeflectAttacks(BaseAbility):
    tag = Ability.DEFLECT_ATTACKS
    _desc = """When an attack roll hits you and its damage includes Bludgeoning, Piercing,or Slashing damage, 
    you can take a Reaction to reduce the attack’s total damage against you. The reduction equals 1d10 plus your 
    Dexterity modifier and Monk level.
     
    If you reduce the damage to 0, you can expend 1 Focus Point to redirect some of the attack’s force. If you do so, 
    choose a creature you can see within 5 feet of yourself if the attack was a melee attack or a creature you can 
    see within 60 feet of yourself that isn’t behind Total Cover if the attack was a ranged attack. That creature 
    must succeed on a Dexterity saving throw or take damage equal to two rolls of your Martial Arts die plus your 
    Dexterity modifier. The damage is the same type dealt by the attack."""


#############################################################################
class SlowFall(BaseAbility):
    tag = Ability.SLOW_FALL
    _desc = """You can take a Reaction when you fall to reduce any damage you take from the fall by an amount equal 
    to five times your Monk level."""


#############################################################################
class StunningStrike(BaseAbility):
    tag = Ability.STUNNING_STRIKE
    _desc = """Once per turn when you hit a creature with a Monk weapon or an Unarmed Strike, you can expend 1 Focus 
    Point to attempt a stunning strike. The target must make a Constitution saving throw. On a failed save, 
    the target has the Stunned condition until the start of your next turn. On a successful save, the target’s Speed 
    is halved until the start of your next turn, and the next attack roll made against the target before then has 
    Advantage."""


#############################################################################
class HandOfHarm(BaseAbility):
    tag = Ability.HAND_OF_HARM
    _desc = """Once per turn when you hit a creature with an Unarmed Strike and deal damage, you can expend 1 Focus 
    Point to deal extra Necrotic damage equal to one roll of your Martial Arts die plus your Wisdom modifier."""


#############################################################################
class HandOfHealing(BaseAbility):
    tag = Ability.HAND_OF_HEALING
    _desc = """As a Magic action, you can expend 1 Focus Point to touch a creature and restore a number of Hit Points 
    equal to a roll of your Martial Arts die plus your Wisdom modifier. When you use your Flurry of Blows, 
    you can replace one of the Unarmed Strikes with a use of this feature without expending a Focus Point for the 
    healing."""


#############################################################################
class ImplementsOfMercy(BaseAbility):
    tag = Ability.IMPLEMENTS_OF_MERCY
    _desc = """You gain proficiency in the Insight and Medicine skills and proficiency with the Herbalism Kit."""


#############################################################################
class ShadowArts(BaseAbility):
    tag = Ability.SHADOW_ARTS
    _desc = """You have learned to draw on the power of the Shadowfell, gaining the following benefits. 
    
    Darkness.You 
    can expend 1 Focus Point to cast the Darkness spell without spell components. You can see within the spell’s area 
    when you cast it with this feature. While the spell persists, you can move its area of Darkness to a space within 
    60 feet of yourself at the start of each of your turns. 
    
    Darkvision. You gain Darkvision with a range of 60 feet. If you already have Darkvision, its range increases by 
    60 feet.
    
    Shadowy Figments. You know the Minor Illusion spell. Wisdom is your spellcasting ability for it."""


#############################################################################
class ElementalAttunement(BaseAbility):
    tag = Ability.ELEMENTAL_ATTUNEMENT
    _desc = """At the start of your turn, you can expend 1 Focus Point to imbue yourself with elemental energy. The 
    energy lasts for 10 minutes or until you have the Incapacitated condition. You gain the following benefits 
    while this feature is active. 
    
    Reach. When you make an Unarmed Strike, your reach is 10 feet greater than normal, as elemental energy extends 
    from you.
    
    Elemental Strikes. Whenever you hit with your Unarmed Strike, you can cause it to deal your choice of Acid, Cold, 
    Fire, Lightning, or Thunder damage rather than its normal damage type. When you deal one of these types with it, 
    you can also force the target to make a Strength saving throw. On a failed save, you can move the target up to 10 
    feet toward or away from you, as elemental energy swirls around it."""


#############################################################################
class ManipulateElements(BaseAbility):
    tag = Ability.MANIPULATE_ELEMENTS
    _desc = """You know the Elementalism spell. Wisdom is your spellcasting ability for it."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        return Reason("Manipulate Elements", Spells.ELEMENTALISM)


#############################################################################
class OpenHandTechnique(BaseAbility):
    tag = Ability.OPEN_HAND_TECHNIQUE
    _desc = """Whenever you hit a creature with an attack granted by your Flurry of Blows, you can impose one of the 
    following effects on that target. 
    
    Addle. The target can’t make Opportunity Attacks until the start of its next turn. 
    
    Push. The target must succeed on a Strength saving throw or be pushed up to 15 feet away from you. 
    
    Topple. The target must succeed on a Dexterity saving throw or have the Prone condition."""


# EOF
