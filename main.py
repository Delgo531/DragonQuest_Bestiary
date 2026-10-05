from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

#Modelos

class MonsterDTO(BaseModel):
    name:str
    level: int
    family:str
    description:str
    habitat:list[str]
    xp:int
    gold:int
    image_url:str
    items:list[str]

class Monster(BaseModel):
    id_number: int
    name:str
    level:int
    family:str
    description:str
    habitat:list[str]
    xp:int
    gold:int
    image_url:str
    items:list[str]

class Move(BaseModel):
    id_number: int
    name: str
    unlock_level: int
    mana_cost: int | None = None
    description: str

class Spell(Move):
    pass

class Ability(Move):
    pass

class CharacterClass(BaseModel):
    id_number: int
    class_name: str
    description: str
    spells: list[Spell]
    abilities: list[Ability]

class PlayerDTO(BaseModel):
    name:str
    CharacterClass_Id:int

class Player(BaseModel):
    name:str
    level:int
    xp:int
    class_type:CharacterClass
    spells:list[Spell]
    abilities:list[Ability]
    defeated_monsters:int

#Clases definidas

hero = CharacterClass(
    id_number=1,
    class_name="Hero",
    description="A balanced class capable of using powerful attacks and a wide variety of spells.",
    spells=[
        Spell(
            id_number=1,
            name="Frizz",
            unlock_level=2,
            mana_cost=2,
            description="Launches a small fireball at one enemy."
        ),
        Spell(
            id_number=2,
            name="Heal",
            unlock_level=3,
            mana_cost=3,
            description="Restores a small amount of health to one ally."
        ),
        Spell(
            id_number=3,
            name="Poof",
            unlock_level=6,
            mana_cost=2,
            description="Attempts to make a group of enemies disappear."
        ),
        Spell(
            id_number=4,
            name="Evac",
            unlock_level=7,
            mana_cost=0,
            description="Allows the party to instantly escape from a dungeon."
        ),
        Spell(
            id_number=5,
            name="Sizz",
            unlock_level=9,
            mana_cost=4,
            description="Deals fire damage to a group of enemies."
        ),
        Spell(
            id_number=6,
            name="Kaclang",
            unlock_level=11,
            mana_cost=6,
            description="Turns the party into metal, making them invulnerable for several turns."
        ),
        Spell(
            id_number=7,
            name="Snooze",
            unlock_level=12,
            mana_cost=3,
            description="Attempts to put a group of enemies to sleep."
        ),
        Spell(
            id_number=8,
            name="Zin",
            unlock_level=14,
            mana_cost=5,
            description="Attempts to revive an ally with a small amount of health."
        ),
        Spell(
            id_number=9,
            name="Zoom",
            unlock_level=14,
            mana_cost=0,
            description="Teleports the party to a previously visited location."
        ),
        Spell(
            id_number=10,
            name="Fizzle",
            unlock_level=14,
            mana_cost=5,
            description="Prevents a group of enemies from using magic."
        ),
        Spell(
            id_number=11,
            name="Zap",
            unlock_level=15,
            mana_cost=8,
            description="Deals lightning damage to one enemy."
        ),
        Spell(
            id_number=12,
            name="Midheal",
            unlock_level=18,
            mana_cost=5,
            description="Restores a moderate amount of health to one ally."
        ),
        Spell(
            id_number=13,
            name="Sizzle",
            unlock_level=18,
            mana_cost=6,
            description="Deals moderate fire damage to a group of enemies."
        ),
        Spell(
            id_number=14,
            name="Holy Protection",
            unlock_level=20,
            mana_cost=4,
            description="Reduces encounters with weaker enemies for a period of time."
        ),
        Spell(
            id_number=15,
            name="Zapple",
            unlock_level=24,
            mana_cost=8,
            description="Deals powerful lightning damage to one enemy."
        ),
        Spell(
            id_number=16,
            name="Boom",
            unlock_level=27,
            mana_cost=9,
            description="Deals explosive damage to all enemies."
        ),
        Spell(
            id_number=17,
            name="Zing",
            unlock_level=27,
            mana_cost=10,
            description="Attempts to revive an ally."
        ),
        Spell(
            id_number=18,
            name="Kasizzle",
            unlock_level=33,
            mana_cost=12,
            description="Deals heavy fire damage to all enemies."
        ),
        Spell(
            id_number=19,
            name="Fullheal",
            unlock_level=34,
            mana_cost=9,
            description="Fully restores one ally's health."
        ),
        Spell(
            id_number=20,
            name="Kazap",
            unlock_level=38,
            mana_cost=30,
            description="Deals powerful lightning damage to one enemy."
        ),
        Spell(
            id_number=21,
            name="Omniheal",
            unlock_level=39,
            mana_cost=62,
            description="Fully restores the health of the entire party."
        )
    ],
    abilities=[
        Ability(
            id_number=1,
            name="Flame Slash",
            unlock_level=8,
            mana_cost=5,
            description="Performs a physical attack that deals fire damage."
        ),
        Ability(
            id_number=2,
            name="Dodgy Dance",
            unlock_level=13,
            mana_cost=4,
            description="Increases the user's ability to evade attacks."
        ),
        Ability(
            id_number=3,
            name="Lightning Slash",
            unlock_level=17,
            mana_cost=7,
            description="Performs a physical attack that deals lightning damage."
        ),
        Ability(
            id_number=4,
            name="Defending Champion",
            unlock_level=22,
            mana_cost=2,
            description="Greatly reduces the damage received."
        ),
        Ability(
            id_number=5,
            name="Gust Slash",
            unlock_level=23,
            mana_cost=7,
            description="Performs a physical attack that deals wind damage."
        ),
        Ability(
            id_number=6,
            name="Meditation",
            unlock_level=28,
            mana_cost=5,
            description="Restores some of the user's health."
        ),
        Ability(
            id_number=7,
            name="Falcon Slash",
            unlock_level=30,
            mana_cost=9,
            description="Performs two consecutive physical attacks."
        ),
        Ability(
            id_number=8,
            name="Gigaslash",
            unlock_level=45,
            mana_cost=38,
            description="Performs a powerful attack against all enemies."
        )
    ]
)

warrior = CharacterClass(
    id_number=2,
    class_name="Warrior",
    description="A powerful physical class focused on strength, defense, and heavy weapons.",
    spells=[],
    abilities=[
        Ability(
            id_number=1,
            name="Cop Out",
            unlock_level=1,
            mana_cost=2,
            description="Redirects attacks toward an enemy or an ally."
        ),
        Ability(
            id_number=2,
            name="Whipping Boy",
            unlock_level=3,
            mana_cost=1,
            description="Redirects attacks targeting one ally toward the user."
        ),
        Ability(
            id_number=3,
            name="Mercurial Thrust",
            unlock_level=9,
            mana_cost=3,
            description="Attacks one enemy before anyone else can act."
        ),
        Ability(
            id_number=4,
            name="Double-Edged Slash",
            unlock_level=16,
            mana_cost=6,
            description="Deals increased damage at the cost of some health."
        ),
        Ability(
            id_number=5,
            name="Pressure Pointer",
            unlock_level=21,
            mana_cost=4,
            description="Attempts to instantly defeat one enemy."
        ),
        Ability(
            id_number=6,
            name="Forbearance",
            unlock_level=25,
            mana_cost=4,
            description="Redirects attacks targeting all allies toward the user."
        ),
        Ability(
            id_number=7,
            name="Sword Dance",
            unlock_level=37,
            mana_cost=10,
            description="Attacks random enemies up to four times."
        ),
        Ability(
            id_number=8,
            name="Metal Slash",
            unlock_level=39,
            mana_cost=6,
            description="Performs a physical attack that always hits metal monsters."
        ),
        Ability(
            id_number=9,
            name="Multislice",
            unlock_level=48,
            mana_cost=8,
            description="Performs a physical attack against all enemies."
        ),
        Ability(
            id_number=10,
            name="Cutting Edge",
            unlock_level=48,
            mana_cost=14,
            description="Performs a powerful physical attack against one enemy."
        )
    ]
)

martial_artist = CharacterClass(
    id_number=3,
    class_name="Martial Artist",
    description="A powerful physical class specializing in martial arts, agility, and critical hits.",
    spells=[],
    abilities=[
        Ability(
            id_number=1,
            name="Leg Sweep",
            unlock_level=3,
            mana_cost=1,
            description="Attempts to prevent one enemy from acting for one turn."
        ),
        Ability(
            id_number=2,
            name="Flying Knee",
            unlock_level=7,
            mana_cost=3,
            description="Performs a flying kick against one enemy."
        ),
        Ability(
            id_number=3,
            name="Hawkeye Claw",
            unlock_level=13,
            mana_cost=4,
            description="Performs a physical attack that never misses."
        ),
        Ability(
            id_number=4,
            name="Wind Sickles",
            unlock_level=17,
            mana_cost=5,
            description="Attacks one enemy with blades of wind."
        ),
        Ability(
            id_number=5,
            name="Knuckle Sandwich",
            unlock_level=24,
            mana_cost=7,
            description="Performs a powerful physical attack against one enemy."
        ),
        Ability(
            id_number=6,
            name="Double Up",
            unlock_level=28,
            mana_cost=9,
            description="Lowers defense to greatly increase physical damage."
        ),
        Ability(
            id_number=7,
            name="Helichopter",
            unlock_level=34,
            mana_cost=8,
            description="Performs a physical attack against a group of enemies."
        ),
        Ability(
            id_number=8,
            name="Multifists",
            unlock_level=38,
            mana_cost=12,
            description="Randomly attacks enemies up to four times."
        ),
        Ability(
            id_number=9,
            name="Ripple of Disruption",
            unlock_level=43,
            mana_cost=10,
            description="Removes all buffs from one enemy."
        ),
        Ability(
            id_number=10,
            name="Critical Claim",
            unlock_level=47,
            mana_cost=64,
            description="Guarantees a critical hit against one enemy."
        )
    ]
)

mage = CharacterClass(
    id_number=4,
    class_name="Mage",
    description="A powerful magic class specializing in offensive spells, buffs, and magical utility.",
    spells=[
        Spell(
            id_number=1,
            name="Frizz",
            unlock_level=1,
            mana_cost=2,
            description="Deals fire damage to one enemy."
        ),
        Spell(
            id_number=2,
            name="Buff",
            unlock_level=2,
            mana_cost=3,
            description="Increases one ally's defense."
        ),
        Spell(
            id_number=3,
            name="Crack",
            unlock_level=5,
            mana_cost=3,
            description="Deals ice damage to one enemy."
        ),
        Spell(
            id_number=4,
            name="Sizz",
            unlock_level=7,
            mana_cost=4,
            description="Deals fire damage to a group of enemies."
        ),
        Spell(
            id_number=5,
            name="Kabuff",
            unlock_level=8,
            mana_cost=5,
            description="Increases the defense of the entire party."
        ),
        Spell(
            id_number=6,
            name="Evac",
            unlock_level=9,
            mana_cost=0,
            description="Allows the party to escape from a dungeon."
        ),
        Spell(
            id_number=7,
            name="Deceleratle",
            unlock_level=10,
            mana_cost=3,
            description="Decreases the agility of a group of enemies."
        ),
        Spell(
            id_number=8,
            name="Bang",
            unlock_level=11,
            mana_cost=5,
            description="Deals explosive damage to all enemies."
        ),
        Spell(
            id_number=9,
            name="Zoom",
            unlock_level=12,
            mana_cost=0,
            description="Teleports the party to a previously visited town."
        ),
        Spell(
            id_number=10,
            name="Drain Magic",
            unlock_level=12,
            mana_cost=0,
            description="Steals MP from one enemy."
        ),
        Spell(
            id_number=11,
            name="Sizzle",
            unlock_level=13,
            mana_cost=6,
            description="Deals fire damage to a group of enemies."
        ),
        Spell(
            id_number=12,
            name="Defizzle",
            unlock_level=14,
            mana_cost=4,
            description="Cures the Fizzle effect."
        ),
        Spell(
            id_number=13,
            name="Peep",
            unlock_level=15,
            mana_cost=3,
            description="Reveals the contents of a treasure chest."
        ),
        Spell(
            id_number=14,
            name="Frizzle",
            unlock_level=16,
            mana_cost=6,
            description="Deals heavy fire damage to one enemy."
        ),
        Spell(
            id_number=15,
            name="Safe Passage",
            unlock_level=19,
            mana_cost=2,
            description="Protects the party from damaging floor tiles."
        ),
        Spell(
            id_number=16,
            name="Crackle",
            unlock_level=20,
            mana_cost=6,
            description="Deals ice damage to a group of enemies."
        ),
        Spell(
            id_number=17,
            name="Oomph",
            unlock_level=21,
            mana_cost=6,
            description="Doubles one ally's attack power."
        ),
        Spell(
            id_number=18,
            name="Bounce",
            unlock_level=22,
            mana_cost=8,
            description="Reflects spells back at their caster."
        ),
        Spell(
            id_number=19,
            name="Boom",
            unlock_level=23,
            mana_cost=9,
            description="Deals explosive damage to all enemies."
        ),
        Spell(
            id_number=20,
            name="Tick-Tock",
            unlock_level=25,
            mana_cost=12,
            description="Changes the time of day."
        ),
        Spell(
            id_number=21,
            name="Kacrack",
            unlock_level=26,
            mana_cost=10,
            description="Deals powerful ice damage to all enemies."
        ),
        Spell(
            id_number=22,
            name="Fuddle",
            unlock_level=27,
            mana_cost=6,
            description="Attempts to confuse one enemy."
        ),
        Spell(
            id_number=23,
            name="Kasizz",
            unlock_level=29,
            mana_cost=12,
            description="Deals heavy fire damage to a group of enemies."
        ),
        Spell(
            id_number=24,
            name="Sheen",
            unlock_level=30,
            mana_cost=18,
            description="Removes a curse from one ally."
        ),
        Spell(
            id_number=25,
            name="Fade",
            unlock_level=31,
            mana_cost=15,
            description="Makes the party invisible for a short time."
        ),
        Spell(
            id_number=26,
            name="Kafrizz",
            unlock_level=31,
            mana_cost=12,
            description="Deals massive fire damage to one enemy."
        ),
        Spell(
            id_number=27,
            name="Click",
            unlock_level=34,
            mana_cost=0,
            description="Opens locked doors."
        ),
        Spell(
            id_number=28,
            name="Kacrackle",
            unlock_level=34,
            mana_cost=14,
            description="Deals massive ice damage to all enemies."
        ),
        Spell(
            id_number=29,
            name="Morph",
            unlock_level=36,
            mana_cost=12,
            description="Copies the stats and abilities of another party member."
        ),
        Spell(
            id_number=30,
            name="Puff!",
            unlock_level=37,
            mana_cost=24,
            description="Transforms the caster into a dragon."
        ),
        Spell(
            id_number=31,
            name="Kaboom",
            unlock_level=38,
            mana_cost=18,
            description="Deals devastating explosive damage to all enemies."
        ),
        Spell(
            id_number=32,
            name="Hocus Pocus",
            unlock_level=40,
            mana_cost=20,
            description="Produces a random magical effect."
        )
    ],
    abilities=[]
)

priest = CharacterClass(
    id_number=5,
    class_name="Priest",
    description="A support-focused class specializing in healing, revival, buffs, and protective magic.",
    spells=[
        Spell(
            id_number=1,
            name="Heal",
            unlock_level=1,
            mana_cost=3,
            description="Restores health to one ally."
        ),
        Spell(
            id_number=2,
            name="Poof",
            unlock_level=2,
            mana_cost=2,
            description="Attempts to banish weak enemies."
        ),
        Spell(
            id_number=3,
            name="Dazzle",
            unlock_level=3,
            mana_cost=4,
            description="Reduces the accuracy of a group of enemies."
        ),
        Spell(
            id_number=4,
            name="Woosh",
            unlock_level=4,
            mana_cost=4,
            description="Deals wind damage to a group of enemies."
        ),
        Spell(
            id_number=5,
            name="Sap",
            unlock_level=6,
            mana_cost=3,
            description="Reduces the defense of one enemy."
        ),
        Spell(
            id_number=6,
            name="Squelch",
            unlock_level=7,
            mana_cost=3,
            description="Cures poison from one ally."
        ),
        Spell(
            id_number=7,
            name="Snooze",
            unlock_level=8,
            mana_cost=3,
            description="Attempts to put a group of enemies to sleep."
        ),
        Spell(
            id_number=8,
            name="Acceleratle",
            unlock_level=9,
            mana_cost=3,
            description="Increases the agility of the entire party."
        ),
        Spell(
            id_number=9,
            name="Zin",
            unlock_level=10,
            mana_cost=5,
            description="Attempts to revive one ally with a small amount of health."
        ),
        Spell(
            id_number=10,
            name="Cock-a-Doodle-Doo",
            unlock_level=10,
            mana_cost=3,
            description="Awakens all sleeping allies."
        ),
        Spell(
            id_number=11,
            name="Fizzle",
            unlock_level=12,
            mana_cost=5,
            description="Prevents a group of enemies from using magic."
        ),
        Spell(
            id_number=12,
            name="Midheal",
            unlock_level=12,
            mana_cost=5,
            description="Restores a moderate amount of health to one ally."
        ),
        Spell(
            id_number=13,
            name="Tingle",
            unlock_level=14,
            mana_cost=6,
            description="Cures paralysis from one ally."
        ),
        Spell(
            id_number=14,
            name="Magic Barrier",
            unlock_level=16,
            mana_cost=6,
            description="Reduces magical damage received by the party."
        ),
        Spell(
            id_number=15,
            name="Kasap",
            unlock_level=16,
            mana_cost=5,
            description="Reduces the defense of a group of enemies."
        ),
        Spell(
            id_number=16,
            name="Swoosh",
            unlock_level=18,
            mana_cost=6,
            description="Deals stronger wind damage to a group of enemies."
        ),
        Spell(
            id_number=17,
            name="Blasto",
            unlock_level=20,
            mana_cost=7,
            description="Attempts to banish one enemy from battle."
        ),
        Spell(
            id_number=18,
            name="Moreheal",
            unlock_level=22,
            mana_cost=7,
            description="Restores a large amount of health to one ally."
        ),
        Spell(
            id_number=19,
            name="Whack",
            unlock_level=22,
            mana_cost=7,
            description="Attempts to instantly defeat one enemy."
        ),
        Spell(
            id_number=20,
            name="Zing",
            unlock_level=23,
            mana_cost=10,
            description="Attempts to revive one ally."
        ),
        Spell(
            id_number=21,
            name="Thwack",
            unlock_level=26,
            mana_cost=10,
            description="Attempts to instantly defeat a group of enemies."
        ),
        Spell(
            id_number=22,
            name="Insulatle",
            unlock_level=27,
            mana_cost=8,
            description="Reduces breath damage received by the party."
        ),
        Spell(
            id_number=23,
            name="Kaswoosh",
            unlock_level=31,
            mana_cost=10,
            description="Deals powerful wind damage to a group of enemies."
        ),
        Spell(
            id_number=24,
            name="Fullheal",
            unlock_level=32,
            mana_cost=9,
            description="Fully restores one ally's health."
        ),
        Spell(
            id_number=25,
            name="Multiheal",
            unlock_level=33,
            mana_cost=18,
            description="Restores health to the entire party."
        ),
        Spell(
            id_number=26,
            name="Kamikazee",
            unlock_level=33,
            mana_cost=1,
            description="Attempts to defeat all enemies at the cost of the caster's life."
        ),
        Spell(
            id_number=27,
            name="Kazing",
            unlock_level=37,
            mana_cost=20,
            description="Fully revives one fallen ally."
        )
    ],
    abilities=[]
)

merchant = CharacterClass(
    id_number=6,
    class_name="Merchant",
    description="A versatile class focused on earning gold, supporting the party, and using unique business-related abilities.",
    spells=[],
    abilities=[
        Ability(
            id_number=1,
            name="Stone's Throw",
            unlock_level=6,
            mana_cost=3,
            description="Throws stones at all enemies."
        ),
        Ability(
            id_number=2,
            name="Muster Strength",
            unlock_level=9,
            mana_cost=3,
            description="Increases the damage of the user's next attack."
        ),
        Ability(
            id_number=3,
            name="Dig",
            unlock_level=12,
            mana_cost=0,
            description="Unearths buried treasure."
        ),
        Ability(
            id_number=4,
            name="Service Call",
            unlock_level=17,
            mana_cost=15,
            description="Summons a wandering Merchant, Innkeeper, or Priest."
        ),
        Ability(
            id_number=5,
            name="Helichopter",
            unlock_level=24,
            mana_cost=8,
            description="Performs a physical attack against a group of enemies."
        ),
        Ability(
            id_number=6,
            name="Call to Arms",
            unlock_level=36,
            mana_cost=1,
            description="Pays gold to summon an army of mercenaries to attack one enemy."
        )
    ]
)

gadabout = CharacterClass(
    id_number=7,
    class_name="Gadabout",
    description="An unpredictable class with extremely high luck that can perform random actions in battle.",
    spells=[],
    abilities=[
        Ability(
            id_number=1,
            name="Sobering Slap",
            unlock_level=9,
            mana_cost=4,
            description="Cures an ally of sleep, confusion, and paralysis."
        ),
        Ability(
            id_number=2,
            name="Whistle",
            unlock_level=13,
            mana_cost=0,
            description="Causes a battle to occur."
        ),
        Ability(
            id_number=3,
            name="Kerplunk Dance",
            unlock_level=22,
            mana_cost=None,
            description="Sacrifices the user to revive and fully heal all allies."
        ),
        Ability(
            id_number=4,
            name="Spooky Aura",
            unlock_level=28,
            mana_cost=6,
            description="Reduces an enemy's magical defense."
        ),
        Ability(
            id_number=5,
            name="Egg On",
            unlock_level=31,
            mana_cost=3,
            description="Greatly increases an ally's attack power for one turn."
        ),
        Ability(
            id_number=6,
            name="Harvest Moon",
            unlock_level=32,
            mana_cost=8,
            description="Attacks all enemies, dealing more damage when fewer enemies remain."
        ),
        Ability(
            id_number=7,
            name="Hustle Dance",
            unlock_level=39,
            mana_cost=14,
            description="Restores at least 70 HP to the entire party."
        ),
        Ability(
            id_number=8,
            name="Channel Anger",
            unlock_level=45,
            mana_cost=16,
            description="Greatly increases the user's offensive spell damage."
        )
    ]
)

thief = CharacterClass(
    id_number=8,
    class_name="Thief",
    description="A fast and agile class specializing in stealing, exploration, and controlling enemies.",
    spells=[
        Spell(
            id_number=1,
            name="Eye for Distance",
            unlock_level=8,
            mana_cost=0,
            description="Reveals nearby towns and dungeons on the world map."
        ),
        Spell(
            id_number=2,
            name="Storyteller",
            unlock_level=10,
            mana_cost=2,
            description="Shows the current floor of the dungeon."
        ),
        Spell(
            id_number=3,
            name="Nose for Treasure",
            unlock_level=13,
            mana_cost=0,
            description="Shows how many treasure chests remain on the current floor."
        ),
        Spell(
            id_number=4,
            name="Padfoot",
            unlock_level=17,
            mana_cost=0,
            description="Reduces the chance of encountering enemies."
        ),
        Spell(
            id_number=5,
            name="Snoop",
            unlock_level=20,
            mana_cost=2,
            description="Reveals hidden objects in a dungeon."
        )
    ],
    abilities=[
        Ability(
            id_number=1,
            name="Sandstorm",
            unlock_level=1,
            mana_cost=3,
            description="Attempts to dazzle a group of enemies."
        ),
        Ability(
            id_number=2,
            name="Sleepy Slap",
            unlock_level=5,
            mana_cost=5,
            description="Attacks one enemy and may put it to sleep."
        ),
        Ability(
            id_number=3,
            name="Gust Slash",
            unlock_level=9,
            mana_cost=7,
            description="Performs a physical attack that deals wind damage."
        ),
        Ability(
            id_number=4,
            name="Shocking Slash",
            unlock_level=12,
            mana_cost=5,
            description="Deals physical damage and may paralyze the enemy."
        ),
        Ability(
            id_number=5,
            name="Assassin's Stab",
            unlock_level=16,
            mana_cost=4,
            description="Attacks an enemy's weak point and may instantly defeat it."
        ),
        Ability(
            id_number=6,
            name="Hypnowhip",
            unlock_level=25,
            mana_cost=9,
            description="Attacks a group of enemies and may put them to sleep."
        ),
        Ability(
            id_number=7,
            name="Persecutter",
            unlock_level=29,
            mana_cost=12,
            description="Deals increased damage to an enemy affected by a status ailment."
        ),
        Ability(
            id_number=8,
            name="Backdraft",
            unlock_level=33,
            mana_cost=10,
            description="Counterattacks enemies that damage the user."
        ),
        Ability(
            id_number=9,
            name="Pile On",
            unlock_level=33,
            mana_cost=15,
            description="Calls upon the party to perform a powerful combined attack."
        )
    ]
)

monster_wrangler = CharacterClass(
    id_number=9,
    class_name="Monster Wrangler",
    description="A versatile class that uses monster-based abilities to attack enemies and support the party.",
    spells=[],
    abilities=[
        Ability(
            id_number=1,
            name="Tongue Lashing",
            unlock_level=1,
            mana_cost=2,
            description="Attempts to stun one enemy for one turn."
        ),
        Ability(
            id_number=2,
            name="Monster Pile-On",
            unlock_level=5,
            mana_cost=8,
            description="Summons rescued monsters to attack random enemies."
        ),
        Ability(
            id_number=3,
            name="Soothing Song",
            unlock_level=7,
            mana_cost=5,
            description="Restores a small amount of HP to the entire party."
        ),
        Ability(
            id_number=4,
            name="Animal Instinct",
            unlock_level=10,
            mana_cost=0,
            description="Detects nearby monsters that can be recruited."
        ),
        Ability(
            id_number=5,
            name="Emergency Groom",
            unlock_level=11,
            mana_cost=5,
            description="Restores HP to one ally."
        ),
        Ability(
            id_number=6,
            name="Attack Attacker",
            unlock_level=13,
            mana_cost=6,
            description="Attacks one enemy and may reduce its attack power."
        ),
        Ability(
            id_number=7,
            name="War Cry",
            unlock_level=18,
            mana_cost=4,
            description="Attempts to stun all enemies."
        ),
        Ability(
            id_number=8,
            name="Tongue Bashing",
            unlock_level=20,
            mana_cost=7,
            description="Attempts to stun one enemy with a high chance of success."
        ),
        Ability(
            id_number=9,
            name="Flame Breath",
            unlock_level=23,
            mana_cost=5,
            description="Deals fire breath damage to all enemies."
        ),
        Ability(
            id_number=10,
            name="Boulder Toss",
            unlock_level=27,
            mana_cost=14,
            description="Throws a boulder at all enemies."
        ),
        Ability(
            id_number=11,
            name="Lashings of Love",
            unlock_level=30,
            mana_cost=5,
            description="Attacks a group of enemies and deals increased damage to humanoid enemies."
        ),
        Ability(
            id_number=12,
            name="Burning Breath",
            unlock_level=36,
            mana_cost=9,
            description="Deals breath damage to all enemies and may paralyze them."
        ),
        Ability(
            id_number=13,
            name="Call of the Wild",
            unlock_level=38,
            mana_cost=3,
            description="Summons wolves to attack random enemies."
        ),
        Ability(
            id_number=14,
            name="C-c-cold Breath",
            unlock_level=44,
            mana_cost=22,
            description="Deals powerful ice breath damage to all enemies."
        ),
        Ability(
            id_number=15,
            name="Wild Side",
            unlock_level=47,
            mana_cost=9,
            description="Allows the user to act twice in a row."
        ),
        Ability(
            id_number=16,
            name="Focus Pocus",
            unlock_level=49,
            mana_cost=3,
            description="Recovers MP for several turns."
        ),
        Ability(
            id_number=17,
            name="Fog of War",
            unlock_level=50,
            mana_cost=12,
            description="Neutralizes magical effects and prevents everyone from casting spells."
        )
    ]
)

sage = CharacterClass(
    id_number=10,
    class_name="Sage",
    description="A powerful magical class that combines the offensive magic of a Mage with the healing and support magic of a Priest.",
    spells=[
        Spell(id_number=1, name="Frizz", unlock_level=1, mana_cost=2, description="Deals fire damage to one enemy."),
        Spell(id_number=2, name="Heal", unlock_level=1, mana_cost=3, description="Restores health to one ally."),
        Spell(id_number=3, name="Buff", unlock_level=2, mana_cost=3, description="Increases one ally's defense."),
        Spell(id_number=4, name="Poof", unlock_level=2, mana_cost=2, description="Attempts to banish weak enemies."),
        Spell(id_number=5, name="Woosh", unlock_level=4, mana_cost=4, description="Deals wind damage to a group of enemies."),
        Spell(id_number=6, name="Crack", unlock_level=5, mana_cost=3, description="Deals ice damage to one enemy."),
        Spell(id_number=7, name="Acceleratle", unlock_level=5, mana_cost=3, description="Increases the agility of the entire party."),
        Spell(id_number=8, name="Sap", unlock_level=6, mana_cost=3, description="Reduces the defense of one enemy."),
        Spell(id_number=9, name="Sizz", unlock_level=7, mana_cost=4, description="Deals fire damage to a group of enemies."),
        Spell(id_number=10, name="Dazzle", unlock_level=7, mana_cost=4, description="Reduces the accuracy of a group of enemies."),
        Spell(id_number=11, name="Squelch", unlock_level=7, mana_cost=3, description="Cures poison from one ally."),
        Spell(id_number=12, name="Kabuff", unlock_level=8, mana_cost=5, description="Increases the defense of the entire party."),
        Spell(id_number=13, name="Snooze", unlock_level=8, mana_cost=3, description="Attempts to put a group of enemies to sleep."),
        Spell(id_number=14, name="Evac", unlock_level=9, mana_cost=0, description="Allows the party to escape from a dungeon."),
        Spell(id_number=15, name="Deceleratle", unlock_level=10, mana_cost=3, description="Decreases the agility of a group of enemies."),
        Spell(id_number=16, name="Zin", unlock_level=10, mana_cost=5, description="Attempts to revive one ally with a small amount of health."),
        Spell(id_number=17, name="Cock-a-Doodle-Doo", unlock_level=10, mana_cost=3, description="Awakens all sleeping allies."),
        Spell(id_number=18, name="Bang", unlock_level=11, mana_cost=5, description="Deals explosive damage to all enemies."),
        Spell(id_number=19, name="Zoom", unlock_level=12, mana_cost=0, description="Teleports the party to a previously visited town."),
        Spell(id_number=20, name="Drain Magic", unlock_level=12, mana_cost=0, description="Steals MP from one enemy."),
        Spell(id_number=21, name="Fizzle", unlock_level=12, mana_cost=5, description="Prevents a group of enemies from using magic."),
        Spell(id_number=22, name="Midheal", unlock_level=12, mana_cost=5, description="Restores a moderate amount of health to one ally."),
        Spell(id_number=23, name="Sizzle", unlock_level=13, mana_cost=6, description="Deals fire damage to a group of enemies."),
        Spell(id_number=24, name="Defizzle", unlock_level=14, mana_cost=4, description="Cures the Fizzle effect."),
        Spell(id_number=25, name="Tingle", unlock_level=14, mana_cost=6, description="Cures paralysis from one ally."),
        Spell(id_number=26, name="Peep", unlock_level=15, mana_cost=3, description="Reveals the contents of a treasure chest."),
        Spell(id_number=27, name="Frizzle", unlock_level=16, mana_cost=6, description="Deals heavy fire damage to one enemy."),
        Spell(id_number=28, name="Magic Barrier", unlock_level=16, mana_cost=6, description="Reduces magical damage received by the party."),
        Spell(id_number=29, name="Kasap", unlock_level=16, mana_cost=5, description="Reduces the defense of a group of enemies."),
        Spell(id_number=30, name="Swoosh", unlock_level=18, mana_cost=6, description="Deals stronger wind damage to a group of enemies."),
        Spell(id_number=31, name="Safe Passage", unlock_level=19, mana_cost=2, description="Protects the party from damaging floor tiles."),
        Spell(id_number=32, name="Crackle", unlock_level=20, mana_cost=6, description="Deals ice damage to a group of enemies."),
        Spell(id_number=33, name="Blasto", unlock_level=20, mana_cost=7, description="Attempts to banish one enemy from battle."),
        Spell(id_number=34, name="Oomph", unlock_level=21, mana_cost=6, description="Doubles one ally's attack power."),
        Spell(id_number=35, name="Bounce", unlock_level=22, mana_cost=8, description="Reflects spells back at their caster."),
        Spell(id_number=36, name="Moreheal", unlock_level=22, mana_cost=7, description="Restores a large amount of health to one ally."),
        Spell(id_number=37, name="Whack", unlock_level=22, mana_cost=7, description="Attempts to instantly defeat one enemy."),
        Spell(id_number=38, name="Zing", unlock_level=23, mana_cost=10, description="Attempts to revive one ally."),
        Spell(id_number=39, name="Boom", unlock_level=23, mana_cost=9, description="Deals explosive damage to all enemies."),
        Spell(id_number=40, name="Kacrack", unlock_level=26, mana_cost=10, description="Deals powerful ice damage to all enemies."),
        Spell(id_number=41, name="Thwack", unlock_level=26, mana_cost=10, description="Attempts to instantly defeat a group of enemies."),
        Spell(id_number=42, name="Fuddle", unlock_level=27, mana_cost=6, description="Attempts to confuse one enemy."),
        Spell(id_number=43, name="Insulatle", unlock_level=27, mana_cost=8, description="Reduces breath damage received by the party."),
        Spell(id_number=44, name="Kasizz", unlock_level=29, mana_cost=12, description="Deals heavy fire damage to a group of enemies."),
        Spell(id_number=45, name="Sheen", unlock_level=30, mana_cost=18, description="Removes a curse from one ally."),
        Spell(id_number=46, name="Fade", unlock_level=31, mana_cost=15, description="Makes the party invisible for a short time."),
        Spell(id_number=47, name="Kafrizz", unlock_level=31, mana_cost=12, description="Deals massive fire damage to one enemy."),
        Spell(id_number=48, name="Kaswoosh", unlock_level=31, mana_cost=10, description="Deals powerful wind damage to a group of enemies."),
        Spell(id_number=49, name="Fullheal", unlock_level=32, mana_cost=9, description="Fully restores one ally's health."),
        Spell(id_number=50, name="Multiheal", unlock_level=33, mana_cost=18, description="Restores health to the entire party."),
        Spell(id_number=51, name="Kamikazee", unlock_level=33, mana_cost=1, description="Attempts to defeat all enemies at the cost of the caster's life."),
        Spell(id_number=52, name="Click", unlock_level=34, mana_cost=0, description="Opens locked doors."),
        Spell(id_number=53, name="Kacrackle", unlock_level=34, mana_cost=14, description="Deals massive ice damage to all enemies."),
        Spell(id_number=54, name="Kazing", unlock_level=37, mana_cost=20, description="Fully revives one fallen ally."),
        Spell(id_number=55, name="Puff!", unlock_level=37, mana_cost=24, description="Transforms the caster into a dragon."),
        Spell(id_number=56, name="Kaboom", unlock_level=38, mana_cost=18, description="Deals devastating explosive damage to all enemies."),
        Spell(id_number=57, name="Hocus Pocus", unlock_level=40, mana_cost=20, description="Produces a random magical effect.")
    ],
    abilities=[]
)

character_classes = [
    hero,
    warrior,
    martial_artist,
    mage,
    priest,
    merchant,
    gadabout,
    thief,
    monster_wrangler,
    sage
]

#funciones

def battle(monster: Monster):
    win = 50 + (player.level - monster.level) * 5
    if (win < 5):
        win = 5
    elif (win > 100):
        win = 100    
    roll = random.randint(1,100)
    if roll <= win:
        return True
    else:
        return False 

def level_up():
    while player.xp >= player.level * 10:
        player.xp = player.xp - player.level * 10
        player.level = player.level + 1

        for spell in player.class_type.spells:
            if spell.unlock_level == player.level and not any(
                s.name == spell.name for s in player.spells
            ):
                player.spells.append(spell)

        for ability in player.class_type.abilities:
            if ability.unlock_level == player.level and not any(
                a.name == ability.name for a in player.abilities
            ):
                player.abilities.append(ability)

def load_initial_moves():
    for spell in player.class_type.spells:
        if spell.unlock_level <= player.level and not any(
            s.name == spell.name for s in player.spells
        ):
            player.spells.append(spell)

    for ability in player.class_type.abilities:
        if ability.unlock_level <= player.level and not any(
            a.name == ability.name for a in player.abilities
        ):
            player.abilities.append(ability)   

#Variables

player = Player(
    name="",
    level=1,
    xp=0,
    class_type=hero,
    spells=[],
    abilities=[],
    defeated_monsters=0
)

monsters = []
counter = 0

#Endpoints

@app.get("/monsters/{id}")
def getone_monster(id: int):
    for monster in monsters:
        if monster.id_number == id:
            return monster
    raise HTTPException(status_code=404, detail="Monster not found")

@app.get("/monsters")
def getall_monsters():
    return monsters                

@app.post("/monsters", status_code=201)
def post_monster(monsterDT0: MonsterDTO):

    global counter 
    counter = counter + 1

    monster = Monster(
        id_number= counter,
        level= monsterDT0.level,
        name= monsterDT0.name,
        family= monsterDT0.family,
        description= monsterDT0.description,
        habitat= monsterDT0.habitat,
        xp= monsterDT0.xp,
        gold= monsterDT0.gold,
        image_url= monsterDT0.image_url,
        items= monsterDT0.items
    )

    monsters.append(monster)
    return monster

@app.put("/monsters/{id}")
def put_monster(monsterDTO: MonsterDTO, id: int):
    for monster in monsters:
        if monster.id_number == id:
            monster.name = monsterDTO.name
            monster.level = monsterDTO.level
            monster.family = monsterDTO.family
            monster.description = monsterDTO.description
            monster.habitat = monsterDTO.habitat
            monster.xp = monsterDTO.xp
            monster.gold = monsterDTO.gold
            monster.image_url = monsterDTO.image_url
            monster.items = monsterDTO.items
            return monster
    raise HTTPException(status_code=404, detail="Monster not found")

@app.delete("/monsters/{id}")
def delete_monster(id: int):
    for monster in monsters:
        if monster.id_number == id:
            monsters.remove(monster)
            return {"detail": "Monster removed successfully"}
    raise HTTPException(status_code=404, detail="Monster not found")

@app.post("/player/register")
def register_player(newPlayer: PlayerDTO):
    if player.name != "":
        raise HTTPException(
            status_code=400,
            detail="Player already registered"
        )

    for classtype in character_classes:
        if newPlayer.CharacterClass_Id == classtype.id_number:
            player.name = newPlayer.name
            player.class_type = classtype
            load_initial_moves()
            return player

    raise HTTPException(status_code=404, detail="Class not found")

@app.get("/player/details")
def getPlayer_details():
    return player

@app.get("/player/spells")
def getSpells():
    return player.spells  

@app.get("/player/abilities")
def getAbilities():
    return player.abilities   

@app.post("/player/battle/{monster_id}")
def player_battle(monster_id: int):
    for monster in monsters:
        if monster.id_number == monster_id:

            if battle(monster):

                player.xp = player.xp + monster.xp
                player.defeated_monsters = player.defeated_monsters + 1

                level_up()

                return {
                    "result": "Victory",
                    "monster": monster.name,
                    "xp_gained": monster.xp,
                    "player": player
                }
            return {
                "result": "Defeat",
                "monster": monster.name,
                "player": player
            }

    raise HTTPException(status_code=404, detail="Monster not found")        

@app.put("/player/class/{class_id}")
def change_class(class_id: int):
    if player.level < 20:
        raise HTTPException(
            status_code=400,
            detail="You must reach level 20 to change class"
        )

    for classtype in character_classes:
        if classtype.id_number == class_id:
            player.class_type = classtype
            player.level = 1
            player.xp = 0

            load_initial_moves()

            return player

    raise HTTPException(status_code=404, detail="Class not found")