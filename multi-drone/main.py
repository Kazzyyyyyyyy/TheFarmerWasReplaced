import async
import utils
import settings

def farming_loop(wantedItem, farmingGoals = False): 
	if wantedItem != Items.Gold and wantedItem != Items.Bone:
		harvest() # to break maze if there
		utils.position_drone(settings.droneStartPos)
		async.create_drone_swarm()
	
	while True: 
		if utils.farming_goals_reached():
			if settings.DEBUG:
				quick_print("[main] done with:", wantedItem, "/", settings.farmingGoals[wantedItem])
			
			break # break loop, advance 'settings.farmingGoals'
			
		async.farm(True)
	

def main(): 
	utils.piggy_gud()
	
	change_hat(Hats.Straw_Hat)
	
	if settings.farmingGoals: # any farming goals?
		if settings.DEBUG: 	
			quick_print("[main] working on 'farmingGoals'")
		
		for wantedItem in settings.farmingGoals:
			async.set_async_data(wantedItem, True)
			farming_loop(wantedItem, True)
			
		
		if settings.DEBUG: 
			quick_print("[main] 'farmingGoals' done, going back to 'oneItemMaxWanted'")

	async.set_async_data(settings.oneItemMaxWanted)
	farming_loop(settings.oneItemMaxWanted)

main()