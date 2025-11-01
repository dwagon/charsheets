from typing import cast

from charsheets.armour import Studded
from charsheets.character import Character
from charsheets.classes import WarlockOldOne, Warlock
from charsheets.classes.warlock import AgonizingBlast, MaskOfManyFaces, PactOfTheTome, OneWithShadows, RepellingBlast
from charsheets.constants import Skill, Stat, Language
from charsheets.features import AbilityScoreImprovement
from charsheets.origins import Hermit
from charsheets.species.homebrew.kuatoa import Kuatoa
from charsheets.spell import Spell
from charsheets.spells import EldritchBlast

character = Character(
    "Thiir",
    Hermit(
        Stat.CHARISMA,
        Stat.CHARISMA,
        Stat.CONSTITUTION,
    ),
    Kuatoa(),
    Language.AQUAN,
    cast(Language, Language.DEEP_SPEECH),
    strength=8,
    dexterity=12,
    constitution=14,
    intelligence=10,
    wisdom=13,
    charisma=15,
    bonds="Everything I do is for the common people",
    flaws="Unquestioning loyalty to my patron and God",
    ideals="We must help bring about the changes that the Gods are constantly working on in the world",
    traits="I am intolerant of other faiths and condemn the worship of other Gods",
    age=40,
    height="5'2",
    weight="100lb",
    skin="Bone White",
    hair="None",
    alignment="CE",
    image="characters/images/thiir.png",
    player_name="Jesse",
    allies="The Lonely Men",
    organization_name="Sigil of YurHuneura",
    organization_symbol="characters/images/YurHuneura.png",
)

character.add_level(Warlock(skills=[Skill.RELIGION, Skill.DECEPTION], add_invocation=AgonizingBlast(Spell.ELDRITCH_BLAST)))
character.add_spell_details(EldritchBlast())
character.learn_spell(Spell.ELDRITCH_BLAST, Spell.MAGE_HAND)
character.wear_armour(Studded())
character.add_level(
    Warlock(
        hp=5,
        add_invocation=[
            PactOfTheTome(
                Spell.TOLL_THE_DEAD, Spell.MIND_SLIVER, Spell.BLADE_WARD, Spell.COMPREHEND_LANGUAGES, Spell.FIND_FAMILIAR
            ),
            MaskOfManyFaces(),
        ],
    )
)
character.add_level(WarlockOldOne(hp=4))
character.add_level(WarlockOldOne(hp=8, feat=AbilityScoreImprovement(Stat.WISDOM, Stat.CHARISMA)))
character.learn_spell(Spell.MINOR_ILLUSION)

character.add_level(WarlockOldOne(hp=5, add_invocation=[RepellingBlast(Spell.ELDRITCH_BLAST), OneWithShadows()]))  # Level 5
character.learn_spell(Spell.ARMOR_OF_AGATHYS, Spell.HEX, Spell.SUGGESTION, Spell.INVISIBILITY, Spell.MISTY_STEP)
character.prepare_spells(Spell.ARMOR_OF_AGATHYS, Spell.HEX, Spell.SUGGESTION, Spell.INVISIBILITY, Spell.MISTY_STEP)

character.add_equipment(
    "Leather Armor",
)
character.add_treasure(
    "Tetrahedron ('The Chime' from the Drowned Temple)",
    "Jewellery Box",
    "Small Gem (50g)",
    "Sketch of path to Temple of Ungulas",
    "Davach Mask",
    "Healing Potion",
)
character.extras = {"gp": "307"}
character.add_level(WarlockOldOne(hp=4))  # Level 6
character.learn_spell(Spell.DISPEL_MAGIC)
