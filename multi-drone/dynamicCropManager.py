import utils
import settings


def sort_list(farmList, wantedEntity): 
	if settings.DEBUG:
		quick_print("[dynamic_crop_manager] sorting crop split...")
	
	listOrder = []
	for round in range(2): 
		for key in farmList: 
			# take items, that have no costs
			if round == 0 and not get_cost(utils.itemToEntity[key]): 
				listOrder.append(key)
			
			# take items that have costs
			elif round == 1 and get_cost(utils.itemToEntity[key]) and key != utils.entityToItem[wantedEntity]:
				listOrder.append(key) 
	
	# 'wantedEntity' comes after the cost items
	listOrder.append(utils.entityToItem[wantedEntity])
	
	# transfer 'farmList' into 'sortedFarmList' in order of 'listOrder'
	sortedFarmList = { }
	for item in listOrder: 
		for key in farmList: 
			if key == item: 
				sortedFarmList[key] = farmList[key]		
					
					
	return sortedFarmList
	
	
def to_swarm_coord_dict(farmList): # need better name
	coordDict = { }
	y = 0
	x = 0
	
	for key in farmList:
		for num in range(farmList[key]): 
			coordDict[(y, x)] = key
			
			if x < get_world_size() - 1: 
				x += 1
				
			else: 
				x = 0
				y += 1
			
	return coordDict

def get_reqs(neededItems, entity, parentYieldMult = None): 
	costs = get_cost(entity)
	
	for key in costs:
		if parentYieldMult: 
		 	# multiply costs by 'needed / yield' ratio, example:
		 	# carrotYield = 128, we need 32 carrots, so we multiply the costs of 'Entities.Carrot' by 0.25
			neededItems[key] = costs[key] * parentYieldMult
		else:
			neededItems[key] = costs[key]	
	
	
		# check if costs of 'entity' also have costs
		if get_cost(utils.itemToEntity[key]):
			# call 'get_reqs()' again to go through every item 'wantedEntity' needs
			get_reqs(neededItems, utils.itemToEntity[key], (costs[key] / utils.get_yield(key))) 


def calculate_costs(wantedEntity): 
	
	neededItems = { } 
	
	# check if calculation is even needed
	if wantedEntity == Entities.Treasure or wantedEntity == Entities.Dinosaur or not get_cost(wantedEntity) or settings.plantOnlyOneEntity:
		return { utils.entityToItem[wantedEntity]: get_world_size() * get_world_size() }
	
	# get items needed for (a single) 'wantedEntity'
	get_reqs(neededItems, wantedEntity)
	
	# calculate how many tiles of item X we need to fill demand
	farmList = { utils.entityToItem[wantedEntity]:1 }
	for key in neededItems: 
		farmList[key] = neededItems[key] / utils.get_yield(key)
	
	# calculate how much space (in tiles) 'farmList' needs in total
	farmListSpaceValue = 0
	for key in farmList: 
		farmListSpaceValue += farmList[key]

	# divide world-size through 'farmListSpaceValue' to get multiplier value for how often it fits
	farmListMultiplier = (get_world_size() * get_world_size()) // farmListSpaceValue	
	
	# multiply every 'farmList[key]' with 'farmListMultiplier' to fill the whole world
	# use modulo operator to remove '0.X' because 'math.floor()' doesnt exist
	# calculate 'farmListSpaceValue' again to check if we have over or underflow problems
	# (overflow is not possible I think, but havent tested it)
	farmListSpaceValue = 0
	for key in farmList: 
		farmList[key] *= farmListMultiplier
		farmList[key] -= farmList[key] % 1
		farmListSpaceValue += farmList[key]
	
	# fill underflow with 'Items.Hay' (bc Hay always gud)
	if farmListMultiplier < (get_world_size() * get_world_size()): 
		farmList[Items.Hay] += ((get_world_size() * get_world_size()) - farmListSpaceValue)
	
	# subtract overflow from 'wantedEntity'
	elif farmListSpaceValue > (get_world_size() * get_world_size()):
		farmList[utils.entity_to_item(wantedEntity)] -= (farmListSpaceValue - (get_world_size() * get_world_size()))	
	
	return farmList


def one_item_max(wantedEntity): 
	if settings.DEBUG:
		quick_print("[dynamic_crop_manager] calculating crop split...")
	
	farmList = calculate_costs(wantedEntity) 

	farmList = sort_list(farmList, wantedEntity) # sort from low to high costs bc satisfying
	
	coordDict = to_swarm_coord_dict(farmList) # new dict, because 'farmList' = 'Entities:int' and 'coordDict' = '(int, int):Entites'
	
	if settings.DEBUG: 
		if settings.plantOnlyOneEntity: 
			quick_print("[dynamic_crop_manager] got crop split - 'plantOnlyOneEntity'")
		else:
			quick_print("[dynamic_crop_manager] got crop split")
			
		for key in farmList: 
			quick_print(key, ":", farmList[key])	
		
	return coordDict