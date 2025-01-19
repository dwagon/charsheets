from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.monk import Monk
from charsheets.constants import Ability
from charsheets.reason import Reason
from charsheets.spells import Spells

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class MonkWarriorOfTheElements(Monk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Monk (Warrior of the Elements)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {ElementalAttunement(), ManipulateElements()}
        abilities |= super().class_abilities()
        if self.level >= 6:
            abilities.add(ElementalBurst())
        return abilities


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
class ElementalBurst(BaseAbility):
    tag = Ability.ELEMENTAL_BURST
    _desc = """As a Magic action, you can expend 2 Focus Points to cause elemental energy to burst in a 
    20-foot-radius Sphere centered on a point within 120 feet of yourself. Choose a damage type: Acid, Cold, Fire, 
    Lightning, or Thunder.

    Each creature in the Sphere must make a Dexterity saving throw. Ona failed save, a creature takes damage of the 
    chosen type equal to three rolls of your Martial Arts die. On a success a creature takes half as much damage."""


# EOF
