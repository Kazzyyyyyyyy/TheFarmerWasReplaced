import dynamic_crop_manager
import utils

def main(): 
	list = dynamic_crop_manager.one_item_max(Entities.Pumpkin) 
	
	while True: 
		if get_pos_x() == 0 and get_pos_y() == 0:  
			break
			
		utils.simpleMove()
		
	
	while True: 
		for item in list: 
			if(list[item] == 0):
				continue
				
			for i in range(list[item]): 
				utils.item_to_farm_call(item)
				utils.simpleMove()
				
				
			
main()