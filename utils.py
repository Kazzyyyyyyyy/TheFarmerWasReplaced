import farm_templates
import settings


# movement
def simpleMove(vertical = North, horizontal = East): 
	if get_pos_x() < get_world_size() - 1:
		move(horizontal) 
	else: 
		move(vertical)
		move(horizontal)
		

def position_drone(pos):
	if settings.DEBUG:
		quick_print("[utils] positioning drone")
		
	while True: 
		if get_pos_y() == pos[0] and get_pos_x() == pos[1]:  
			break
	
		simpleMove()
	
	if settings.DEBUG:
		quick_print("[utils] drone positioned (", pos[0], "/", pos[1], ")")
		
		
		
# data 
def get_yield(itemOrEnt):
	defaultYield = 2 # needs to be bigger than 1 because '1 ** X' is always 1
	 				 # we make up for it with subtraction: 'defaultYield ** (X - 1)'
	
	if itemOrEnt == Items.Hay or itemOrEnt == Entities.Grass:
		return defaultYield ** (num_unlocked(Unlocks.Grass) - 1)
		
	elif itemOrEnt == Items.Wood or itemOrEnt == Entities.Bush or itemOrEnt == Entities.Tree: 
		return defaultYield ** (num_unlocked(Unlocks.Trees) - 1)
		
	elif itemOrEnt == Items.Carrot or itemOrEnt == Entities.Carrot: 
		return defaultYield ** (num_unlocked(Unlocks.Carrots) - 1)
	
	elif itemOrEnt == Items.Pumpkin or itemOrEnt == Entities.Pumpkin: 
		return defaultYield ** (num_unlocked(Unlocks.Pumpkins) - 1)
	
	elif itemOrEnt == Items.Power or itemOrEnt == Entities.Sunflower: 
		return defaultYield ** (num_unlocked(Unlocks.Sunflowers) - 1)
	
	elif itemOrEnt == Items.Cactus or itemOrEnt == Entities.Cactus: 
		return defaultYield ** (num_unlocked(Unlocks.Cactus) - 1)
		

		
# conversions
itemToEntity = {
	Items.Hay: Entities.Grass, 
	Items.Wood: Entities.Bush, # change to tree if needed 
	Items.Carrot: Entities.Carrot, 
	Items.Pumpkin: Entities.Pumpkin, 
	Items.Power: Entities.Sunflower, 
	Items.Cactus: Entities.Cactus
}

entityToItem = {
	Entities.Grass: Items.Hay, 
	Entities.Bush: Items.Wood, Entities.Tree: Items.Wood, 
	Entities.Carrot: Items.Carrot,
	Entities.Pumpkin: Items.Pumpkin, 
	Entities.Sunflower: Items.Power, 
	Entities.Cactus: Items.Cactus
}
	
def auto_farm_call(itemOrEnt): 
	if itemOrEnt == Items.Hay or itemOrEnt == Entities.Grass:
		farm_templates.farm_hay() 
		
	elif itemOrEnt == Items.Wood or itemOrEnt == Entities.Bush or itemOrEnt == Entities.Tree: 
		farm_templates.farm_bush() # change to tree if needed
		
	elif itemOrEnt == Items.Carrot or itemOrEnt == Entities.Carrot: 
		farm_templates.farm_carrots()
	
	elif itemOrEnt == Items.Pumpkin or itemOrEnt == Entities.Pumpkin: 
		farm_templates.farm_pumpkin()
	
	elif itemOrEnt == Items.Power or itemOrEnt == Entities.Sunflower: 
		farm_templates.farm_sunflower()
	
	#elif itemOrEnt == Items.Cactus or itemOrEnt == Entities.Cactus: 
				
	
		
		

