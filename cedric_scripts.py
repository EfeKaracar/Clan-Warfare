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

    (troop_set_class, "trp_eu_sniper", grc_archers),
    (troop_set_class, "trp_loyal_noob", grc_infantry),
    (troop_set_class, "trp_open_mapper", grc_cavalry),
    (display_message, "@set_classes"),
    
]),

]