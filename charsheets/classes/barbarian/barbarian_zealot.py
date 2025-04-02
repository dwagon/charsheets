from typing import Any

from aenum import extend_enum

from charsheets.classes.barbarian import Barbarian
from charsheets.constants import Feature, Recovery
from charsheets.features.base_feature import BaseFeature


extend_enum(Feature, "DIVINE_FURY", "Divine Fury")
extend_enum(Feature, "WARRIOR_OF_THE_GODS", "Warrior of the Gods")
extend_enum(Feature, "FANATICAL_FOCUS", "Fanatical Focus")
extend_enum(Feature, "ZEALOUS_PRESENCE", "Zealous Presence")


#################################################################################
class BarbarianPathOfTheZealot(Barbarian):

    #############################################################################
    def level3(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(DivineFury())
        self.add_feature(WarriorOfTheGods())

    #############################################################################
    def level6(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(FanaticalFocus())

    #############################################################################
    def level10(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(ZealousPresence())


#############################################################################
class DivineFury(BaseFeature):
    tag = Feature.DIVINE_FURY
    _desc = """"""

    @property
    def desc(self) -> str:
        return f"""You can channel divine power into your strikes. On each of your turns while your Rage is active, 
        the first creature you hit with a weapon or an Unarmed Strike takes extra damage equal to 
        1d6 plus {self.owner.level // 2}. The extra damage is Necrotic or Radiant; you choose the type each 
        time you deal the damage."""


#############################################################################
class WarriorOfTheGods(BaseFeature):
    tag = Feature.WARRIOR_OF_THE_GODS
    _goes = 4
    recovery = Recovery.LONG_REST
    _desc = """You have a pool of four d12s that you
    can spend to heal yourself. As a Bonus Action, you can expend dice from the pool, roll them, and regain a number
    of Hit Points equal to the roll's total."""


#############################################################################
class FanaticalFocus(BaseFeature):
    tag = Feature.FANATICAL_FOCUS
    _desc = ""

    @property
    def desc(self) -> str:
        assert self.owner.barbarian is not None
        return f"""Once per active Rage, if you fail a saving throw, you can reroll it with a 
        bonus of {self.owner.barbarian.rage_dmg_bonus}, and you must use the new roll."""


#############################################################################
class ZealousPresence(BaseFeature):
    tag = Feature.ZEALOUS_PRESENCE
    _goes = 1
    recovery = Recovery.LONG_REST
    _desc = """As a Bonus Action, you unleash a battle cry infused with divine energy. Up to ten other creatures of 
    your choice within 60 feet of you gain Advantage on attack rolls and saving throws until the start of your next 
    turn. 
    
    Once you use this feature, you can't use it again until you finish a Long Rest unless you expend a use of 
    your Rage (no action required) to restore your use of it.."""


# EOF
