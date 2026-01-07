# it takes ~2s to clear a row for a drone
entityGrowthTime = { # median out of 20 plants
	Entities.Grass: 0.5, 
	Entities.Bush: 4.27, 
	Entities.Carrot: 5.9,
	Entities.Pumpkin: 2.12
}


neededEntityWaterLevel = {
	Entities.Carrot: 0.5, 
	Entities.Pumpkin: 0.25,
	Entities.Bush: 0.25
}


actualYield = {
	Entities.Pumpkin: 403 # yield per pumpkin on avg (calculated bc 'Entities.Dead_Pumpkin' exists)
}


dirs = [ North, East, South, West ] 