from charsheets.constants import Origin, Feat
from charsheets.exception import UnhandledException


#################################################################################
class BaseOrigin:

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        raise NotImplemented


#################################################################################
class AcolyteOrigin(BaseOrigin):

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.MAGIC_INITIATE_CLERIC}


#################################################################################
class ArtisanOrigin(BaseOrigin):

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.CRAFTER}


#################################################################################
class CharlatanOrigin(BaseOrigin):

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.SKILLED}


#################################################################################
class CriminalOrigin(BaseOrigin):

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.ALERT}


#################################################################################
class EntertainerOrigin(BaseOrigin):

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.MUSICIAN}


#################################################################################
class FarmerOrigin(BaseOrigin):

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.TOUGH}


#################################################################################
class GuardOrigin(BaseOrigin):

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.ALERT}


#################################################################################
class GuideOrigin(BaseOrigin):

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.MAGIC_INITIATE_DRUID}


#################################################################################
class HermitOrigin(BaseOrigin):

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.HEALER}


#################################################################################
class MerchantOrigin(BaseOrigin):

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.LUCKY}


#################################################################################
class NobleOrigin(BaseOrigin):

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.SKILLED}


#################################################################################
class SageOrigin(BaseOrigin):

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.MAGIC_INITIATE_WIZARD}


#################################################################################
class SailorOrigin(BaseOrigin):

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.TAVERN_BRAWLER}


#################################################################################
class ScribeOrigin(BaseOrigin):

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.SKILLED}


#################################################################################
class SoldierOrigin(BaseOrigin):

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.SAVAGE_ATTACKER}


#################################################################################
class WayfarerOrigin(BaseOrigin):

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return {Feat.LUCKY}


#################################################################################
def origin_picker(origin: Origin) -> BaseOrigin:
    match origin:
        case Origin.ACOLYTE:
            return AcolyteOrigin()
        case Origin.ARTISAN:
            return ArtisanOrigin()
        case Origin.CHARLATAN:
            return CharlatanOrigin()
        case Origin.CRIMINAL:
            return CriminalOrigin()
        case Origin.ENTERTAINER:
            return EntertainerOrigin()
        case Origin.FARMER:
            return FarmerOrigin()
        case Origin.GUARD:
            return GuardOrigin()
        case Origin.GUIDE:
            return GuideOrigin()
        case Origin.HERMIT:
            return HermitOrigin()
        case Origin.MERCHANT:
            return MerchantOrigin()
        case Origin.NOBLE:
            return NobleOrigin()
        case Origin.SAGE:
            return SageOrigin()
        case Origin.SAILOR:
            return SailorOrigin()
        case Origin.SCRIBE:
            return ScribeOrigin()
        case Origin.SOLDIER:
            return SoldierOrigin()
        case Origin.WAYFARER:
            return WayfarerOrigin()
        case _:
            raise UnhandledException(f"Origin {origin} not implemented")


# EOF
