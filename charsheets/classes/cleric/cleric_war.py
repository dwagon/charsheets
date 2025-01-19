from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.cleric import Cleric
from charsheets.constants import Ability
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class ClericWarDomain(Cleric):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Cleric (War Domain)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {GuidedStrike(), WarDomainSpells(), WarPriest()}
        abilities |= super().class_abilities()
        if self.level >= 6:
            abilities |= {WarGodsBlessing()}
        return abilities


#################################################################################
class GuidedStrike(BaseAbility):
    tag = Ability.GUIDED_STRIKE
    _desc = """When you or a creature within 30 feet of you misses with an attack roll, you can expend one use of
    your Channel Divinity and give that roll a +10 bonus, potentially causing it to hit. When you use this feature to
    benefit another creature's attack roll, you must take a Reaction to do so"""


#############################################################################
class WarDomainSpells(BaseAbility):
    tag = Ability.WAR_DOMAIN_SPELLS
    _desc = """Your connection to this divine domain ensures you always have certain spells ready. When you reach a
    Cleric level specified in the War Domain Spells table, you thereafter always have the listed spells prepared."""
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason("War Domain Spells", Spell.GUIDING_BOLT, Spell.MAGIC_WEAPON, Spell.SHIELD_OF_FAITH, Spell.SPIRITUAL_WEAPON)
        if character.level >= 5:
            spells |= Reason("War Domain Spells", Spell.CRUSADERS_MANTLE, Spell.SPIRIT_GUARDIANS)
        return spells


#################################################################################
class WarPriest(BaseAbility):
    tag = Ability.WAR_PRIEST
    _desc = ""

    @property
    def goes(self) -> int:
        return max(1, self.owner.wisdom.modifier)

    @property
    def desc(self) -> str:
        return f"""As a Bonus Action, you can make one attack with a weapon or an Unarmed Strike. You can use this
        Bonus Action {self.goes} times. You regain all expended uses when you finish a Short or Long Rest."""


#################################################################################
class WarGodsBlessing(BaseAbility):
    tag = Ability.WAR_GODS_BLESSING
    _desc = """You can expend a use of your Channel Divinity to cast Shield of Faith or Spiritual Weapon rather than 
    expending a spell slot. When you cast either spell in this way, the spell doesn't require Concentration. Instead 
    the spell lasts for 1 minute, but it ends early if you cast that spell again, have the Incapacitate condition, 
    or die."""


# EOF
