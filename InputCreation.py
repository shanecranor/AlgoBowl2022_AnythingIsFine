import Tools
import random
import math
"""
Helper function to get rid of weirdness with the random.randint function
Does the same thing as random.randint
"""
def randint(start, end):
	tmpstart = min(start,end)
	end = max(start,end)
	start = tmpstart
	if start == end:
		return start
	return random.randint(start,end)

"""
Input: target sum and number of items
Output: List of of length items that sums to the target sum
"""
def createRandomListWithDefiniteSum(targetSum, items, seed=-1):
	if seed != -1: random.seed(seed)
	MAX_TASK = 10000
	if items >= targetSum:
		print("ERROR, there must be less items than the target sum")
		return None
	if targetSum/items > MAX_TASK:
		#print("ERROR: target sum too large")
		return None
	out = []
	movingTargetSum = targetSum
	movingItems = items
	for i in range(items):
		upperBound = min(1 + movingTargetSum - movingItems, MAX_TASK)
		lowerBound = 1
		if movingTargetSum/MAX_TASK == movingItems:
			lowerBound = MAX_TASK
		elif math.ceil(movingTargetSum/MAX_TASK) == movingItems:
			lowerBound = math.ceil(((movingTargetSum/MAX_TASK)-int(movingTargetSum/MAX_TASK))*MAX_TASK)
		if upperBound == lowerBound:
			newTask = lowerBound
		else:
			newTask = randint(lowerBound, upperBound)#, random.randint(lowerBound, max(math.ceil(upperBound/2),lowerBound))])
		out.append(newTask)
		movingTargetSum -= newTask
		movingItems -= 1
		#print(upperBound, lowerBound, movingTargetSum,targetSum-sum(out), movingItems, out, sep="\t")
	out.sort()
	t = 0
	while sum(out) != targetSum:
		if(sum(out) < targetSum):
			out[t%len(out)] += 1
		if(sum(out)> targetSum):
			out[t%len(out)] -= 1
		t += 1
	return out

"""
input: array of integer tasks and optionally array of blacklisted numbers
output: array of integers with no duplicates (this doesn't fully work, but idc)
integers are constrained from 1 to 10000
"""
def removeDupesKeepSum(arr, prevItems = [], seed=-1):
	arr.sort()
	for i in range(len(arr)-1):
		modifier = 0
		modIndex = i
		if sum(arr)/len(arr) > 9969:
			return arr
		while (arr[i]+modifier in prevItems
				or arr[modIndex]-modifier in prevItems 
				or arr[i]+modifier in arr 
				or (arr[modIndex]-modifier in arr and modIndex != i) 
				or arr[i]+modifier < 1 or arr[modIndex]-modifier < 1
				or arr[i]+modifier > 10000 or arr[modIndex]-modifier > 10000):
			if arr[i] == 10000:
				modIndex = randint(0,int(len(arr)/2))
				modifier = -1*randint(1,(10000-arr[modIndex])-1)
			elif arr[i] == 1:
				#modIndex = -1*random.randint(1,int(len(arr)/2))c
				modIndex = randint(0, len(arr)-1)
				modifier = randint(1,arr[modIndex]-1)
			else:
				modIndex = randint(0, len(arr)-1)
				modifier = randint(min(10000-arr[i], arr[modIndex]-1), -1*min(arr[i]-1,10000-arr[modIndex]))
		arr[i]+=modifier
		arr[modIndex]-=modifier
	return arr

"""
Input: target sum and number of items
Output: List of of length items that sums to the target sum
"""
def createListDefiniteSum(targetSum, items, seed=-1, evolutions=1000):
	if seed != -1: random.seed(seed)
	out = []
	MAX_TASK = 10000
	if items >= targetSum:
		print("ERROR, there must be less items than the target sum")
		return None
	if targetSum/items > MAX_TASK:
		#print("ERROR: target sum too large")
		return None


	for i in range(items):
		out.append(int(targetSum/items))
	fail = 0			
	for i in range(evolutions):
		idx1 = random.randint(0,len(out)-1)
		idx2 = random.randint(0,len(out)-1)
		if( out[idx1]-1 > 1 and out[idx2]+1 < 10000):
			out[idx1]-=1
			out[idx2]+=1 
		elif( out[idx2]-1 > 1 and out[idx1]+1 < 10000):
			out[idx2]-=1
			out[idx1]+=1 
		else:
			fail +=1
	t = 0
	while sum(out) != targetSum:
		if(sum(out) < targetSum):
			out[t%len(out)] += 1
		if(sum(out)> targetSum):
			out[t%len(out)] -= 1
		t += 1
	return out
""" 
Input: number of tasks, number of machines, optimal run time
Output: list of tasks and machines as well as an output distribution
Description:
	creates two lists of random integers in the appropriate ranges except there is a known optimal solution
"""
def createOptimalInput(tasks, machines, optimal, seed=-1):
	tasksList = []
	machinesList = []
	distribution = []
	# create machine speeds
	if seed != -1: random.seed(seed)
	for i in range(machines):
		machinesList.append(random.randint(1,20))
		sumSeed = random.randint(1,5000)
		machineItems = createRandomListWithDefiniteSum(optimal * machinesList[-1], int(tasks/machines), sumSeed)
		if machineItems is None:
			return None
		# if(sum(machineItems) != optimal * machinesList[-1]):
		# 	print(sum(machineItems), optimal * machinesList[-1],int(tasks/machines), sumSeed)
		distribution.append([])
		for k in range(int(tasks/machines)):
			distribution[i].append(k+(i*int(tasks/machines)))
		tasksList += machineItems
	return (distribution, tasksList, machinesList)


""" 
Input: number of tasks, number of machines, optimal run time
Output: list of tasks and machines as well as an output distribution
Description:
	creates two lists of random integers in the appropriate ranges except there is a known optimal solution
"""
def createBetterOptimalInput(tasks, machines, optimal, seed=-1, diffLengthMachines=False, removeDupes=True, isGlobalDupes=True, useWorseRandom=True, numberOfWorseIterations=1000):
	tasksList = []
	machinesList = []
	distribution = []
	# create machine speeds
	if seed != -1: random.seed(seed)
	machineSizes = []
	#Create list of machines and sort them from slowest to fastest
	for i in range(machines):
		machinesList.append(random.randint(1,20))
	machinesList.sort()

	if diffLengthMachines:
		#create list of the length of each machine
		machineSizes = createListDefiniteSum(tasks, machines)
		#sort from least items to most items
		machineSizes.sort()
	else:
		#every machine should have the same length
		for i in range(machines):
			machineSizes.append(int(tasks/machines))
	
	for i in range(machines):
		if useWorseRandom:
			machineItems = createListDefiniteSum(optimal * machinesList[i], machineSizes[i], evolutions=numberOfWorseIterations)
		else:
			machineItems = createRandomListWithDefiniteSum(optimal * machinesList[i], machineSizes[i])
	
		if machineItems is None: return (None, None, None)
		if(sum(machineItems) != optimal * machinesList[i]):
			print(sum(machineItems), optimal * machinesList[i], machineItems)
		if removeDupes:
			if isGlobalDupes:
				machineItems = removeDupesKeepSum(machineItems)
			else:
				machineItems = removeDupesKeepSum(machineItems, tasksList, True)
		distribution.append([])
		for k in range(machineSizes[i]):
			distribution[i].append(k+(sum(machineSizes[0:i])))
		tasksList += machineItems
	return (distribution, tasksList, machinesList)


"""
Input: number of tasks, number of machines
Output: the lists
Description:
	creates two lists of random integers in the appropriate ranges
"""
def createInput(tasks, machines, taskSeed=-1, machineSeed=-1):
	tasksList = []
	machinesList = []

	# create tasks runtimes
	if taskSeed != -1: random.seed(taskSeed)
	for i in range(tasks):
		tasksList.append(random.randint(1,10000))
	# create machine speeds
	if machineSeed != -1: random.seed(machineSeed)
	for i in range(machines):
		machinesList.append(random.randint(1,20))

	return (tasksList, machinesList)

def createInputFile(tasksList, machinesList, fileName):
	out = ""

	# add the number of tasks and machines
	out += str(len(tasksList)) + "\n" + str(len(machinesList)) + "\n"
	
	# for loop to output 
	for task in tasksList:
		out += str(task) + " "

	out += "\n"

	# for loop to output tasks speeds
	# ASK TO SEE IF WE NEED TO REMOVE LAST SPACE
	for machine in machinesList:
		out += str(machine) + " "

	f = open(fileName, "w")
	f.write(out)
	f.close()
