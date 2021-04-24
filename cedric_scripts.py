from header_common import *
from header_operations import *
from module_constants import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from header_map_icons import *
from header_presentations import *
from ID_animations import *

cedric_scripts = [


("set_classes", [
    #Rattonia
        (troop_set_class, "trp_swadian_recruit", grc_infantry),
        (troop_set_class, "trp_swadian_militia", grc_infantry),
        (troop_set_class, "trp_swadian_footman", grc_infantry),
        (troop_set_class, "trp_swadian_infantry", grc_infantry),
        (troop_set_class, "trp_swadian_sergeant", grc_infantry),
        (troop_set_class, "trp_swadian_skirmisher", grc_archers),
        (troop_set_class, "trp_swadian_crossbowman", grc_archers),
        (troop_set_class, "trp_swadian_sharpshooter", grc_archers),
        (troop_set_class, "trp_swadian_man_at_arms", grc_infantry),
        (troop_set_class, "trp_swadian_knight", grc_cavalry),
     
    #Brightfyre
        (troop_set_class, "trp_vaegir_recruit", grc_infantry),
        (troop_set_class, "trp_vaegir_footman", grc_infantry),
        (troop_set_class, "trp_vaegir_skirmisher", grc_infantry),
        (troop_set_class, "trp_vaegir_archer", grc_infantry),
        (troop_set_class, "trp_vaegir_marksman", grc_infantry),
        (troop_set_class, "trp_vaegir_veteran", grc_archers),
        (troop_set_class, "trp_vaegir_infantry", grc_archers),
        (troop_set_class, "trp_vaegir_guard", grc_cavalry),
        (troop_set_class, "trp_vaegir_horseman", grc_cavalry),
        
    #RCC
        (troop_set_class, "trp_khergit_tribesman", grc_infantry),
        (troop_set_class, "trp_khergit_skirmisher", grc_archers),
        (troop_set_class, "trp_khergit_horse_archer", grc_archers),
        (troop_set_class, "trp_rooftopper", grc_archers),
        (troop_set_class, "trp_khergit_veteran_horse_archer", grc_cavalry),
        (troop_set_class, "trp_khergit_horseman", grc_cavalry),
        (troop_set_class, "trp_khergit_lancer", grc_cavalry),
        (troop_set_class, "trp_battle_brother", grc_cavalry),
        (troop_set_class, "trp_bowling_ball", grc_cavalry),
        (troop_set_class, "trp_tin_can", grc_cavalry),
        (troop_set_class, "trp_abu_inf", grc_infantry),
        (troop_set_class, "trp_dog_inf", grc_infantry),
        (troop_set_class, "trp_eliteDog_inf", grc_infantry),
    
    #wK
        (troop_set_class, "trp_nord_recruit", grc_infantry),
        (troop_set_class, "trp_PPKCLONE", grc_infantry),
        (troop_set_class, "trp_nord_footman", grc_infantry),
        (troop_set_class, "trp_nord_trained_footman", grc_infantry),
        (troop_set_class, "trp_nord_warrior", grc_infantry),
        (troop_set_class, "trp_nord_veteran", grc_cavalry),
        (troop_set_class, "trp_nord_champion", grc_cavalry),
        (troop_set_class, "trp_nord_huntsman", grc_cavalry),
        (troop_set_class, "trp_nord_archer", grc_archers),
        (troop_set_class, "trp_nord_veteran_archer", grc_archers),
    
    
    #tK/OE
        
        (troop_set_class, "trp_rhodok_tribesman", grc_infantry),
        (troop_set_class, "trp_rhodok_spearman", grc_infantry),
        (troop_set_class, "trp_veteran_hiltslasher", grc_infantry),
        (troop_set_class, "trp_rhodok_trained_spearman", grc_infantry),
        (troop_set_class, "trp_rhodok_veteran_spearman", grc_infantry),
        (troop_set_class, "trp_rhodok_sergeant", grc_infantry),
        (troop_set_class, "trp_rhodok_crossbowman", grc_archers),
        (troop_set_class, "trp_rhodok_trained_crossbowman", grc_archers),
        (troop_set_class, "trp_rhodok_veteran_crossbowman", grc_cavalry),
        (troop_set_class, "trp_rhodok_sharpshooter", grc_cavalry),
        (troop_set_class, "trp_bunga_elite", grc_cavalry),

    #GK
        (troop_set_class, "trp_sarranid_recruit", grc_infantry),
        (troop_set_class, "trp_sarranid_footman", grc_infantry),
        (troop_set_class, "trp_sarranid_veteran_footman", grc_infantry),
        (troop_set_class, "trp_sarranid_infantry", grc_infantry),
        (troop_set_class, "trp_sarranid_guard", grc_infantry),
        (troop_set_class, "trp_sarranid_skirmisher", grc_archers),
        (troop_set_class, "trp_sarranid_archer", grc_archers),
        (troop_set_class, "trp_sarranid_master_archer", grc_archers),
        (troop_set_class, "trp_sarranid_horseman", grc_cavalry),
        (troop_set_class, "trp_sarranid_mamluke", grc_cavalry),
        (troop_set_class, "trp_pubstar", grc_infantry),
        (troop_set_class, "trp_godlike_pubstar", grc_infantry),
    
    #KoA/Wappaw
        
        (troop_set_class, "trp_alliance_recruit", grc_infantry),
        (troop_set_class, "trp_boar_spearman", grc_infantry),
        (troop_set_class, "trp_boar_hoplite", grc_infantry),
        (troop_set_class, "trp_avalonian_infantry", grc_infantry),
        (troop_set_class, "trp_avalonian_crossbowman", grc_archers),
        (troop_set_class, "trp_tacoss_bowman", grc_archers),
        (troop_set_class, "trp_avalonian_swordsman", grc_infantry),
        (troop_set_class, "trp_taco_knights", grc_cavalry),
        (troop_set_class, "trp_roxhardian", grc_cavalry),
        (troop_set_class, "trp_awlpiker", grc_cavalry),
        
    #DoF
        (troop_set_class, "trp_loyal_noob", grc_infantry),
        (troop_set_class, "trp_defender", grc_infantry),
        (troop_set_class, "trp_veteran_defender", grc_infantry),
        (troop_set_class, "trp_open_mapper", grc_cavalry),
        (troop_set_class, "trp_alejanbro_in_arms", grc_cavalry),
        (troop_set_class, "trp_disciple_of_erminas", grc_cavalry),
        (troop_set_class, "trp_javby_defender", grc_infantry),
        (troop_set_class, "trp_javby_offender", grc_infantry),
        (troop_set_class, "trp_eu_archer_recruit", grc_archers),
        (troop_set_class, "trp_eu_archer", grc_archers),
        (troop_set_class, "trp_eu_sniper", grc_archers),
        (troop_set_class, "trp_allied_gk_spammer", grc_infantry),
        (troop_set_class, "trp_allied_smashmas_champion", grc_infantry),
        






    (display_message, "@set_classes"),
    
]),

]