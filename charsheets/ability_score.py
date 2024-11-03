""" Ability Score"""


#############################################################################
class AbilityScore:
    def __init__(self, value: int = 0):
        self.value: int = value
        self.proficient = 0

    #########################################################################
    @property
    def saving_throw(self) -> int:
        return self.modifier

    #########################################################################
    @property
    def modifier(self):
        return int((self.value - 10) / 2)

    #########################################################################
    def __str__(self):
        return f"{self.value} {self.modifier} {self.proficient}"
