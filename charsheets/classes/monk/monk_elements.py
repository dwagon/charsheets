from typing import TYPE_CHECKING

from charsheets.classes.monk import Monk
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class MonkWarriorOfTheElements(Monk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Monk (Warrior of the Elements)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {ElementalAttunement(), ManipulateElements()}
        abilities |= super().class_features()
        if self.level >= 6:
            abilities |= {ElementalBurst()}
        if self.level >= 11:
            abilities |= {StrideOfTheElements()}
        return abilities


#############################################################################
class ElementalAttunement(BaseFeature):
    tag = Feature.ELEMENTAL_ATTUNEMENT

    @property
    def desc(self) -> str:
        return f"""At the start of your turn, you can expend 1 Focus Point to imbue yourself with elemental energy. The 
    energy lasts for 10 minutes or until you have the Incapacitated condition. You gain the following benefits 
    while this feature is active. 

    Reach. When you make an Unarmed Strike, your reach is 10 feet greater than normal, as elemental energy extends 
    from you.

    Elemental Strikes. Whenever you hit with your Unarmed Strike, you can cause it to deal your choice of Acid, Cold, 
    Fire, Lightning, or Thunder damage rather than its normal damage type. When you deal one of these types with it, 
    you can also force the target to make a Strength saving throw (DC {self.owner.monk_dc}). On a failed save,
    you can move the target up to 10 feet toward or away from you, as elemental energy swirls around it."""


#############################################################################
class ManipulateElements(BaseFeature):
    tag = Feature.MANIPULATE_ELEMENTS
    _desc = """You know the 'Elementalism' spell. Wisdom is your spellcasting ability for it."""

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Manipulate Elements", Spell.ELEMENTALISM)


#############################################################################
class ElementalBurst(BaseFeature):
    tag = Feature.ELEMENTAL_BURST

    @property
    def desc(self) -> str:
        return f"""As a Magic action, you can expend 2 Focus Points to cause elemental energy to burst in a 
    20-foot-radius Sphere centered on a point within 120 feet of yourself. Choose a damage type: Acid, Cold, Fire, 
    Lightning, or Thunder.

    Each creature in the Sphere must make a Dexterity saving throw (DC {self.owner.monk_dc}). On a failed save,
    a creature takes damage of the 
    chosen type equal to three rolls of your Martial Arts die. On a success a creature takes half as much damage."""


#############################################################################
class StrideOfTheElements(BaseFeature):
    tag = Feature.STRIDE_OF_THE_ELEMENTS
    _desc = """While your Elemental Attunement is active, you also have a Fly Speed and a Swim Speed equal to your 
    Speed."""


# EOF
