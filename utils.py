import constants
import farm_templates

# movement
def simpleMove(): 
	if get_pos_x() < get_world_size() - 1:
		move(East) 
	else: 
		move(North)
		move(East)
		
		
# conversions
def item_to_yield(item):
	if(item == Items.Carrot): 
		return constants.carrot_yield
		
	elif(item == Items.Wood):
		return constants.wood_yield
		
	elif(item == Items.Hay):
		return constants.hay_yield

def item_to_entities(item): 
	if(item == Items.Carrot): 
		return Entities.Carrot
		
	elif(item == Items.Wood):
		return Entities.Bush
		
	elif(item == Items.Hay):
		return Entities.Grass
	
	elif (item == Items.Pumpkin):
		return Entities.Pumpkin
		
def entities_to_item(item): 
	if(item == Entities.Carrot): 
		return Items.Carrot
		
	elif(item == Entities.Bush):
		return Items.Wood
		
	elif(item == Entities.Grass):
		return Items.Hay
	
	elif (item == Entities.Pumpkin):
		return Items.Pumpkin
		
	elif item == Entities.Sunflower: 
		return Items.Power 

# farming 
def item_to_farm_call(item): 
	if item == Items.Carrot: 
		farm_templates.farm_carrots() 
				
	elif item == Items.Hay:
		farm_templates.farm_hay() 
				
	elif item == Items.Wood: 
		farm_templates.farm_bush()
			
	elif item == Items.Pumpkin: 
		farm_templates.farm_pumpkin()
	
	elif item == Items.Power: 
		farm_templates.farm_sunflower()
	
		
		


		
