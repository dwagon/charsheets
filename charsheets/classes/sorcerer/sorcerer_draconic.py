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


#################################################################################
class SorcererDraconic(Sorcerer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Draconic Sorceror"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {DraconicResilience(), DraconicSpells()}
        abilities |= super().class_features()

        return abilities

    #############################################################################
    def level6(self, **kwargs: Any):
        if "feature" not in kwargs or not isinstance(kwargs["feature"], ElementalAffinity):
            raise NotDefined("Draconic Sorcerors need to have feature Elemental Affinity")
        self._add_level(6, **kwargs)


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


# EOF
