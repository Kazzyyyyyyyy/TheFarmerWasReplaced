import utils
import dynamicCropManager
import settings

threadState = {
	"farmDict": None, 
	"wantedItem": None,
	"activeFarmingGoal": None
}

def set_async_data(wantedItem, activeFarmingGoal = False):	
	threadState["farmDict"] = dynamicCropManager.one_item_max(utils.itemToEntity[wantedItem]) 
	threadState["wantedItem"] = wantedItem
	threadState["activeFarmingGoal"] = activeFarmingGoal


def farm(mainDrone = False):
	if settings.DEBUG and mainDrone: 
		quick_print("[async] farming...")
		
	while True: 
		for _ in range(get_world_size()): 
			utils.auto_farm_call(threadState["farmDict"][(get_pos_y(), get_pos_x())]) 
			
			if threadState["wantedItem"] == Items.Weird_Substance: 
				use_item(Items.Fertilizer)
				continue
			
			move(North)
		
		if utils.farming_goals_reached():
			break # break loop, advance 'settings.farmingGoals'
		
def create_drone_swarm():
	if settings.DEBUG: 
		quick_print("[async] creating drone swarm...")
		
	move(East)
	for _ in range(get_world_size()):
		if spawn_drone(farm): 
			move(East) 
		