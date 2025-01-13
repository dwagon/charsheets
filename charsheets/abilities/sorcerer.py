from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability
from charsheets.reason import Reason
from charsheets.spells import Spells

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class AberrantSorcery(BaseAbility):
    tag = Ability.ABERRANT_SORCERY
    _desc = """An alien influence has wrapped its tendrils around your mind, giving you psionic power. You can now 
    touch other minds with that power and alter the world around you. Will this power shine from you asa hopeful 
    beacon to others? Or will you be a terror to those who feel the stab of your mind? Perhaps a psychic wind 
    from the Astral Plane carried psionic energy to you, or you were exposed to the Far Realm’s warping 
    influence. Alternatively, you were implanted with a mind flayer tadpole, but your transformation into a mind 
    flayer never occurred; now the tadpole’s psionic power is yours. However you acquired this power, your mind is 
    aflame with it"""


#############################################################################
class ClockworkSpells(BaseAbility):
    tag = Ability.CLOCKWORK_SPELLS
    _desc = """Consult the Manifestations of Order table and choose or randomly determine away your 
    connection to order manifests while you are casting any of your Sorcerer spells.

    MANIFESTATIONS OF ORDER
    1d6 Manifestation
    1 Spectral cog wheels hover behind you.
    2 The hands of a clock spin in your eyes.
    3 Your skin glows with a brassy sheen.
    4 Floating equations and geometric objects overlay your body.
    5 Your Spellcasting Focus temporarily takes the form of a tiny clockwork mechanism.
    6 The ticking of gears or ringing of a clock can be heard by you and those affected by your magic."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        spells = Reason[Spells]()
        spells.add("Clockwork Spells", Spells.AID)
        spells.add("Clockwork Spells", Spells.LESSER_RESTORATION)
        spells.add("Clockwork Spells", Spells.PROTECTION_FROM_EVIL_AND_GOOD)
        spells.add("Clockwork Spells", Spells.ALARM)
        if character.level >= 5:
            spells.add("Clockwork Spells", Spells.DISPEL_MAGIC)
            spells.add("Clockwork Spells", Spells.PROTECTION_FROM_ENERGY)

        return spells


#############################################################################
class InnateSorcery(BaseAbility):
    tag = Ability.INNATE_SORCERY
    _desc = """An event in your past left an indelible mark on you, infusing you with simmering magic. As a Bonus 
    Action, you can unleash that magic for 1 minute, during which you gain the following benefits: 
    
    The spell save DC of your Sorcerer spells increases by 1. 
    
    You have Advantage on the attack rolls of Sorcerer spells you cast. 
    
    You can use this feature twice, and you regain all expended uses of it when you finish a Long Rest."""


#############################################################################
class FontOfMagic(BaseAbility):
    tag = Ability.FONT_OF_MAGIC
    _desc = """You can tap into the wellspring of magic within yourself. This wellspring is represented by Sorcery 
    Points, which allow you to create a variety of magical effects."""


#############################################################################
class MetaMagic(BaseAbility):
    tag = Ability.METAMAGIC
    _desc = """Because your magic flows from within, you can alter your spells to suit your needs; you gain two 
    Metamagic options of your choice from “Metamagic Options” later in this class’s description. You use the chosen 
    options to temporarily modify spells you cast. To use an option, you must spend the number of Sorcery Points that 
    it costs.
    
    You can use only one Metamagic option on a spell when you cast it unless otherwise noted in one of those options.

    Whenever you gain a Sorcerer level, you can replace one of your Metamagic options with one you don’t know. You 
    gain two more options at Sorcerer level 10 and two more at Sorceror level 17"""


#############################################################################
class SorcerousRestoration(BaseAbility):
    tag = Ability.SORCEROUS_RESTORATION
    _desc = """When you finish a Short Rest, you can regain expended Sorcery Points, but no more than a number equal 
    to half your Sorcerer level (round down). Once you use this feature, you can’t do so again until you finish a 
    Long Rest."""


#############################################################################
class RestoreBalance(BaseAbility):
    tag = Ability.RESTORE_BALANCE
    _desc = """Your connection to the plane of absolute order allows you to equalize chaotic moments. When a creature 
    you can see within 60 feet of yourself is about to roll a d20 with Advantage or Disadvantage, you can take a 
    Reaction to prevent the roll from being affected by Advantage and Disadvantage.

    You can use this feature a number of times equal to your Charisma modifier (minimum of once), and you regain all 
    expended uses when you finish a Long Rest."""


#############################################################################
class DraconicResilience(BaseAbility):
    tag = Ability.DRACONIC_RESILIENCE
    _desc = """The magic in your body manifests physical traits of your draconic gift. Your Hit Point maximum 
    increases by 3, and it increases by 1 whenever you gain another Sorcerer level. Parts of you are also covered by 
    dragon-like scales. While you aren’t wearing armor, your base Armor Class equals 10 plus your Dexterity and 
    Charisma modifiers."""


#############################################################################
class WildMagicSurge(BaseAbility):
    tag = Ability.WILD_MAGIC_SURGE
    _desc = """Your spellcasting can unleash surges of untamed magic. Once per turn, you can roll 1d20 immediately 
    after you cast a Sorceror spell with a spell slot. If you roll a 20, roll on the Wild Magic Surge table to create 
    a magical effect. If the magical effect is a spell, it is too wild to be affected by your Metamagic."""


#############################################################################
class TidesOfChaos(BaseAbility):
    tag = Ability.TIDES_OF_CHAOS
    _desc = """You can manipulate chaos itself to give yourself Advantage on one D20 Test before you roll the d20. 
    Once you do so, you must cast a Sorcerer spell with a spell slot or finish a Long Rest before you can use 
    this feature again. If you do cast a Sorcerer spell with a spell slot before you finish a Long Rest, 
    you automatically roll on the Wild Magic Surge table."""


#############################################################################
class TelepathicSpeech(BaseAbility):
    tag = Ability.TELEPATHIC_SPEECH
    _desc = """You can form a telepathic connection between your mind and the mind of another. As a Bonus Action, 
    choose one creature you can see within 30 feet of yourself. You and the chosen creature can communicate 
    telepathic with each other while the two of you are within a number of miles of each other equal to your Charisma 
    modifier (minimum of 1 mile). To understand each other, you each must mentally use a language the other knows. 
    
    The telepathic connection lasts for a number of minutes equal to your Sorcerer level. It ends early if you use 
    this ability to form a connection with a different creature."""


#############################################################################
class BendLuck(BaseAbility):
    tag = Ability.BEND_LUCK
    _desc = """You have the ability to twist fate using your wild magic. Immediately after another creature you can 
    see rolls the d20 for a D20 Test, you can take a Reaction and spend 1 Sorcery Point to roll 1d4 and apply the 
    number rolled as a bonus or penalty (your choice) to the d20 roll."""


#############################################################################
class ElementalAffinity(BaseAbility):
    tag = Ability.ELEMENTAL_AFFINITY
    _desc = """Your draconic magic has an affinity with a damage type associated with dragons. Choose one of those 
    types: Acid, Cold, Fire, Lightning or Poison.
    
    You have Resistance to that damage typem and when you cast a spell that deals damage of that type you can add 
    your Charisma modifier to one damage roll of that spell."""


#############################################################################
class BastionOfLaw(BaseAbility):
    tag = Ability.BASTION_OF_LAW
    _desc = """You can tap into the grand equation of existence to imbue a creature with a shimmering shield of 
    order. As a Magic action, you can expend 1 to 5 Sorcery Points to create a magical ward around yourself or 
    another creature you can see within 30 feet of yourself. The ward is represented by a number of d8s equal to the 
    number of Sorcery Points spent to create it. When the warded creature takes damage, it can expend a number of 
    those dice, roll them, and reduce the damage taken by the total rolled on those dice.
    
    The ward lasts until you finish a Long Rest or until you use this feature again."""


#############################################################################
class PsionicSorcery(BaseAbility):
    tag = Ability.PSIONIC_SORCERY
    _desc = """When you cast any level 1+ spell from your Psionic Spells feature, you can cast it by expending a 
    spell slot as normal or by spending a number of Sorcery Points equal to the spell's level. If you cast the spell 
    using Sorcery Points, it requires no Verbal or Somatic components, and it requires no Material components unless 
    they are consumed by the spell or have a cost specified in it."""


#############################################################################
class PsychicDefenses(BaseAbility):
    tag = Ability.PSYCHIC_DEFENSES
    _desc = """You have Resistance to Psychic damage, and you have Advantage on saving throws to avoid or end the 
    Charmed or Frightened condition."""


# EOF
