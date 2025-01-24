from enum import StrEnum, auto


#############################################################################
class MetamagicNames(StrEnum):
    CAREFUL_SPELL = auto()
    DISTANT_SPELL = auto()
    EMPOWERED_SPELL = auto()
    EXTENDED_SPELL = auto()
    HEIGHTENED_SPELL = auto()
    NONE = auto()
    QUICKENED_SPELL = auto()
    SEEKING_SPELL = auto()
    SUBTLE_SPELL = auto()
    TRANSMUTED_SPELL = auto()
    TWINNED_SPELL = auto()


#############################################################################
class BaseMetamagic:
    _desc = "Unspecified"
    cost = 1
    tag: MetamagicNames = MetamagicNames.NONE

    @property
    def desc(self):
        return self._desc


#############################################################################
class CarefulSpell(BaseMetamagic):
    tag = MetamagicNames.CAREFUL_SPELL
    _desc = """When you cast a spell that forces other creatures to make a saving throw, you can protect some of 
    those creatures from the spell’s full force. To do so, spend 1 Sorcery Point and choose a number of those 
    creatures up to your Charisma modifier (minimum of one creature). A chosen creature automatically succeeds on its 
    saving throw against the spell, and it takes no damage if it would normally take half damage on a successful 
    save."""


#############################################################################
class DistantSpell(BaseMetamagic):
    tag = MetamagicNames.DISTANT_SPELL
    _desc = """When you cast a spell that has a range of at least 5 feet, you can spend 1 Sorcery Point to double the 
    spell’s range. Or when you cast a spell that has a range of Touch, you can spend 1 Sorcery Point to make the 
    spell’s range 30 feet."""


#############################################################################
class EmpoweredSpell(BaseMetamagic):
    tag = MetamagicNames.EMPOWERED_SPELL
    _desc = """When you roll damage for a spell, you can spend 1 Sorcery Point to reroll a number of the damage dice 
    up to your Charisma modifier (minimum of one), and you must use the new rolls.

    You can use Empowered Spell even if you’ve already used a different Metamagic option during the casting of the 
    spell."""


#############################################################################
class ExtendedSpell(BaseMetamagic):
    tag = MetamagicNames.EXTENDED_SPELL
    _desc = """When you cast a spell that has a duration of 1 minute or longer, you can spend 1 Sorcery Point to 
    double its duration to a maximum duration of 24 hours.

    If the affected spell requires Concentration, you have Advantage on any saving throw you make to maintain that 
    Concentration."""


#############################################################################
class HeightenedSpell(BaseMetamagic):
    tag = MetamagicNames.HEIGHTENED_SPELL
    cost = 2
    _desc = """When you cast a spell that forces a creature to make a saving throw, you can spend 2 Sorcery Points to 
    give one target of the spell Disadvantage on saves against the spell."""


#############################################################################
class QuickenedSpell(BaseMetamagic):
    tag = MetamagicNames.QUICKENED_SPELL
    cost = 2
    _desc = """When you cast a spell that has a casting time of an action, you can spend 2 Sorcery Points to change 
    the casting time to a Bonus Action for this casting. You can’t modify a spell in this way if you’ve already cast 
    a level 1+ spell on the current turn, nor can you cast a level 1+ spell on this turn after modifying a spell in 
    this way."""


#############################################################################
class SeekingSpell(BaseMetamagic):
    tag = MetamagicNames.SEEKING_SPELL
    _desc = """If you make an attack roll for a spell and miss, you can spend 1 Sorcery Point to reroll the d20, 
    and you must use the new roll.

    You can use Seeking Spell even if you’ve already used a different Metamagic option during the casting of the 
    spell."""


#############################################################################
class SubtleSpell(BaseMetamagic):
    tag = MetamagicNames.SUBTLE_SPELL
    _desc = """When you cast a spell, you can spend 1 Sorcery Point to cast it without any Verbal, Somatic, 
    or Material components, except Material components that are consumed by the spell or that have a cost specified 
    in the spell."""


#############################################################################
class TransmutedSpell(BaseMetamagic):
    tag = MetamagicNames.TRANSMUTED_SPELL
    _desc = """When you cast a spell that deals a type of damage from the following list, you can spend 1 Sorcery 
    Point to change that damage type to one of the other listed types: Acid, Cold, Fire, Lightning, Poison, Thunder."""


#############################################################################
class TwinnedSpell(BaseMetamagic):
    tag = MetamagicNames.TWINNED_SPELL
    _desc = """When you cast a spell, such as Charm Person, that can be cast with a higher-level spell slot to target 
    an additional creature, you can spend 1 Sorcery Point to increase the spell’s effective level by 1."""


# EOF
