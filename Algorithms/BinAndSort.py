import Tools
import random
"""
Input: tuple (tasks, machines)
Output: tuple (max length, 2D array of task allocation per machine)
Description:
	Bins the tasks equally onto each machine
	Removes tasks from one of the longest running machines to the shortest running machine it can fit in until they are about the same size
"""
def BAS(tasks, machines, rand=-1, seed=-1):
	if seed != -1: random.seed(seed)
	outputMatrix = bin(tasks, machines)
	# choose n random elements from the longest running machines
	for i in range(500):
		#sort machines from longest to shortest
		outputMatrix.sort(key=lambda x: x[2]*-1)
		#select a random long running machine
		randMachine = random.randint(0, len(outputMatrix)//2)
		# skip if length is zero
		if(len(outputMatrix[randMachine][1]) == 0): continue
		#sort the matrix
		outputMatrix[randMachine][1].sort(key = lambda x: x[0])
		# choose the smallest element, or a random element
		randElement = random.choice( ([0]*i)+[random.randint(0,len(outputMatrix[randMachine][1])-1)]*150)
		#print(randElement, outputMatrix[randMachine][1] )
		temp = outputMatrix[randMachine][1][randElement]
		bestTransfer = []
		for i in range(len(outputMatrix)):
			if i == randMachine: continue
			if outputMatrix[i][2] + temp[0]/outputMatrix[i][0][0] < outputMatrix[randMachine][2]:
				bestTransfer.append(i)
		if len(bestTransfer) != 0:
			bestTransfer = random.choice(bestTransfer)
			# remove element
			outputMatrix[randMachine][1].pop(randElement)
			# correct the sum
			outputMatrix[randMachine][2]-= temp[0]/outputMatrix[randMachine][0][0]
			# add to new list
			outputMatrix[bestTransfer][1].append(temp)
			# correct the sum
			outputMatrix[bestTransfer][2] += temp[0]/outputMatrix[bestTransfer][0][0]
			#print("S", end = '')
		else:
			pass
			#print("F", end ='')

	def getMachineId(machine):
		return machine[0][1]
	outputMatrix.sort(key=lambda x: x[0][1])
	# create the output distribution in the right format
	distribution = []
	for i in range(len(machines)):
		machine = []
		for task in outputMatrix[i][1]:
			machine.append(task[1])
		distribution.append(machine)
	#print("MUTATIONS: ", mutations)
	return (Tools.calcTotalTime(distribution, tasks, machines), distribution)
"""
Input: tasks, machines
Output: distribution matrix
Description:
	Bins each task into a machine
	There is priority for the longer tasks to go in the faster machines
"""
def bin(tasks, machines):
	#shuffle tasks and machines
	taskOrder = sortRememberOrder(tasks)
	machineOrder = sortRememberOrder(machines)
	outputMatrix = []
	# create temp distribution array
	for machine in machineOrder:
		outputMatrix.append([machine, [], 0])
	#distribute tasks
	m = 0
	for i, task in enumerate(taskOrder):
		l = len(machineOrder)
		outputMatrix[m%l][1].append(task)
		outputMatrix[m%l][2] += task[0]
		if len(outputMatrix[m][1]) > len(taskOrder)/l:
			m+=1
	#finish calculations 
	for i, machine in enumerate(outputMatrix):
		outputMatrix[i][2]/=machine[0][0]
		#could sort the tasks on each machine here, rn we'll just remove a random one
	return outputMatrix
	
def shuffleRememberOrder(list):
	listOrder = []
	for i, item in enumerate(list):
		listOrder.append((item, i))
	random.shuffle(listOrder)
	return listOrder

def sortRememberOrder(list):
	listOrder = []
	for i, item in enumerate(list):
		listOrder.append((item, i))
	def listKey(itemPair):
		return itemPair[0]*-1
	listOrder.sort(key=listKey)
	return listOrder