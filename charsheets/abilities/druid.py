from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability, Proficiency
from charsheets.reason import Reason
from charsheets.spells import Spells

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Druidic(BaseAbility):
    tag = Ability.DRUIDIC
    _desc = """You know Druidic, the secret language of Druids."""


#############################################################################
class WildShape(BaseAbility):
    tag = Ability.WILD_SHAPE
    _desc = """The power of nature allows you to assume the form of an animal.
    As a Bonus Action, you shape-shift into a Beast form that you have learned for this feature."""


#############################################################################
class WildCompanion(BaseAbility):
    tag = Ability.WILD_COMPANION
    _desc = """You can summon a nature spirit that assumes an animal form to aid you. As a Magic action,
    you can expend a spell slot or a use of Wild Shape to cast the Find Familiar spell without Material components.
    When you cast the spell in this way, the familiar is Fey and disappears when you finish a long rest."""


#############################################################################
class LandsAid(BaseAbility):
    tag = Ability.LANDS_AID
    _desc = """As a Magic action, you can expend a use of your Wild Shape a choose a point within 60 feet of yourself.
    Vitality-giving flowers and life-draining thorns appear for a moment in a 10-foot-radius Sphere centered on
    that point. Each creature of your choice in the Sphere must make a Constitution saving throw against your
    spell save DC, taking 2d6 Necrotic damage on a failed save or half as much damage on a successful one. One
    creature of your choice in that area regains 2d6 Hit Points."""


#############################################################################
class LandSpellArid(BaseAbility):
    tag = Ability.LAND_SPELL_ARID
    _desc = """ Blur, Burning Hands, Fire Bolt"""


#############################################################################
class LandSpellPolar(BaseAbility):
    tag = Ability.LAND_SPELL_POLAR
    _desc = """ Fog Cloud, Hold Person, Ray of Frost"""


#############################################################################
class LandSpellTropical(BaseAbility):
    tag = Ability.LAND_SPELL_TROPICAL
    _desc = """ Acid Splash, Ray of Sickness, Web"""


#############################################################################
class LandSpellTemperate(BaseAbility):
    tag = Ability.LAND_SPELL_TEMPERATE
    _desc = """ Misty Step, Shocking Grasp, Sleep"""


#############################################################################
class CircleForms(BaseAbility):
    tag = Ability.CIRCLE_FORMS
    _desc = """ You can channel lunar magic when you assume a Wild Shape form, granting you the benefits below.
    
    Challenge Rating. The maximum Challenge Rating for the form equals your Druid level divided by 3 (round down).
    
    Armor Class. Until you leave the form, your AC equals 13 plus your Wisdom modifier if that total is higher than
    the Beast's AC.
    
    Temporary Hit Points. You gain a number of Temporary Hit Points equal to three times your Druid level."""


#############################################################################
class WrathOfTheSea(BaseAbility):
    tag = Ability.WRATH_OF_THE_SEA
    _desc = """ As a Bonus Action, you can expend a use of your Wild Shape to manifest a 5-foot Emanation that takes
    the form of ocean spray that surrounds you for 10 minutes. It ends early if you dismiss it (no action required),
    manifest it again, or have the Incapacitated condition.
    
    When you manifest the Emanation and as a Bonus Action on your subsequent turns, you can choose another
    creature you can see in the Emanation. The target must succeed on a Constitution saving throw against your
    spell save DC or take Cold damage and, if the creature is Large or smaller, be pushed up to 15 feet away from you.
    To determine this damage, roll a number of d6s equal to your Wisdom modifier (minimum of one die)."""


#############################################################################
class StarMap(BaseAbility):
    tag = Ability.STAR_MAP
    _desc = """You've created a star chart as part of your heavenly studies.
    
    While holding the map, you have the Guidance and Guiding Blot spells prepared, and you can Guiding Bolt without
    expending a spell slot. You can cast it in that way a number of times equal to your Wisdom modifier (minumum of
    once) and you regain all expended uses when you finish a Long Rest."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        return Reason("Star Map", Spells.GUIDANCE, Spells.GUIDING_BOLT)


#############################################################################
class StarryForm(BaseAbility):
    tag = Ability.STARRY_FORM
    _desc = """As a Bonus Action you cn expend a use of your 
    Wild Shape feature to take on a starry form rather than shape-shifting.
    
    While in your starry form, you retain your game statistics, but your body becomes luminous, your joints glimmer
    like stars, and glowing lines connect them as on a star chart. This form sheds Bright Light in a 10-foot radius
    and Dim Light for additional 10 feet. The form lasts for 10 minutes. It ends early if you dismiss it
    (no action required), have the Incapacitated condition, or use this feature again.
    
    Whenever you assume your starry form, choose which of the following constellations glimmers on your body;
    your choice gives you certain benefits while in the form.
    
    Archer. A constellation of an archer appears on you. When you activate this form and as a Bonus Action on your
    subsequent turns while it lasts, you can make a ranged spell attack, hurling a luminous arrow that targets one 
    creature within 60 feet of yourself. On a hit, the attack deals Radiant damage equal to 1d8 plus your Wisdom
    modifier.
    
    Chalice. A constellation of a life-giving goblet appears on you. Whenever you cast a spell using a spell slot that
    restores Hit Points to a creature, you or another creature within 30 feet of you can regain Hit Points equal to 
    1d8 plus your Wisdom modifier.
    
    Dragon. A constellation of a wise dragon appears on you. When you make an Intelligence or a Wisdom check or a
    Constitution saving throw to maintain Concentration, you can treat a roll of 9 or lower on the d20 as a 10.
    """


#################################################################################
class Magician(BaseAbility):
    tag = Ability.MAGICIAN
    _desc = """You know one extra cantrip from the Druid spell list. In addition, your mystical connection to nature gives
    you a bonus to your Intelligence (Arcana or Nature) checks.
    The bonus equals your Wisdom modifier (minimum bonus of +1)"""

    def mod_skill_arcana(self, character: "Character") -> Reason:
        return Reason("Magician", max(1, character.wisdom.modifier))

    def mod_skill_nature(self, character: "Character") -> Reason:
        return Reason("Magician", max(1, character.wisdom.modifier))


#################################################################################
class Warden(BaseAbility):
    tag = Ability.WARDEN
    _desc = """Trained for battle, you gain proficiency with Martial weapons and training with Medium armour"""

    #############################################################################
    def mod_weapon_proficiency(self, character: "Character") -> Reason[Proficiency]:
        return Reason("Warden", Proficiency.MARTIAL_WEAPONS)

    #############################################################################
    def mod_armour_proficiency(self, character: "Character") -> Reason[Proficiency]:
        return Reason("Warden", Proficiency.MEDIUM_ARMOUR)


# EOF
