from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x888888),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  ("dark_knights","{!}Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []),

    ("culture_1",  "{!}culture_1", 0, 0.9, [], []),
    ("culture_2",  "{!}culture_2", 0, 0.9, [], []),
    ("culture_3",  "{!}culture_3", 0, 0.9, [], []),
    ("culture_4",  "{!}culture_4", 0, 0.9, [], []),
    ("culture_5",  "{!}culture_5", 0, 0.9, [], []),
    ("culture_6",  "{!}culture_6", 0, 0.9, [], []),
    ("culture_7",  "{!}culture_6", 0, 0.9, [], []),
    ("culture_8",  "{!}culture_6", 0, 0.9, [], []),

#  ("swadian_caravans","Swadian Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
#  ("vaegir_caravans","Vaegir Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),

  ("player_faction","Player Faction",0, 0.9, [], []),
  ("player_supporters_faction","Player's Supporters",0, 0.9, 
  [("player_faction",1.00),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xFF4433), #changed name so that can tell difference if shows up on map
  
    ("kingdom_1",  "The Kingdom of Rattonia", 0, 0.9, 
    [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),
    ("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xfa690f),
  
    ("kingdom_2",  "House Brightfyre",    0, 0.9, [("outlaws",-0.05),
    ("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),
    ("forest_bandits", -0.05)], [], 0x2394fc),
  
    ("kingdom_3",  "The Roaming Cavalry Company", 0, 0.9, 
    [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),
    ("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0x177a49),
  
    ("kingdom_4",  "The West Knights",    0, 0.9, [("outlaws",-0.05),
    ("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),
    ("forest_bandits", -0.05)], [], 0xFFFFFF),
  
    ("kingdom_5",  "The Turtle Knights Coalition",  0, 0.9, [("outlaws",-0.05),
    ("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),
    ("forest_bandits", -0.05)], [], 0x1eff00),
  
    ("kingdom_6",  "The Golden Kingdom",  0, 0.9, [("outlaws",-0.05),
    ("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),
    ("forest_bandits", -0.05)], [], 0xdecd18),
    
    ("kingdom_7",  "Avalonian Alliance",  0, 0.9, [("outlaws",-0.05),
    ("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),
    ("forest_bandits", -0.05)], [], 0xd13bff),
    
    ("kingdom_8",  "Defenders of Faith",  0, 0.9, [("outlaws",-0.05),
    ("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),
    ("forest_bandits", -0.05)], [], 0xf52020),
    
##  ("kingdom_1_rebels",  "Swadian rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_2_rebels",  "Vaegir rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_3_rebels",  "Khergit rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_4_rebels",  "Nord rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_5_rebels",  "Rhodok rebels",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

   ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),
   ("black_shields",  "Black Shields", 0, 0.1, [], [], 0x000000),
   
    
  ("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),
  ("black_khergits","{!}Black Khergits", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.02),("kingdom_2",-0.02)], []),

##  ("rebel_peasants","Rebel Peasants", 0, 0.5,[("vaegirs",-0.5),("player_faction",0.0)], []),

  ("manhunters","Manhunters", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], []),
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0x888888),
  ("mountain_bandits","Mountain Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),
  ("forest_bandits","Forest Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),

  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("peasant_rebels","{!}Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
#INVASION MODE START
  ("ccoop_all_stars","All Stars", 0, 0.5,[], []),
#INVASION MODE END
]
