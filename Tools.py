from cgi import test
<<<<<<< HEAD
import itertools 		# for permuting
=======
from operator import index
>>>>>>> 2916dc04c37f35a964dd1821f2594fe1b98393ac
import statistics
import random

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

		# add currentCombination to big list
		permutedLists.append(currentCombination)