import utils
import settings

items = { } # needed items for one 'wantedEntity'

def get_reqs(entity, parentYieldMult = None): 
	costs = get_cost(entity) 
	
	for key in costs:
		if parentYieldMult: 
		 	# multiply costs by 'needed / yield' ratio, example:
		 	# carrotYield = 128, we need 32 carrots, so we multiply the costs of 'Entities.Carrot' by 0.25
			items[key] = costs[key] * parentYieldMult
		else:
			items[key] = costs[key]	
			
		# check if costs of 'entity' also have costs
		if get_cost(utils.itemToEntity[key]):
			# call 'get_reqs()' again to go through every item 'wantedEntity' needs
			get_reqs(utils.itemToEntity[key], (costs[key] / utils.get_yield(key))) 

def one_item_max(wantedEntity): 

	# start-msg
	if settings.DEBUG:
		quick_print("[dynamic_crop_manager] calculating crop split")
		
		
	# get items needed for (a single) 'wantedEntity'
	get_reqs(wantedEntity)
	
	# calculate how many squares of item X we need to fill demand
	fields = { utils.entityToItem[wantedEntity]:1 }
	for key in items: 
		fields[key] = items[key] / utils.get_yield(key)
	
	# calculate how much space (in squares) 'fields' needs in total
	fieldsSpaceValue = 0
	for key in fields: 
		fieldsSpaceValue += fields[key]

	# divide world-size through 'fieldsSpaceValue' to get multiplier value for how often it fits
	fieldsMultiplier = (get_world_size() * get_world_size()) // fieldsSpaceValue	
	
	# multiply every 'fields[key]' with 'fieldsMultiplier' to fill the whole world
	# use modulo operator to remove '0.X' because 'math.floor()' doesnt exist
	# calculate needed space again to check if we have over or underflow problems
	# (overflow is not possible I think, but havent tested it)
	fieldsSpaceValue = 0
	for key in fields: 
		fields[key] *= fieldsMultiplier
		fields[key] -= fields[key] % 1
		fieldsSpaceValue += fields[key]	
	
	# fill underflow with 'Items.Hay' (bc Hay always gud)
	if fieldsSpaceValue < (get_world_size() * get_world_size()): 
		fields[Items.Hay] += ((get_world_size() * get_world_size()) - fieldsSpaceValue)
	
	# subtract overflow from 'wantedEntity'
	elif fieldsSpaceValue > (get_world_size() * get_world_size()):
		fields[utils.entity_to_item(wantedEntity)] -= (fieldsSpaceValue - (get_world_size() * get_world_size()))
		
	
	# success-msg
	if settings.DEBUG:
		quick_print("[dynamic_crop_manager] calculated crop split")
		for key in fields: 
			quick_print(key, ":", fields[key])	
		
		
	return fields
