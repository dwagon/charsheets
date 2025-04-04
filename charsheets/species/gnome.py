from aenum import extend_enum

from charsheets.constants import Feature
from charsheets.features import Darkvision60
from charsheets.features.base_feature import BaseFeature
from charsheets.species.base_species import BaseSpecies

extend_enum(Feature, "GNOMISH_CUNNING", "Gnomish Cunning")
extend_enum(Feature, "GNOMISH_LINEAGE", "Gnomish Lineage")


#############################################################################
class Gnome(BaseSpecies):
    #########################################################################
    def species_feature(self) -> set[BaseFeature]:
        results: set[BaseFeature] = {GnomishCunning(), GnomishLineage(), Darkvision60()}
        if self.character.level >= 3:
            results.add(Feature.CELESTIAL_REVELATION)
        return results


#############################################################################
class GnomishCunning(BaseFeature):
    tag = Feature.GNOMISH_CUNNING
    _desc = """You have Advantage on Intelligence, Wisdom, and Charisma saving throws."""


#############################################################################
class GnomishLineage(BaseFeature):
    tag = Feature.GNOMISH_LINEAGE
    _desc = """You are part of a lineage that grants you supernatural features. Choose one of the following options; 
    whichever one you choose, Intelligence, Wisdom, or Charisma is your spellcasting ability for the spells you 
    cast with this trait (choose the ability when you select the lineage):

    Forest Gnome. You know the Minor Illusion cantrip. You also always have the Speak with Animals spell prepared. 
    You can cast it without a spell slot a number of times equal to your Proficiency Bonus, and you regain all 
    expended uses when you finish a Long Rest. You can also use any spell slots you have to cast the spell.

    Rock Gnome. You know the Mending and Prestidigitation cantrips. In addition,you can spend 10 minutes casting 
    Prestidigitation to create a Tiny clockwork device (AC 5, 1 HP), such as a toy, fire starter, or music box. When 
    you create the device, you determine its function by choosing one effect from Prestidigitation; the device 
    produces that effect whenever you or another creature takes a Bonus Action to activate it with a touch. If the 
    chosen effect has options within it, you choose one of those options for the device when you create it. For 
    example, if you choose the spell's ignite-extinguish effect, you determine whether the device ignites or 
    extinguishes fire; the device doesn't do both. You can have three such devices in existence at a time, 
    and each falls apart 8 hours after its creation or when you dismantle it with a touch asa Utilize action."""


# EOF
