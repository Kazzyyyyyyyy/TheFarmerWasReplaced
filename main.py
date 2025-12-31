import dynamic_crop_manager
import utils
import settings


def main(): 
	list = dynamic_crop_manager.one_item_max(settings.oneItemMaxWanted) # get list of Entities to plant 
	
	utils.position_drone(settings.droneStartPos) # not needed but nice
		
	if settings.DEBUG: 
		quick_print("[main] farming...") 
		
	while True: 
		for item in list: 
			for i in range(list[item]): 
				utils.auto_farm_call(item)
				utils.simpleMove()
			
main()