import farmTemplates
import settings
import constants
import async

# movement
def autoMove(vertical = North, horizontal = East): 
	if get_pos_x() < get_world_size() - 1:
		move(horizontal) 
	else: 
		move(vertical)
		move(horizontal)
		

def position_drone(pos):
	if settings.DEBUG:
		quick_print("[utils] positioning drone (", pos[0], "/", pos[1], ")")
		
	moveOptionsY = { True:North, False:South }
	moveOptionsX = { True:East, False:West }
	
	yMove = moveOptionsY[pos[0] > get_pos_y()]
	while get_pos_y() != pos[0]: 
		move(yMove) 
	
	xMove = moveOptionsX[pos[1] > get_pos_x()]
	while get_pos_x() != pos[1]: 
		move(xMove)
		
		
		
# data 
def farming_goals_reached():
	if not async.threadState["activeFarmingGoal"]: 
		return False
		
	return num_items(async.threadState["wantedItem"]) >= settings.farmingGoals[async.threadState["wantedItem"]]
	

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
		return constants.actualYield[Entities.Pumpkin]
		#return defaultYield ** (num_unlocked(Unlocks.Pumpkins) - 1)
	
	elif itemOrEnt == Items.Power or itemOrEnt == Entities.Sunflower: 
		return defaultYield ** (num_unlocked(Unlocks.Sunflowers) - 1)
	
	elif itemOrEnt == Items.Cactus or itemOrEnt == Entities.Cactus: 
		return defaultYield ** (num_unlocked(Unlocks.Cactus) - 1)
		

def can_use_item(item): 
	if not settings.keepItemsAboveNum: 
		return True
	
	for key in settings.keepItemsAboveNum: 
		if key == item: 
			if num_items(item) > settings.keepItemsAboveNum[key]:
				return True
			
			return False 
	
		
		
# conversions
itemToEntity = {
	Items.Hay: Entities.Grass, 
	Items.Wood: Entities.Bush, # change to tree if needed 
	Items.Carrot: Entities.Carrot, 
	Items.Pumpkin: Entities.Pumpkin, 
	Items.Power: Entities.Sunflower, 
	Items.Cactus: Entities.Cactus, 
	Items.Weird_Substance: Entities.Grass,
	Items.Gold: Entities.Treasure, 
	Items.Bone: Entities.Dinosaur
}

entityToItem = {
	Entities.Grass: Items.Hay, 
	Entities.Bush: Items.Wood, Entities.Tree: Items.Wood, 
	Entities.Carrot: Items.Carrot,
	Entities.Pumpkin: Items.Pumpkin, 
	Entities.Sunflower: Items.Power, 
	Entities.Cactus: Items.Cactus,
	Entities.Treasure: Items.Gold,
	Entities.Dinosaur: Items.Bone
}
	
def auto_farm_call(itemOrEnt): 
	if itemOrEnt == Items.Hay or itemOrEnt == Entities.Grass:
		farmTemplates.farm_grass() 
		
	elif itemOrEnt == Items.Wood or itemOrEnt == Entities.Bush or itemOrEnt == Entities.Tree: 
		farmTemplates.farm_bush() # change to tree if you want
		
	elif itemOrEnt == Items.Carrot or itemOrEnt == Entities.Carrot: 
		farmTemplates.farm_carrots()
	
	elif itemOrEnt == Items.Pumpkin or itemOrEnt == Entities.Pumpkin: 
		farmTemplates.farm_pumpkin()
	
	elif itemOrEnt == Items.Power or itemOrEnt == Entities.Sunflower: 
		farmTemplates.farm_sunflower()
	
	elif itemOrEnt == Items.Cactus or itemOrEnt == Entities.Cactus: 
		farmTemplates.farm_cactus()
	
	elif itemOrEnt == Items.Gold or itemOrEnt == Entities.Treasure:
		farmTemplates.farm_treasure()
	
	elif itemOrEnt == Items.Bone or itemOrEnt == Entities.Dinosaur:
		farmTemplates.farm_bone()

		
		
# very important 
def piggy_gud(): 
	if settings.DEBUG: 	
		quick_print("[utils] petting the piggy...")
		
	pet_the_piggy() # very important		
