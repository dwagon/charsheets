from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.barbarian import Barbarian
from charsheets.constants import Ability


#################################################################################
class BarbarianPathOfTheZealot(Barbarian):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Barbarian (Path of the Zealot)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {DivineFury(), WarriorOfTheGods()}
        if self.level >= 6:
            abilities.add(FanaticalFocus())
        abilities |= super().class_abilities()
        return abilities


#############################################################################
class DivineFury(BaseAbility):
    tag = Ability.DIVINE_FURY
    _desc = """"""

    @property
    def desc(self) -> str:
        return f"""You can channel divine power into your strikes. On each of your turns while your Rage is active, 
        the first creature you hit with a weapon or an Unarmed Strike takes extra damage equal to 
        1d6 plus {self.owner.level // 2}. The extra damage is Necrotic or Radiant; you choose the type each 
        time you deal the damage."""


#############################################################################
class WarriorOfTheGods(BaseAbility):
    tag = Ability.WARRIOR_OF_THE_GODS
    _goes = 4
    _desc = """A divine entity helps ensure you can continue the fight. You have a pool of four d12s that you
    can spend to heal yourself. As a Bonus Action, you can expend dice from the pool, roll them, and regain a number
    of Hit Points equal to the roll's total.

    Your pool regains all expended dice when you finish a Long Rest."""


#############################################################################
class FanaticalFocus(BaseAbility):
    tag = Ability.FANATICAL_FOCUS
    _desc = ""

    @property
    def desc(self) -> str:
        return f"""Once per active Rage, if you fail a saving throw, you can reroll it with a 
        bonus of {self.owner.rage_dmg_bonus}, and you must use the new roll."""


# EOF
