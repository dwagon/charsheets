""" Ability Score"""


#############################################################################
class Ability:
    def __init__(self, value: int = 0):
        self.value: int = value
        self.saving_throw: int = 0

    #########################################################################
    @property
    def modifier(self):
        return int((self.value - 10) / 2)

    #########################################################################
    def __str__(self):
        return f"{self.value} {self.modifier}"
