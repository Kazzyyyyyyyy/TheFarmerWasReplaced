import settings 
import constants

# constants 
up = North
right = East
down = South
left = West

# right hand algorithm 
turnToRightHand = { right:down, left:up, up:right, down:left }
turnLeft = { right:up, left:down, up:left, down:right }	

# left hand algorithm
turnToLeftHand = { right:up, left:down, up:left, down:right }
turnRight = { right:down, left:up, up:right, down:left }	

def right_hand_solver(): 
	lookDir = constants.dirs[random() * len(constants.dirs) // 1]
	startTime = get_time()
	calledNewDrone = False
	
	while True: 
		if not calledNewDrone and get_time() >= startTime + 2 and num_drones() < max_drones(): 
			calledNewDrone = True
			if spawn_drone(left_hand_solver): 
				continue
		
		lookDir = turnToRightHand[lookDir]
		
		if get_entity_type() == Entities.Treasure:
			harvest()
			break 
		
		elif get_entity_type() == Entities.Grass: 
			break 
		
		for i in range(4): 
			if move(lookDir): 
				break
			
			lookDir = turnLeft[lookDir]
	

def left_hand_solver(): 
	lookDir = constants.dirs[random() * len(constants.dirs) // 1]
	startTime = get_time()
	calledNewDrone = False
	
	while True: 
		if not calledNewDrone and get_time() >= startTime + 2 and num_drones() < max_drones(): 
			calledNewDrone = True
			if spawn_drone(right_hand_solver): 
				continue
				
		lookDir = turnToLeftHand[lookDir]
		
		if get_entity_type() == Entities.Treasure:
			harvest()
			break 
		
		elif get_entity_type() == Entities.Grass: 
			break
		
		for i in range(4): 
			if move(lookDir): 
				break
		
			lookDir = turnRight[lookDir]