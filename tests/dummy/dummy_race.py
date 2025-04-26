from charsheets.features.base_feature import BaseFeature
from charsheets.race2014.base_race import BaseRace


#############################################################################
class DummyRace(BaseRace):

    def race_feature(self) -> set[BaseFeature]:
        return set()


# EOF
