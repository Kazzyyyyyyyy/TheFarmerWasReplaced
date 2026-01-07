import mazeSolver
import constants
import bones

def farm_grass():
	if get_ground_type() != Grounds.Grassland: 
		till() 
		
	elif can_harvest() or get_entity_type() != Entities.Grass: 
		harvest() 
	
	
def farm_bush(): 
	if get_ground_type() != Grounds.Soil: # not needed but looks better
		till() 
		
	elif can_harvest() or get_entity_type() != Entities.Bush: 
		harvest() 
	
	if get_water() <= constants.neededEntityWaterLevel[Entities.Bush]: 
		use_item(Items.Water)
		
	plant(Entities.Bush)


def farm_carrots(): 
	if get_ground_type() != Grounds.Soil:
		till() 
			
	elif can_harvest() or get_entity_type() != Entities.Carrot: 
		harvest() 
	
	if get_water() <= constants.neededEntityWaterLevel[Entities.Carrot]: 
		use_item(Items.Water)
		
	plant(Entities.Carrot) 
		
		
def farm_pumpkin(): 
	if get_ground_type() != Grounds.Soil: 
		till() 
		
	elif get_entity_type() == Entities.Dead_Pumpkin:
		plant(Entities.Pumpkin)
		return
	
	elif can_harvest() or get_entity_type() != Entities.Pumpkin: 
		harvest() 
		
		
	if get_water() <= constants.neededEntityWaterLevel[Entities.Carrot]: 
		use_item(Items.Water)	
		
	plant(Entities.Pumpkin) 


def farm_sunflower(): 	
	if get_ground_type() != Grounds.Soil: 
		till() 
		
	elif can_harvest():
		harvest()	
		
	plant(Entities.Sunflower)

	
def farm_cactus(): 
	if get_ground_type() != Grounds.Soil: 
		till() 
	else:
		harvest()

	plant(Entities.Cactus)	


def farm_treasure(): 
	if get_entity_type() != Entities.Bush: 
		harvest()
		plant(Entities.Bush)
	 	
	amount = get_world_size() * (2 ** (num_unlocked(Unlocks.Mazes) - 1))
	use_item(Items.Weird_Substance, amount)
	
	if spawn_drone(mazeSolver.right_hand_solver): 
		mazeSolver.left_hand_solver()
		
def farm_bone(): 
	clear() 
	change_hat(Hats.Dinosaur_Hat) 
	bones.farm_bones() 
	change_hat(Hats.Straw_Hat)