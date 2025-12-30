import constants
import farm_templates
import utils

fields = {}

def get_reqs(entity, mult = 1):
	costs = get_cost(entity)
	
	for key in costs:
		sub_costs = get_cost(utils.item_to_entities(key))

		if sub_costs: 
			sub_reqs = get_reqs(utils.item_to_entities(key), costs[key] / utils.item_to_yield(key))
			fields[key] = costs[key] / utils.item_to_yield(key)
		else:  
			fields[key] = (costs[key] * mult) / utils.item_to_yield(key)
	

def one_item_max(wantedEntity): 

	fields[wantedEntity] = 1
	
	if len(get_cost(wantedEntity)) == 0: 
		fields[wantedEntity] = (get_world_size() * get_world_size())
		return fields
	
	get_reqs(wantedEntity)
	
	val = 0
	for key in fields: 
		val += fields[key]
		
	quick_print(val)
	
	fieldMult = (get_world_size() * get_world_size()) // val
	
	for key in fields: 
		fields[key] *= fieldMult
		
	for key in fields: 
		val += fields[key]
	
	if (val / (get_world_size() * get_world_size())) < 0: 
		fields[wantedEntity] -= 1
	
	fieldsClone = dict(fields)
	for key in fieldsClone: 
		if utils.entities_to_item(key) != None: 
			val = fields[key] 
			fields[utils.entities_to_item(key)] = val
			fields[key] = 0
	
	for item in fields: 
		quick_print(item, ", ", fields[item])
		
	return fields
