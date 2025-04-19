from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.monk import Monk
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "ELEMENTAL_ATTUNEMENT", "Elemental Attunement")
extend_enum(Feature, "ELEMENTAL_BURST", "Elemental Burst")
extend_enum(Feature, "ELEMENTAL_EPITOME", "Elemental Epitome")
extend_enum(Feature, "MANIPULATE_ELEMENTS", "Manipulate Elements")
extend_enum(Feature, "STRIDE_OF_THE_ELEMENTS", "Stride of the Elements")


#################################################################################
class MonkWarriorOfTheElements(Monk):
    _class_name = "Warrior of the Elements"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(ElementalAttunement())
        self.add_feature(ManipulateElements())
        super().level3(**kwargs)

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(ElementalBurst())
        super().level6(**kwargs)

    #############################################################################
    def level11(self, **kwargs: Any):
        self.add_feature(StrideOfTheElements())

    #############################################################################
    def level17(self, **kwargs: Any):
        self.add_feature(ElementalEpitome())


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
    you can also force the target to make a Strength saving throw (DC {self.owner.monk.monk_dc}). On a failed save,
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

    Each creature in the Sphere must make a Dexterity saving throw (DC {self.owner.monk.monk_dc}). On a failed save,
    a creature takes damage of the 
    chosen type equal to three rolls of your Martial Arts die. On a success a creature takes half as much damage."""


#############################################################################
class StrideOfTheElements(BaseFeature):
    tag = Feature.STRIDE_OF_THE_ELEMENTS
    _desc = """While your Elemental Attunement is active, you also have a Fly Speed and a Swim Speed equal to your 
    Speed."""


#############################################################################
class ElementalEpitome(BaseFeature):
    tag = Feature.ELEMENTAL_EPITOME
    _desc = """While your Elemental Attunement is active, you also gain the following benefits. 
    
    Damage Resistance. You gain Resistance to one of the following damage types of your choice: Acid, Cold, Fire, 
    Lightning, or Thunder. At the start of each of your turns, you can change this choice.
    
    Destructive Stride. When you use your Step of the Wind, your Speed increases by 20 feet until the end of the 
    turn. For that duration, any creature of your choice takes damage equal to one roll of your Martial Arts die when 
    you enter a space within 5 feet of it. The damage type is your choice of Acid, Cold, Fire, Lightning, or Thunder. 
    A creature can take this damage only once per turn.
    
    Empowered Strikes. Once on each of your turns, you can deal extra damage to a target equal to one roll of your 
    Martial Arts die when you hit it with an Unarmed Strike. The extra damage is the same type dealt by that strike."""


# EOF
