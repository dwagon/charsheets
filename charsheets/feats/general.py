from typing import TYPE_CHECKING
from charsheets.constants import Feat
from charsheets.feats.base_feat import BaseFeat

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class Actor(BaseFeat):
    tag = Feat.ACTOR

    #############################################################################
    @property
    def desc(self) -> str:
        bonus = self.character.charisma.modifier + 8 + self.character.proficiency_bonus
        return f"""You gain the following benefits.

Impersonation. While you're disguised as a real or fictional person,you have Advantage on Charisma (Deception or 
Performance) checks to convince others that you are that person.

Mimicry. You can mimic the sounds of other creatures, including speech. A creature that hears the mimicry must 
succeed on a Wisdom (Insight) check to determine the effect is faked (DC {bonus})."""

    #############################################################################
    def mod_stat_cha(self, character: "Character") -> int:
        return 1


# EOF
