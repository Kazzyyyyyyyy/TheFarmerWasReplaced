import constants

def convert_to_correct_coords(pos): 
		  # y   -   x
	return (pos[1], pos[0])

def get_move(nextPos): 
	if nextPos[0] < get_pos_y(): 
		return South
	elif nextPos[0] > get_pos_y():
		return North
	elif nextPos[1] < get_pos_x(): 
		return West	 
	elif nextPos[1] > get_pos_x(): 
		return East
			
			
def get_blocked_dir(moveHistory, tailLength): 
	blocked = set() 
	currPos = convert_to_correct_coords((get_pos_y(), get_pos_x()))
	
	offset = len(moveHistory) - tailLength
	for i in range(tailLength): 
		pos = moveHistory[offset + i] 
		if pos[0] < currPos[0]: 
			blocked.add(South)
			quick_print("blocked north") 
		elif pos[0] > currPos[0]: 
			blocked.add(North)
			quick_print("blocked sotuh") 
		elif pos[1] < currPos[1]: 
			blocked.add(West)
			quick_print("blocked west") 
		elif pos[0] > currPos[0]: 
			blocked.add(East)
			quick_print("blocked east") 
		
		if len(blocked) == 3: 
			break
			
	return blocked


def move_straight(currPos): 
	y = currPos[0] 
	x = currPos[1]
	
	if y == get_world_size() - 1 and x == 1: 
		return West 
	
	if y != 0 and x == 0: 
		return South
	
	if y % 2 == 0:
		if x < 31:
			return East
		else:  
			if y == 30:
				return North
			else:
				return North
	else:  
		if x > 1:
			return West
		else:  
			if y == 31:
				return South
			else:
				return North

	
	

def farm_bones(): 
	clear() 
	change_hat(Hats.Dinosaur_Hat) 
	
	tailLength = 0
	nextPos = (0, 0)
	moveHistory = []	

	while True: 
		if tailLength < 40: 
			if get_entity_type() == Entities.Apple: 
				nextPos = convert_to_correct_coords(measure())
				tailLength += 1
				
				
			if not move(get_move(nextPos)):
				moved = False
				blockedDir = get_blocked_dir(moveHistory, tailLength)
				for key in constants.dirs: 
					if not key in blockedDir and move(key):
						moved = True
						break
				
				if not moved: 
					for key in constants.dirs: 
						if move(key):
							moved = True
							break
			
				
				if not moved: 
					return # done bc bad algo	
			
			moveHistory.append((get_pos_y(), get_pos_x())) 
			continue
			
			
		if not move(move_straight((get_pos_y(), get_pos_x()))): 
			moved = False
			for key in constants.dirs: 
				if move(key):
					moved = True
			
			if not moved: 
				return 



# idee nach 40: 
# snake kann sich "frei" bewegen, aber nur nach oben und sie muss sich in der y koordinate dann 
# nach der dir richten => sehr viel schneller aber trotzdem keine gefahr auf block


