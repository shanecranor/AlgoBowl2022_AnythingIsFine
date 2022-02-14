import Tools
import random
"""
Input: tuple (tasks, machines)
Output: tuple (max length, 2D array of task allocation per machine)
Description:
	Sorts the tasks and machines from best to worst and gives the fastest machines the worst tasks
	Returns the length of the solution and the task distribution table
"""
def SAB(tasks, machines):
	taskOrder = sortRememberOrder(tasks)
	# print("TASKORDER\n", taskOrder)
	machineOrder = sortRememberOrder(machines)
	# print("MACHINEORDER\n", machineOrder)
	outputMatrix = []
	for machine in machineOrder:
		outputMatrix.append([machine, [], 0])
	# loop through every task
	for task in taskOrder:
		# simulate putting the task on the fastest machine
		fastestMachine = 0
		fastestMachineSpeed = outputMatrix[0][2] + (task[0]/outputMatrix[0][0][0])
		#loop throuch each machine to see if we can find a scenario where it is faster 
		# or the same to add a task to a different machine
		for i, machine in enumerate(outputMatrix):
			# calculate time it would take with the new task added
			machineSpeed = machine[2] + (task[0]/machine[0][0])
			if(machineSpeed <= fastestMachineSpeed): #or random.randint(0,1000) < 1):
				fastestMachine, fastestMachineSpeed = i, machineSpeed
		# put the task on the best machine for said task and add the task length
		outputMatrix[fastestMachine][1].append(task)
		outputMatrix[fastestMachine][2] = fastestMachineSpeed
	#print("OUT:\n",outputMatrix)
	def getMachineId(machine):
		return machine[0][1]
	outputMatrix.sort(key=getMachineId)
	# create the output distribution in the right format
	distribution = []
	for i in range(len(machines)):
		machine = []
		for task in outputMatrix[i][1]:
			machine.append(task[1])
		distribution.append(machine)
	return (Tools.calcTotalTime(distribution, tasks, machines), distribution)
	
def sortRememberOrder(list):
	listOrder = []
	for i, item in enumerate(list):
		listOrder.append((item, i))
	def listKey(itemPair):
		return itemPair[0]*-1
	listOrder.sort(key=listKey)
	return listOrder