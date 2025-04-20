from typing import TYPE_CHECKING, cast, Any

from aenum import extend_enum

from charsheets.classes.sorcerer import Sorcerer
from charsheets.constants import Feature, Armour, DamageType
from charsheets.exception import InvalidOption, NotDefined
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


extend_enum(Feature, "DRACONIC_RESILIENCE", "Draconic Resilience")
extend_enum(Feature, "DRACONIC_SPELLS", "Draconic Spells")
extend_enum(Feature, "ELEMENTAL_AFFINITY", "Elemental Affinity")
extend_enum(Feature, "DRAGON_WINGS", "Dragon Wings")
extend_enum(Feature, "DRAGON_COMPANION", "Dragon Companion")


#################################################################################
class SorcererDraconic(Sorcerer):
    _class_name = "Draconic Sorcerer"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(DraconicResilience())
        self.add_feature(DraconicSpells())

    #############################################################################
    def level6(self, **kwargs: Any):
        if "feat" not in kwargs or not isinstance(kwargs["feat"], ElementalAffinity):
            raise NotDefined("Draconic Sorcerors need to have Elemental Affinity at level 6. 'feat=ElementalAffinity(...)'")

    #############################################################################
    def level14(self, **kwargs: Any):
        self.add_feature(DragonWings())

    #############################################################################
    def level18(self, **kwargs: Any):
        self.add_feature(DragonCompanion())


#############################################################################
class DraconicSpells(BaseFeature):
    tag = Feature.DRACONIC_SPELLS
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason("Oath of Devotion", Spell.ALTER_SELF, Spell.CHROMATIC_ORB, Spell.COMMAND)
        if character.level >= 5:
            spells |= Reason("Oath of Devotion", Spell.FEAR, Spell.FLY)
        if character.level >= 7:
            spells |= Reason("Oath of Devotion", Spell.ARCANE_EYE, Spell.CHARM_MONSTER)
        if character.level >= 9:
            spells |= Reason("Oath of Devotion", Spell.LEGEND_LORE, Spell.SUMMON_DRAGON)
        return spells


#############################################################################
class DraconicResilience(BaseFeature):
    tag = Feature.DRACONIC_RESILIENCE
    _desc = """The magic in your body manifests physical traits of your draconic gift. Parts of you are covered by 
    dragon-like scales."""
    hide = True

    #############################################################################
    def mod_hp_bonus(self, character: "Character") -> Reason[int]:
        return Reason("Draconic Resilience", character.level)

    #############################################################################
    def mod_ac_bonus(self, character: "Character") -> Reason[int]:
        if character.armour.tag == Armour.NONE and not character.shield:
            return Reason("Draconic Resilience", character.charisma.modifier)  # Dex is already included
        return Reason("Draconic Resilience", 0)


#############################################################################
class ElementalAffinity(BaseFeature):
    tag = Feature.ELEMENTAL_AFFINITY

    @property
    def desc(self) -> str:
        resistance = cast(ElementalAffinity, self.owner.find_feature(Feature.ELEMENTAL_AFFINITY)).resistance
        modifier = self.owner.charisma.modifier
        return f"""When you cast a spell that deals {resistance.title()} damage you can add 
        your Charisma modifier ({modifier}) to one damage roll of that spell."""

    def __init__(self, resistance: DamageType):
        super().__init__()
        if resistance not in (DamageType.ACID, DamageType.COLD, DamageType.FIRE, DamageType.LIGHTNING, DamageType.POISON):
            raise InvalidOption("ElementalAffinity resistance must be one of: Acid, Cold, Fire, Lightning or Poison ")
        self.resistance = resistance

    def mod_add_damage_resistances(self, character: "Character") -> Reason[DamageType]:
        return Reason("Elemental Affinity", self.resistance)


#############################################################################
class DragonWings(BaseFeature):
    tag = Feature.DRAGON_WINGS
    _desc = """As a Bonus Action, you can cause draconic wings to appear on your back. The wings last for 1 hour or 
    until you dismiss them (no action required). For the duration, you have a Fly Speed of 60 feet. Once you use this 
    feature, you can't use it again until you finish a Long Rest unless you spend 3 Sorcery Points (no action 
    required) to restore your use of it."""


#############################################################################
class DragonCompanion(BaseFeature):
    tag = Feature.DRAGON_COMPANION
    _desc = """You can cast Summon Dragon without a Material component. You can also cast it once without a spell 
    slot, and you regain the ability to cast it in this way when you finish a Long Rest.
    
    Whenever you start casting the spell, you can modify it so that it doesn't require Concentration. If you do so, 
    the spell's duration becomes 1 minute for that casting."""


# EOF
