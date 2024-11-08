from charsheets.constants import Origin, Feat
from charsheets.exception import UnhandledException


#################################################################################
class BaseOrigin:

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        raise NotImplemented


#################################################################################
class NobleOrigin(BaseOrigin):

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return set([Feat.SKILLED])


#################################################################################
class AcolyteOrigin(BaseOrigin):

    #############################################################################
    def origin_feat(self) -> set[Feat]:
        return set([Feat.MAGIC_INITIATE_CLERIC])


#################################################################################
def origin_picker(origin: Origin) -> BaseOrigin:
    match origin:
        case Origin.ACOLYTE:
            return AcolyteOrigin()
        case Origin.NOBLE:
            return NobleOrigin()
        case _:
            raise UnhandledException(f"Origin {origin} not implemented")


# EOF
