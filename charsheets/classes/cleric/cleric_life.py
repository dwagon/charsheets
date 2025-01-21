from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.cleric import Cleric
from charsheets.constants import Ability
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class ClericLifeDomain(Cleric):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Cleric (Life Domain)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {LifeDomainSpells(), DiscipleOfLife(), PreserveLife()}
        if self.level >= 6:
            abilities |= {BlessedHealer()}
        return abilities


#############################################################################
class LifeDomainSpells(BaseAbility):
    tag = Ability.LIFE_DOMAIN_SPELLS
    _desc = """Your connection to this divine domain ensures you always have certain spells ready. When you reach a
    Cleric level specified in the Life Domain Spells table, you thereafter always have the listed spells prepared."""
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason("Life Domain Spells", Spell.BLESS, Spell.CURE_WOUNDS, Spell.AID, Spell.LESSER_RESTORATION)
        if character.level >= 5:
            spells |= Reason("Life Domain Spells", Spell.MASS_HEALING_WORD, Spell.REVIVIFY)
        if character.level >= 7:
            spells |= Reason("Life Domain Spells", Spell.AURA_OF_LIFE, Spell.DEATH_WARD)
        return spells


#############################################################################
class DiscipleOfLife(BaseAbility):
    tag = Ability.DISCIPLE_OF_LIFE
    _desc = """When a spell you cast with a spell slot restores Hit Points to a creature, that creature regains
    additional Hit Points on the turn you cast the spell. The additional Hit Points equal 2 plus the spell
    slot’s level."""


#############################################################################
class PreserveLife(BaseAbility):
    tag = Ability.PRESERVE_LIFE
    _desc = ""

    @property
    def desc(self) -> str:
        return f"""As a Magic action, you present your Holy Symbol and expend a use of your Channel Divinity to evoke 
        healing energy that can restore {self.owner.level * 5} Hit Points. Choose Bloodied creatures within 30 feet 
        of yourself (which can include you), and divide those Hit Points among them. This feature can
        restore a creature to no more than half its Hit Point maximum."""


#################################################################################
class BlessedHealer(BaseAbility):
    tag = Ability.BLESSED_HEALER
    _desc = """The healing spells you cast on others heal you as well. Immediately after you cast a spell with a spell 
    slot that restores Hit Points to one or more creatures other than yourself, you regain Hit Points equal to 2 plus 
    the spell slot's level."""


# EOF
