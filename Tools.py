from ast import mod
from cgi import test
import itertools 		# for permuting
from operator import index
from platform import machine
from re import L
import statistics
import random
import math

"""
Input: distribution, list of tasks, list of machines
Output: machine that takes the longest
Description:
	Loops through each machine in the distribution and find out which one ends last
"""
def calcTotalTime(distribution, tasks, machines):
	timesArr = [0]*len(machines)
	for i, machine in enumerate(distribution):
		#TODO: use numpy for faster addition  (probably not a huge bottleneck tho)
		#https://stackoverflow.com/questions/47734392/python-numpy-array-sum-over-certain-indices
		timesArr[i] = sum(tasks[i] for i in machine)/machines[i]
	return max(timesArr)


def printDetailedStats(distribution, tasks, machines):
	timesArr = [0]*len(machines)
	for i, machine in enumerate(distribution):
		#TODO: use numpy for faster addition  (probably not a huge bottleneck tho)
		#https://stackoverflow.com/questions/47734392/python-numpy-array-sum-over-certain-indices
		timesArr[i] = sum(tasks[i] for i in machine)/machines[i]
		if timesArr[i] == 0:
			print(f"Machine {i}: \t Speed:{machines[i]} No tasks alloted")
		else:
			print(f"Machine {i}: \t Speed:{machines[i]} \t Runtime: {round(timesArr[i],2)} \t shortest task = {min(tasks[i] for i in machine)} longest task = {max(tasks[i] for i in machine)}")
		#print(f"{machines[i]}, {timesArr[i]}, {min(tasks[i] for i in machine)}")
	print(
		f"""STATS:
	Longest machine: Machine {timesArr.index(max(timesArr))} with a time of: {max(timesArr)} time units
	Average machine time: {sum(timesArr)/len(timesArr)}
	Shortest machine: {min(timesArr)}
	Range: {max(timesArr)-min(timesArr)}
	Standard deviation: {statistics.stdev(timesArr)}
		"""
	)
	return


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
		return
	if targetSum/items > MAX_TASK:
		print("ERROR: target sum too large")
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
	return out

"""
input: array of integer tasks and optionally array of blacklisted numbers
output: array of integers with no duplicates (this doesn't fully work, but idc)
integers are constrained from 1 to 10000
"""
def removeDupesKeepSum(arr, prevItems = [], seed=-1):
	arr.sort()
	for i, item in enumerate(arr[0:-1]):
		modifier = 0
		modIndex = i
		while (item+modifier in prevItems
				or arr[modIndex]-modifier in prevItems 
				or item+modifier in arr 
				or (arr[modIndex]-modifier in arr and modIndex != i) 
				or item+modifier < 1 or arr[modIndex]-modifier < 1
				or item+modifier > 10000 or arr[modIndex]-modifier > 10000):
			if item == 10000:
				modIndex = randint(0,int(len(arr)/2))
				modifier = -1*randint(1,(10000-arr[modIndex])-1)
			elif item == 1:
				#modIndex = -1*random.randint(1,int(len(arr)/2))
				modIndex = randint(0, len(arr)-1)
				modifier = randint(1,arr[modIndex]-1)
			else:
				modIndex = randint(0, len(arr)-1)
				modifier = randint(min(10000-item, arr[modIndex]-1), -1*min(item-1,10000-arr[modIndex]))
		arr[i]+=modifier
		arr[modIndex]-=modifier
	return arr

			

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
def createBetterOptimalInput(tasks, machines, optimal, seed=-1):
	tasksList = []
	machinesList = []
	distribution = []
	# create machine speeds
	if seed != -1: random.seed(seed)
	for i in range(machines):
		machinesList.append(random.randint(1,20))
		sumSeed = random.randint(1,5000)
		machineItems = createRandomListWithDefiniteSum(optimal * machinesList[-1], int(tasks/machines), sumSeed)
		machineItems = removeDupesKeepSum(machineItems, tasksList)
		# if(sum(machineItems) != optimal * machinesList[-1]):
		# 	print(sum(machineItems), optimal * machinesList[-1],int(tasks/machines), sumSeed)
		distribution.append([])
		for k in range(int(tasks/machines)):
			distribution[i].append(k+(i*int(tasks/machines)))
		tasksList += machineItems
	return (distribution, tasksList, machinesList)
eee= createBetterOptimalInput(1000,50,7000)[1]
eee.sort()
print(eee)
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


"""
Input: tasksList
Output: A list of permuted tasksLists
Description:
	Use the itertools module to create a list of all permutations
	of inputted tasksList

	in-depth explanation found here:
	https://www.kite.com/python/answers/how-to-find-all-combinations-of-a-list-in-python
"""
def combinationCompiler(tasksList):
	# create a list to hold the permuted lists
	permutedLists = []
	for r in range(len(tasksList)+1):
		# permute the current combination
		combinationObject = itertools.combinations(tasksList, r)

		# add current combination to a list
		currentCombination = list(combinationObject)

		# add currentCombination to big listxw
		permutedLists.append(currentCombination)