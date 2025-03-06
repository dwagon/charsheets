from typing import Optional

from aenum import extend_enum

from charsheets.classes.fighter import Fighter
from charsheets.constants import Stat, Feature
from charsheets.features.base_feature import BaseFeature


#################################################################################
class FighterEldritchKnight(Fighter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Eldritch Knight"

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.INTELLIGENCE

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {WarBond()}
        abilities |= super().class_features()
        if self.level >= 7:
            abilities |= {WarMagic()}
        if self.level >= 7:
            abilities |= {EldritchStrike()}
        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [0, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [0, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [1, 0, 0, 0, 0, 0, 0, 0, 0],
            4: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            5: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            6: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            7: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            8: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            9: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            10: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            11: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            12: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            13: [4, 3, 2, 0, 0, 0, 0, 0, 0],
            14: [4, 3, 2, 0, 0, 0, 0, 0, 0],
            15: [4, 3, 2, 0, 0, 0, 0, 0, 0],
            16: [4, 3, 3, 0, 0, 0, 0, 0, 0],
            17: [4, 3, 3, 0, 0, 0, 0, 0, 0],
            18: [4, 3, 3, 0, 0, 0, 0, 0, 0],
            19: [4, 3, 3, 1, 0, 0, 0, 0, 0],
            20: [4, 3, 3, 1, 0, 0, 0, 0, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def max_spell_level(self) -> int:
        if self.level >= 19:
            return 4
        elif self.level >= 13:
            return 3
        elif self.level >= 7:
            return 2
        return 1


extend_enum(Feature, "ELDRITCH_STRIKE", "Eldritch Strike")
extend_enum(Feature, "WAR_BOND", "War Bond")
extend_enum(Feature, "WAR_MAGIC", "War Magic")


############################################################################
class WarBond(BaseFeature):
    tag = Feature.WAR_BOND
    _desc = """You learn a ritual that creates a magical bond between yourself and one weapon. You perform the ritual
    over the course of 1 hour, which can be done during a Short Rest.

    Once you have bonded a weapon to yourself, you can't be disarmed of that weapon unless you have the Incapacitated
    condition. You can summon that weapon as a Bonus Action, causing it to teleport instantly to your hand."""


############################################################################
class WarMagic(BaseFeature):
    tag = Feature.WAR_MAGIC
    _desc = """When you take the Attack action on your turn, you can replace one of the attacks with a casting of one 
    of your Wizard cantrips that has a casting time of an action."""


############################################################################
class EldritchStrike(BaseFeature):
    tag = Feature.ELDRITCH_STRIKE
    _desc = """When you hit a creature with an attack using a weapon, that creature has Disadvantage on the next 
    saving throw it makes against a spell you cast before the end of your next turn."""


# EOF
