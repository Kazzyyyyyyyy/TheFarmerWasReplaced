def farm_carrots(): 
	if get_ground_type() != Grounds.Soil: 
		till() 
		plant(Entities.Carrot)
			
	elif can_harvest() or get_entity_type() != Entities.Carrot: 
		harvest() 
		plant(Entities.Carrot) 
		
def farm_bush(): 
	if get_ground_type() != Grounds.Soil: 
		till() 
		plant(Entities.Carrot)
	
	elif can_harvest() or get_entity_type() != Entities.Bush: 
		harvest() 
		plant(Entities.Bush) 
		
def farm_hay():
	if get_ground_type() != Grounds.Grassland: 
		till() 
		
	elif can_harvest() or get_entity_type() != Entities.Grass: 
		harvest() 
				
def farm_pumpkin(): 
	if get_ground_type() != Grounds.Soil: 
		till() 
		plant(Entities.Pumpkin)
		
	elif get_entity_type() == Entities.Dead_Pumpkin: 
		plant(Entities.Pumpkin) 
	
	elif can_harvest() or get_entity_type() != Entities.Pumpkin: 
		harvest() 
		plant(Entities.Pumpkin) 

def farm_sunflower(): 
	if get_ground_type() != Grounds.Soil: 
		till() 
		plant(Entities.Pumpkin)
		
	else:
		harvest()
		plant(Entities.Sunflower)