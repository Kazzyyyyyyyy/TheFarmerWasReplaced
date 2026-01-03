import dynamicCropManager
import utils
import settings

def farming_loop(farmList, wantedItem, farmingGoals = False): 
	if wantedItem != Items.Gold: 
		utils.position_drone(settings.droneStartPos) # not needed but nice
	
	if settings.DEBUG: 
		quick_print("[main] farming...") 
	
	while True: 	
		# check if item ammount of 'wantedItem' fullfills goal
		if farmingGoals and num_items(wantedItem) >= settings.farmingGoals[wantedItem]: 
			if settings.DEBUG:
				quick_print("[main] done with:", wantedItem, "/", settings.farmingGoals[wantedItem]) 
			break # break loop, advance 'settings.farmingGoals'
	
		for item in farmList: 
			for i in range(farmList[item]):
				utils.auto_farm_call(item)
				
				if wantedItem == Items.Gold: 
					break
				
				if wantedItem == Items.Weird_Substance and utils.can_use_item(Items.Fertilizer):
					use_item(Items.Fertilizer)
					continue # no need to move when using fertilizer bc of insta growth
								
				utils.autoMove()
				

def main(): 
	if settings.farmingGoals: # any farming goals?
		if settings.DEBUG: 
			quick_print("[main] working on 'farmingGoals'")
	
		for wantedItem in settings.farmingGoals:
			farmList = dynamicCropManager.one_item_max(utils.itemToEntity[wantedItem])
			farming_loop(farmList, wantedItem, True)
		
		if settings.DEBUG: 
			quick_print("[main] 'farmingGoals' done, going back to 'oneItemMaxWanted'")
	
	farmList = dynamicCropManager.one_item_max(utils.itemToEntity[settings.oneItemMaxWanted])
	farming_loop(farmList, settings.oneItemMaxWanted)

main()